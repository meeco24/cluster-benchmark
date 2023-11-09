import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

for n in range(1,8):

    #lettura csv (trasformazione in pandas dataframe)
    filename = f"/home/meeco/Documents/cluster-banchmark/data/nodesMetrics/Nodo{n}.csv"
    df = pd.read_csv(filename)
    
    medieCPU = []
    marginiDiErroreCPU = []

    medieMem = []
    marginiDiErroreMem = []

    for i in range(1, 11) :
        #calcoli utilizzo cpu
        mediaCPU = df[f"Nodo{n} CPU {i}0%"].mean()                          #media
        deviazioneStandardCPU = df[f"Nodo{n} CPU {i}0%"].std()              #deviazione standard
        z = stats.norm.ppf(0.975)
        margineDiErroreCPU = z * (deviazioneStandardCPU / (10 ** 0.5))      #intervallo di confidenza al 95%
        
        medieCPU.append(mediaCPU)
        marginiDiErroreCPU.append(margineDiErroreCPU)
        
        #calcoli utilizzo memoria
        mediaMem = df[f"Nodo{n} Memory {i}0%"].mean()                       #media
        deviazioneStandardMem = df[f"Nodo{n} Memory {i}0%"].std()           #deviazione standard
        z = stats.norm.ppf(0.975)
        margineDiErroreMem = z * (deviazioneStandardMem / (10 ** 0.5))      #intervallo di confidenza al 95%
        
        medieMem.append(mediaMem)
        marginiDiErroreMem.append(margineDiErroreMem)
        
    plt.style.use('seaborn-v0_8-pastel')

    etichetteAscisse = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

    #creazione grafico utilizzo cpu (in secondi)
    plt.figure(figsize=(8, 4))
    plt.bar(etichetteAscisse, medieCPU, edgecolor='black', alpha=1, align='center')
    plt.errorbar(etichetteAscisse, medieCPU, fmt='.', yerr=marginiDiErroreCPU, capsize=4, elinewidth=1, ecolor='black', color='red', alpha=0.5)
    plt.xlabel('percentuale workload')
    plt.ylabel('secondi')
    plt.title('Utilizzo della CPU al variare del workload del cluster')
    plt.suptitle(f'Nodo{n}')
    plt.grid(axis='y', alpha=0.5)

    plt.savefig(f'/home/meeco/Documents/cluster-banchmark/charts/graficoCPUNodo{n}.png', format='png', dpi=300)

    #creazione grafico utilizzo memoria (in byte)
    plt.figure(figsize=(8, 4))
    plt.bar(etichetteAscisse, medieMem, edgecolor='black', alpha=1, color='green',align='center')
    plt.errorbar(etichetteAscisse, medieMem, fmt='.', yerr=marginiDiErroreMem, capsize=4, elinewidth=1, ecolor='black', color='red', alpha=0.5)
    plt.xlabel('percentuale workload')
    plt.ylabel('mega byte')
    plt.title('Utilizzo della Memoria al variare del workload del cluster')
    plt.suptitle(f'Nodo{n}')
    plt.grid(axis='y', alpha=0.5)

    plt.savefig(f'/home/meeco/Documents/cluster-banchmark/charts/graficoMemoryNodo{n}.png', format='png', dpi=300)


