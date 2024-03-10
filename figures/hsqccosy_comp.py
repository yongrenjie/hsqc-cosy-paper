import penguins as pg
import aptenodytes as apt

apt.thesis()

p = apt.nmrd() / '210303-7a-hsqc-cosy'

dss = pg.read(p, [
    111001,   # CLIP
    121001,   # DSE
    101001,   # TSE f=1 no relay suppression
    131001,   # HSQC-TOCSY
    21001,    # TSE f=1 with relay suppression
])

fig, axs = pg.subplots(3, 2, figsize=(5.2, 7.5))
axs[2][1].remove(); axs = axs.flat[:5]

for ds, ax in zip(dss, axs):
    ds.stage(ax, f1_bounds=(20.5, 81), f2_bounds=(1.15, 3.31), levels=3e3)
    pg.mkplot(ax)
    pg.ymove(ax)

pos = axs[4].get_position()
pos.x0 = pos.x0 + 0.25
pos.x1 = pos.x1 + 0.25
axs[4].set_position(pos)

for ax in axs[2:4]:
    p = dict(arrowstyle="->", color="#888")
    ax.annotate("", xy=(3.22, 37), xytext=(3.08, 32), arrowprops=p)
    ax.annotate("", xy=(1.96, 55), xytext=(2.10, 50), arrowprops=p)
    ax.annotate("", xy=(1.20, 38), xytext=(1.20, 45), arrowprops=p)

apt.label_axes_def(axs)
# apt.show()
apt.save(__file__)
