import graph


def gerarGraficoDeLinha(dados, sex = "M", name="linha", cor="#FF6600", text=("label1", "label2", "label2",)):

   # Buscando axis x and y
   axis = dados['axis'](filter=filtreSexo(sex), tipo="M")

	# Setting Names for plot 
   title,xlabel,ylabel = text
   graph.createPlot(axis, xlabel, ylabel, title, color=cor)
   graph.saveExistingPlot(filename=name)

## Filtragem de dados
def filtragem(lista: list):
	Sex,Year,Age,Medal = (lista[2], lista[9], lista[3],lista[-1])
	# Se medalha ou age é desconhecida ignoramos
	if Medal == 'NA' or Age == 'NA':
		return False
	else: 
		return (Sex,Year,Age)


# Fitra sexo F ou M
def filtreSexo(sexo:str):
   sexo = sexo.upper()[0]
   def filter(lista):
       Sex,Year,Age = lista
       if Sex == sexo:
           return (int(Year), int(Age))
       return False
   return filter


