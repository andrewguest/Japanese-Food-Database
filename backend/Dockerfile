# Base image for this custom image
FROM ubuntu:20.04

RUN apt update && \
    apt upgrade -y && \
    apt install -y python3-pip python3-dev build-essential 

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["api.py"]