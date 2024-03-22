import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, FixedLocator


def draw(
    filename,
    data,
    xlabel=None,
    ylabel=None,
    legend=False,
    legend_loc="upper left",
    legend_bbox=None,
    pointsize=60,
    fontsize=18,
    width=6,
    height=6,
    xlog=False,
    ylog=False,
    x_ticks=None,
    x_tick_labels=None,
    y_tick_positions=None,
    facecolor="white",
    labelcolor="black",
    tickcolor="black",
    bordercolor="black",
    linewidth=1,
    tickwidth=1,
    borderwidth=1,
    borders=["left", "right", "top", "bottom"],
    pdf=True,
    dpi=300,
):
    fig = plt.figure(figsize=(width, height), facecolor=facecolor)
    ax = fig.add_subplot(1, 1, 1, facecolor=facecolor)

    for xvs, yvs, color in data:
        ax.plot(xvs, yvs, color=color, linewidth=linewidth)

    if legend:
        ax.legend(fontsize=fontsize, loc=legend_loc, bbox_to_anchor=legend_bbox)

    if xlog:
        ax.set_xscale("log")
    if ylog:
        ax.set_yscale("log")

    
    if x_ticks:
        ax.set_xticks(x_ticks)
        ax.xaxis.set_major_locator(FixedLocator(x_ticks))
        ax.xaxis.set_minor_locator(FixedLocator([]))
    if x_tick_labels:
        ax.set_xticklabels(x_tick_labels)

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

x_ticks = [2 ** i for i in range(17)]
x_tick_labels = [f'$2^{{{i}}}$' for i in range(16)]
x_tick_labels.append('$\infty$')

x, y = read("nopcrat-n.txt")
data = [(x, y, color)]
draw(
    "prog",
    data,
    width=8,
    height=2.5,
    xlog=True,
    y_tick_positions=[i for i in range(47, 56)],
    xlabel="Max Sensitivity",
    ylabel="# of Programs",
    fontsize=16,
    x_ticks=x_ticks,
    x_tick_labels=x_tick_labels,
    tickcolor=color,
    labelcolor=color,
    bordercolor=color,
    # borders=["left", "bottom"],
    # tickwidth=2,
    # borderwidth=2,
    # linewidth=4,
    # pdf=False,
)

x, y = read("nopcrat-fn.txt")
data = [(x, y, 'black')]
draw(
    "fn",
    data,
    width=8,
    height=2.5,
    xlog=True,
    xlabel="Max Sensitivity",
    ylabel="# of Functions",
    fontsize=16,
    x_ticks=x_ticks,
    x_tick_labels=x_tick_labels,
)

x, y = read("nopcrat-must.txt")
data = [(x, y, 'black')]
draw(
    "must",
    data,
    width=8,
    height=2.5,
    xlog=True,
    xlabel="Max Sensitivity",
    ylabel="# of Parameters",
    fontsize=16,
    x_ticks=x_ticks,
    x_tick_labels=x_tick_labels,
)

x, y = read("nopcrat-may.txt")
data = [(x, y, 'black')]
draw(
    "may",
    data,
    width=8,
    height=2.5,
    xlog=True,
    xlabel="Max Sensitivity",
    ylabel="# of Parameters",
    fontsize=16,
    x_ticks=x_ticks,
    x_tick_labels=x_tick_labels,
)

x, y = read("nopcrat-param.txt")
data = [(x, y, color)]
draw(
    "param",
    data,
    width=8,
    height=2.5,
    xlog=True,
    xlabel="Max Sensitivity",
    ylabel="# of Parameters",
    fontsize=16,
    x_ticks=x_ticks,
    x_tick_labels=x_tick_labels,
    tickcolor=color,
    labelcolor=color,
    bordercolor=color,
    # borders=["left", "bottom"],
    # tickwidth=2,
    # borderwidth=2,
    # linewidth=4,
    # pdf=False,
)

x, y = read("nopcrat-time.txt")
data = [(x, y, color)]
draw(
    "time",
    data,
    width=8,
    height=2.5,
    xlog=True,
    xlabel="Max Sensitivity",
    ylabel="Average Time (s)",
    fontsize=16,
    x_ticks=x_ticks,
    x_tick_labels=x_tick_labels,
    tickcolor=color,
    labelcolor=color,
    bordercolor=color,
    # borders=["left", "bottom"],
    # tickwidth=2,
    # borderwidth=2,
    # linewidth=4,
    # pdf=False,
)
