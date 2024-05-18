import requests
import pickle
from PIL import Image
from src import GOESObserver as go

# ==================================================================================================================== #

class GOESWallpaper(object):
    def __init__(self):
        self.diretorio = None
        self.link_img = None
        self.tamanho = None
        self.data_recente = None
        self.working = False
# ----------------------------- #
    def get_image(
            self,
            resolucao: str,
            satelite: str,
            instrumento: str,
            abrangencia: str,
            filtro=None,
            banda=None
            ) :
        goes = go.GOESObserver(
            satelite=satelite,
            instrumento=instrumento,
            abrangencia=abrangencia,
            filtro=filtro, banda=banda
            )
        goes.set_imagery(resolucao=resolucao)
        self.diretorio = goes.diretorio
        self.link_img = goes.df_imagens.iloc[0]
        self.data_recente = goes.df_imagens.iloc[1]
        self.tamanho = round(goes.df_imagens.iloc[2] / (1024 * 1024), 3)
        self.working = True
        status_code = requests.get(url=self.link_img, timeout=1).status_code
        if status_code == 200:
            self.working = True
            with open('recente.picke', mode='wb') as recente:
                pickle.dump(f'{self.data_recente} {self.link_img}', recente)
            recente.close()
        return None
# -------------------------------------------------------------------------- #
    def update_img(self):
        if self.working:
            file = open('./imagens/recente.jpg', mode='wb')
            file.write(requests.get(url=self.link_img).content)
            Image.MAX_IMAGE_PIXELS = None
            imagem = Image.open(fp='./imagens/recente.jpg')
            nova_resolucao = (int(1810 * (16 / 9)), 1810)
            wallpaper = Image.new("RGB", nova_resolucao, (0, 0, 0))
            posicao_central = ((nova_resolucao[0] - imagem.size[0]) // 2,
                               (nova_resolucao[1] - imagem.size[1]) // 2)
            wallpaper.paste(imagem, posicao_central)
            wallpaper.save('/home/k-lila/Pictures/Wallpapers/wallpaper.jpg')

# ==================================================================================================================== #
