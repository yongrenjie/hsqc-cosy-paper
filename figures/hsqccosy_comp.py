import penguins as pg
import aptenodytes as apt

apt.thesis()

p = apt.nmrd() / '210303-7a-hsqc-cosy'

dss = pg.read(p, [
    111002,   # HSQC only
    111001,   # CLIP
    121001,   # DSE
    101001,   # TSE f=1 no relay suppression
    131001,   # HSQC-TOCSY
    21001,    # TSE f=1 with relay suppression
])

fig, axs = pg.subplots(3, 2, figsize=(5.2, 7.5))

for i, ds, ax in apt.enzip(dss, axs.flat):
    # For first plot, use blue for both positive and negative contours
    # to remove the effect of multiplicity editing
    extra_kwargs = {"colors": ("#023EFF", "#023EFF")} if i == 0 else {}
    ds.stage(ax, f1_bounds=(20.5, 81), f2_bounds=(1.15, 3.31), levels=3e3,
             **extra_kwargs)
    pg.mkplot(ax)
    pg.ymove(ax)

for ax in axs[3:5]:
    p = dict(arrowstyle="->", color="#888")
    ax.annotate("", xy=(3.22, 37), xytext=(3.08, 32), arrowprops=p)
    ax.annotate("", xy=(1.96, 55), xytext=(2.10, 50), arrowprops=p)
    ax.annotate("", xy=(1.20, 38), xytext=(1.20, 45), arrowprops=p)

apt.label_axes_def(axs)
# apt.show()
apt.save(__file__)
