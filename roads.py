import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins, utils
import networkx as nx
from scipy.misc import imread

class LinkedView(plugins.PluginBase):
    """A simple plugin showing how multiple axes can be linked"""

    JAVASCRIPT = """
    mpld3.register_plugin("linkedview", LinkedViewPlugin);
    LinkedViewPlugin.prototype = Object.create(mpld3.Plugin.prototype);
    LinkedViewPlugin.prototype.constructor = LinkedViewPlugin;
    LinkedViewPlugin.prototype.requiredProps = ["idpts", "idline", "data"];
    LinkedViewPlugin.prototype.defaultProps = {}
    function LinkedViewPlugin(fig, props){
        mpld3.Plugin.call(this, fig, props);
    };

    LinkedViewPlugin.prototype.draw = function(){
      var pts = mpld3.get_element(this.props.idpts);
      var line = mpld3.get_element(this.props.idline);
      var data = this.props.data;

      function mouseover(d, i){
        line.data = data[i];
        line.elements().transition()
            .attr("d", line.datafunc(line.data))
            .style("stroke", this.style.fill);
      }
      pts.elements().on("mouseover", mouseover);
    };
    """

    def __init__(self, points, line, linedata):
        if isinstance(points, matplotlib.lines.Line2D):
            suffix = "pts"
        else:
            suffix = None

        self.dict_ = {"type": "linkedview",
                      "idpts": utils.get_id(points, suffix),
                      "idline": utils.get_id(line),
                      "data": linedata}

def test_plots():
    fig, ax = plt.subplots(2)

    # scatter periods and amplitudes
    np.random.seed(0)
    P = 0.2 + np.random.random(size=20)
    A = np.random.random(size=20)
    x = np.linspace(0, 10, 100)
    data = np.array([[x, Ai * np.sin(x / Pi)]
                     for (Ai, Pi) in zip(A, P)])
    points = ax[1].scatter(P, A, c=P + A,
                           s=200, alpha=0.5)
    ax[1].set_xlabel('Period')
    ax[1].set_ylabel('Amplitude')

    # create the line object
    lines = ax[0].plot(x, 0 * x, '-w', lw=3, alpha=0.5)
    ax[0].set_ylim(-1, 1)

    ax[0].set_title("Hover over points to see lines")

    # transpose line data and add plugin
    linedata = data.transpose(0, 2, 1).tolist()
    plugins.connect(fig, LinkedView(points, lines[0], linedata))

    return mpld3.fig_to_html(fig)

def world_plot():
    fig, ax = plt.subplots(2)

    # scatter periods and amplitudes
    np.random.seed(0)
    P = [350, 650, 1200, 1200, 2100]
    A = [350, 800, 250, 600, 950]
    x = np.linspace(0, 10, 100)
    data = np.array([[x, Ai * np.sin(x )]
                     for Ai in A])
    points = ax[1].scatter(P, A,
                           s=200, alpha=0.5)
    img = imread("databases\pics\worldmap.png")
    ax[1].imshow(img, zorder=0)
    ax[1].axis('off')
    ax[1].set_xlabel('Period')
    ax[1].set_ylabel('Amplitude')

    # create the line object
    lines = ax[0].plot(x, 0 * x, '-w', lw=3, alpha=0.5)
    ax[0].set_ylim(-1, 1)

    ax[0].set_title("Hover over points to see lines")

    # transpose line data and add plugin
    linedata = data.transpose(0, 2, 1).tolist()
    plugins.connect(fig, LinkedView(points, lines[0], linedata))

    return mpld3.fig_to_html(fig)


def continent_plot(name):
    fig, ax = plt.subplots(2)
    # scatter periods and amplitudes
    np.random.seed(0)
    P = [350, 650, 1200, 1200, 2100]
    A = [350, 800, 250, 600, 950]
    # To be made
    x = np.linspace(0, 10, 100)
    data = np.array([[x, Ai * np.sin(x )]
                     for Ai in A])
    points = ax[1].scatter(P, A,
                           s=200, alpha=0.5)
    img = imread("databases\pics\{}.png".format(name))
    ax[1].imshow(img, zorder=0)
    ax[1].axis('off')
    ax[1].set_xlabel('Period')
    ax[1].set_ylabel('Amplitude')

    # create the line object
    lines = ax[0].plot(x, 0 * x, '-w', lw=3, alpha=0.5)
    ax[0].set_ylim(-1, 1)

    ax[0].set_title("Hover over points to see lines")

    # transpose line data and add plugin
    linedata = data.transpose(0, 2, 1).tolist()
    plugins.connect(fig, LinkedView(points, lines[0], linedata))

    return mpld3.fig_to_html(fig)

continent_plot('australiapic')

def test_australia():
    G = nx.read_gpickle('./australia')
    fig = plt.figure()
    nx.draw_networkx(G)
    return mpld3.fig_to_html(fig)







# make the map global rather than have it zoom in to
# the extents of any plotted data
ax.set_global()
ax.stock_img()
ax.coastlines()

plt.show()


    