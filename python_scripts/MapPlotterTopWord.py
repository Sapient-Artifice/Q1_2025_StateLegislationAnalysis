import pandas as pd
import plotly.express as px

# === State Abbreviation Map ===
us_state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR',
    'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE',
    'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
    'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
    'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
    'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY'
}

# === Load Data ===
df = pd.read_csv("Cleaned_sort2_Legislation_Data.csv")
theme_data = pd.read_csv("dominant_filtered_theme_per_state.csv")
df['Theme Keywords'] = df['State'].map(theme_data.set_index('State')['Theme Keywords'])

# === Compute Top Themes per State ===
theme_counts = (
    df.groupby(['State', 'Theme Keywords']).size().reset_index(name='Count')
    .sort_values(['State', 'Count'], ascending=[True, False])
)

theme_counts['MaxStateCount'] = theme_counts.groupby('State')['Count'].transform('max')
theme_counts['RelativeSize'] = theme_counts['Count'] / theme_counts['MaxStateCount']

top_themes = theme_counts.groupby('State').head(5)
top_themes['State Abbrev'] = top_themes['State'].map(us_state_abbrev)
top_themes = top_themes.dropna(subset=['State Abbrev'])

# === Build Text Annotations ===
text_annotations = top_themes.groupby('State Abbrev').apply(
    lambda x: "<br>".join(
        f"<span style='font-size:{int(10 + 15 * row.RelativeSize)}px'>{row['Theme Keywords'].split(',')[0]}</span>"
        for _, row in x.iterrows()
    )
).reset_index(name='Label')

# === Create Plot ===
fig = px.choropleth(
    top_themes,
    locations='State Abbrev',
    locationmode='USA-states',
    color='Count',
    scope='usa',
    title='Top AI Legislative Themes per State (2025)',
    color_continuous_scale='Blues'
)

# === Add Labels to Map ===
for _, row in text_annotations.iterrows():
    fig.add_scattergeo(
        locations=[row['State Abbrev']],
        locationmode='USA-states',
        mode='text',
        text=[row['Label']],
        textposition='middle center',
        showlegend=False
    )

fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
fig.show()
