FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /scrabble_picker
COPY requirements.txt /scrabble_picker/
RUN pip install -r requirements.txt
COPY . /scrabble_picker/
