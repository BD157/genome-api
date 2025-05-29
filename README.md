# Genome Clustering & Variant Classification API

Application for clustering and classifying SARS-CoV-2 genome sequences.

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
