# AI Policy Analysis Scripts

This repository contains the Python scripts used for the AI policy visualization, analysis, and state-federal legislative comparisons as of Q1 2025. 
A lot of this work was done live with the relevant data already loaded as a data frame in the python interpreter. 
Add the following lines to any script (with foo replaced by the relevant dataFile.csv) 

```python
import pandas as pd
df = pd.read_csv('foo.csv')
```
Scripts are designed to be executed independently.

## Contents

- **`BillsByState.py`** – Visualizes bill counts by state using bar or map plots.
- **`ConflictLandscape.py`** – Creates a bubble chart showing AI policy conflict risk by topic, using federal and state bill data.
- **`Conflict_Dataframe.py`** – Constructs a unified conflict summary DataFrame for later visualization.
- **`HaetmapofConflict.py`** – Creates a heatmap of policy conflicts across topics.
- **`MapPlotterTopWord.py`** – Plots the most frequent policy keywords or topics across states using map overlays.
- **`NormalizedFedVStateTopicPercentages.py`** – Creates a normalized comparison of topic coverage percentages between federal and state levels.
- **`PCA.py`** – Applies Principal Component Analysis to AI policy text data (e.g., topic distributions).
- **`PolicyConflictHeatmap.py`** – Generates a heatmap of conflict risks across AI policy domains.
- **`PolicyCoverageHeatmap.py`** – Plots legislative coverage (not conflict) across AI domains for federal vs. state levels.
- **`SentimentDistribution.py`** – Plots the distribution of sentiment scores across legislative text samples.
- **`SentimentPolarity.py`** – Visualizes average sentiment polarity per topic or jurisdiction.
- **`SentimentSubjectivity.py`** – Visualizes subjectivity of policy discourse by source or topic.
- **`StateFocus.py`** – Plots state-level policy focus areas across the AI landscape.
- **`StateThemeClusters.py`** – Uses clustering (likely K-means) to identify state policy similarity clusters.
- **`WordCloud.py`** – Generates word clouds of legislative text per topic, state, or level.
- **`federalTopics.py`** – Plots federal topic trends by bill count or relative frequency.
- **`filtering_script_4_dominant_filtered.py`** – Filters legislative text data to extract dominant topics or patterns (likely NLP preprocessing).
