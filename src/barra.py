import matplotlib.pyplot as plt
import graph
import utils
import numpy as np


# ##### Funcções FILTRAGEM de seleção, por esporte, ano, e sexo
def filterSex(sexo="F", *rest):
    def filtre(lista: list):
        #lista = (Year, Season, Sex, Sport, Height)
        Year, Season, Sex, Sport, Height = lista

        # sex é o sexo passado, mas se nada for passado então assunmi o valor de Sexo do CSV
        sex = sexo or Sex
        # Apenas adiocionamos tiver o Sexo escolhido
        if sex == Sex:
            return (Sport, int(Height))
    return filtre


def filtreBarra(esportes=[], anos=[], olimpiada=""):
    def filter(lista: list):
        # "ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Year","Season","City","Sport","Event","Medal"
        Year, Season, Sex, Sport, Height, Medal = (
            lista[9],  lista[10], lista[2],  lista[12], lista[4], lista[-1])
        # Caso os sportes ou anos ou sexo ou tipo de olimpiada não seja passado, sera considerado todos
        # Se altura é desconhecida não pegamos o elemento
        if (Medal == "NA" or Year == "NA" or Height == "NA"):
            return False

        #Caso um valor Falsy seja passado, então iremos assumir o valor pego no csv
        year, season, sports = (
            anos or [Year],
            olimpiada or Season,
            esportes or [Sport]
        )
        
        # Se o Sport esta na em sports passado nessa fn
        # E Year esta na lista de anos passado nessa dn
        # Então iremos retornar (Year, Season, Sex, Sport, Height)
        if utils.match(sports, [Sport]) and utils.match(year, [Year]):
            if Season == season:
                return (Year, Season, Sex, Sport, Height)
    return filter


def gerarGraficoDeBarra(dados, name="barra", cores=("#4472C4", "#D15656", "#25255"), size=(16, 9), olimpiada = "Winter", intervalos_de_anos = [1998,2002],esportes=[]):

    # Damos um titulo que faça sentido com o intervalo de anos escolhido
    titulo = f"Média de altura {intervalos_de_anos[0]}-{intervalos_de_anos[1]} {olimpiada}"

    # Pegamos Axis de Homens
    AxisM = dados['axis'](
        filter=filterSex(sexo="M"),
        finalcb=utils.normalizedict(esportes),
        tipo="M")
    # Pegamos Axis de Mulher
    AxisF = dados['axis'](
        filter=filterSex(sexo="F"),
        tipo="M",
        finalcb=utils.normalizedict(esportes))
    
    # Axis com esportes
    AxisSport = AxisF[0] or AxisM[0] # Doenst really matter because the data is normalized, but i wanna make it explicit


    plt.figure(figsize=size)
    # Endereitamos ticks para caber tudinho com o nome dos esportes inclinados pi/2 rad
    plt.xticks(rotation=90, ticks=np.arange(len(AxisSport)), labels=AxisSport, fontsize=10.5)
    if len(AxisSport) > 20:
        decimais = False
    else:
        decimais = True
    # Criamos 2 barras uma para cada sexo:
    graph.createBar(axis=AxisM, label="M", color=cores[1], offset=-1.5,bar=decimais)
    graph.createBar(axis=AxisF, label="F", color=cores[0], offset=-0.5,bar=decimais)

    # Setamos textos
    [plt.title(titulo), plt.xlabel("Esportes"), plt.ylabel(" Altura(cm)")]

    # Salvamos o Gráfico que existe as duas barras
    graph.saveExistingPlot(name)
