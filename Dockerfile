FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
COPY manage.py /app/
RUN pip install -r requirements.txt
COPY ./api /app/api/
