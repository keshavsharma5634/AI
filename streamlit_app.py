import streamlit as st
import json
from predict import predict_threat

st.set_page_config(page_title="AI Cyber Threat Detection")

st.title("🛡️ AI Cybersecurity Threat Detection System")

st.write(
    "Upload a network traffic feature file to detect whether it is a cyber threat."
)

# ===============================
# FILE UPLOAD SECTION (REAL)
# ===============================
st.subheader("📂 Upload Network Traffic File (Real Detection)")

uploaded_file = st.file_uploader(
    "Upload JSON file (feature vector)",
    type=["json"]
)

if uploaded_file is not None:
    try:
        data = json.load(uploaded_file)

        if "features" not in data:
            st.error("Invalid file format: 'features' key not found")
        else:
            features = data["features"]

            if len(features) != 78:
                st.error(f"Expected 78 features, got {len(features)}")
            else:
                prediction, result = predict_threat(features)

                if prediction == 1:
                    st.error("🚨 THREAT DETECTED")
                else:
                    st.success("✅ NO THREAT DETECTED")

                st.write("Prediction Code:", prediction)

    except Exception as e:
        st.error(f"Error reading file: {e}")

# ===============================
# INFO SECTION
# ===============================
st.markdown("---")
st.info(
    "This system uses real feature vectors extracted from network traffic. "
    "Manual input is intentionally avoided to ensure realistic threat detection."
)
