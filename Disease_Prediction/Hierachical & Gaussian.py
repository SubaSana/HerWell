import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
from sklearn.preprocessing import StandardScaler  
from sklearn.mixture import GaussianMixture  
from sklearn.decomposition import PCA

# Load datasets
disease_symptom_df = pd.read_csv("disease_symptom.csv")  
symptom_severity_df = pd.read_csv("symptom_severity.csv")  

# Remove duplicate diseases
disease_symptom_df = disease_symptom_df.drop_duplicates(subset=["Disease"], keep="first")

# Ensure unique symptoms in severity dataset
symptom_severity_df = symptom_severity_df.drop_duplicates(subset=["Symptom"], keep="first")

# Map severity weight to symptoms
severity_map = dict(zip(symptom_severity_df["Symptom"], symptom_severity_df["weight"]))
for col in disease_symptom_df.columns[1:]:  
    disease_symptom_df[col] = disease_symptom_df[col].map(severity_map).fillna(0)

# Standardize the data
X = disease_symptom_df.iloc[:, 1:].values  
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Ensure GMM is fitted and labels are generated
gmm = GaussianMixture(n_components=2, random_state=42)  # Adjust clusters as needed
gmm_labels = gmm.fit_predict(X_scaled)  # Assign cluster labels

# PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Scatter plot with colors based on GMM clusters
plt.figure(figsize=(8, 5))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=gmm_labels, palette="viridis")
plt.title("PCA Visualization of Disease Data (Colored by Clusters)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Clusters")
plt.show()


# Try clustering with 2 to 4 clusters
best_n_clusters = 2  

# Apply GMM with best cluster count
gmm = GaussianMixture(n_components=best_n_clusters, random_state=42)
disease_symptom_df["GMM_Cluster"] = gmm.fit_predict(X_scaled)

# Define recommendations only for detected clusters
recommendations = {
    0: "Regular health check-ups & balanced diet.",
    1: "Increase physical activity & monitor symptoms.",
    2: "Follow a strict diet & consult a specialist.",
    3: "Practice mindfulness & improve mental health."
}

# Apply recommendations only to existing clusters
existing_clusters = disease_symptom_df["GMM_Cluster"].unique()
disease_symptom_df["Recommendation"] = disease_symptom_df["GMM_Cluster"].map(
    {k: recommendations[k] for k in existing_clusters if k in recommendations}
)

# Save the results
disease_symptom_df.to_csv("segmented_diseases.csv", index=False)

# Plot final clustering result
plt.figure(figsize=(8, 5))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=disease_symptom_df["GMM_Cluster"], palette="viridis")
plt.title("GMM Clustering of Disease Symptoms (PCA View)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

# Display results
print(disease_symptom_df[["Disease", "GMM_Cluster", "Recommendation"]].head())
