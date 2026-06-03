import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
x = np.arange(1, 102)                       # x = 1 ... 101
base = np.sin(2 * np.pi * x / 50.0)          # underlying sinusoid (period 50)
y = base + rng.normal(0, 0.15, size=x.size)  # scatter around the sinusoid

# nudge the last point (x=101) close to the value at x=100, so the
# manuscript-vs-replication difference is a subtle, easy-to-miss one
y[-1] = y[-2] + 0.04

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# left: Manuscript -> only 100 points (published figure drops the last one)
# right: Replication -> all 101 points (code output includes x=101)
datasets = [(x[:100], y[:100], "Manuscript"), (x, y, "Replication")]

for ax, (xx, yy, title) in zip(axes, datasets):
    ax.scatter(xx, yy, s=20)
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    for gx in range(0, 101, 10):            # vertical gridlines at 0,10,...,100
        ax.axvline(gx, color="0.8", linewidth=0.8, zorder=0)
    ax.set_xlim([-5, 105])                   # same xlimit on both

fig.tight_layout()
out = "/Users/moroa/Library/CloudStorage/Dropbox/Misc/Github/blog/assets/images/two_charts.png"
fig.savefig(out, dpi=120)
print("saved", out)
