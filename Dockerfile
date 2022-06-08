FROM python:3.8.13-buster

COPY api /api
COPY viroid-streamlit /viroid-streamlit
COPY ohe_for_flow /ohe_for_flow
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
