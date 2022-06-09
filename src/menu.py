import barra,linha,textual,boxplot,extra
import re
import utils
import sys
sys.path.append('./src')
from csvdata import data

# Função para abrir Menu
def abrirMenu(choice:str):
    choice = " " if len(choice) < 1 else choice.strip().upper()[0] 
    url = "./assets/athlete_events.csv"

    # Escolha do gráfico de barras 
    if choice == 'B': 
        menuBarra(url)

    # Escolha de Linhas 
    elif choice == 'L':
        # Pegando dados do csv, usando filtro
        dados = data(url, filter=linha.filtragem)
        # Escolha de sexo
        sexo = input("Esolha sexo: (\033[93mM\033[0m para homem, \033[93mF\033[0m para mulher)\n").upper().strip()
        titulo = f" Evolução da idade média dos atletas do sexo {'masculino' if sexo == 'M' else 'femenino'}"

        # Geramos grafico de linha
        linha.gerarGraficoDeLinha(dados,sex=sexo, text=(titulo,"Anos","Idade"))

    # Escolha de resposta Textual 
    elif choice == "T":
        textual.gerarRespostaTextual(input("Digite  \033[93mGold\033[0m, \033[93mSilver\033[0m, ou \033[93mBronze\033[0m para saber\nQual o(a) atleta que mais ganhou medalha de: "))

    # Escolha de gráfico Boxplot
    elif choice == "X":
        boxplot.gerarGraficoBoxplot(url=url,anos=chooseYears()[0])
    elif choice == "E":
        extra.gerarGraficoDeBarra(url=url)

    choice = input("\033[0m\nDigite 'quit' ou 'sair' para sair do programa\nOu esolha proximo graphico:  \033[93m").lower().strip()
    # Voltar Cor normal
    if choice == 'quit' or choice == 'sair':
        print("\033[0m")

        return True
    return abrirMenu(choice)


# Menu especifico pra barra
def menuBarra(url:str):
    # Coletamos esportes escolhidos
    esportes_escolhidos = chooseSports()
    # Coletamos anos escolhidos e um dupla de intervalo
    anos_escolhidos,intervalo = chooseYears()

    # Coletamos Temporada
    user_input_temporada = input("\nEscolha temporada (\033[92m\033[1mw\033[0m para winter/inverno, \033[92m\033[1ms\033[0m para summer/verão, \033[92m\033[1mall\033[0m para todos)\nTemporada:").strip()[0].upper()

    temporada = "Winter" if user_input_temporada == "W" else "Summer" if user_input_temporada == "S" else ""
    
    # Criamos dados com o devidos filtros a partir do url fornecido:
    dados = data(url, filter=barra.filtreBarra(esportes=esportes_escolhidos,anos=anos_escolhidos,olimpiada=temporada))
    # Geramos Grafico
    barra.gerarGraficoDeBarra(dados,esportes=esportes_escolhidos,intervalos_de_anos=intervalo,olimpiada=temporada or "Summer and Winter")


# Escolha Esportes
def chooseSports():

    # Relação entre indices e esportes:
    sports = {
        1: 'Aeronautics', 2: 'Alpine Skiing', 3: 'Alpinism', 4: 'Archery', 5: 'Art Competitions', 6: 'Athletics', 7: 'Badminton', 8: 'Baseball', 9: 'Basketball', 10: 'Basque Pelota', 11: 'Beach Volleyball', 12: 'Biathlon', 13: 'Bobsleigh', 14: 'Boxing', 15: 'Canoeing', 16: 'Cricket', 17: 'Croquet', 18: 'Cross Country Skiing', 19: 'Curling', 20: 'Cycling', 21: 'Diving', 22: 'Equestrianism', 23: 'Fencing', 24: 'Figure Skating', 25: 'Football', 26: 'Freestyle Skiing', 27: 'Golf', 28: 'Gymnastics', 29: 'Handball', 30: 'Hockey', 31: 'Ice Hockey', 32: 'Jeu De Paume', 33: 'Judo', 34: 'Lacrosse', 35: 'Luge', 36: 'Military Ski Patrol', 37: 'Modern Pentathlon', 38: 'Motorboating', 39: 'Nordic Combined', 40: 'Polo', 41: 'Racquets', 42: 'Rhythmic Gymnastics', 43: 'Roque', 44: 'Rowing', 45: 'Rugby', 46: 'Rugby Sevens', 47: 'Sailing', 48: 'Shooting', 49: 'Short Track Speed Skating', 50: 'Skeleton', 51: 'Ski Jumping', 52: 'Snowboarding', 53: 'Softball', 54: 'Speed Skating', 55: 'League of Legends', 56: 'Swimming',
        57: 'Synchronized Swimming', 58: 'Table Tennis', 59: 'Taekwondo', 60: 'Tennis', 61: 'Trampolining', 62: 'Triathlon', 63: 'Tug-Of-War', 64: 'Volleyball', 65: 'Water Polo', 66: 'Weightlifting', 67: 'Wrestling'}
    
    # Disponibilizamos todos os sports com seus indices
    print("\033[94m 1: 'Aeronautics',  2: 'Alpine Skiing' 3: 'Alpinism', 4: 'Archery', 5: 'Art Competitions', 6: 'Athletics'\n7: 'Badminton',  8: 'Baseball', 9: 'Basketball', 10: 'Basque Pelota', 11: 'Beach Volleyball', 12: 'Biathlon'\n13: 'Bobsleigh',  14: 'Boxing', 15: 'Canoeing', 16: 'Cricket', 17: 'Croquet', 18: 'Cross Country Skiing'\n19: 'Curling',  20: 'Cycling', 21: 'Diving', 22: 'Equestrianism', 23: 'Fencing', 24: 'Figure Skating'\n25: 'Football',  26: 'Freestyle Skiing', 27: 'Golf', 28: 'Gymnastics', 29: 'Handball', 30: 'Hockey'\n31:'Ice Hockey',  32: 'Jeu De Paume', 33: 'Judo', 34: 'Lacrosse', 35: 'Luge', 36: 'Military Ski Patrol'\n37: 'Modern Pentathlon',  38: 'Motorboating', 39: 'Nordic Combined', 40: 'Polo', 41: 'Racquets'\n42: 'Rhythmic Gymnastics',  43: 'Roque', 44: 'Rowing', 45: 'Rugby', 46: 'Rugby Sevens', 47: 'Sailing'\n48: 'Shooting',  49: 'Short Track Speed Skating', 50: 'Skeleton', 51: 'Ski Jumping', 52: 'Snowboarding'\n53: 'Softball',  54: 'Speed Skating', 55: 'League of Legends', 56: 'Swimming',57: 'Synchronized Swimming'\n58: 'Table Tennis,  59: 'Taekwondo', 60: 'Tennis', 61: 'Trampolining', 62: 'Triathlon', 63: 'Tug-Of-War'\n64: 'Volleyball',  65: 'Water Polo', 66: 'Weightlifting', 67: 'Wrestling''\033[0m'")
    print('Escolha os esportes botando index (ex:\033[92m\033[1m 1 2 3\033[0m )\nequivale á (\033[92m\033[1m Aeronautics, Alpine Skiing, Alpinism\033[0m ),\nOu use "\033[92m\033[1mall\033[0m ":todos esportes disponíveis\nOu use "\033[92m\033[1mbons\033[0m":10 esportes bons ')

    while True:
        user_input = input("Esportes: ")
        if user_input.lower() == 'all':
            return list(sports.values())
        if user_input.lower() == 'bons':
            user_input = "9 11 14 28 56 64 20 6"
        if utils.match([user_input],["quit","quits"]):
            return

        # limpamos a string caso tenha algo não numerico
        index_para_esportes= [int(n) for n in re.sub(r"([^\d])+"," ",user_input.strip()).split()]

        # Testamos se existe alguma chave que não é válida
        if utils.match(index_para_esportes,sports.keys()) != len(index_para_esportes):
            print("Escolha apenas numeros válidos de 1-67")
            continue
        else:
            # Se for válido podemos sair do loop e informamos os esportes escolhidos
            chosen_sports= list(set([sports[n] for n in index_para_esportes]))
            print(f"\nSeus Esportes escolhidos são: {chosen_sports}\n")
            break
    return chosen_sports


# Escolher um intervalo
def chooseYears():
    print('Escolha o intervalo dentre dois anos que deseja \n(ex: \033[92m\033[1m1986 2002\033[0m) equivale á de 1986 até 2002.\nOu use "\033[92m\033[1mall\033[0m":todos anos disponíveis' )
    while True:
        user_input = input("Intervalo de anos: ")
        # Se all for digitado, todos os anos de olimipadas são considerados
        if user_input.lower() == 'all':
            return ([str(n) for n in range(1896,2016)],[1896,2016])
        # Se digitarmos quit sairmos da função
        if utils.match([user_input],["quit","quits"]):
            return

        # Tiramos qualquer char que não seja número e separamos em exatamente duas strings.
        intervalo = re.sub(r"([^\d])+"," ",user_input.strip()).split(" ",1)
        # Se não tiver quatro algarismos cada numero, repetimos o processor
        if intervalo.__len__() == 1:
            _ = int(intervalo[0])
            intervalo =  [_,_]
            break
        # Se for quatro algarismos cada, então deu bom, logo saimos do loop
        if len(intervalo[0]) == 4 and len(intervalo[1]) == 4:
            intervalo = [int(n) for n in intervalo]
            break
        else:
            print("desculpa, acho que você esqueceu que são quatro algarismos separados por um espaço\n Tente '1986 2002'")

    # Criamos uma lista de todos os anos entre o intervalo
    lista_anos = [str(n) for n in range(intervalo[0],intervalo[1]+1)]
    print(f"Intervalo escolhido vai de {intervalo[0]} até {intervalo[1]}")

    # Caso não haja nenhum ano entre o intervalo, retornamos esse função novamente
    if lista_anos.__len__() <= 0 :
        print("Por favor entre um invervalo não vazio")
        return chooseYears()
    # Retornamos lista de anos, e o começo da lista e final da lista como "invertalo"
    return [lista_anos,intervalo]
