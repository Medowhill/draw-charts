import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter


def draw(data, tick, legend, colors, yticks, ylabel, filename, legend_loc="upper left"):
    dim = len(data[0])
    w = 0.8
    dimw = w / dim

    fig, ax = plt.subplots(figsize=(len(data), 4))
    x = np.arange(len(data))
    for i in range(len(data[0])):
        y = [d[i] for d in data]
        b = ax.bar(x + i * dimw, y, dimw, color=colors[i])
    ax.legend(legend, fontsize=18, loc=legend_loc)

    ax.set_xticks(x + dimw * (dim - 1) / 2, labels=map(lambda x: tick[x], x))
    plt.xticks(rotation=40, ha="right", va="top")
    plt.yticks(yticks)

    ax.set_ylabel(ylabel, fontsize=18)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x):,}"))

    ax.tick_params(axis="x", labelsize=18)
    ax.tick_params(axis="y", labelsize=18)

    ax.margins(x=0.005)

    fn = f"{filename}.pdf"
    plt.savefig(fn, bbox_inches="tight", pad_inches=0.05)


def read(file):
    data = []
    tick = []
    with open(file, "r") as f:
        for line in f:
            line = line.split()
            tick.append(line.pop(0))
            data.append([float(s) for s in line])
    return data, tick


data, tick = read("tokens.txt")
draw(
    data=data,
    tick=tick,
    legend=["Simcrat", "Simcrat-f", "Simcrat-a", "Simcrat-fa", "Simcrat-c"],
    colors=["black", "red", "green", "blue", "gray"],
    yticks=np.arange(0, 1200000, 200000),
    ylabel="Tokens",
    filename="tokens",
)

data, tick = read("time.txt")
draw(
    data=data,
    tick=tick,
    legend=["Simcrat", "Simcrat-f", "Simcrat-a", "Simcrat-fa", "Simcrat-c"],
    colors=["black", "red", "green", "blue", "gray"],
    yticks=np.arange(0, 5000, 1000),
    ylabel="Time (s)",
    filename="time",
)

data, tick = read("errors.txt")
draw(
    data=data,
    tick=tick,
    legend=["Simcrat", "Simcrat-f", "Simcrat-a", "Simcrat-fa"],
    colors=["black", "red", "green", "blue"],
    yticks=np.arange(0, 400, 50),
    ylabel="Type Errors",
    filename="errors",
)

data, tick = read("sigs.txt")
draw(
    data=data,
    tick=tick,
    legend=["Simcrat", "Simcrat-c"],
    colors=["black", "gray"],
    yticks=np.arange(0, 50, 10),
    ylabel="Modernized Signatures",
    filename="sigs",
)

data, tick = read("category.txt")
draw(
    data=data,
    tick=tick,
    legend=["Simcrat", "Simcrat-c"],
    colors=["black", "gray"],
    yticks=np.arange(0, 600, 100),
    ylabel="Modernized Signatures",
    filename="category",
    legend_loc="upper right",
)
