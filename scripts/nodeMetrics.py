import pandas as pd

for n in range(1,8):

    resultDf = pd.DataFrame()
    
    for x in range(1,11):

        filename = f'/home/meeco/Documents/cluster-banchmark/data/lighstressappMetrics/risultatiLightstressapp{x}0%.csv'
        df = pd.read_csv(filename)

        df = df[[f"Nodo{n} CPU", f"Nodo{n} Memory"]]
        df.columns = [f"Nodo{n} CPU {x}0%", f"Nodo{n} Memory {x}0%"]
        
        resultDf = df if resultDf.empty else resultDf.join(df)
    
    resultDf.to_csv(f"/home/meeco/Documents/cluster-banchmark/data/nodesMetrics/Nodo{n}.csv", index=False)