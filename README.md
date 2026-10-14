# One Day of Farm Water: Data Centers vs. US Industry, With the Labels On

A data brief comparing how much water US data centers use with other US industries, agriculture included, built only on figures that measure the same thing. Follow-on to [Known vs. Asserted: US Data Center Water](https://github.com/adowlen/us-data-center-water-brief).

**Headline:** US irrigation consumed about 101 trillion liters in 2015 (USGS), the largest consumptive use the federal government measures. All US data centers together, onsite water plus the water consumed generating their electricity, consumed about 866 billion liters in 2023 (Berkeley Lab), 0.86% of irrigation consumption. Irrigation consumes in one day what data centers consume in about 117 days. The ratios usually quoted in this debate are larger or smaller than these because they compare consumption against withdrawals, two quantities that differ for power plants by a factor of 31. And the all-industry consumption ranking the debate keeps demanding cannot be built: USGS publishes national consumption figures for irrigation and thermoelectric power only.

Read the full brief: [brief/us-data-center-water-comparison.md](brief/us-data-center-water-comparison.md)

## Contents

- `brief/` - the narrative brief with findings, charts, methods, and caveats
- `charts/` - 3 charts (PNG) + hero graphic
- `data/` - `stats.json` (headline figures with source keys) and `sources.md` (per-figure audit trail: value, unit as printed, document, conversions, dropped comparisons)
- `code/` - `charts.py`, which embeds the transcribed source values and regenerates every chart

## Data sources

All primary: US Geological Survey, "Estimated Use of Water in the United States in 2015", Circular 1441 (the full category table: withdrawals for all eight categories, consumptive use for irrigation and thermoelectric power); US Geological Survey, Professional Paper 1894, Chapter D (modeled 2010-20 conterminous US estimates, used as a corroboration footnote only); Lawrence Berkeley National Laboratory, "2024 United States Data Center Energy Usage Report" (data center direct and indirect water consumption, 2014 and 2023). Full citations in `data/sources.md`.

## Reproduce

1. Read `data/sources.md` for the document, unit, and conversion behind every figure
2. Run `python code/charts.py` - charts land in `charts/`
3. Cross-check figures in `data/stats.json`

Requires Python 3 with matplotlib and numpy. The hero graphic is a composite: generated artwork with type set in PIL; its figures are the derived equivalences audited in `data/sources.md`.

## Caveats (short version)

Withdrawal is not consumption, and the two are never mixed in one figure here. USGS categories are 2015, the last compilation with a national consumptive-use split; data center figures are 2023; every cross-year figure carries both years. Data centers' indirect (electricity) water is part of thermoelectric consumption, never added to it, and its ratio to that total is printed as part-vs-whole wherever it appears. USGS publishes no national consumption figure for industry, public supply, livestock, aquaculture, mining, or domestic use, so no all-sector consumption ranking appears in this brief. Full caveats in the brief.

## Methods and data

The analysis uses the public sources listed under Data sources. The figures were transcribed from the source documents, converted with the factors stated in `data/sources.md` (1 US gallon = 3.78541 liters; billion gallons per day to billion liters per year multiplies by 1,381.67), and stored in `data/stats.json` keyed to their sources. The script in `code/` regenerates the charts from those values. Methods limits, definitions, and the full caveat set are documented in the [full brief](brief/us-data-center-water-comparison.md) and in Caveats (short version) above.

## Part of Machine Readable

This brief is part of [Machine Readable](https://adowlen.github.io/machine-readable/), the catalog of all Machine Readable briefs.


## Reuse and citation

This brief is free to cite, quote, and reuse under the CC BY 4.0 license (see LICENSE). If you use it, please credit Machine Readable and link back to this repository.

Attribution line: Machine Readable (Alex Dowlen), https://github.com/adowlen/us-data-center-water-comparison
