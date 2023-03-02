FROM python:3.11

WORKDIR /platzi
COPY . /platzi/

RUN pip install --no-cache-dir --upgrade pip
RUN chmod +x ./scripts/wait-for-it.sh
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8082
