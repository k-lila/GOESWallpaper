# GOESWallpaper
Um pequeno script que salva como wallpaper a imagem mais recente dos satélites GOES-16 e GOES-18.

#

O script salva a imagem mais recente, segundo o filtro ou banda escolhida, em imagens/recente.jpg.
Após, o script ajusta a imagem para a proporção 16/9, e salva essa imagem ajustada no caminho presente
no arquivo "caminho.txt". É importante que o nome do arquivo salvo seja "wallpaper.jpg".

# 

1) instale  as bibliotecas necessárias;
2) adicione o diretório do plano de fundo no arquivo 'caminho.txt';
3) adicione a permissão para criar/deletar arquivos no diretório;
4) inicie o script run.py e faça a configuração inicial;

Obs.: Esse script foi escrito para o Linux Ubuntu

# Imagens disponíveis

Bandas: 1-16;

Filtros: GEOCOLOR, AirMass, DMW, DayCloudPhase, DayNightCloudMicroCombo, Dust, DayLandCloudFire,
         DayConvection, FireTemperature, NightMicrophysics, SWD, Sandwich.
