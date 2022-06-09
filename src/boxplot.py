import matplotlib.pyplot as plt
import graph
import utils
from csvdata import data

# Filtragem de ano e idade
def filtreBoxPlot(anos=[]):
    def filter(lista: list):
        # "ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Year","Season","City","Sport","Event","Medal"
        Age,Year= (lista[3],lista[9])
        # Caso ano or idade seja desconhecida ignoramos
        if (Age == "NA" or Year == "NA"):
            return False

        else:
            if utils.match(anos,[Year]):
                return (int(Year),int(Age))
    return filter


def gerarGraficoBoxplot(url, name="boxplot",anos=[]):
    # Pegamos dados do CSV com o devido filtro

    dados = data(url, filter=filtreBoxPlot(anos))

    # Pegado o dicionario com lista com cada valor encontrado como value,
    # depois transformamos esse dicionario em lista de keys e values como axis
    axis = utils.sortdict(utils.dictlist(dados['linhas']))
    if len(axis[0]) == 0:
        print("\nNão existem competidores nessa sessão")
        return 

    # Passamos o axis para o boxplot e o criamos
    graph.createBoxplot(axis, title=f"Idade dos atletas olímpicos de {anos[0]} à {anos[-1]}")
    # Salvamos plot Atual
    graph.saveExistingPlot(filename=name)

