import utils
from csvdata import data


# ##### Funcções FILTRAGEM de seleção, por esporte, ano, e sexo

def filtreMedal(medalha:str):
    def filter(lista: list):
        # "ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Year","Season","City","Sport","Event","Medal"
        Name, Medal = (lista[1],lista[-1])
        
        # Caso medalha ou nome seja desconhecido não pegamos elemento
        if (Medal == "NA" or Name == "NA"):
            return False
        # Caso uma medalha não for especificada, damos default em Medal como vem, ou seja, qualquer uma,
        # e, portanto, medal == Medal dara true 
        medal = medalha or Medal
        if medal == Medal:
            return (Name,Medal)
    return filter


def gerarRespostaTextual(medalha = "Gold"):
    # Geramos dados a partir do url, filtramos a medalha que queremos
    dados = data(url="./assets/athlete_events.csv",filter=filtreMedal(medalha.lower().capitalize()))

    # Pegamos a Quantidade de medalhas por nome
    nomes_medalhas = utils.todict(list(dados['axis'](tipo="Quantidade")))

    # Pegamos a chave com mais medalhas
    nome_com_mais_medalhas = utils.biggerkey(nomes_medalhas)
    
    # Disponibilizamos para o usuario
    print(f"\nJogados com mais medalha de {medalha} é: {nome_com_mais_medalhas[0]}, com {nome_com_mais_medalhas[1]} medalhas.")




