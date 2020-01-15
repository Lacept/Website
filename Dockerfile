FROM python:3.6

COPY ["Actual Web/requirements.txt", "/app/requirements.txt"]

WORKDIR /app
RUN pip install -r requirements.txt

COPY ["Actual Web/*", "/app/"]

CMD ["python", "web.py"]

