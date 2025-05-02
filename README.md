# 💊 Sentiment Analysis & Auto-Replier for Drug Reviews
An end-to-end Natural Language Processing (NLP) pipeline to analyze patient-written drug reviews and automatically respond to negative feedback using a sentiment-aware chatbot. This project combines lexicon-based and transformer-based models with aspect-level sentiment detection to improve pharmaceutical feedback interpretation and engagement.

🧪 Core Features

1. Data Fusion - Integrated ~10,000 reviews from WebMD with 5,000+ labeled UCI entries
2. NLP Preprocessing - Lemmatization, stopword removal, regex cleaning, POS-based filtering
3. Sentiment Modeling - Multi-tier system: VADER → SVM → Voting Classifier → DistilBERT (fine-tuned)
4. Visual Analytics -	WordClouds, Heatmaps, Pie Charts, Radar Charts, Treemaps
5. Aspect-Based Analysis - Using SpaCy to extract noun phrases and correlate with sentiment
6. Smart Auto-Replier	Chatbot - generates human-like replies for negative/neutral reviews

🧩 Key Innovations

- Multi-model Sentiment Strategy: A progression from rule-based to deep contextual understanding
- Healthcare-Focused Aspects: Targeted extractions (e.g., "side effects", "efficacy") critical to pharma analytics
- Real-Time Conversational AI: A bot that reacts to sentiment, not just input text

📊 Model Performance & Visual Insights

- Model Accuracy:
  SVM (TF-IDF): 80% accuracy
  Voting Classifier: 82% accuracy
  DistilBERT (fine-tuned): 87% accuracy
  Aspect Extraction Accuracy: 90% (manual validation)
  Chatbot Relevance Score: 92%, Empathy Score: 87%

🚀 Future Extensions

- Multi-language support (e.g., Hindi, German, French)
- GPT-4/LLM integration for smarter repliers
- Clinical validation through partnerships with pharma
- Deploy to Hugging Face Spaces or Streamlit Cloud

🔗 Data Access

Due to file size constraints, all datasets (raw and cleaned), models, and preprocessed CSVs are available here:
📎 Google Drive Link: https://drive.google.com/drive/folders/1EKRoAs0yrQwHV3Utn1xUAgKG1bfTcB-R 



