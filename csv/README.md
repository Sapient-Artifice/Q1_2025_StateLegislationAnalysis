# AI Policy Legislative Data – Q1 2025

This directory contains all primary datasets used in the federal and state AI legislation analysis for Q1 2025, including topic classification, sentiment analysis, and conflict mapping across jurisdictions.

## 📁 Contents

- **`AI_Conflict_Visualization_Data_Q1_2025.csv`** – Condensed version of conflict mapping with risk scores, bill counts, and short summaries for use in bubble plots and heatmaps.
- **`AI_Legislation_State_Tracker_2025.csv`** – Master dataset of 594 AI-related bills introduced at the state level across all 50 states during Q1 2025.
- **`AI_Policy_Conflict_Map_Detailed_Q1_2025.csv`** – Detailed comparison of 13 AI policy topics showing state vs. federal action, misalignments, and conflict risk scoring.
- **`FederalCongress_AI_Q1_2025_SearchResults_RAW.csv`** – Original raw search export from Congress.gov used to derive the cleaned federal bill dataset.
- **`Federal_AI_Bills_Q1_2025_Cleaned.csv`** – Cleaned dataset of 28 federal AI-related bills introduced in Q1 2025, including metadata like sponsor, committee, and categorized topics.
- **`README_AI_Legislation_Tracker_2025.md`** – Outlines the construction of the state legislation tracker, including how bills were sourced and tagged.
- **`README_AI_Policy_Conflict_Map_Q1_2025.md`** – Details the methodology and structure of the policy conflict map and its scoring.
- **`README_FedData.md`** – Describes the cleaned federal bill dataset and its structure.
- **`Sentiment_Analysis_Summary.csv`** – Aggregated sentiment scores (polarity, subjectivity) from legislative texts across jurisdictions.
- **`Top_5_AI_Legislative_Themes_Per_State_2025.csv`** – For each state, lists the top 5 legislative themes (ranked by frequency) based on AI-related proposals.
- **`dominant_filtered_theme_per_state.csv`** – Filtered version of dominant themes per state, with minor categories removed or merged.
- **`dominant_theme_per_state.csv`** – Mapped dominant legislative theme (topic) per state based on frequency analysis.
- **`state_theme_overlay_data.csv`** – Structured data used to overlay state-specific AI legislative focus areas on maps or regional plots.