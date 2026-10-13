# Sources and figure audit trail

Every number in the brief traces to an entry below: value, unit as printed, document, publisher, date. Conversions are shown where the brief or charts restate a figure in different units. Figures carried from the Oct 12, 2026 brief (us-data-center-water-brief) were verified there against the primary documents; this package re-uses only the LBNL water figures (S1) and the USGS compilation (S2), both re-checked against this brief's data spine on October 12, 2026. All other figures in this package come from S2 and S3.

## Conversion factors used

- 1 US gallon = 3.78541 liters
- Billion gallons per day to billion liters per year: multiply by 365 x 3.78541 = 1,381.67
- Billion gallons per day to billion liters per day: multiply by 3.78541

## Definitions the brief never mixes without labels

- Withdrawal: water taken from a source. Some of it is returned (discharge).
- Consumption: water withdrawn and not returned, mostly evaporated in cooling or taken up by crops.
- Direct (onsite): water used at the data center itself.
- Indirect: water consumed generating the electricity the data center buys.

## S1. LBNL, 2024 United States Data Center Energy Usage Report

- Document: "2024 United States Data Center Energy Usage Report", Lawrence Berkeley National Laboratory, report LBNL-2001637, December 2024. Publisher site: eta.lbl.gov. (Same source as S1 in the Oct 12 brief's audit, where the full citation and page locations are recorded.)
- Direct water consumption 2014: 21.2 billion liters. Section 5, "Direct Water Consumption", p. 55.
- Direct water consumption 2023: 66 billion liters; hyperscale plus colocation facilities = 84% of the total. Same section, p. 55. Equals 17.4 billion gallons per year (converted).
- Indirect water consumption 2023: nearly 800 billion liters, consumed through electricity use. Section 5, "Indirect Water Consumption and Emissions from Electricity Use", p. 57.
- Indirect water intensity 2023: national average 4.52 L/kWh for data center electricity, vs. 4.35 L/kWh average for US electricity overall. Same section, p. 57.
- Water currency note: LBNL's June 2026 update (United States Data Center Energy Usage Report: 2025 Update, LBNL-2001758) contains no water-use estimates, so S1 remains the most recent LBNL water assessment and the water source of record for this package.
- Classification: modeled estimates by a federal laboratory with a stated method, built from equipment shipments, surveys, and metered samples. Not a census of meter readings, because no US reporting mandate exists.

## S2. USGS, Estimated Use of Water in the United States in 2015 (Circular 1441)

- Document: "Estimated Use of Water in the United States in 2015", US Geological Survey, Circular 1441 (Dieter et al.), June 2018. Summary and trends tables at usgs.gov. Geography: 50 states plus DC, Puerto Rico, and the US Virgin Islands. Single-year compilation for 2015.
- Total withdrawals 2015: 322 billion gallons per day (Bgal/d). Category withdrawals, Bgal/d as printed:
  - Thermoelectric power: 133 (41% of total)
  - Irrigation: 118 (37%)
  - Public supply: 39.0 (12%)
  - Self-supplied industrial: 14.8 (5%)
  - Aquaculture: 7.55 (2%)
  - Mining: 4.00 (1%)
  - Self-supplied domestic: 3.26 (1%)
  - Livestock: 2.00 (1%)
- Consumptive use 2015, printed for two categories only (the first national consumptive-use estimates USGS published since 1995):
  - Irrigation: 73.2 Bgal/d, stated as 62% of irrigation's total use (withdrawals plus reclaimed wastewater).
  - Thermoelectric power: 4.31 Bgal/d, about 3% of thermoelectric withdrawals. Most power-plant cooling water is returned; the gap between 133 and 4.31 Bgal/d for the same plants is the single most-abused number pair in this debate.
  - No national consumptive-use figure is printed in Circular 1441 for public supply, self-supplied industrial, livestock, aquaculture, mining, or self-supplied domestic use. Any chart or ranking in this package that needs such a figure does not exist, and the brief says why.
- Conversions used throughout this package (billion liters per year = Bgal/d x 1,381.67): total 444,899; thermoelectric withdrawals 183,763; irrigation withdrawals 163,038; public supply 53,885; industrial 20,449; aquaculture 10,432; mining 5,527; domestic 4,504; livestock 2,763; irrigation consumption 101,139; thermoelectric consumption 5,955.
- Category notes as printed in the circular's summaries: aquaculture withdrawals come mostly from flow-through raceways that return the water directly after use, so aquaculture's withdrawal rank overstates its consumption; self-supplied industrial withdrawals fell from a 1970 peak of 47 Bgal/d to 14.8 Bgal/d in 2015; irrigation was the one major category whose withdrawals rose 2010 to 2015 (+2%); thermoelectric withdrawals fell 18% over 2010 to 2015.
- Salinity note: thermoelectric's 133 Bgal/d as printed includes saline cooling water; irrigation is all freshwater. This package uses the as-published totals and runs no freshwater-only cut (see Dropped).
- Classification: federal compilation of reported and estimated use.

## S3. USGS, Professional Paper 1894, Chapter D (corroboration only)

- Document: "Water use across the conterminous United States, water years 2010-20", Chapter D of USGS Professional Paper 1894 (National Water Availability Assessment), Medalie et al. Modeled monthly estimates, conterminous US only, decade averages for water years 2010-20. Covers the three largest categories only.
- Crop irrigation: withdrawals 105,497 Mgal/d; consumptive use 75,698 Mgal/d.
- Thermoelectric power (freshwater only): withdrawals 82,656 Mgal/d; consumptive use 2,904 Mgal/d.
- Public supply: withdrawals 35,400 Mgal/d; consumptive use 4,219 Mgal/d.
- Series status, verified from USGS's own pages October 12, 2026: the quinquennial "Estimated Use of Water in the United States" Circular series ends at 2015. There is no 2020 Circular. The remaining five categories (industrial, mining, domestic, livestock, aquaculture) have post-2015 estimates released through ScienceBase data releases rather than one citable report, per USGS's "Accessing Water Use Data" page.
- Use in this package: footnote corroboration only. PP 1894 figures are NOT interchangeable with Circular 1441 figures (different geography, different basis, thermoelectric freshwater-only) and never appear in the same chart or table as S2 figures.

## Derived comparisons used in the brief, charts, and hero (all arithmetic shown)

Conversion basis: 1 Bgal/d = 1,381.67 billion liters per year; 1 Bgal/d = 3.78541 billion liters per day. Data center figures are LBNL 2023 (S1); USGS figures are 2015 (S2). Cross-year shares are labeled with both years wherever they appear.

- Data center total consumption 2023: 66 + nearly 800 = about 866 billion liters (about 229 billion gallons per year, about 0.63 Bgal/d). Derived in the Oct 12 package.
- Agriculture withdrawals (S2): irrigation 118 + livestock 2.00 = 120 Bgal/d = 165,801 billion liters per year = 37.3% of total withdrawals (derived sum: 120 / 322).
- Irrigation consumption vs. data center direct consumption: 101,139 / 66 = 1,532, stated as about 1,530x (consumption vs. consumption).
- Data center total as a share of irrigation consumption: 866 / 101,139 = 0.86% (consumption vs. consumption).
- One day of irrigation consumption: 73.2 x 3.78541 = 277.1 billion liters per day. Against data center direct consumption of 66 billion liters per year: 277.1 / 66 = 4.20, stated as about 4.2 years. Against data center total consumption per day (866 / 365 = 2.37 billion liters per day): 277.1 / 2.37 = 116.8, stated as about 117 days (about four months).
- Data center indirect water vs. thermoelectric consumptive use: 800 / 5,955 = 13.4%; data center total vs. thermoelectric consumption: 866 / 5,955 = 14.5%. NEEDS FRAMING and carries it wherever printed: this compares a part to a whole that contains it (data centers' electricity water is inside the power sector's consumption total) across a year gap (2023 vs. 2015). The two totals are never added together anywhere in this package.
- Data center direct consumption vs. total US withdrawals: 17.4 billion gallons per year / (322 Bgal/d x 365) = about 0.015%. Carried from the Oct 12 brief. Cross-measure (consumption against withdrawals); used only as an order-of-magnitude scale check with the label printed.

## Dropped during verification (not used anywhere in the brief)

- Any all-sector "who consumes the most water in America" ranking: impossible from official data, because Circular 1441 publishes national consumptive use for only two categories. The absence is reported as a finding instead of being papered over with withdrawal figures.
- A freshwater-only comparison (thermoelectric or irrigation): the splits sit in Circular 1441's data tables but were not extracted and verified for this package; the as-published totals are used and the saline inclusion is disclosed in S2.
- Golf-course irrigation and other irrigation sub-splits: not verified to a primary source for this package; the circular's published irrigation total is used as printed.
- State- or basin-level cuts (for example, irrigation vs. data centers in one state or watershed): not built; would require the circular's state tables or the ScienceBase 2020 releases, and national averages are this brief's stated scope.
- Individual ScienceBase 2020 estimates for the five smaller categories: status taken from USGS's access page only; the releases themselves were not opened, so no figure from them is used.
- Data center total consumption placed in the withdrawals table as if it were a withdrawal figure (0.63 Bgal/d vs. the smallest category, livestock at 2.00 Bgal/d): retained only as an explicitly labeled exhibit inside the withdrawals chart note of why the two tables cannot be merged. Never used as a finding or a ranking.
- "Data centers use X% of US water" built on total withdrawals (444,899 billion liters per year): a consumption-over-withdrawals ratio that flatters or damns depending on the author's intent; dropped in favor of consumption-vs-consumption ratios with both years printed.

## Predecessor package

This brief is a follow-on to "Known vs. Asserted: US Data Center Water" (Oct 12, 2026), https://github.com/adowlen/us-data-center-water-brief, whose audit trail carries the full S1/S2 citations, the hyperscaler disclosures, and the per-prompt analysis this brief does not repeat.
