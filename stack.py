import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter, FixedLocator


def draw(
    data,
    categories,
    colors,
    labels,
    filename,
    xlabel=None,
    ylabel=None,
    fontsize=18,
    height=6,
    legend=None,
    legend_loc="upper left",
    legend_bbox=None,
    bottom=None,
    minor_tick_positions=None,
    percent=False,
    facecolor="white",
    w=0.8,
):
    bar_positions = np.arange(len(categories))
    left = np.zeros(len(categories))

    fig = plt.figure(figsize=(height, len(data) * 0.8), facecolor=facecolor)
    ax = fig.add_subplot(1, 1, 1, facecolor=facecolor)

    for i in range(len(data)):
        ax.barh(bar_positions, data[i], w, left=left, label=labels[i], color=colors[i])
        left += data[i]

    ax.set_yticks(bar_positions)
    ax.set_yticklabels(categories)
    ax.legend(fontsize=fontsize, loc=legend_loc, bbox_to_anchor=legend_bbox)

    if xlabel:
        ax.set_xlabel(xlabel, fontsize=fontsize)

    if ylabel:
        ax.set_ylabel(ylabel, fontsize=fontsize)

    ax.xaxis.set_major_formatter(mtick.PercentFormatter(1))
    ax.xaxis.set_minor_formatter(mtick.PercentFormatter(1))

    ax.tick_params(axis="x", labelsize=fontsize)
    ax.tick_params(axis="y", labelsize=fontsize)

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


# data0 = [0.136, 0.112, 0.752]
# data1 = [0.124, 0.140, 0.736]
# data2 = [0.041, 0.117, 0.842]
# data3 = [0.026, 0.114, 0.860]
# data4 = [0.026, 0.112, 0.862]
# data = np.array([data4, data3, data2, data1, data0])
# data = np.rot90(data, k=-1)
# categories = ["0", "1", "2", "3", "4"]
# draw(
#     data=data,
#     categories=categories,
#     colors=["black", "gray", "silver"],
#     labels=["Unmigrated", "Partial", "Full"],
#     filename="signatures",
#     ylabel="# of signatures",
#     legend_bbox=(1, 1),
#     fontsize=15,
#     w=0.7,
# )

# datac = [0.861, 0.015, 0.124]
# datal = [0.802, 0.029, 0.169]
# data0 = [0.091, 0.117, 0.792]
# data1 = [0.189, 0.151, 0.660]
# data2 = [0.049, 0.103, 0.848]
# data3 = [0.034, 0.077, 0.889]
# data4 = [0.046, 0.079, 0.875]
# data = np.array([data4, data3, data2, data1, data0, datal, datac])
# data = np.rot90(data, k=-1)
# categories = ["C2Rust", "Laertes", "0", "1", "2", "3", "4"]
# draw(
#     data=data,
#     categories=categories,
#     colors=["black", "gray", "silver"],
#     labels=["Unmigrated", "Partial", "Full"],
#     filename="laertes",
#     ylabel="# of signatures",
#     legend_bbox=(1, 1),
#     fontsize=15,
#     w=0.7,
# )

# datac2 = [0.746, 0.019, 0.235]
# datac = [0.711, 0.054, 0.235]
# data0 = [0.129, 0.078, 0.793]
# data1 = [0.200, 0.126, 0.674]
# data2 = [0.054, 0.111, 0.835]
# data3 = [0.042, 0.100, 0.858]
# data4 = [0.037, 0.104, 0.859]
# data = np.array([data4, data3, data2, data1, data0, datac, datac2])
# data = np.rot90(data, k=-1)
# categories = ["C2Rust", "Concrat", "0", "1", "2", "3", "4"]
# draw(
#     data=data,
#     categories=categories,
#     colors=["black", "gray", "silver"],
#     labels=["Unmigrated", "Partial", "Full"],
#     filename="concrat",
#     ylabel="# of signatures",
#     legend_bbox=(1, 1),
#     fontsize=15,
#     w=0.7,
# )

datac2 = [0.861, 0.005, 0.134]
datac = [0.641, 0.143, 0.216] 
data0 = [0.093, 0.067, 0.840]
data1 = [0.101, 0.121, 0.778]
data2 = [0.026, 0.086, 0.888]
data3 = [0.018, 0.060, 0.922]
data4 = [0.020, 0.061, 0.919]
data = np.array([data4, data3, data2, data1, data0, datac, datac2])
data = np.rot90(data, k=-1)
categories = ["C2Rust", "Crown", "0", "1", "2", "3", "4"]
draw(
    data=data,
    categories=categories,
    colors=["black", "gray", "silver"],
    labels=["Unmigrated", "Partial", "Full"],
    filename="crown",
    ylabel="# of signatures",
    legend_bbox=(1, 1),
    fontsize=15,
    w=0.7,
)
