import pandas as pd

def load_and_clean():
    covid = pd.read_csv("data/covid_19_data.csv")
    line = pd.read_csv("data/covid_19_line_list_data_modified.csv")

    covid.fillna(0, inplace=True)
    line.dropna(subset=['age', 'gender'], inplace=True)

    covid['ObservationDate'] = pd.to_datetime(covid['ObservationDate'])

    return covid, line
