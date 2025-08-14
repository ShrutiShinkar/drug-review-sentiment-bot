# 💊 Sentiment Analysis & Auto-Replier for Drug Reviews

An end-to-end Natural Language Processing (NLP) pipeline to analyze patient-written drug reviews and automatically respond to negative feedback using a sentiment-aware chatbot. This project combines lexicon-based and transformer-based models with aspect-level sentiment detection to improve pharmaceutical feedback interpretation and engagement.

---
## 🧪 Core Features

-   **Data Fusion:** Integrated ~10,000 reviews from WebMD with 5,000+ labeled UCI entries.
-   **NLP Preprocessing:** Lemmatization, stopword removal, regex cleaning, and POS-based filtering.
-   **Sentiment Modeling:** Multi-tier system: VADER → SVM → Voting Classifier → DistilBERT (fine-tuned).
-   **Visual Analytics:** WordClouds, Heatmaps, Pie Charts, Radar Charts, and Treemaps.
-   **Aspect-Based Analysis:** Using SpaCy to extract noun phrases (e.g., "side effects") and correlate them with sentiment.
-   **Smart Auto-Replier Chatbot:** Generates human-like replies for negative/neutral reviews.

---
## 📊 Visual Analytics & Insights

The analysis begins with an overview of the dataset, identifying the most frequently discussed drugs and the overall sentiment distribution.

<p align="center">
  <img src="images/wordcloud.png" alt="Word Cloud of Reviews" width="48%">
  <img src="images/top_drugs.png" alt="Top Reviewed Drugs" width="48%">
</p>
<p align="center">
  <em>Initial EDA reveals the most common terms and the top 10 drugs by review volume.</em>
</p>

Deeper analysis reveals the sentiment breakdown and the specific aspects (like side effects or efficacy) associated with different drugs.

<p align="center">
  <img src="images/sentiment_pie.png" alt="Sentiment Distribution Pie Chart" width="32%">
  <img src="images/treemap.png" alt="Treemap of Conditions" width="32%">
  <img src="images/aspect_heatmap.png" alt="Aspect Sentiment Heatmap" width="32%">
</p>
<p align="center">
  <em>Sentiment distribution, the prevalence of medical conditions, and a heatmap linking aspects to sentiment.</em>
</p

---
## 🧠 Model Performance

A multi-model strategy was employed, starting with a baseline SVM and progressing to a more advanced Voting Classifier. The confusion matrices below show their performance in classifying sentiment.

<p align="center">
  <img src="images/svm_confusion.png" alt="SVM Confusion Matrix" width="48%">
  <img src="images/voting_confusion.png" alt="Voting Classifier Confusion Matrix" width="48%">
</p>

-   **SVM (TF-IDF):** 80% accuracy
-   **Voting Classifier:** 82% accuracy
-   **DistilBERT (fine-tuned):** 87% accuracy
-   **Aspect Extraction Accuracy:** 90% (manual validation)

---
## 🤖 Smart Auto-Replier Chatbot

A key innovation of this project is a sentiment-aware chatbot that generates empathetic and relevant responses to user reviews. Below is a demonstration of the bot in action, followed by its performance metrics.

<p align="center">
  <img src="images/chatbot_demo.png" alt="Chatbot Demo" width="90%">
</p>

The bot's performance was evaluated based on its relevance and empathy.

<p align="center">
  <img src="images/radar_chart.png" alt="Chatbot Performance Radar Chart" width="48%">
  <img src="images/response_count.png" alt="Chatbot Response Counts" width="48%">
</p>

-   **Chatbot Relevance Score:** 92%
-   **Chatbot Empathy Score:** 87%

---
## 🚀 Future Extensions

-   Multi-language support (e.g., Hindi, German, French)
-   GPT-4/LLM integration for smarter repliers
-   Clinical validation through partnerships with pharma
-   Deploy to Hugging Face Spaces or Streamlit Cloud

---
## 🔗 Data Access

Due to file size constraints, all datasets (raw and cleaned), models, and preprocessed CSVs are available at the following link:

📎 **Google Drive:** [Project Data & Models](https://drive.google.com/drive/folders/1EKRoAs0yrQwHV3Utn1xUAgKG1bfTcB-R)
