FROM python:3.8.0-slim AS builder

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

COPY . .
ENV FLASK_APP=api.py
ENV FLASK_ENV=development

EXPOSE 5000

CMD [ "python", "-m", "flask", "run", "--host", "0.0.0.0" ]
