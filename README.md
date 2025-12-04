
# 🎤🤖 Speech-Enabled Anime Chatbot  
A Streamlit-based chatbot that accepts **typed text** or **speech input**, transcribes voice to text using **SpeechRecognition**, and generates anime-related responses using **TF-IDF similarity** + rule-based logic.

---

## 🚀 Features

### ✔ Text Chat  
- Ask any anime-related question using text  
- Chatbot responds using rule-based and TF-IDF similarity search  

### ✔ Speech-to-Text Chat  
- Upload an audio file (WAV, MP3, OGG, M4A)  
- Audio is converted into text using Google Speech Recognition  
- The transcribed text is passed to the chatbot  
- Chatbot responds like a normal text query  

### ✔ TF-IDF NLP Engine  
- Uses Scikit-Learn’s **TfidfVectorizer**  
- Computes similarity between your question and sentences from `anime.txt`  
- Falls back to rule-based answers for common anime questions  

---

## 📁 Project Structure

```

📦 speech-enabled-anime-chatbot
│
├── app.py               # Main Streamlit application
├── anime.txt            # Text corpus used by the chatbot
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

```

---

## 🛠 Installation & Setup

### 1. Clone the Repository
```

git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
cd <your-repo-name>

```

### 2. Create Virtual Environment (Optional but Recommended)
```

python -m venv venv
venv\Scripts\activate   # On Windows

````

### 3. Install Dependencies
```bash
pip install -r requirements.txt
````

### 4. Install FFmpeg (Required for pydub)

**Windows:**
Download from: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
Extract → Add `ffmpeg/bin` to PATH → Restart terminal.

Confirm:

```
ffmpeg -version
```

---

## ▶ Run the App

```
streamlit run app.py
```

Streamlit will show a local URL:

```
http://localhost:8501
```

Open it in your browser.

---

## 🎧 Supported Audio Formats

* `.wav`
* `.mp3`
* `.ogg`
* `.m4a`

Uploaded audio is automatically converted to WAV using **pydub**.

---

## 🧠 How the Chatbot Works

### 1. Preprocessing

All text is cleaned (lowercase, special characters removed).

### 2. Rule-Based Responses

If the user asks:

* *"what is anime"*
* *genres/types*
* *best anime*

The chatbot replies instantly.

### 3. TF-IDF Similarity

If no rule matches:

* It searches the `anime.txt` dataset
* Finds the most similar sentence using cosine similarity
* Responds with the closest match

### 4. Low-confidence fallback

If similarity score is too low:

```
"I’m not sure about that. Try asking about anime genres, characters, or recommendations."
```

---

## 📦 Requirements (requirements.txt)

```txt
streamlit
nltk
numpy
scikit-learn
speechrecognition
pydub
```

---

## 📸 Screenshots (Optional)

You can later add these:

* Chatbot text mode
* Voice transcription mode
* Anime response examples

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📜 License

This project is open-source under the MIT License.

---

## ⭐ Show Some Support

If you like this project, give the repo a **star** on GitHub!


