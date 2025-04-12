
# AI Legislation State Tracker (Spring 2025)

This dataset includes **594 AI-related state legislative bills** filed across **46 U.S. states** during the **Spring 2025 legislative session**. It was created to help policymakers, researchers, journalists, and the public better understand the rapid emergence of artificial intelligence regulation at the state level.

## 📊 Dataset Overview

- **Bills included:** 594
- **States covered:** 46
- **Timeframe:** Spring 2025 legislative sessions (generally January–March)
- **File:** `AI_Legislation_State_Tracker_2025.csv`

## 🧠 Methodology

This dataset was compiled through a structured process using OpenAI’s research assistant with the following prompt executed individually for each state:

> Task: Find all artificial intelligence–related bills filed in the `<STATE>` State Legislature during the Spring 2025 legislative session. Include bills explicitly addressing AI (e.g., generative AI, facial recognition, algorithmic transparency, robotics) and those mentioning AI tangentially (e.g., AI in education, healthcare, criminal justice, government services).  
> Format: Provide each entry clearly formatted in CSV style with the following columns only:  
> - State  
> - Bill Number  
> - Bill Name or Title  
> - 1–2 sentence summary of the bill’s contents and intent  
> - Direct hyperlink to the official `<STATE>` Legislature website's bill text or summary  
> Please include only officially sourced, current legislative data. No additional commentary needed.

The data was then reviewed and cleaned through **three quality control passes**:
1. **De-duplication:** Identical or refiled bills were merged or removed.
2. **Carryover filtering:** Bills filed in prior sessions but still visible in 2025 records were excluded.
3. **Formatting homogenization:** Names, summaries, and links were standardized across states.

## 📁 Columns

| Column Name     | Description                                                             |
|-----------------|-------------------------------------------------------------------------|
| `State`         | Full U.S. state name                                                    |
| `Bill_Number`   | The bill's official identifier (e.g., HB 123, SB 45)                    |
| `Bill_Name`     | Title or short name of the bill                                         |
| `Summary`       | 1–2 sentence summary of the bill’s contents and intent                  |
| `Source_Link`   | Direct link to the bill’s page on the official state legislature website|
| `Bill_Type`     | Standardized bill type (e.g., HB, SB, HJR, etc.)                        |
| `Year`          | Legislative year (all entries = 2025)                                   |

## 📌 Citation

If you use this dataset, please cite as:

> *AI Legislation State Tracker (Spring 2025).* Sapient Artifice, 2025. 
[https://sapientartifice.com](https://sapientartifice.com)

## 📬 Contact

For questions, corrections, or contributions:  
📧 contact@sapientartifice.com

---

*Created with the help of OpenAI’s research assistant and rigorous human validation.
However if you find something that should be corrected or added please reach out*
