import streamlit as st
import nltk
import numpy as np
import re
import speech_recognition as sr
from pydub import AudioSegment
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')

# PREPROCESSING
def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text


# LOAD & PREPARE CHATBOT TEXT FILE
with open("anime.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

sentences = nltk.sent_tokenize(raw_text)
clean_sentences = [preprocess(s) for s in sentences]

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(clean_sentences)


# SIMILARITY SEARCH
def get_most_relevant_sentence(query):
    cleaned = preprocess(query)
    query_vec = vectorizer.transform([cleaned])
    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()

    idx = np.argmax(scores)
    return sentences[idx], scores[idx]


# CHATBOT FUNCTION
def chatbot(user_query):
    q = user_query.lower()

    # RULE-BASED RESPONSES
    if "what is anime" in q:
        return "Anime is a style of Japanese animation known for vibrant art and storytelling."

    if "genres" in q or "types" in q:
        return "Major anime genres include Shonen, Shojo, Seinen, Josei, Mecha, Isekai, and Slice of Life."

    if "best anime" in q:
        return "Popular anime include Fullmetal Alchemist Brotherhood, Attack on Titan, Naruto, Demon Slayer, and One Piece."

    # SIMILARITY FALLBACK
    response, score = get_most_relevant_sentence(user_query)
    if score < 0.05:
        return "I’m not sure about that. Try asking about anime genres, characters, or recommendations."

    return response


# SPEECH RECOGNITION
def convert_to_wav(uploaded_file):
    audio = AudioSegment.from_file(uploaded_file)
    wav_name = "temp.wav"
    audio.export(wav_name, format="wav")
    return wav_name


def transcribe_audio(wav_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio_data)
    except:
        return "Could not recognize speech."


# STREAMLIT UI
def main():
    st.title("🎤🤖 Speech-Enabled Anime Chatbot")

    st.write("Ask a question *by typing* or *using your voice*!")

    # -----------------------------
    # TEXT INPUT
    # -----------------------------
    st.subheader("📝 Text Input")
    text_query = st.text_input("Type your question here:")

    if st.button("Send Text"):
        if text_query.strip():
            answer = chatbot(text_query)
            st.success(answer)

    st.markdown("---")

  
    # SPEECH INPUT
  
    st.subheader("🎤 Voice Input")

    audio_file = st.file_uploader(
        "Upload an audio file (mp3, wav, m4a, ogg)",
        type=["mp3", "wav", "m4a", "ogg"]
    )

    if audio_file and st.button("Transcribe & Ask"):
        wav = convert_to_wav(audio_file)
        user_text = transcribe_audio(wav)

        st.write("### 🎧 Transcribed Text:")
        st.info(user_text)

        # Pass transcribed text to chatbot
        answer = chatbot(user_text)

        st.write("### 🤖 Chatbot Response:")
        st.success(answer)


if __name__ == "__main__":
    main()
