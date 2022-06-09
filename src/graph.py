import sys
sys.path.append('./src')
import matplotlib.pyplot as plt
import numpy as np
# conta quantas vezes uma lista aparece na outra

# Mostra e  salva um plot que já existe aberto 
def saveExistingPlot(filename="default.png"):
    plt.tight_layout()
    plt.savefig(f"./graphs/{filename}", dpi=100)
    plt.show(block=False)
    plt.pause(0.001) # Pause for interval seconds.
    input("Aperte [enter] para fechar plot.")
    plt.close('all') # all open plots are correctly closed after each run
    plt.close()

# Cria uma barra
def createBar(axis=[(1, 2), (2, 2)], width=0.35, offset: int = 1, color="#FF66aa", label="label",style='fivethirtyeight',bar=True):
    x, y = axis
    x_index = np.arange(len(x))

    # Mudar estilo
    plt.style.use(style)
    # Labels: Titulo, xLabel, yLabel
    # Criar offset para barras posteriores
    offset = width+(width*offset)

    # Ajeita o eixo X
    # Plotar o grafico de barra em si
    barra = plt.bar(x_index+offset, y, color=color, width=width,
            linestyle="-", linewidth=1.1, label=label)
    #plt.xticks(rotation=90, ticks=x_index, labels=x)
    if bar:
        plt.bar_label(barra, fmt="%.1f", fontsize = 6.2)
    plt.legend()

# Cria grafico de Linha
def createPlot(axis, xlabel, ylabel, title, color="#FF6600", size=(15, 7)):
    x, y = axis
    plt.close()
    plt.figure(figsize=size)
    plt.style.use('fivethirtyeight')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(x, y, color=color, linestyle="-", linewidth=2.2)

# Cria um grafico de boxplot a partir de axis
def createBoxplot(axis, xlabel="Anos", ylabel="Idade", title="Idade dos atletas olímpicos de 1896 à 2016", color="#8888ff", size=(16, 7)):
    # Atribuição para axis
    x,y = axis
    plt.close()
    plt.style.use('fivethirtyeight')
    plt.figure(figsize=size)


    ## ART & Beauty
    plt.xticks(rotation=70,fontsize=11)
    medianprops= {'linestyle':'-.', 'linewidth':1.5, 'color':color}
    flierprops={'markersize':2,'marker':'o', 'markerfacecolor':color,'markeredgecolor':'none'}

    ## Plotting
    plt.boxplot(y,labels=x, meanline=True, notch=True, medianprops=medianprops, flierprops=flierprops)
    # Textos
    plt.title(title), plt.xlabel(xlabel), plt.ylabel(ylabel)
    # Da um padding para enchergar labels
    plt.subplots_adjust(bottom=0.2)
