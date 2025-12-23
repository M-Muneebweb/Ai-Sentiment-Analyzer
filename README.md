# 🧠 AI Sentiment Analyzer

An interactive **AI-powered Sentiment Analysis web app** built with **Streamlit** and **Hugging Face Transformers**. This app uses a **deep learning model (DistilBERT)** to analyze text and predict whether the sentiment is **Positive** or **Negative**, along with confidence scores and visual feedback.

---

## 🚀 Features

* 📝 Text input for sentiment analysis
* 🧠 Deep Learning model (DistilBERT – fine-tuned on SST-2)
* 📊 Confidence score with interactive gauge chart
* 📈 Word count & sentiment metrics
* ⚡ Fast performance using Streamlit caching
* 🎨 Clean and responsive UI

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – Web App Framework
* **Hugging Face Transformers** – NLP Model
* **DistilBERT** – Sentiment Analysis Model
* **Plotly** – Interactive Gauge Chart
* **NumPy**

---

## 📂 Project Structure

```text
.
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-sentiment-analyzer.git
cd ai-sentiment-analyzer
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

The app will open automatically in your browser 🚀

---

## 📦 requirements.txt

```txt
streamlit
numpy
transformers
torch
plotly
```

---

## 🧠 Model Details

* **Model Name:** `distilbert-base-uncased-finetuned-sst-2-english`
* **Task:** Sentiment Analysis (Positive / Negative)
* **Framework:** Hugging Face Transformers

The model is cached using `@st.cache_resource` to improve performance.

---

## 📌 How It Works

1. User enters text into the input box
2. The text is passed to a pre-trained DistilBERT model
3. Model predicts sentiment label and confidence score
4. Results are displayed with metrics and a gauge chart

---

## 🎯 Use Cases

* Sentiment analysis of reviews
* Social media text analysis
* NLP learning project
* AI / Data Science portfolio project

---

## ⚠️ Notes

* Internet connection is required on first run to download the model
* Large inputs may take slightly longer to process

---

## 👨‍💻 Author

**Muneeb Rashid**
Web Developer | AI & Data Science Learner

---

⭐ If you like this project, don’t forget to **star the repository**!
