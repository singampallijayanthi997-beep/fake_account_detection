import streamlit as st
import joblib
import pandas as pd

# Load trained model and scaler
model = joblib.load("fake_account_rf_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Fake Social Media Account Detection")
st.subheader("Enter Account Details")

# ----------- User Inputs -----------

edge_followed_by = st.number_input("Followers Count", min_value=0)
edge_follow = st.number_input("Following Count", min_value=0)
username_length = st.number_input("Username Length", min_value=0)
full_name_length = st.number_input("Full Name Length", min_value=0)

username_has_number = st.selectbox("Username has number?", [0, 1])
full_name_has_number = st.selectbox("Full name has number?", [0, 1])
is_private = st.selectbox("Is Private Account?", [0, 1])
is_joined_recently = st.selectbox("Joined Recently?", [0, 1])
has_channel = st.selectbox("Has Channel?", [0, 1])
is_business_account = st.selectbox("Is Business Account?", [0, 1])
has_guides = st.selectbox("Has Guides?", [0, 1])
has_external_url = st.selectbox("Has External URL?", [0, 1])

# ----------- Prepare Input Data -----------

input_data = pd.DataFrame([{
    "edge_followed_by": edge_followed_by,
    "edge_follow": edge_follow,
    "username_length": username_length,
    "username_has_number": username_has_number,
    "full_name_has_number": full_name_has_number,
    "full_name_length": full_name_length,
    "is_private": is_private,
    "is_joined_recently": is_joined_recently,
    "has_channel": has_channel,
    "is_business_account": is_business_account,
    "has_guides": has_guides,
    "has_external_url": has_external_url
}])

numeric_cols = [
    "edge_followed_by",
    "edge_follow",
    "username_length",
    "full_name_length"
]

input_data[numeric_cols] = scaler.transform(input_data[numeric_cols])

# ----------- Prediction -----------

if st.button("Predict Account Type"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.error(f"🚨 Fake Account Detected (Confidence: {probability[1]*100:.2f}%)")
    else:
        st.success(f"✅ Real Account (Confidence: {probability[0]*100:.2f}%)")
