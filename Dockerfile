FROM python:3.9.7-slim

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apt-get update

RUN apt-get install -y tshark

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ] 

CMD [ "app.py" ]