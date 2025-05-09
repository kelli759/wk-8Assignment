import pandas as pd
#Data loading
df = pd.read_csv('owid-covid-data.csv')

#first few rows
df.head()

# Chec column names
print(df.columns)

# Check missing values
df.isnull().sum()

# Basic info about data
df.info()

# Converting 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Filtering countries of interest
countries = ['Kenya', 'United States', 'India']
df_countries = df[df['location'].isin(countries)]

# Drop rows with missing values in key columns
df_cleaned = df_countries.dropna(subset=['total_cases', 'total_deaths', 'total_vaccinations'])

import matplotlib.pyplot as plt
import seaborn as sns
# Line plot: total cases over time
plt.figure(figsize=(10, 6))
for country in countries:
    data = df_cleaned[df_cleaned['location'] == country]
    plt.plot(data['date'], data['total_cases'], label=country)
plt.legend()
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.show()

# Plot: % of fully vaccinated population over time
plt.figure(figsize=(10, 6))
for country in countries:
    data = df_cleaned[df_cleaned['location'] == country]
    plt.plot(data['date'], data['people_fully_vaccinated_per_hundred'], label=country)

plt.legend()
plt.title('% of Population Fully Vaccinated Over Time')
plt.xlabel('Date')
plt.ylabel('People Fully Vaccinated (%)')
plt.grid(True)
plt.tight_layout()
plt.show()


# Death rate calculation
df_cleaned['death_rate'] = df_cleaned['total_deaths'] / df_cleaned['total_cases']

# Line plot: total vaccinations over time
plt.figure(figsize=(10, 6))
for country in countries:
    data = df_cleaned[df_cleaned['location'] == country]
    plt.plot(data['date'], data['total_vaccinations'], label=country)
plt.legend()
plt.title('Total COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.show()


import plotly.express as px

# Latest date
latest = df[df['date'] == df['date'].max()]

# Plot choropleth
fig = px.choropleth(latest,
                    locations='iso_code',
                    color='total_cases',
                    hover_name='location',
                    color_continuous_scale='Reds',
                    title='Global COVID-19 Cases')
fig.show()

### Key Insights:
# India had the highest total cases among the selected countries.
# Vaccination rates rose sharply in 2021 across all regions.
# Death rates varied over time, with the US showing higher peaks.
