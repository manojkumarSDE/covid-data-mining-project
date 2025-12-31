import pandas as pd

def top_affected(covid):
    data = covid.groupby('Country/Region')[['Confirmed','Deaths','Recovered']].sum()
    sorted_data = data.sort_values(by='Confirmed', ascending=False)
    return sorted_data.head(2)

def mortality_recovery_ratio(covid):
    return covid['Deaths'].sum() / covid['Recovered'].sum()

def age_mortality(line):

    # Convert death column to numeric
    line['death'] = pd.to_numeric(line['death'], errors='coerce')

    # Replace NaN with 0 safely
    line['death'] = line['death'].fillna(0)

    # Create age groups
    line['age_group'] = pd.cut(
        line['age'],
        bins=[0, 18, 35, 50, 65, 100],
        labels=['0-18', '19-35', '36-50', '51-65', '65+']
    )

    # Mortality percentage
    mortality = line.groupby('age_group', observed=False)['death'].mean() * 100
