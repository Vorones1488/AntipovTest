FROM python:alpine

WORKDIR /app

COPY . /app

RUN pip3 install -r requerements.txt

EXPOSE 5000

CMD ["uvicorn", "main:app"]