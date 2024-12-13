# ChatGPT-sentiment-analysis

# ChatGPT Sentiment Analysis

This repository contains a real-time sentiment analysis system for analyzing user sentiments about ChatGPT based on Reddit data. The project leverages modern big data and machine learning technologies, such as Apache Kafka and Apache Spark, to stream, process, and visualize sentiment data effectively.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)

## Overview

ChatGPT has quickly become one of the most widely used AI-driven chatbot systems. This project aims to analyze the sentiment of Reddit posts mentioning ChatGPT in real-time, enabling users to gain insights into community opinions. It utilizes submissions containing keywords such as `ChatGPT`, `OpenAI`, and `GPT`.

The analysis system is divided into two main components:
1. Offline: Machine learning model training for sentiment classification.
2. Online: Real-time pipeline for streaming and classifying Reddit data and visualizing results.

## Features
- Real-time sentiment analysis of Reddit posts about ChatGPT.
- Machine learning models trained on a labeled dataset with Naive Bayes, SVM, and Logistic Regression.
- Data streaming and processing using Apache Kafka and Apache Spark.
- Interactive web interface built with Streamlit and Plotly for visualization.
- Sentiment breakdown into positive, neutral, and negative categories.

## System Architecture

### Offline Component
- **Data Source**: Dataset from [Kaggle](https://www.kaggle.com/datasets/charunisa/chatgpt-sentiment-analysis) with 217,622 labeled observations.
- **Preprocessing**:
  - Replacing URLs.
  - Lowercasing text.
  - Removing non-alphabet characters and stop-words.
- **Feature Extraction**:
  - HashingTF (Term Frequency), IDF (Inverse Document Frequency), and NGram.
- **Machine Learning Models**:
  - Logistic Regression, SVM (One-vs-Rest strategy), and Naive Bayes.
  - Best-performing model: SVM with a weighted F1-score of 81%.

### Online Component
- **Data Pipeline**:
  1. Reddit Streaming via PRAW and Reddit API.
  2. Apache Kafka for real-time data ingestion.
  3. Apache Spark Streaming for data preprocessing and classification.
- **Visualization**:
  - Streamlit web app for dashboards.
  - Plotly for interactive charts (e.g., bar and line charts for sentiment trends).

![System Architecture](path-to-system-architecture-image)

## Technologies Used
- **Programming Languages**: Python
- **Big Data Frameworks**: Apache Kafka, Apache Spark
- **Libraries**: Streamlit, Plotly, PRAW, Spark MLlib
- **Development Environment**: Google Colab

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nguyen-Thien-Tri/ChatGPT-sentiment-analysis.git
   cd ChatGPT-sentiment-analysis
   ```
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Apache Kafka and Spark in your environment.
4. Configure Reddit API credentials in a `.env` file.

## Future Enhancements

- Extend analysis to other AI tools (e.g., Google Bard, Midjourney).
- Support full Reddit submission content (not just titles).
- Improve visualization with additional interactive features.
- Optimize data storage for growing datasets.

## Contributors
- **Nguyen Thien Tri**
- **Doan Bao Long**
- **Nguyen Viet Tien**
- **Do Trong Hop**

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

For any inquiries or issues, feel free to open an issue or contact the contributors.
