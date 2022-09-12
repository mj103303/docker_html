FROM python:3.7

WORKDIR /usr/src/flask_app
COPY . .
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
