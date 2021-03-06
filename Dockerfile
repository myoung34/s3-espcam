FROM python:3.7-slim
COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt
CMD ["python", "/src/main.py"]
