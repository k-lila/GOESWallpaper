from datetime import datetime
import re
import requests
import pandas as pd

timeout = 5

# ==================================================================================================================== #
# retorna uma str contendo o html do link


def getHtml(link: str) -> str:
    request = requests.get(link, timeout=timeout)
    html = request.text
    return html

# -------------------------------------------------------------------------------------------------------------------- #
# retorna um conjunto com todos os diretórios da string contendo o html


def getDiretorios(html: str) -> set:
    padrao = re.compile(r'".*"')  # regex
    totalLinks = padrao.findall(html)
    totalLinks = [link[1:-1] for link in totalLinks if link != '"../"' and link[-2] == '/']
    return set(totalLinks)

# -------------------------------------------------------------------------------------------------------------------- #
# exclui ou adiciona elementos em um conjunto de diretórios


def filtroPesquisa(conjunto, gate=set(), key=set()):
    del1 = {'CONUS', 'MESO', 'SECTOR', 'FD'}
    del2 = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16'}
    del3 = {'AirMass', 'DMW', 'DayCloudPhase', 'DayNightCloudMicroCombo', 'Dust', 'DayLandCloudFire', 'DayConvection',
            'FireTemperature', 'NightMicrophysics', 'SWD', 'Sandwich', 'FireTemperature', 'test_MESO', 'GEOCOLOR'}
    filtro = del1 | del2 | del3 | key
    filtro = filtro.difference(gate)
    conjuntoDelete = set()
    for link in conjunto:
        if link.split('/')[-2] in filtro:
            conjuntoDelete.add(link)
    conjunto = conjunto.difference(conjuntoDelete)
    return conjunto

# -------------------------------------------------------------------------------------------------------------------- #
# motor de procura, retorna o conjunto de diretórios mapeados, limitado pela função filtro


def motor(htmlRoot, funcaoFiltro, gate=set(), key=set()):

    conjuntoDiretorios = {htmlRoot}
    conjuntoProcura = {htmlRoot}

    while True:
        # -------------------------- quebra do loop
        if conjuntoProcura == set():
            break
        # ------------------------- adiciona os links que vão ser requisitados no conjunto de diretórios
        for link in conjuntoProcura:
            conjuntoDiretorios.add(link)
        # ------------------------------ requisição HTML e busca pelos diretórios
        conjuntoAux = set()
        for diretorio in conjuntoProcura:
            diretorios = {(diretorio + d) for d in getDiretorios(getHtml(diretorio))}
            conjuntoAux = conjuntoAux | diretorios
        # ############################################################### #
        # Filtro dos links. O filtro é a função dada como parâmetro.
        conjuntoProcura = funcaoFiltro(conjuntoAux, gate, key)
    return conjuntoDiretorios

# -------------------------------------------------------------------------------------------------------------------- #
# retorna um dataframe com os links, a data e o tamanho dos arquivos do diretório


def getFiles(diretorio):
    requisicaoHtml = getHtml(diretorio)
    lista_informacoes = []
    for linha in requisicaoHtml.split('<a'):
        listaData = linha.split(' ')
        while '' in listaData:
            listaData.remove('')
        if len(listaData) == 4:
            lista_informacoes.append(listaData)
    lista_dataframe = []
    for info in lista_informacoes:
        # contrução das linhas do dataframe
        # --------------------------------- link
        padrao = re.compile('".*"')
        link = padrao.findall(info[0])
        link = link[0][1:-1]
        # --------------------------------- data e hora
        dataHora = f'{info[1]} {info[2]}'
        padrao_datahora = '%d-%b-%Y %H:%M'
        dataHora = datetime.strptime(dataHora, padrao_datahora)
        # ----------------------------------------------------- tamanho
        tamanho = int(info[3].split('\r')[0])
        # ----------------------------------------------------- append lista_dataframe
        lista_dataframe.append([diretorio + link, dataHora, tamanho])
    df = pd.DataFrame(lista_dataframe, columns=['link', 'data', 'tamanho (bytes)'])

    return df.sort_values(by='data', ascending=False, ignore_index=True)  # mais recente ao mais antigo

# -------------------------------------------------------------------------------------------------------------------- #


def imageFinder(dataframe, resolucao, data=None):

    resolucao += '.jpg'
    df_resolucao = dataframe.loc[dataframe['link'].str.endswith(resolucao)]
    df_resolucao = df_resolucao.reset_index(drop=True)
    if data:
        data = datetime.strptime(data, '%d/%m/%Y').date()
        novo_df = df_resolucao.loc[df_resolucao['data'].dt.date == data]
        return novo_df.reset_index(drop=True)
    else:
        return df_resolucao.iloc[0]

# -------------------------------------------------------------------------------------------------------------------- #


def dowloader(nome_arquivo: str, link):
    print(f'iniciando o dowload | {link}')
    request = requests.get(link, timeout=timeout)
    if request.status_code == 200:
        with open(f'./imagens/{nome_arquivo}.jpg', mode='wb') as img:
            img.write(request.content)
            print(f'imagem salva')
    else:
        print('request inválida, dowload abortado')

# ==================================================================================================================== #
