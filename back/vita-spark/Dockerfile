FROM python:3.8

WORKDIR /app

COPY . .

RUN apt-get update
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "./app.py"]