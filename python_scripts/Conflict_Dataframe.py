import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Build a structured dataset for visualization prep using synthesized summaries
# NOTE: Add your dataframe loading logic here if needed
conflict_data = {
    "Policy Topic": [
        "Deepfakes / Misinformation", "Automated Hiring / Employment", "Healthcare & Pandemic Preparedness",
        "Generative AI & LLMs", "Algorithmic Discrimination", "Facial Recognition / Biometrics",
        "Autonomous Systems / Vehicles", "AI Governance / Infrastructure", "AI in Schools / Curriculum",
        "Robocalls / Communications", "Economic Regulation", "Workforce / Education", "Other / Emerging Uses"
    ],
    "Conflict Risk": [
        "High", "Medium", "Medium", "High", "High", "High", "Medium", "Low", "Low", "Medium", "Medium", "Low", "Medium"
    ],
    "Federal Bills": [2, 1, 3, 1, 1, 0, 2, 5, 0, 2, 1, 2, 4],
    "State Bills": [46, 35, 12, 8, 29, 22, 18, 8, 21, 26, 14, 35, 70],
    "Actors Involved": [
        "AK, CT, Congress", "CA, NY, IL, Congress", "AZ, CA, AR, Congress", "CA, IL, FL, Congress",
        "HI, IL, MD, NY, Congress", "CO, MA, NY, IL", "ND, RI, CA, Congress", "ND, AL, AK, Congress",
        "TN, IL, MS", "OK, CA, FL, Congress", "CA, CO, IL, AZ, Congress", "NY, CA, OH, GA, Congress",
        "AZ, CT, OK, CO, CA, Congress"
    ],
    "Conflict Type": [
        "Disclosure standards vs. lack of federal law",
        "Audit + notice rules differ; federal silence",
        "Federal push vs. state oversight limits",
        "Transparency + user warnings vary",
        "Bias audit requirements vs. undefined federal standards",
        "Consent vs. prohibition inconsistencies",
        "Surveillance + deployment fragmentation",
        "Diverging task force strategies",
        "Curriculum inconsistency; no federal requirement",
        "Impersonation bans vs. pending robocall rules",
        "Antitrust vs. proactive price algorithm bans",
        "Upskilling focus differs by jurisdiction",
        "Early bans + protections uneven across states"
    ],
    "Conflict Summary": [
        "States like Alaska and Connecticut impose disclosure rules and campaign blackout periods for AI-generated political media, while Congress has introduced but not passed any uniform federal standard, creating a fragmented compliance landscape for platforms and campaigns.",
        "Several states now mandate audit trails and candidate notifications for AI hiring tools, but federal law is silent, forcing national employers to navigate divergent obligations depending on applicant location.",
        "Federal policy encourages AI use in pandemic response and healthcare innovation, while some states actively restrict AI-driven care decisions unless human oversight is present — raising the risk of implementation barriers for federally supported systems.",
        "California requires disclosure of training data and Illinois mandates consumer warnings, but no federal law governs generative AI outputs or model transparency, leaving developers vulnerable to conflicting state obligations.",
        "States like Illinois and Hawaii enforce fairness audits and impact assessments for high-risk AI, yet the absence of a federal law defining discriminatory AI creates inconsistent protections and uncertainty for deployers.",
        "With some states banning facial recognition outright in schools and housing, and others allowing it with consent, the lack of a federal standard forces businesses and agencies to comply with contradictory biometric rules across jurisdictions.",
        "While states regulate drones, driverless cars, and police robots differently — some banning weaponized AI outright — Congress has yet to establish national operating standards, complicating interstate deployment.",
        "Both federal and state governments are building task forces and R&D support structures, but without a unifying framework, risk remains that state-level AI strategies diverge from national goals or standards.",
        "Some states require AI literacy in K–12 education, while others are silent, and the federal government provides only advisory guidance — resulting in uneven AI preparedness across the country’s school systems.",
        "States are moving fast to criminalize AI voice impersonation and grant publicity rights, while Congress debates rules on AI robocalls — leading to mixed enforcement landscapes and potential preemption issues.",
        "States like California and Colorado are banning algorithmic price-fixing and rent-collusion tools, while the federal government still treats algorithmic collusion under legacy antitrust doctrine, risking enforcement inconsistency.",
        "Most states and the federal government agree on funding and upskilling efforts for the AI workforce, though state-specific scholarship and training strategies may miss opportunities for national coordination.",
        "States criminalize harmful or exploitative AI uses (e.g. CSAM, impersonation, addictive bots) ahead of federal action, leaving patchy protections and inconsistent rights depending on jurisdiction."
    ]
}

df_conflict_viz = pd.DataFrame(conflict_data)

# Save the structured data to CSV for use in visualizations
conflict_viz_path = "/mnt/data/AI_Conflict_Visualization_Data_Q1_2025.csv"
df_conflict_viz.to_csv(conflict_viz_path, index=False)

conflict_viz_path
