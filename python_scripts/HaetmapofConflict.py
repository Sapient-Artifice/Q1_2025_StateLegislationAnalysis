import pandas as pd
import matplotlib.pyplot as plt
# NOTE: Add your dataframe loading logic here if needed
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
import textwrap

# Step 1: Build the conflict summary dataset
data = {
    "Policy Topic": [
        "Deepfakes / Misinformation", "Automated Hiring / Employment", "Healthcare & Pandemic Preparedness",
        "Generative AI & LLMs", "Algorithmic Discrimination", "Facial Recognition / Biometrics",
        "Autonomous Systems / Vehicles", "AI Governance / Infrastructure", "AI in Schools / Curriculum",
        "Robocalls / Communications", "Economic Regulation", "Workforce / Education", "Other / Emerging Uses"
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
    ],
    "Conflict Risk": [
        "High", "Medium", "Medium", "High", "High", "High", "Medium", "Low", "Low", "Medium", "Medium", "Low", "Medium"
    ]
}

# Step 2: Create the DataFrame
risk_scale = {"Low": 1, "Medium": 2, "High": 3}
df = pd.DataFrame(data)
df["Risk Score"] = df["Conflict Risk"].map(risk_scale)
df.set_index("Policy Topic", inplace=True)

# Step 3: Set up color scale (green to red)
cmap = LinearSegmentedColormap.from_list("risk_scale", ["#b7e4c7", "#ffe066", "#e63946"])

# Step 4: Wrap long summaries for display
wrapped_annotations = [[textwrap.fill(summary, width=94)] for summary in df["Conflict Summary"]]

# Step 5: Generate the heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(
    df[["Risk Score"]],
    annot=wrapped_annotations,
    fmt='',
    cmap=cmap,
    linewidths=0.75,
    linecolor='gray',
    cbar=False,
    annot_kws={"fontsize": 8, "va": "center"}
)
plt.title("AI Policy Conflict Summary by Topic (Q1 2025)", fontsize=15, pad=20)
plt.xticks([])
plt.yticks(rotation=0, fontsize=10)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
