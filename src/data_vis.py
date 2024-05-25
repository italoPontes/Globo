import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation(df: pd.DataFrame = [],
                     method: str = "spearman"):
    """
    Plota um heatmap de correlação triangular de um DataFrame.

    Parâmetros:
    df (pd.DataFrame): DataFrame contendo os dados.
    method (str): Método de correlação a ser usado
    ('pearson', 'kendall', 'spearman').
    """
    plt.figure(figsize=(16, 6))

    correlation = df.corr(method=method)
    mask = np.triu(np.ones_like(correlation, dtype=bool))
    graph_corr = sns.heatmap(correlation,
                             mask=mask,
                             vmin=-1,
                             vmax=1,
                             annot=True,
                             fmt=".2f",
                             cmap='BrBG')
    graph_corr.set_title('Triangle Correlation Heatmap',
                         fontdict={'fontsize': 18},
                         pad=16)
    plt.show()
