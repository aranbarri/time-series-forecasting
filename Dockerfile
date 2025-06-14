FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["streamlit", "run", "main.py", "--server.port=8888", "--server.address=0.0.0.0"]
