import streamlit as st
from PIL import Image

# App config
st.set_page_config(page_title="Langly", page_icon="🌍", layout="centered")

# Sidebar mascot
with st.sidebar:
    st.markdown("### Welcome to Langly! 🌟")
    st.markdown("Choose a language and test your level!")

# Language selection
st.title("🌍 Choose a language to learn")
language = st.selectbox("Select a language:", ["Lithuanian", "Bulgarian", "Luxembourgish"])

questions = {
    "Lithuanian": [
        {"q": "How do you say 'Hello' formally in Lithuanian?", "options": ["Labas", "Bonjour", "Hola", "Ciao"], "answer": "Labas"},
        {"q": "How do you say 'Hello' informally in Lithuanian?", "options": ["Sveiki", "Salut", "Ey", "Čau"], "answer": "Sveiki"},
        {"q": "How do you say 'Goodbye' formally in Lithuanian?", "options": ["Au revoir", "Ate", "Uz redzēšanos", "Nägemist"], "answer": "Ate"},
        {"q": "How do you say 'Goodbye' informally in Lithuanian?", "options": ["Viso gero", "Tšau", "Čau", "Visu labu"], "answer": "Viso gero"},
        {"q": "What does 'Ačiū' mean?", "options": ["Please", "Goodbye", "Thank you", "Yes"], "answer": "Thank you"},
        {"q": "What does 'Prašau' mean?", "options": ["Present", "Tree", "Please", "Direction"], "answer": "Please"},
        {"q": "What does 'Atsiprašau' mean?", "options": ["Excuse me ", "Watch out", "Be careful", "Attention"], "answer": "Excuse me"},
        {"q": "What else could 'Atsiprašau' mean?", "options": ["Take care", "Fine", "Grateful", "Sorry"], "answer": "Sorry"},
        {"q": "When someone does not understand something: They respond with:____-?", "response": user_answer = input(q +"/nYour answer:"), "answer": "Aš nesuprantu"},
    ],
    "Bulgarian": [
        {"q": "What is 'Hello' in Bulgarian?", "options": ["Azul", "Labas", "Salam", "Hallo"], "answer": "Azul"},
        {"q": "What does 'Tanemmirt' mean?", "options": ["Sorry", "Thanks", "Good night", "No"], "answer": "Thanks"},
    ],
    "Luxembourgish": [
        {"q": "Translate 'Hello' to Luxembourgish:", "options": ["Kamusta", "Aloha", "Salamat", "Ni hao"], "answer": "Kamusta"},
        {"q": "What does 'Salamat' mean?", "options": ["Goodbye", "Hello", "Thank you", "Love"], "answer": "Thank you"},
    ]
}

if st.button("Start Test"):
    st.session_state.score = 0
    st.session_state.question_index = 0
    st.session_state.language = language

# Quiz logic
if "language" in st.session_state:
    lang = st.session_state.language
    score = st.session_state.get("score", 0)
    index = st.session_state.get("question_index", 0)
    q_list = questions[lang]

    if index < len(q_list):
        q = q_list[index]
        st.subheader(f"Question {index + 1} of {len(q_list)}")
        st.write(q["q"])
        selected = st.radio("Choose one:", q["options"], key=index)

        if st.button("Submit Answer"):
            if selected == q["answer"]:
                st.session_state.score += 1
            st.session_state.question_index += 1
            st.experimental_rerun()
    else:
        st.success("Test Completed!")
        st.markdown(f"**Your Score: {score}/{len(q_list)}**")

        if score == len(q_list):
            level = "Advanced"
        elif score >= len(q_list) // 2:
            level = "Intermediate"
        else:
            level = "Beginner"

        st.markdown(f"### 🎓 Recommended Level: **{level}**")
        st.info("Lessons will begin from the appropriate level. (Coming soon!)")
