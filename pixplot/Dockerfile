FROM python:3.7-slim-buster

WORKDIR /app

COPY output /app/output
ENV FL_URL=http://localhost:5000

CMD [ "python", "-m", "http.server", "4000", "--directory", "/app/output" ]