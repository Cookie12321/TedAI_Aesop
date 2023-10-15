FROM python:3.7

RUN apt-get update && apt-get install -y sqlite3
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

COPY response_example.json /
COPY scoring_criteria.json /

EXPOSE 5000
