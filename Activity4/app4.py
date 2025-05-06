import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.title("🌍 COVID-19 Statistics Dashboard")

# Fetch Data
@st.cache_data
def load_data():
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.json_normalize(response.json())
    else:
        st.error("Failed to fetch data")
        return pd.DataFrame()

df = load_data()

# Sidebar: Country selection
countries = df['country'].sort_values().tolist()
selected_countries = st.sidebar.multiselect("Select Countries", countries, default=["India", "USA", "Brazil", "Germany", "Russia"])

filtered_df = df[df['country'].isin(selected_countries)]

# Show summary table
st.subheader("📋 Summary Table")
st.dataframe(filtered_df[['country', 'cases', 'todayCases', 'deaths', 'recovered']].set_index('country'))

# Chart 1: Bar Chart - Total Cases
st.subheader("📊 Total COVID-19 Cases (Bar Chart)")
st.bar_chart(filtered_df.set_index("country")['cases'])

# Chart 2: Line Chart - Deaths
st.subheader("📈 Total Deaths (Line Chart)")
st.line_chart(filtered_df.set_index("country")['deaths'])

# Chart 3: Pie Chart - Recovered Proportion
st.subheader("🥧 Recovered Cases Distribution (Pie Chart)")
fig1, ax1 = plt.subplots()
ax1.pie(filtered_df['recovered'], labels=filtered_df['country'], autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# Chart 4: Area Chart - Active vs Critical
st.subheader("📐 Active vs Critical Cases (Area Chart)")
area_data = filtered_df[['country', 'active', 'critical']].set_index('country')
st.area_chart(area_data)

# Chart 5: Map Chart (Plotly) - Cases by Location
st.subheader("🗺️ Cases Distribution on Map (Scatter Geo)")
fig2 = px.scatter_geo(filtered_df,
                      locations="countryInfo.iso2",
                      locationmode="ISO-3",
                      size="cases",
                      color="country",
                      hover_name="country",
                      projection="natural earth",
                      title="COVID-19 Cases per Country")
st.plotly_chart(fig2)
