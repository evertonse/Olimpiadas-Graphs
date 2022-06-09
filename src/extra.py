import matplotlib.pyplot as plt
from csvdata import data
from menu import chooseYears
import utils
import graph
import numpy as np

STRINGFILE = ""

# ##### Funcções FILTRAGEM de seleção, por esporte, ano, e sexo

# Filtra o tipo de medalha
def filterMedalha(medal="Gold"):
    def filtre(lista: list):
        #lista = (Year, Season, Sex, Sport, Height)
        (Country, Medal)= lista
        # Apenas adiocionamos na contagem se houver, na lista, o esporte e o ano que queremos.
        if medal == Medal:
            return (Country, Medal)
    return filtre

# Filtra Medalha de cada país
def filtrePaisMedalha(anos=[]):
    def filter(lista: list):
        global STRINGFILE
        Year,Season, Country, Medal,  = (lista[9],lista[10], lista[7], lista[-1])
        # Caso com NA são ignorados
        if (Medal == "NA" or Year == "NA" or Country == "NA"):
            return False
        if Year in anos:
            # retornamos o interessante, pais e medalha
            return (Country, Medal)
    return filter


# Filtra paises e siglas do CSV noc_regions
def filtrePaisSigla():
    def filter(lista: list):
        # NOC,region,notes
        Sigla, Country, *_ = lista
        return (Sigla,Country)
    return filter



def gerarGraficoDeBarra(url, name="extra", cores={'G':"#FDE101",'S':"#D7D7D7",'B':"#A67949"}, size=(14, 6)):
    # Pegamos os anos que serão calculados
    anos,intervalo = chooseYears()
    # Pegamos o dados com o filtro
    dados = data(url=url,filter=filtrePaisMedalha(anos))
    
	 # Façamos o titulo fazer sentido
    titulo = f"Total de Medalhas dos 5 primeiros países de {intervalo[0]} até {intervalo[1]}"


    Axis = {}
    # Para cada tipo de medalha criamos uma key em 'Axis' com o axis daquela medalha 
    for tipo in ["Gold", "Silver", "Bronze"]:
        Axis[tipo] = dados['axis'](sort = False ,finalcb = lambda x:utils.sortbyvalue(x,reverse=True), filter = filterMedalha(medal=tipo), tipo = "Q")


    # dictionary que traduz sihla para nome do pais
    paiscode = utils.dictlist(data(url = "./assets/noc_regions.csv", filter=filtrePaisSigla())['linhas'])
    # 5 Primeiros de paises e medalhas de cada axis (GOLD, SILVER, BRONZE):
    AxisGold = [list(n)[0:5] for n in Axis['Gold']]
    # A partir de quem ganhou mais ouro, buscamos os de prata e de bronze, respectivamente
    yAxisSilver = [utils.todict(Axis['Silver'])[n] for n in AxisGold[0]]
    yAxisBronze = [utils.todict(Axis['Bronze'])[n] for n in AxisGold[0]]

    # Tradução das siglas para país
    paisesnames = [paiscode[n][0] for n in AxisGold[0]]

    plt.figure(figsize=size)
    # Criamos 3 barras uma para cada tipo de medalha
    graph.createBar(axis=AxisGold, label="Ouro", color=cores['G'], offset=-2, width=0.20,style="seaborn-whitegrid")
    graph.createBar(axis=(paisesnames,yAxisSilver), label="Prata", color=cores['S'], offset=-1, width=0.20,style="seaborn-whitegrid")
    graph.createBar(axis=(paisesnames,yAxisBronze), label="Bronze", color=cores['B'], offset=0, width=0.20,style="seaborn-whitegrid")
    
    # axis x sendo ajeitado
    plt.xticks(rotation=0, ticks = np.arange(len(AxisGold[0])),labels=paisesnames,fontsize=11)
    # Labels
    [plt.title(titulo), plt.xlabel("Países"), plt.ylabel("Medalhas")]
    # Plot sendo salvado
    graph.saveExistingPlot(name)