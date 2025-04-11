FROM python:3.12

ENV PYTHONUNBUFFERED 1

RUN mkdir /teamA_app

WORKDIR /teamA_app

COPY requirements.txt /teamA_app/

RUN pip install -r requirements.txt

COPY . /teamA_app/

RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs
    
RUN npm install bootstrap@5.3.0