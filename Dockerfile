FROM python:3.9-slim-buster

WORKDIR /apps/DockerMonitor

COPY . .

RUN apt-get update
RUN apt-get install -y python3 python3-pip apt-transport-https ca-certificates curl gnupg-agent software-properties-common 
RUN mkdir -m 0755 -p /etc/apt/keyrings && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian buster stable"
RUN apt-get update
RUN apt-get install -y docker-ce docker-ce-cli containerd.io

RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
