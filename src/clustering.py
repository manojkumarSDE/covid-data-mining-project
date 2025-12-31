from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def perform_clustering(country_data):
    X = country_data[['Confirmed', 'Deaths', 'Recovered']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = KMeans(n_clusters=3, random_state=42)
    country_data['Cluster'] = model.fit_predict(X_scaled)

    return country_data
