
import time
import datetime
import pickle
import requests

from src import wpp
from src import biblioteca_auxiliar as aux

# ==================================================================================================================== #

def partida():
    config_dict = None
    try:
        with open(file='config.pickle', mode='rb') as arquivo:
            config_dict = pickle.load(arquivo)
        arquivo.close()
        conf = input(' Configurar GOESWallpaper? (s/n) ')
        if conf.upper() == 'S':
            aux.configura()
            with open(file='config.pickle', mode='rb') as arquivo:
                config_dict = pickle.load(arquivo)
            arquivo.close()
    except:
        aux.configura()
        with open(file='config.pickle', mode='rb') as arquivo:
            config_dict = pickle.load(arquivo)
        arquivo.close()
    return config_dict
# ----------------------------------------------------------- #
def runner(satelite, instrumento, banda, filtro):
    current_wallpaper = wpp.GOESWallpaper()
    while True:
        try:
            datahora_antiga = None
            datahora_nova = None
            update = True
            try:
                with open(file='recente.picke', mode='rb') as recent:
                    datahora_antiga = pickle.load(recent)
            except:
                pass
            imagem = current_wallpaper.get_image(
                resolucao='1808x1808',
                satelite=satelite,
                instrumento=instrumento,
                abrangencia='fulldisk',
                banda=banda,
                filtro=filtro
            )
            with open(file='recente.picke', mode='rb') as recent:
                datahora_nova = pickle.load(recent)
            if datahora_nova != datahora_antiga:
                current_wallpaper.update_img()
                now = datetime.datetime.now().strftime('%H:%M:%S')
                print(f'  {now} | {current_wallpaper.data_recente}'.center(71))
                time.sleep(500)
            else:
                time.sleep(120)
                pass
        except requests.Timeout as timeout:
            print(' link indisponível no momento '.center(71))
            time.sleep(30)
        except Exception as exc:
            print(exc)
            time.sleep(120)
        time.sleep(5)
# ----------------------------------------------------------- #
def run():
    print(f' .v.\u03B1.0.')
    print('.' + ' GOESWallpaper '.center(69, '-') + '.\n')
    config_dict = partida()
    print('\n.' + ' GOESWallpaper iniciado '.center(69, '-') + '.')
    print('Aproveite a vista!'.center(71) + '\n')
    print('hora da busca | atualização da imagem'.center(71))
    runner(
        satelite=config_dict['satélite'],
        instrumento=config_dict['instrumento'],
        banda=config_dict['banda'],
        filtro=config_dict['filtro']
    )

# ==================================================================================================================== #

run()
