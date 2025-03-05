import pandas as pd

# Load datasets
disease_symptoms = pd.read_csv("disease_symptom.csv")  # Symptoms per disease
symptom_description = pd.read_csv("symptom_description.csv")  # Disease descriptions
disease_precautions = pd.read_csv("disease_precautions.csv")  # Precautionary measures

# Reshape the disease-symptom dataset
disease_symptoms = disease_symptoms.melt(id_vars=["Disease"], value_name="Symptom").dropna()
disease_symptoms["Symptom"] = disease_symptoms["Symptom"].str.strip().str.lower()

# Convert to dictionary mapping: {symptom: [diseases]}
symptom_to_diseases = {}
for _, row in disease_symptoms.iterrows():
    symptom = row["Symptom"]
    disease = row["Disease"]
    
    if symptom in symptom_to_diseases:
        symptom_to_diseases[symptom].append(disease)
    else:
        symptom_to_diseases[symptom] = [disease]

# Function to predict diseases based on symptoms
def predict_disease(user_symptoms):
    user_symptoms = [sym.strip().lower() for sym in user_symptoms]

    disease_counts = {}  # Store disease occurrence frequency
    for symptom in user_symptoms:
        if symptom in symptom_to_diseases:
            for disease in symptom_to_diseases[symptom]:
                disease_counts[disease] = disease_counts.get(disease, 0) + 1

    if not disease_counts:
        return ["Unknown Disease"], "No matching symptoms found."

    # Rank diseases by symptom match count and return top 3
    sorted_diseases = sorted(disease_counts.items(), key=lambda x: x[1], reverse=True)
    top_diseases = [disease for disease, _ in sorted_diseases[:3]]  # Top 3 predicted diseases
    return top_diseases

# Function to get disease details
def get_disease_info(diseases):
    details = []
    for disease in diseases:
        desc = symptom_description[symptom_description["Disease"] == disease]["Description"].values
        precautions = disease_precautions[disease_precautions["Disease"] == disease].iloc[:, 1:].values

        description = desc[0] if len(desc) > 0 else "No description available."
        precaution_list = precautions[0] if len(precautions) > 0 else ["No precautions available."]
        
        details.append((disease, description, precaution_list))
    
    return details

# Main Function
if __name__ == "__main__":
    print("\n🩺 Disease Prediction System 🏥")
    user_input = input("Enter your symptoms separated by commas: ").strip().lower()
    user_symptoms = [symptom.strip() for symptom in user_input.split(",")]

    # Predict Top 3 Diseases
    predicted_diseases = predict_disease(user_symptoms)

    # Show disease details
    print("\n🔍 Most Probable Diseases (Top 3):")
    disease_info = get_disease_info(predicted_diseases)
    for i, (disease, description, precautions) in enumerate(disease_info, 1):
        print(f"\n{i}. 🦠 Disease: {disease}")
        print(f"📌 Description: {description}")
        print("\n🛡️ Precautions:")
        for j, prec in enumerate(precautions, 1):
            print(f"   {j}. {prec}")
