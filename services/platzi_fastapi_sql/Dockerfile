FROM python:3.11

WORKDIR /platzi

RUN pip install --no-cache-dir --upgrade pip
COPY . /platzi/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8082
