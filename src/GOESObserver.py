from src import biblioteca_central as bib

# ==================================================================================================================== #

class GOESObserver(object):
    def __init__(self, satelite: str, instrumento: str, abrangencia: str, filtro=None, banda=None):
        self.html_root = f'https://cdn.star.nesdis.noaa.gov/{satelite}/'
        self.satelite = satelite
        self.instrumento = instrumento
        self.abrangencia = abrangencia
        self.filtro = filtro
        self.banda = banda
        self.diretorio = None
        self.df_files = None
        self.df_imagens = None
        self.info = self._getinfo()
    def __str__(self):
        sep = f'+{"-" * 80}+'
        sep2 = f'+{"-" * 152}+'
        print(sep)
        if self.satelite == 'GOES16':
            print('Geostationary Operational Environmental Satellite 16 (GOES16)'.center(80))
        if self.satelite == 'GOES18':
            print('Geostationary Operational Environmental Satellite 18 (GOES18)'.center(80))
        print(sep)
        lista = [
            f' Instrumento: {self.instrumento}',
            f' Abrangência: {self.abrangencia}',
            f' Filtro: {self.filtro}',
            f' Banda: {self.banda}',
            f' Diretório: {self.diretorio}'
        ]
        for atributo in lista:
            print(f'{atributo}')
        print(sep2)
        print(f' {self.df_files.shape[0]} arquivos disponíveis | 15 arquivos mais recentes:')
        print(self.df_files.head(15).to_string())
        print()
        print(sep2)
        try:
            if self.df_imagens.shape[0] == 3:
                print(f'\n link da imagem mais recente: {self.df_imagens["link"]}')
            else:
                print(f' {self.df_imagens.shape[0]} imagens disponíveis ')
                print(self.df_imagens.to_string())
            print('\n' + sep2)
        except:
            pass
        return ''
# ------------------------------------------------------------------------- #
    def _getinfo(self):
        if self.abrangencia == 'fulldisk':
            return self._get_fulldisk()
# ---------------------------------------- #
    def _get_fulldisk(self):
        gate = None
        key = None
        aqui = None
        if self.instrumento == 'GLM':
            aqui = 'EXTENT3'
            gate = {'FD', aqui}
            key = {'ABI'}
        if self.instrumento == 'ABI':
            aqui = lambda x, y: x if x != None else y
            aqui = aqui(self.filtro, self.banda)
            gate = {'FD', aqui}
            key = {'GLM', 'EXTENT3'}
        diretorios = bib.motor(self.html_root, bib.filtroPesquisa, gate=gate, key=key)
        for diretorio in diretorios:
            if diretorio.split('/')[-2] == aqui:
                self.diretorio = diretorio
        self.df_files = bib.getFiles(self.diretorio)
# ------------------------------------------------------------------------------------ #
    def set_imagery(self, resolucao, data=None):
        dataframe = bib.imageFinder(dataframe=self.df_files,
                                    resolucao=resolucao,
                                    data=data)
        self.df_imagens = dataframe

# ==================================================================================================================== #
