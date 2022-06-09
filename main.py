############################################################
# Dados da Equipe
############################################################
# EVERTON SANTOS DE ANDRADE JUNIOR
# Turma 03
# Graficos: Linha, Barra, Textual
import sys
sys.path.append('./src')
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

from os.path import exists 
from src import menu,utils

OUT_ASSETS_ATHELE_PATH = f"./assets/athlete_events.csv"

ASSETS_FILE_PATHS = [
"./assets/athlete_events.csv0",
"./assets/athlete_events.csv1",
] 

def __main__():
	if not exists(OUT_ASSETS_ATHELE_PATH):
		utils.files_concat(*ASSETS_FILE_PATHS, outfilepath=OUT_ASSETS_ATHELE_PATH)

	menu.abrirMenu(input(
"""\033[0mEscolha seu Gráfico digitando um dos códigos:\n
	L9: Evolução da idade média dos atletas do <Gênero> que ganharam medalhas em alguma das Olimpíadas\n
	B12: Altura média dos atletas para um grupo de <Esportes> na olimpíada de <Ano> de <Tipo de Olimpíada>, separados por sexo.\n
	T2: Qual o(a) atleta que mais ganhou medalha de <Tipo de Medalha>?\n
	X1: Idade dos atletas a cada ano.\n
	E: Quantidade de medalhas, ouro, prata e bronze, (uma barra pra cada) para os 5 primeiros países colocados de um determinado invervalo de ano.\n
"""))

if __name__ == '__main__':
	__main__()
