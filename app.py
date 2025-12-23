import streamlit as st
import numpy as np
from transformers import pipeline
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size: 3rem; color: #1E88E5; text-align: center;}
</style>
""", unsafe_allow_html=True)

# Load model (cached for performance)
@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def main():
    st.markdown('<h1 class="main-header">🧠 AI Sentiment Analyzer</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.title("About")
        st.info("This app uses **Deep Learning** (DistilBERT) to analyze text sentiment.")
    
    # Main Content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Enter Your Text")
        user_input = st.text_area("Type or paste text:", height=200)
        analyze_button = st.button("🔍 Analyze Sentiment", type="primary")
    
    with col2:
        st.subheader("How It Works")
        st.markdown("1. Input text\n2. Click Analyze\n3. View prediction")
    
    if analyze_button and user_input:
        with st.spinner("🧠 Analyzing..."):
            classifier = load_sentiment_model()
            result = classifier(user_input)[0]
            label, score = result['label'], result['score']
        
        # Display Results
        col1, col2, col3 = st.columns(3)
        col1.metric("Sentiment", f"{'😊' if label == 'POSITIVE' else '😔'} {label}")
        col2.metric("Confidence", f"{score*100:.1f}%")
        col3.metric("Words", len(user_input.split()))
        
        # Gauge Chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number", value=score*100,
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': "#4CAF50" if label == "POSITIVE" else "#F44336"}}
        ))
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
