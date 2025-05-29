# Genome Clustering & Variant Classification API

Application for clustering and classifying SARS-CoV-2 genome sequences. This app allows users to input RNA sequences and instantly receive either a predicted variant classification or an assigned cluster ID based on sequence similarity. It combines a FastAPI backend for processing and a Streamlit frontend for easy interaction.


## Local Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Docker

```bash
docker build -t genome-api .
docker run -p 8000:8000 genome-api
```

## Streamlit

## Link: https://genome-api-bd-mle.streamlit.app/

## API (Hosted via Render)

- `/health`
- `/cluster`
- `/classify`
