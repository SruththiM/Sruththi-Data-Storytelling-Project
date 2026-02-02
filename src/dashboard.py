import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


df = pd.read_csv("../data/sruththi_lifestyle_dataset.csv")


color_map = {
    "Past_Active": "#39FF14",    
    "Present_Active": "#FF3131", 
    "Future_Active": "#1E90FF"   
}


fig_study_marks = px.scatter(
    df, x="Study_Hours", y="Marks",
    color="Phase", size="Energy_Level",
    hover_data=["Mood", "Activity", "Stress_Level", "Sleep_Hours"],
    labels={"Study_Hours":"Study Hours", "Marks":"Marks"},
    color_discrete_map=color_map
)

coef = np.polyfit(df['Study_Hours'], df['Marks'], 1)
trend = np.poly1d(coef)
fig_study_marks.add_traces(go.Scatter(
    x=df['Study_Hours'], y=trend(df['Study_Hours']),
    mode='lines', name='Trend Line', line=dict(color='cyan', dash='dash')
))


max_marks = df['Marks'].max()
max_row = df[df['Marks']==max_marks].iloc[0]
fig_study_marks.add_annotation(
    x=max_row['Study_Hours'], y=max_row['Marks'],
    text="Highest Marks 🎯", showarrow=True, arrowhead=2,
    font=dict(color="#39FF14", size=14)
)


fig_stress_concentration = px.scatter(
    df, x="Stress_Level", y="Concentration_Score",
    color="Phase", size="Water_Intake_Liters",
    hover_data=["Energy_Level", "Mood", "Sleep_Hours"],
    labels={"Stress_Level":"Stress Level", "Concentration_Score":"Concentration Score"},
    color_discrete_map=color_map
)


fig_stress_concentration.add_annotation(
    x=df['Stress_Level'].max(), y=df['Concentration_Score'].min(),
    ax=df['Stress_Level'].min(), ay=df['Concentration_Score'].max(),
    text="Stress ↑ → Concentration ↓", showarrow=True, arrowhead=3, arrowsize=1,
    arrowwidth=2, font=dict(color="#FF3131", size=14)
)


df_avg = df.groupby("Phase")[["Marks","Concentration_Score","Stress_Level"]].mean().reset_index()
fig_avg = go.Figure(data=[
    go.Bar(name='Marks', x=df_avg["Phase"], y=df_avg["Marks"], marker_color="#39FF14"),
    go.Bar(name='Concentration', x=df_avg["Phase"], y=df_avg["Concentration_Score"], marker_color="#FF3131"),
    go.Bar(name='Stress', x=df_avg["Phase"], y=df_avg["Stress_Level"], marker_color="#1E90FF")
])


df_past = df[df['Phase']=="Past_Active"]
fig_energy_activity = px.box(
    df_past, x="Activity", y="Energy_Level",
    color="Activity"
)


med_energy = df_past['Energy_Level'].median()
fig_energy_activity.add_shape(
    type="line", x0=-0.5, x1=len(df_past['Activity'].unique())-0.5,
    y0=med_energy, y1=med_energy, line=dict(color="#FF3131", dash="dash")
)
fig_energy_activity.add_annotation(
    x=len(df_past['Activity'].unique())-1, y=med_energy,
    text=f"Median Energy {med_energy}", showarrow=False, font=dict(color="#39FF14", size=12)
)


fig_mood = px.histogram(
    df, x="Mood", color="Phase", barmode="group",
    color_discrete_map=color_map
)


most_common_mood = df['Mood'].mode()[0]
fig_mood.add_annotation(
    x=most_common_mood, y=df[df['Mood']==most_common_mood].shape[0],
    text="Most Common Mood 🙂", showarrow=True, arrowhead=2,
    font=dict(color="#1E90FF", size=12)
)

fig_combined = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        "Study Hours vs Marks",
        "Stress vs Concentration",
        "Average Marks, Concentration & Stress",
        "Energy Level by Activity",
        "Mood Distribution"
    ),
    vertical_spacing=0.12,
    horizontal_spacing=0.08
)


for trace in fig_study_marks.data:
    fig_combined.add_trace(trace, row=1, col=1)
for trace in fig_stress_concentration.data:
    fig_combined.add_trace(trace, row=1, col=2)
for trace in fig_avg.data:
    fig_combined.add_trace(trace, row=2, col=1)
for trace in fig_energy_activity.data:
    fig_combined.add_trace(trace, row=2, col=2)
for trace in fig_mood.data:
    fig_combined.add_trace(trace, row=3, col=1)

fig_combined.update_layout(
    height=1600, width=1400,
    title_text="Sruththi's Lifestyle Dashboard: Performance & Wellbeing Insights",
    title_font_size=26,
    font=dict(family="Arial", size=12, color="white"),
    template="plotly_dark",
    paper_bgcolor="#1a1a1a",
    plot_bgcolor="#1a1a1a",
    showlegend=True
)


fig_combined.show()
