import streamlit as st
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders.youtube import TranscriptFormat
from scripts import llm
import whisper
import os
from moviepy import *



# === App Title ===
st.title("🎬 YouTube & Video SEO Keyword Generator")
st.write("Upload a **YouTube URL** or a **local video file** to generate **SEO keywords**.")

# === Functions ===
def get_youtube_transcript(url, chunk_size_seconds=600):
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=True, transcript_format=TranscriptFormat.CHUNKS, chunk_size_seconds=chunk_size_seconds)
    docs = loader.load()
    return docs

def transcribe_local_video(file_path):
    st.info("Transcribing video... ⏳")
    model = whisper.load_model("base")
    video = VideoFileClip(file_path)
    audio_path = "temp_audio.mp3"
    video.audio.write_audiofile(audio_path)

    result = model.transcribe(audio_path)
    os.remove(audio_path)
    return [{"page_content": result["text"], "metadata": {"source": file_path}}]

def generate_seo_keywords(docs):
    initial_keywords = []
    question = """You are an assistant for generating SEO keywords for YouTube.
                  Please generate a list of keywords from the above context.
                  You can use your creativity and correct spelling if it is needed."""
    
    for doc in docs:
        # ✅ Check if it's a Document object or dict
        if isinstance(doc, dict):
            context = doc['page_content']
        else:
            context = doc.page_content
        
        kws = llm.ask_llm(context=context, question=question)
        initial_keywords.append(kws)

    keywords = ", ".join(initial_keywords)

    # Refine for SEO
    seo_question = """Above context is the list of relevant keywords for a YouTube video.
                      You need to generate SEO Keywords for it."""
    seo_keywords = llm.ask_llm(context=keywords, question=seo_question)

    return seo_keywords


# === User Inputs ===
youtube_url = st.text_input("🔗 Enter YouTube URL")
uploaded_file = st.file_uploader("📁 Or upload a local video file", type=["mp4", "mov", "avi", "mkv"])

# === Process Button ===
if st.button("🚀 Generate SEO Keywords"):
    if youtube_url:
        st.success("Processing YouTube URL...")
        docs = get_youtube_transcript(youtube_url)
        seo_keywords = generate_seo_keywords(docs)
        st.subheader("✅ SEO Keywords:")
        st.write(seo_keywords)

    elif uploaded_file:
        temp_file_path = f"temp_video.{uploaded_file.name.split('.')[-1]}"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        docs = transcribe_local_video(temp_file_path)
        seo_keywords = generate_seo_keywords(docs)
        st.subheader("✅ SEO Keywords:")
        st.write(seo_keywords)
        os.remove(temp_file_path)

    else:
        st.warning("⚠️ Please enter a YouTube URL or upload a video file.")

# === Footer ===
st.markdown("---")
st.caption("Built with ❤️ using Streamlit, LangChain & Whisper")
