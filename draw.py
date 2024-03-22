import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter, FixedLocator


def draw(
    data,
    tick,
    colors,
    filename,
    width=1,
    xlabel=None,
    ylabel=None,
    fontsize=18,
    height=6,
    legend=None,
    legend_loc="upper left",
    legend_bbox=None,
    log_scale=False,
    bottom=None,
    minor_tick_positions=None,
    percent=False,
    facecolor="white",
    rotation=40,
):
    dim = len(data[0])
    w = 0.8
    dimw = w / dim

    width *= len(data)
    fig = plt.figure(figsize=(width, height), facecolor=facecolor)
    ax = fig.add_subplot(1, 1, 1, facecolor=facecolor)

    x = np.arange(len(data))
    for i in range(len(data[0])):
        y = [d[i] - (bottom if bottom else 0) for d in data]
        b = ax.bar(x + i * dimw, y, dimw, bottom=bottom, color=colors[i])

    if legend:
        ax.legend(legend, fontsize=fontsize, loc=legend_loc, bbox_to_anchor=legend_bbox)

    ax.set_xticks(x + dimw * (dim - 1) / 2, labels=map(lambda x: tick[x], x))
    if rotation:
        plt.xticks(rotation=rotation, ha="right", va="top")
    else:
        plt.xticks()

    if log_scale:
        ax.set_yscale("log")

    if minor_tick_positions:
        ax.yaxis.set_minor_locator(FixedLocator(minor_tick_positions))

    if xlabel:
        ax.set_xlabel(xlabel, fontsize=fontsize)

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

# data, tick = read("tokens.txt")
# draw(
#     data=data,
#     tick=tick,
#     legend=["Simcrat", "Simcrat-f", "Simcrat-a", "Simcrat-fa", "Simcrat-c"],
#     colors=["black", "red", "green", "blue", "gray"],
#     ylabel="Tokens",
#     filename="tokens",
#     facecolor=facecolor,
# )

# data, tick = read("time.txt")
# draw(
#     data=data,
#     tick=tick,
#     legend=["Simcrat", "Simcrat-f", "Simcrat-a", "Simcrat-fa", "Simcrat-c"],
#     colors=["black", "red", "green", "blue", "gray"],
#     ylabel="Time (s)",
#     filename="time",
#     facecolor=facecolor,
# )

# data, tick = read("errors.txt")
# draw(
#     data=data,
#     tick=tick,
#     legend=["Simcrat", "Simcrat-f", "Simcrat-a", "Simcrat-fa"],
#     colors=["black", "red", "green", "blue"],
#     ylabel="Type Errors",
#     filename="errors",
#     facecolor=facecolor,
# )

# data, tick = read("sigs.txt")
# draw(
#     data=data,
#     tick=tick,
#     legend=["Simcrat", "Simcrat-c"],
#     colors=["black", "gray"],
#     ylabel="Modernized Signatures",
#     filename="sigs",
#     facecolor=facecolor,
# )

# data, tick = read("category.txt")
# draw(
#     data=data,
#     tick=tick,
#     legend=["0", "1", "2", "3", "4"],
#     colors=["black", "dimgray", "gray", "darkgray", "silver"],
#     ylabel="Frequencies",
#     filename="category",
#     legend_loc="upper right",
#     log_scale=True,
#     bottom=1,
#     minor_tick_positions=[1, 5, 10, 50, 100, 500, 1000, 5000, 10000],
#     legend_bbox=(1.08, 1),
#     fontsize=14,
#     height=3,
# )

# data, tick = read("errors3.txt")
# draw(
#     data=data,
#     tick=tick,
#     legend=["Tymcrat", "Tymcrat-f", "Tymcrat-a", "Tymcrat-fa"],
#     colors=["black", "dimgray", "gray", "darkgray"],
#     xlabel="# of candidate signatures",
#     ylabel="Average # of type errors",
#     filename="errors",
#     rotation=0,
#     width=1.9,
#     height=4.3,
#     fontsize=20,
#     legend_bbox=(1.00, 1),
# )

data, tick = read("time2.txt")
draw(
    data=data,
    tick=tick,
    legend=["Tymcrat", "Tymcrat-f", "Tymcrat-a", "Tymcrat-fa"],
    colors=["black", "dimgray", "gray", "darkgray"],
    xlabel="# of candidate signatures",
    ylabel="Time (s)",
    filename="time",
    rotation=0,
    width=1.8,
    height=4.3,
    fontsize=20,
    legend_bbox=(1.00, 1),
)

# data, tick = read("rv6latency.txt")
# draw(
#     data=data,
#     tick=tick,
#     legend=["w/o lock", "w/ lock"],
#     colors=["black", "gray"],
#     ylabel="Latency (μs)",
#     height=8,
#     filename="rv6latency",
#     log_scale=True,
#     bottom=100,
#     minor_tick_positions=[100, 250, 500, 750, 1000, 2500, 5000],
#     legend_bbox=(0.9, 1),
#     facecolor=facecolor,
# )

# data, tick = read("rv6bandwidth.txt")
# draw(
#     data=data,
#     tick=tick,
#     legend=["w/o lock", "w/ lock"],
#     colors=["black", "gray"],
#     ylabel="Bandwidth (MB/s)",
#     height=8,
#     filename="rv6bandwidth",
#     log_scale=True,
#     legend_bbox=(0.7, 1),
#     facecolor=facecolor,
# )

# data, tick = read("rv6.txt")
# draw(
#     data=data,
#     tick=tick,
#     legend=[],
#     colors=["black"],
#     ylabel="Latency",
#     height=20,
#     filename="rv6",
#     log_scale=True,
#     bottom=1,
#     percent=True,
#     minor_tick_positions=[0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1, 1.2],
#     fontsize=25,
#     facecolor=facecolor,
# )

# data, tick = read("rv6louc.txt")
# draw(
#     data=data,
#     tick=tick,
#     legend=[],
#     colors=["black"],
#     ylabel="LOUC / LOC",
#     height=2.5,
#     filename="rv6louc",
#     # log_scale=True,
#     # bottom=1,
#     percent=True,
#     # minor_tick_positions=[0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1, 1.2],
#     fontsize=10,
#     facecolor=facecolor,
# )

# data, tick = read("rv6latency2.txt")
# draw(
#     data=data,
#     tick=tick,
#     legend=[],
#     colors=["black"],
#     ylabel="Latency (ms)",
#     height=6,
#     filename="rv6latency2",
#     facecolor=facecolor,
# )

# data, tick = read("sigs2.txt")
# tick[0] = "w/o candidate"
# tick[1] = "w/ candidate"
# draw(
#     data=data,
#     tick=tick,
#     legend=[],
#     colors=["black"],
#     ylabel="Modernized signatures",
#     height=6,
#     filename="sigs2",
#     facecolor=facecolor,
# )

# data, tick = read("errors2.txt")
# tick[0] = "base"
# tick[1] = "" # "callee"
# tick[2] = "" # "fix"
# tick[3] = "" # "both"
# draw(
#     data=data,
#     tick=tick,
#     legend=[],
#     colors=["black"],
#     ylabel="Type errors",
#     height=6,
#     filename="errors2",
#     facecolor=facecolor,
# )

# data, tick = read("long.txt")
# tick[0] = "diff"
# tick[1] = "find"
# tick[2] = "grep"
# tick[3] = "nano"
# tick[4] = "tar"
# tick[5] = "wget"
# draw(
#     data=data,
#     tick=tick,
#     legend=[],
#     colors=["black"],
#     ylabel="Long functions",
#     height=6,
#     filename="long",
#     facecolor=facecolor,
# )

# tick = ["0", "1", "2", "3", "4"]
# data = [[759.0], [878.0], [1214.0], [1292.0], [1318.0]]
# draw(
#     data=data,
#     tick=tick,
#     legend=[],
#     colors=["black"],
#     xlabel="# of candidate signatures",
#     ylabel="Average # of Rust types",
#     height=4.2,
#     filename="types",
#     rotation=0,
#     fontsize=20,
# )

# tick = ["0", "1", "2", "3", "4"]
# data = [[50.0], [51.0], [80.0], [86.0], [100.0]]
# draw(
#     data=data,
#     tick=tick,
#     legend=[],
#     colors=["black"],
#     xlabel="# of candidate signatures",
#     ylabel="# of distinct Rust types",
#     height=4.2,
#     filename="dtypes",
#     rotation=0,
#     fontsize=20,
# )
