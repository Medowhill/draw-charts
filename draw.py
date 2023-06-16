import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter, FixedLocator


def draw(
    data,
    tick,
    colors,
    filename,
    ylabel=None,
    fontsize=18,
    height=6,
    legend=None,
    legend_loc="upper left",
    log_scale=False,
    legend_bbox=None,
    bottom=None,
    minor_tick_positions=None,
    percent=False,
    facecolor="white",
):
    dim = len(data[0])
    w = 0.8
    dimw = w / dim

    fig = plt.figure(figsize=(len(data), height), facecolor=facecolor)
    ax = fig.add_subplot(1, 1, 1, facecolor=facecolor)

    x = np.arange(len(data))
    for i in range(len(data[0])):
        y = [d[i] - (bottom if bottom else 0) for d in data]
        b = ax.bar(x + i * dimw, y, dimw, bottom=bottom, color=colors[i])

    if legend:
        ax.legend(legend, fontsize=fontsize, loc=legend_loc, bbox_to_anchor=legend_bbox)

    ax.set_xticks(x + dimw * (dim - 1) / 2, labels=map(lambda x: tick[x], x))
    plt.xticks(rotation=40, ha="right", va="top")

    if log_scale:
        ax.set_yscale("log")

    if minor_tick_positions:
        ax.yaxis.set_minor_locator(FixedLocator(minor_tick_positions))

    if ylabel:
        ax.set_ylabel(ylabel, fontsize=fontsize)

    for tick in ax.yaxis.get_minor_ticks():
        tick.label1.set_fontsize(fontsize)

    if percent:
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(1))
        ax.yaxis.set_minor_formatter(mtick.PercentFormatter(1))
    else:
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x):,}"))
        ax.yaxis.set_minor_formatter(FuncFormatter(lambda x, pos: f"{int(x):,}"))

    ax.tick_params(axis="x", labelsize=fontsize)
    ax.tick_params(axis="y", labelsize=fontsize)

    ax.margins(x=0.005)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

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


facecolor = "#f6f8fa"

data, tick = read("tokens.txt")
draw(
    data=data,
    tick=tick,
    legend=["Simcrat", "Simcrat-f", "Simcrat-a", "Simcrat-fa", "Simcrat-c"],
    colors=["black", "red", "green", "blue", "gray"],
    ylabel="Tokens",
    filename="tokens",
    facecolor=facecolor,
)

data, tick = read("time.txt")
draw(
    data=data,
    tick=tick,
    legend=["Simcrat", "Simcrat-f", "Simcrat-a", "Simcrat-fa", "Simcrat-c"],
    colors=["black", "red", "green", "blue", "gray"],
    ylabel="Time (s)",
    filename="time",
    facecolor=facecolor,
)

data, tick = read("errors.txt")
draw(
    data=data,
    tick=tick,
    legend=["Simcrat", "Simcrat-f", "Simcrat-a", "Simcrat-fa"],
    colors=["black", "red", "green", "blue"],
    ylabel="Type Errors",
    filename="errors",
    facecolor=facecolor,
)

data, tick = read("sigs.txt")
draw(
    data=data,
    tick=tick,
    legend=["Simcrat", "Simcrat-c"],
    colors=["black", "gray"],
    ylabel="Modernized Signatures",
    filename="sigs",
    facecolor=facecolor,
)

data, tick = read("category.txt")
draw(
    data=data,
    tick=tick,
    legend=["Simcrat", "Simcrat-c"],
    colors=["black", "gray"],
    ylabel="Modernized Signatures",
    filename="category",
    legend_loc="upper right",
    facecolor=facecolor,
)

data, tick = read("rv6latency.txt")
draw(
    data=data,
    tick=tick,
    legend=["w/o lock", "w/ lock"],
    colors=["black", "gray"],
    ylabel="Latency (μs)",
    height=8,
    filename="rv6latency",
    log_scale=True,
    bottom=100,
    minor_tick_positions=[100, 250, 500, 750, 1000, 2500, 5000],
    legend_bbox=(0.9, 1),
    facecolor=facecolor,
)

data, tick = read("rv6bandwidth.txt")
draw(
    data=data,
    tick=tick,
    legend=["w/o lock", "w/ lock"],
    colors=["black", "gray"],
    ylabel="Bandwidth (MB/s)",
    height=8,
    filename="rv6bandwidth",
    log_scale=True,
    legend_bbox=(0.7, 1),
    facecolor=facecolor,
)

data, tick = read("rv6.txt")
draw(
    data=data,
    tick=tick,
    legend=[],
    colors=["black"],
    ylabel="Latency",
    height=20,
    filename="rv6",
    log_scale=True,
    bottom=1,
    percent=True,
    minor_tick_positions=[0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1, 1.2],
    fontsize=25,
    facecolor=facecolor,
)
