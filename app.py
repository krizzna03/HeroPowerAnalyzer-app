import streamlit as st
import pickle
import numpy as np

# Load the trained model and scaler
try:
    with open('best_dt_model.pkl', 'rb') as f:
        model = pickle.load(f)
    # In a real application, you would save and load the scaler as well.
    # For this example, we'll manually define the min/max values observed in the training data.
    # min_Feat_Score = 2.0, max_Feat_Score = 10.0
    # min_Fan_Rating = 7.0, max_Fan_Rating = 9.8
    # min_Comic_Appearances = 100.0, max_Comic_Appearances = 12500.0
    min_vals = np.array([2.0, 7.0, 100.0])
    max_vals = np.array([10.0, 9.8, 12500.0])

except FileNotFoundError:
    st.error("Model file not found. Please ensure 'best_dt_model.pkl' is in the same directory.")
    st.stop()

def predict_power_tier(feat_score, fan_rating, comic_appearances, model, min_vals, max_vals):
    """Predicts the power tier based on input features.

    Args:
        feat_score: The feat score of the character.
        fan_rating: The fan rating of the character.
        comic_appearances: The approximate number of comic appearances.
        model: The trained machine learning model.
        min_vals: Minimum values of the features from the training data.
        max_vals: Maximum values of the features from the training data.


    Returns:
        The predicted power tier as a string.
    """
    # Create a NumPy array from the input values
    input_data = np.array([[feat_score, fan_rating, comic_appearances]])

    # Scale the input data manually using min/max values
    scaled_input_data = (input_data - min_vals) / (max_vals - min_vals)

    # Make prediction
    prediction = model.predict(scaled_input_data)

    # Map the predicted tier back to the original labels
    tier_map = {0: 'Street-Level', 1: 'Metahuman', 2: 'Powerhouse', 3: 'Herald', 4: 'Cosmic'}
    predicted_tier = tier_map[prediction[0]]

    return predicted_tier

st.title("Marvel Character Power Tier Predictor")
st.write("Enter the character's attributes to predict their power tier.")

# Add input fields for the features
feat_score = st.slider("Feat Score (1 to 10)", 1.0, 10.0, 5.0)
fan_rating = st.slider("Fan Rating (1 to 10)", 1.0, 10.0, 5.0)
comic_appearances = st.slider("Comic Appearances (Approx)", 0, 15000, 5000)


# Create a button to make predictions
if st.button("Predict Power Tier"):
    # Make prediction
    predicted_tier = predict_power_tier(feat_score, fan_rating, comic_appearances, model, min_vals, max_vals)

    # Display the prediction
    st.success(f"Predicted Power Tier: {predicted_tier}")