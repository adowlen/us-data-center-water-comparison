"""Charts for the US data center water comparison brief - Machine Readable brand palette.

Every value plotted here is transcribed from a primary source document and
recorded, with its unit as printed and a full citation, in data/sources.md.
The same values live in data/stats.json keyed to their source IDs.

Comparability rules enforced in this file:
- Withdrawals and consumption are never plotted in the same bar set.
- Every bar label carries its measure, source, and year.
- Data centers' indirect (electricity) water is part of thermoelectric
  consumption; the two are never added, and the overlap is disclosed on
  the consumption chart itself.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Brand palette (same as the Oct 12, 2026 data center water brief)
CHARCOAL = "#23221F"
PAPER = "#F1E7DA"
AMBER = "#E8A33D"
TEAL = "#2AA198"
AMBER_DIM = "#8A6420"
TEAL_DIM = "#1E6E68"
GRID = "#4A453C"
TEXT = "#F1E7DA"
TEXT_DIM = "#B8AE9C"
GRAY_BAR = "#6E675C"

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "charts")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "figure.facecolor": CHARCOAL,
    "axes.facecolor": CHARCOAL,
    "axes.edgecolor": GRID,
    "axes.labelcolor": TEXT,
    "text.color": TEXT,
    "xtick.color": TEXT_DIM,
    "ytick.color": TEXT_DIM,
    "grid.color": GRID,
    "grid.alpha": 0.5,
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.titlecolor": TEXT,
})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), dpi=150, facecolor=CHARCOAL, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print("saved", name)


# ---------------------------------------------------------------------------
# (a) The consumption comparison (sources S1, S2)
# Consumption only, billion liters per year, log scale.
# USGS 2015 (Circular 1441): irrigation consumptive use 73.2 Bgal/d;
#   thermoelectric consumptive use 4.31 Bgal/d.
# LBNL 2023: data center direct consumption 66 B liters;
#   direct + indirect (electricity water, nearly 800 B liters) about 866 B.
# USGS publishes national consumption for these two categories only; there
# is no bar for industry, public supply, or livestock because no official
# national consumption figure exists for them.
# ---------------------------------------------------------------------------
items = [
    ("Irrigation, consumption (USGS 2015)", 101139, AMBER),
    ("Thermoelectric power, consumption (USGS 2015)", 5955, AMBER),
    ("Data centers, direct + electricity water (LBNL 2023)", 866, TEAL),
    ("Data centers, onsite only (LBNL 2023)", 66, TEAL),
]
items.sort(key=lambda t: t[1])
fig, ax = plt.subplots(figsize=(9.4, 5.4))
ypos = np.arange(len(items))
ax.barh(ypos, [i[1] for i in items], color=[i[2] for i in items], height=0.6)
ax.set_yticks(ypos)
ax.set_yticklabels([i[0] for i in items], fontsize=10.5)
for y, i in zip(ypos, items):
    ax.annotate(f"{i[1]:,} billion liters/yr",
                (i[1] * 1.25, y), va="center", fontsize=10, color=TEXT)
ax.set_xscale("log")
ax.set_xlim(30, 1_200_000)
ax.set_xlabel("")
ax.set_title("The consumption table that can be built: farms, power plants, data centers")
ax.grid(axis="x")
ax.set_axisbelow(True)
fig.text(0.01, -0.03,
         "Water consumption, billion liters per year, log scale. Consumption only; withdrawals\n"
         "are a different quantity and are charted separately.\n"
         "USGS publishes national consumption for irrigation and thermoelectric power only.\n"
         "Data centers' electricity water is part of thermoelectric consumption; the two are\n"
         "never added. Years differ (USGS 2015, LBNL 2023) and are labeled on every bar.",
         fontsize=9, color=TEXT_DIM)
save(fig, "consumption_comparison.png")

# ---------------------------------------------------------------------------
# (b) Withdrawals by category, USGS Circular 1441, 2015 (source S2)
# Billion gallons per day as printed. This is the complete table, shown in
# its own chart precisely because withdrawals cannot be merged with the
# consumption figures above.
# ---------------------------------------------------------------------------
cats = [
    ("Thermoelectric power", 133, "consumption published: 4.31 Bgal/d"),
    ("Irrigation", 118, "consumption published: 73.2 Bgal/d"),
    ("Public supply", 39.0, "consumption not published nationally"),
    ("Self-supplied industrial", 14.8, "consumption not published nationally"),
    ("Aquaculture", 7.55, "consumption not published nationally"),
    ("Mining", 4.00, "consumption not published nationally"),
    ("Self-supplied domestic", 3.26, "consumption not published nationally"),
    ("Livestock", 2.00, "consumption not published nationally"),
]
cats.sort(key=lambda t: t[1])
fig, ax = plt.subplots(figsize=(9.4, 5.8))
ypos = np.arange(len(cats))
ax.barh(ypos, [c[1] for c in cats], color=AMBER_DIM, height=0.6)
ax.set_yticks(ypos)
ax.set_yticklabels([c[0] for c in cats], fontsize=10.5)
for y, c in zip(ypos, cats):
    ax.annotate(f"{c[1]:g} Bgal/d - {c[2]}",
                (c[1] * 1.06, y), va="center", fontsize=9.5, color=TEXT)
ax.set_xlim(0, 320)
ax.set_xlabel("")
ax.set_title("Withdrawals are not consumption: the complete 2015 table")
ax.grid(axis="x")
ax.set_axisbelow(True)
fig.text(0.01, -0.03,
         "Withdrawals, billion gallons per day, 2015 (USGS Circular 1441). Withdrawals measure\n"
         "water taken from a source, not water used up; most cooling water is\n"
         "returned. Data centers appear in the consumption chart, not here: no data center withdrawal\n"
         "figure exists in these sources. For scale only, and cross-measure: data center total\n"
         "consumption was about 0.63 Bgal/d (LBNL 2023), below the smallest row of this table.",
         fontsize=9, color=TEXT_DIM)
save(fig, "withdrawals_table.png")

# ---------------------------------------------------------------------------
# (c) Time equivalence (derived from S1, S2; arithmetic in data/sources.md)
# One day of US irrigation consumption = 73.2 Bgal/d x 3.78541 = 277.1
# billion liters. Days to consume the same volume at each measured rate:
#   irrigation: 1 day
#   data centers, direct + indirect (866 B liters/yr = 2.37 B liters/day):
#     277.1 / 2.37 = about 117 days
#   data centers, onsite only (66 B liters/yr): 277.1 / 66 = 4.20 years
#     = 1,533 days
# ---------------------------------------------------------------------------
rows = [
    ("Irrigation (USGS 2015)", 1, AMBER, "1 day"),
    ("Data centers, direct + electricity water (LBNL 2023)", 117, TEAL,
     "about 117 days (about 4 months)"),
    ("Data centers, onsite only (LBNL 2023)", 1533, TEAL_DIM,
     "1,533 days (about 4.2 years)"),
]
rows.sort(key=lambda t: t[1], reverse=True)
fig, ax = plt.subplots(figsize=(9.4, 5.0))
ypos = np.arange(len(rows))
ax.barh(ypos, [r[1] for r in rows], color=[r[2] for r in rows], height=0.55)
ax.set_yticks(ypos)
ax.set_yticklabels([r[0] for r in rows], fontsize=10.5)
for y, r in zip(ypos, rows):
    ax.annotate(r[3], (r[1] * 1.3, y), va="center", fontsize=10.5, color=TEXT)
ax.set_xscale("log")
ax.set_xlim(0.6, 30_000)
ax.set_xlabel("")
ax.set_title("One day of irrigation consumption, at three different clocks")
ax.grid(axis="x")
ax.set_axisbelow(True)
fig.text(0.01, -0.03,
         "Days to consume 277 billion liters, log scale (derived). 277 billion liters is one day\n"
         "of US irrigation consumption (USGS 2015,\n"
         "73.2 Bgal/d). Each bar is the time that sector takes to consume the same volume at its\n"
         "measured consumption rate. Consumption only; years labeled on every row.",
         fontsize=9, color=TEXT_DIM)
save(fig, "time_equivalence.png")

print("done")
