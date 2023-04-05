
from source import GOESObserver as go

# ==================================================================================================================== #


teste = go.GOESObserver(satelite='GOES16', instrumento='ABI', abrangencia='fulldisk', banda='08')











# def dowloader2(self, resolucao, data=None):
#     self.set_imagery(resolucao=resolucao, data=data)
#     print('dowloader iniciado\n')
#     time_tostring = lambda x: x.strftime('%d-%m-%Y %H:%M:%S')
#     bytes_tomb = lambda x: str(round(x / (1024 * 1024), 3))
#     nomefunc = lambda x, y: f'{self.filtro} {x} {y}'
#     if data:
#         num = self.df_imagens.shape[0]
#         print(f'{num} arquivos a serem salvos\n')
#         for valores in self.df_imagens.values:
#             link = valores[0]
#             data_hora = time_tostring(valores[1])
#             tamanho = bytes_tomb(valores[2])
#             nome = nomefunc(data_hora, resolucao)
#             print(f'# link localizado | tamanho do arquivo: {tamanho} mb, {num} arquivos restantes')
#             bib.dowloader(nome_arquivo=nome, link=link)
#             num -= 1
#             print()
#     else:
#         valores = self.df_imagens.values
#         link = valores[0]
#         data_hora = time_tostring(valores[1])
#         tamanho = bytes_tomb(valores[2])
#         nome = nomefunc(data_hora, resolucao)
#         print(f'# link localizado | tamanho do arquivo: {tamanho} mb')
#         bib.dowloader(nome_arquivo=nome, link=link)
#     print('\ndowloader concluido\n')
#     return None


# def videoMaker():
#
#     path = './imagens'
#     nome_video = 'airmass, uma semana.mp4'
#     fps = 24
#     frame_size = (1808, 1808)
#     imagens = [img for img in os.listdir(path)]
#     imagens = sorted(imagens)
#
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(nome_video, fourcc, fps, frame_size)
#     contador = 0
#     for filename in imagens:
#         img_path = os.path.join(path, filename)
#         img = cv2.imread(img_path)
#         out.write(img)
#         contador += 1
#         print(f'frame: {contador} escrito')
#     out.release()
#     print('release')

# ==================================================================================================================== #




