import streamlit as st
from solver import solve_text

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI LeetCode Solver",
    page_icon="🤖"
)

# ---------------- MOBILE CSS ----------------
st.markdown("""
<style>

/* Reduce padding */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 0.6rem;
    padding-right: 0.6rem;
}

/* Full-width buttons */
.stButton>button {
    width: 100%;
    height: 3em;
    border-radius: 10px;
    font-size: 16px;
}

/* Better textarea */
textarea {
    font-size: 16px !important;
}

/* Mobile tweaks */
@media (max-width: 768px) {
    h1 {
        font-size: 22px !important;
        text-align: center;
    }

    .stTextArea textarea {
        height: 140px;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🤖 AI LeetCode Solver")
st.markdown("Solve coding problems with AI (Hints or Full Solution)")

st.divider()

# ---------------- SETTINGS ----------------
st.subheader("⚙️ Settings")

mode = st.selectbox(
    "Choose Mode",
    ["Hints", "Full Solution"]
)

st.divider()

# ---------------- INPUT ----------------
st.subheader("📄 Enter Problem")

problem_text = st.text_area(
    "Paste your LeetCode problem here:",
    placeholder="e.g. Given an array nums, find the maximum subarray sum...",
)

# ---------------- BUTTON ----------------
if st.button("🚀 Solve Problem", use_container_width=True):

    if not problem_text.strip():
        st.error("❌ Please enter a problem.")
        st.stop()

    # ---------------- AI CALL ----------------
    with st.spinner("🤖 Solving..."):
        result = solve_text(problem_text, mode)

    # ---------------- OUTPUT ----------------
    st.divider()
    st.subheader("🧠 Result")

    with st.expander("Click to view solution", expanded=True):
        st.markdown(result)