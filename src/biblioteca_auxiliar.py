import pickle

# ==================================================================================================================== #

def info():
    print('.---------------------------------------------------------------------.')
    print(' Geostationary Operational Environmental Satellite '.center(71))
    print('-----------------------------------------------------------------------\n')
    print('    O GOES-16 e o GOES-18 são satélites estacionários de observação do')
    print(' clima na  Terra operados pela NOAA - National Oceanic and Atmospheric')
    print(' Administration  -  uma instituição  do  Departamento de Comércio  dos')
    print(' Estados Unidos.')
    print('. . .'.center(71) + '\n')
    print('    #    O GOES-16, ou GOES-R, foi lançado em 2016 e abrange a América')
    print('         do Sul, América Central e América do Norte.')
    print('    #    O GOES-18, ou GOES-S, foi lançado em 2018 e abrange o  Oceano')
    print('         Pacífico oriental e a costa oesteda América do Norte.')
    print('         da América do Norte.')
    print('. . .'.center(71) + '\n')
    print('     Dois dos principais instrumentos  de  captura de  imagem  do GOES')
    print(' são o GLM e o ABI. O Geostationary Lightning Mapper observa  em tempo')
    print(' real  as  descargas  elétricas  da atmosfera,  e  o Advanced Baseline')
    print(' Imager captura dados em 16 diferentes comprimentos de onda.  Além dos')
    print(' 16  comprimentos de  onda observados  e a visualização  das descargas')
    print(' elétricas  há também filtros  disponíveis. Um deles é o GEOCOLOR, que')
    print(' utiliza  várias faixas  do espectro eletromagnético  para  formar uma')
    print(' formar uma imagem da nossa vista da Terra.')
    print('\n' + ' Bandas disponíveis '.center(71, '-') + '\n')
    print(f'{"  Banda  01   |"}{"Visível".center(31)}{"|   0,47-0,51 μm"}'.center(71))
    print(f'{"  Banda  02   |"}{"Visível".center(31)}{"|   0,64-0,68 μm"}'.center(71))
    print(f'{"  Banda  03   |"}{"Visível".center(31)}{"|   0,84-0,88 μm"}'.center(71))
    print(f'{"  Banda  04   |"}{"Infravermelho próximo".center(31)}{"|   0,85-0,89 μm"}'.center(71))
    print(f'{"  Banda  05   |"}{"Infravermelho próximo".center(31)}{"|   1,55-1,65 μm"}'.center(71))
    print(f'{"  Banda  06   |"}{"Infravermelho próximo".center(31)}{"|   2,11-2,27 μm"}'.center(71))
    print(f'{"  Banda  07   |"}{"Infravermelho de onda curta".center(31)}{"|   3,80-4,00 μm"}'.center(71))
    print(f'{"  Banda  08   |"}{"Infravermelho de onda curta".center(31)}{"|   6,19-6,37 μm"}'.center(71))
    print(f'{"  Banda  09   |"}{"Infravermelho de onda curta".center(31)}{"|   6,87-7,25 μm"}'.center(71))
    print(f'{"  Banda  10   |"}{"Infravermelho de onda curta".center(31)}{"|   7,30-7,90 μm"}'.center(71))
    print(f'{"  Banda  11   |"}{"Infravermelho de onda curta".center(31)}{"|   8,20-8,60 μm"}'.center(71))
    print(f'{"  Banda  12   |"}{"Infravermelho de onda curta".center(31)}{"|   9,55-9,85 μm"}'.center(71))
    print(f'{"   Banda  13   |"}{"Infravermelho de onda curta".center(31)}{"|  10,30-11,30 μm"}'.center(71))
    print(f'{"   Banda  14   |"}{"Infravermelho de onda curta".center(31)}{"|  11,50-11,90 μm"}'.center(71))
    print(f'{"   Banda  15   |"}{"Infravermelho de onda longa".center(31)}{"|  12,80-13,40 μm"}'.center(71))
    print(f'{"   Banda  16   |"}{"Infravermelho de onda longa".center(31)}{"|  13,00-13,60 μm"}'.center(71))
    print('\n' + ' Filtros disponíveis '.center(71, '-') + '\n')
    print('- GEOCOLOR -'.center(71))
    print('- Air Mass -'.center(71))
    print('- Day Cloud Phase -'.center(71))
    print('- Day Convection -'.center(71))
    print('- Day Land Cloud Fire -'.center(71))
    print('- Day Night Cloud Micro Combo -'.center(71))
    print('- Dust -'.center(71))
    print('- DMW -'.center(71))
    print('- Fire Temperature -'.center(71))
    print('- Night Microphysics -'.center(71))
    print('- Sandwich -'.center(71))
    print('- SWD -'.center(71))
    print('.____________________________________________________________________.')

# -------------------------------------------------------------------------------------------------------------------- #

def configura():
    informacoes = input(' Visualizar informações? (s/n) ')
    print()
    if informacoes.upper() == 'S':
        info()
        print()
    else:
        print('-' * 71 + '\n')
    print('Configure seu GOESWallpaper'.center(71))
    dict = {}
    glm = False
    print()
    print(' digite "R" ou "16" para o GOES-16 e "S" ou "18" para o GOES-18 '.center(71, '-'))
    print()
    while True:
        satelite = input('  Satélite GOES-')
        if satelite.upper() in {'16', 'R'}:
            dict.update({'satélite': 'GOES16'})
            break
        elif satelite.upper() in {'18', 'S'}:
            dict.update({'satélite': 'GOES18'})
            break
        else:
            print(' - tente novamente -')
    print('\n' + ' escolha o instrumento de imagem: ABI ou GLM '.center(71, '-') + '\n')
    while True:
        instrumento = input(' Instrumento escolhido: ')
        if instrumento.upper() in {'ABI', 'GLM'}:
            dict.update({'instrumento': instrumento.upper()})
            if instrumento.upper() == 'GLM':
                glm = True
            break
        else:
            print('   - tente novamente')
    filtros = {'AirMass', 'DMW', 'DayCloudPhase', 'DayNightCloudMicroCombo', 'Dust', 'DayLandCloudFire',
               'DayConvection', 'FireTemperature', 'NightMicrophysics', 'SWD', 'Sandwich', 'GEOCOLOR'}
    if not glm:
        print('\n' + ' digite a banda da imagem ou o nome do filtro '.center(71, '-') + '\n')
    while True:
        if glm:
            dict.update({'filtro': None})
            dict.update({'banda': None})
            break
        bandafiltro = input('  Banda ou filtro escolhido: ')
        if bandafiltro in filtros:
            dict.update({'filtro': bandafiltro})
            dict.update(({'banda': None}))
            break
        try:
            banda = int(bandafiltro)
            if 0 < banda < 17:
                dict.update({'filtro': None})
                banda = lambda x: x if len(x) == 2 else '0' + x
                dict.update({'banda': banda(bandafiltro)})
                break
        except:
            print('   - tente novamente')
        else:
            print('   - tente novamente')
    with open('config.pickle', 'wb') as arquivo:
        pickle.dump(dict, arquivo)
    arquivo.close()
    return None

# ==================================================================================================================== #
