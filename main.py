from src.data_preprocessing import load_and_clean
from src.clustering import perform_clustering
from src.analysis import *

covid, line = load_and_clean()

country_data = covid.groupby('Country/Region')[['Confirmed','Deaths','Recovered']].sum().reset_index()
clustered = perform_clustering(country_data)

clustered.to_csv("outputs/clustered_data.csv", index=False)

print("Top affected regions:")
print(top_affected(covid))

print("\nMortality vs Recovery Ratio:")
print(mortality_recovery_ratio(covid))

age_data = age_mortality(line)
age_data.to_csv("outputs/age_mortality.csv")

print("\nMortality Rate by Age Group:")
print(age_data)
