FROM python:3.10

# Add python file and directory
COPY telebot/source /app/source
COPY telebot/requirements.txt /app/requirements.txt
COPY .env /app/.env

WORKDIR /app/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt