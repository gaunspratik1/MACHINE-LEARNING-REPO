FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8081
CMD gunicorn --workers=4 --bind 0.0.0.0:8081 app:app
