FROM python:3.8-slim-buster
WORKDIR /app
ADD ./src /app/src
ADD ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
CMD ["python3", "src/main.py"]
