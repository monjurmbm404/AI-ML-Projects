import streamlit as st
from PIL import Image
from api_utils import analyze_code

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Code Debugger",
    page_icon="🐞",
    layout="centered"
)

st.title("🐞 AI Code Debugger")
st.markdown("Upload your **code error screenshot** and get instant debugging help.")

st.divider()

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload Code Screenshot",
    type=["png", "jpg", "jpeg"]
)

# ---------------- MODE SELECT ----------------
mode = st.selectbox(
    "Choose Output Type",
    ["Hints", "Solution with code"]
)

# ---------------- BUTTON ----------------
debug_btn = st.button("🔍 Debug Code")

# ---------------- LOGIC ----------------
if debug_btn:

    # ❌ Validation
    if not uploaded_file or not mode:
        st.error("⚠️ Please upload an image and select a type.")
        st.stop()

    # Show image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Screenshot", use_container_width=True)

    # API CALL
    with st.spinner("🤖 Analyzing code..."):
        result = analyze_code(image, mode)

    # OUTPUT
    st.markdown("## 🧠 Result")
    st.markdown(result)