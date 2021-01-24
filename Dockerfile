FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /picker
COPY requirements.txt /picker/
RUN pip install -r requirements.txt
COPY . /picker/

