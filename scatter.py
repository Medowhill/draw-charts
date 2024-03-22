import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, FixedLocator


class Data:
    def __init__(self, xs, ys, label=None, marker=None, color=None, edgecolor=None):
        self.xs = xs
        self.ys = ys
        self.marker = marker
        self.label = label
        self.color = color
        self.edgecolor = edgecolor


def draw(
    data,
    filename,
    xlabel=None,
    ylabel=None,
    legend=False,
    legend_loc="upper left",
    legend_bbox=None,
    pointsize=60,
    pointalpha=0.7,
    edgewidth=1,
    fontsize=18,
    width=6,
    height=6,
    ylog=False,
    x_tick_positions=None,
    y_tick_positions=None,
    facecolor="white",
    labelcolor="black",
    tickcolor="black",
    bordercolor="black",
    tickwidth=1,
    borderwidth=1,
    borders=["left", "right", "top", "bottom"],
    pdf=True,
    dpi=300,
):
    fig = plt.figure(figsize=(width, height), facecolor=facecolor)
    ax = fig.add_subplot(1, 1, 1, facecolor=facecolor)

    for d in data:
        ax.scatter(
            d.xs,
            d.ys,
            s=pointsize,
            alpha=pointalpha,
            edgecolors=d.edgecolor,
            linewidths=edgewidth,
            marker=d.marker,
            label=d.label,
            color=d.color,
        )

    if legend:
        ax.legend(fontsize=fontsize, loc=legend_loc, bbox_to_anchor=legend_bbox)

    if ylog:
        ax.set_yscale("log")

    if x_tick_positions:
        ax.xaxis.set_major_locator(FixedLocator(x_tick_positions))
        ax.xaxis.set_minor_locator(FixedLocator([]))
    if y_tick_positions:
        ax.yaxis.set_major_locator(FixedLocator(y_tick_positions))
        ax.yaxis.set_minor_locator(FixedLocator([]))

    if xlabel:
        ax.xaxis.label.set_color(labelcolor)
        ax.set_xlabel(xlabel, fontsize=fontsize)
    if ylabel:
        ax.yaxis.label.set_color(labelcolor)
        ax.set_ylabel(ylabel, fontsize=fontsize)

    ax.tick_params(axis="x", labelsize=fontsize, colors=tickcolor, width=tickwidth)
    ax.tick_params(axis="y", labelsize=fontsize, colors=tickcolor, width=tickwidth)

    for b in borders:
        ax.spines[b].set_color(bordercolor)
        ax.spines[b].set_linewidth(borderwidth)
    for b in ["left", "right", "top", "bottom"]:
        if b not in borders:
            ax.spines[b].set_visible(False)

    if pdf:
        fn = f"{filename}.pdf"
        plt.savefig(fn, bbox_inches="tight", pad_inches=0.05)
    else:
        fn = f"{filename}.png"
        plt.savefig(fn, dpi=dpi, bbox_inches="tight", pad_inches=0.05)


def read(file):
    xs = []
    ys = []
    with open(file, "r") as f:
        for line in f:
            line = line.split()
            xs.append(float(line[0]))
            ys.append(float(line[1]))
    return xs, ys

color = "black"
# color = "#2e3c7e"

# xs, ys = read("qtime.txt")
# d = Data(xs, ys)
# draw([d], "qtime", width=12, height=5, fontsize=18, xlabel="Qubits", ylabel="Time (s)")

# xs, ys = read("ctime.txt")
# d1 = Data(xs, ys, color="blue", marker="o", label="Concrat")
# xs, ys = read("gtime.txt")
# d2 = Data(xs, ys, color="red", marker="^", label="Goblint")
# draw(
#     [d1, d2],
#     "atime",
#     width=5,
#     height=3,
#     pointsize=100,
#     fontsize=20,
#     xlabel="Rust LOC",
#     ylabel="Time (s)",
#     legend=True,
#     legend_loc="upper right",
#     ylog=True,
# )

xs, ys = read("nopcrat-atime.txt")
d1 = Data(xs, ys, color="gray", edgecolor="black", marker="o")
draw(
    [d1],
    "atime",
    width=8,
    height=2.5,
    pointsize=80,
    fontsize=16,
    xlabel="Rust LOC",
    ylabel="Time (s)",
    x_tick_positions=[0, 50000, 100000, 150000],
    y_tick_positions=[0, 50, 100, 150, 200],
    # tickcolor=color,
    # labelcolor=color,
    # bordercolor=color,
    # borders=["left", "bottom"],
    # tickwidth=2,
    # borderwidth=2,
    # edgewidth=1.5,
    # pointalpha=1,
    # pdf=False,
)

xs, ys = read("nopcrat-ttime.txt")
d1 = Data(xs, ys, color="gray", edgecolor="black", marker="o")
draw(
    [d1],
    "ttime",
    width=8,
    height=2.5,
    pointsize=80,
    fontsize=16,
    xlabel="Rust LOC",
    ylabel="Time (s)",
    x_tick_positions=[0, 50000, 100000, 150000],
    y_tick_positions=[0, 0.5, 1, 1.5],
)
