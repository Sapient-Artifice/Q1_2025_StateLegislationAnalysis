# AI Policy Legislative Data – Q1 2025

This repository documents our comprehensive review of U.S. federal and state artificial intelligence legislation introduced during Q1 2025. It includes curated datasets, structured analysis scripts, and visual outputs exploring legislative trends, jurisdictional conflicts, and policy focus areas across the nation.

The work supports policymakers, journalists, and researchers seeking a fast, credible understanding of the fast-moving AI policy landscape in the U.S.

📌 Project Overview

Between January and March 2025, over 590 AI-related state bills and 28 federal proposals were introduced. Our project tracked, categorized, and compared these initiatives across 13 core AI policy domains, highlighting areas of alignment, misalignment, and legal uncertainty between state and federal levels.

This repository provides:
-    Primary legislative data (state + federal) in CSV format
-    Policy conflict mapping across jurisdictions
-    Sentiment and theme analysis of legislative language
-    Python scripts for visualization and transformation
-    Plot visualizations (.png) 

This work complements our in-depth Substack article:
[“Navigating the AI Policy Storm”]([https://sapientartifice.substack.com](https://open.substack.com/pub/sapientartifice/p/navigating-the-ai-policy-storm?r=58tol0&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false))

📁 Repository Structure
```
├── csv/                # All cleaned and derived datasets + associated README files
│   ├── README_AI_Legislation_Tracker_2025.md
│   ├── README_AI_Policy_Conflict_Map_Q1_2025.md
│   └── README_FedData.md
├── python_scripts/     # Python analysis and visualization scripts
├── png/                # Final visual outputs (charts, heatmaps, maps, etc.)
├── README.md           # (this file)
```
📂 csv/

This directory contains all core datasets used in the analysis, including:
-    State-level legislation tracker (594 bills across 46 states)
-    Federal legislation summary and metadata
-    Policy conflict map comparing state and federal actions across 13 AI topics
-    Sentiment scores, dominant themes, and top issues per state
Each subtopic includes its own detailed README:
-    README_AI_Legislation_Tracker_2025.md
-    README_AI_Policy_Conflict_Map_Q1_2025.md
-    README_FedData.md
📂 python_scripts/

All scripts used for data transformation, visualization, and analysis. Each script is self-contained and assumes relevant CSV data is already loaded locally. Common libraries include pandas, matplotlib, seaborn, plotly, and sklearn.

Highlights:
-    Topic conflict heatmaps
-    Sentiment and subjectivity analysis
-    Policy theme clustering and word clouds
-    Federal vs. state coverage normalization
See inline docstrings or comments in each script for usage.
📂 png/

Exported charts, plots, and heatmaps generated from the analysis scripts.
-    Data visualizations: theme clustering, state and federal activity and comparisons.
-    Policy classification: Manual and NLP-aided topic tagging based on bill content.
-    Conflict scoring: Evaluated for alignment, risk, and fragmentation between state and federal approaches.
-    Sentiment analysis: Applied TextBlob to derive polarity and subjectivity for each bill summary or excerpt.

  Note: FederalBillsPerYear.png came from [R-Street](https://www.rstreet.org/commentary/how-do-we-measure-what-congress-has-accomplished/)

  ⚖️ License

This repository is licensed under the MIT License.
  
  AI Policy Legislative Data – Q1 2025
  
  Sapient Artifice, 2025.
  
  https://sapientartifice.com
  

📬 Contact & Contributions

For corrections, suggestions, or to contribute:

📧 contact@sapientartifice.com

