FROM python:3.7.6-alpine
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 1235
CMD ["python", "./server.py"]