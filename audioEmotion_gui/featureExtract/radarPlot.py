import numpy as np
import pylab as pl
import pandas as pd
#
# output1 = 'output1.csv'
# emo1 = pd.read_csv(output1, sep=',', header=0)
# dataEmo1 = emo1.values
#
# category1 = emo1['category1'].tolist()
# anger = emo1['anger'].tolist()
# boredom = emo1['boredom'].tolist()
# disgust = emo1['disgust'].tolist()
# sadness = emo1['sadness'].tolist()
# fear = emo1['fear'].tolist()
# happiness = emo1['happiness'].tolist()
# neutral_1 = emo1['neutral_1'].tolist()
# sadness = emo1['sadness'].tolist()
#
# print sadness
# print neutral_1
# print neutral_1

class Radar(object):

    def __init__(self, fig, titles, labels, rect=None):
        if rect is None:
            rect = [0.15, 0.15, 0.7, 0.7]

        self.n = len(titles)
        self.angles = np.arange(30, 30+360, 360.0/self.n)
        self.axes = [fig.add_axes(rect, projection="polar", label="axes%d" % i)
                         for i in range(self.n)]

        self.ax = self.axes[0]
        self.ax.set_thetagrids(self.angles, labels=titles, fontsize=10)

        for ax in self.axes[1:]:
            ax.patch.set_visible(False)
            ax.grid("off")
            ax.xaxis.set_visible(False)

        for ax, angle, label in zip(self.axes, self.angles, labels):
            ax.set_rgrids(range(1, 6), angle=angle, labels=label)
            ax.spines["polar"].set_visible(False)
            ax.set_ylim(0, 5)

    def plot(self, values, *args, **kw):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        print values
        values = np.r_[values, values[0]]

        self.ax.plot(angle, values, *args, **kw)



# fig = pl.figure(figsize=(6, 6))
#
# titles = ["a","b","c","d","e"]
#
# labels = [
#     [0.2, 0.4, 0.6, 0.8, 1.0],  [0.2, 0.4,0.6,0.8,1.0],  [0.2, 0.4,0.6,0.8,1.0],
#     [0.2, 0.4,0.6,0.8,1.0],
#     [0.2, 0.4, 0.6, 0.8, 1.0], [0.2, 0.4,0.6,0.8,1.0]
# ]
#
# radar = Radar(fig, titles, labels)
# radar.plot([0, 0.2, 0.4, 0.4, 0.5],  "-", lw=2, color="b", alpha=0.4, label="first")
# radar.ax.legend()
# pl.show()