# 🎬 YouTube & Video SEO Keyword Generator

A powerful tool that extracts **SEO-optimized keywords** from **YouTube videos** or **local video files** using **LangChain**, **OpenAI Whisper**, and **Streamlit**.

## 🚀 Features

- ✅ Extract keywords from **YouTube URLs**.
- ✅ Upload **local video files** and transcribe them.
- ✅ Use **OpenAI Whisper** for high-accuracy transcriptions.
- ✅ Generate **SEO-friendly keywords**.
- ✅ Intuitive **Streamlit** UI.

---

## 📂 Demo Screenshot

![Demo Screenshot](path_to_screenshot.png)

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/seo-keyword-generator.git
cd seo-keyword-generator

2️⃣ Create and Activate a Virtual Environment

conda create -n seo_env python=3.10
conda activate seo_env

3️⃣ Install Dependencies
pip install -r requirements.txt

✅ Run the App:
streamlit run app.py


🧠 How It Works
YouTube Video:
Uses YoutubeLoader from Langchain to fetch transcripts.
Local Video:
Uses MoviePy to extract audio.
Whisper transcribes the audio into text.
Keyword Generation:
Uses an LLM to extract contextually relevant SEO keywords.


