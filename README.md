# WhatsApp Chat Analyzer

This is a Streamlit app to analyze and visualize a WhatsApp chat text export file.

## Features

- Statistics include total messages, words, media messages, and links
- Monthly and daily timeline is provided
- Busiest Days and Months
- Weekly activity heatmap
- Wordcloud with the most often used words and design
- Highest Emoji usage
- Most active group members

## Code Structure

The project has the following main files:

**app.py**: Main Streamlit app code and UI

**helper.py**: Functions to process and analyze chats

**preprocessor.py**: Preprocess raw WhatsApp export to clean DataFrame

**requirements.txt**: Python packages needed to run project

**whatsapp-chat-analysis**: Jupyter Notebook containing my rough work for the project

**stop_hinglish**: contains Stop words in hindi and english with country codes

## Running the App

1. Clone this repo
2. Install requirements from requirements.txt
3. Run `streamlit run app.py` in terminal 
4. Upload your WhatsApp chat export text file

## Customization

Customizable by tweaking parameters in `helper.py` or adding new visualizations and charts in `app.py`.

## Coming Soon...

- NLP Sentiment for Individual and Group Chat 
- Multilingual Support
