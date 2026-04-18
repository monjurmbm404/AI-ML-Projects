import streamlit as st
from PIL import Image
from api_calling import note_generator, quiz_generator, audio_generator

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Exam Helper AI",
    page_icon="📚",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("📚 Exam Helper AI")
st.markdown("Upload your notes/images and get **Exam-ready notes, quiz & audio** instantly.")
st.divider()

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Exam Settings")

    images = st.file_uploader(
        "Upload Notes Images (Max 3)",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    subject = st.text_input("📘 Subject (Optional)", placeholder="e.g. Math, Physics, ICT")

    difficulty = st.selectbox(
        "❓ Quiz Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    generate = st.button("🚀 Generate Exam Content", type="primary")

# ---------------- IMAGE PREVIEW ----------------
pil_images = []

if images:
    if len(images) > 3:
        st.error("❌ Maximum 3 images allowed.")
        st.stop()

    st.subheader("📸 Uploaded Notes")

    cols = st.columns(len(images))

    for i, img in enumerate(images):
        pil_img = Image.open(img)
        pil_images.append(pil_img)

        with cols[i]:
            st.image(pil_img, use_container_width=True)

# ---------------- MAIN ----------------
if generate:

    if not images:
        st.error("❌ Please upload at least 1 image.")
        st.stop()

    # ---------------- NOTES ----------------
    st.subheader("📝 Exam Notes")

    with st.spinner("Generating exam-ready notes..."):
        notes = note_generator(pil_images, subject)
        st.markdown(notes)

    # ---------------- AUDIO ----------------
    st.subheader("🔊 Audio Notes")

    with st.spinner("Converting to audio..."):
        audio_file = audio_generator(notes)
        st.audio(audio_file, format="audio/mp3")

    # ---------------- QUIZ ----------------
    st.subheader(f"❓ Exam Quiz ({difficulty})")

    with st.spinner("Generating quiz..."):
        quiz_data = quiz_generator(pil_images, difficulty, subject)

    # ---------------- QUIZ UI ----------------
    score = 0

    for i, q in enumerate(quiz_data):
        st.markdown(f"### Q{i+1}: {q['question']}")

        answer = st.radio(
            "Choose answer:",
            q["options"],
            key=f"q{i}"
        )

        if st.button(f"Submit Q{i+1}", key=f"btn{i}"):
            if answer == q["answer"]:
                st.success("✅ Correct!")
                score += 1
            else:
                st.error(f"❌ Wrong! Correct answer: {q['answer']}")

    st.subheader(f"🏆 Final Score: {score}/{len(quiz_data)}")