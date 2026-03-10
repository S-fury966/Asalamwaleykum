import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(scores, labels):

    matrix = [[s] for s in scores]

    plt.figure(figsize=(6,6))

    sns.heatmap(
        matrix,
        annot=True,
        cmap="coolwarm",
        yticklabels=labels,
        xticklabels=["Stability"]
    )

    plt.title("LLM Stability Heatmap")

    plt.show()