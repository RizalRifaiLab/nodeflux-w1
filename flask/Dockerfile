FROM jjanzic/docker-python3-opencv:opencv-3.2.0

WORKDIR /app
COPY haarcascade haarcascade
COPY templates templates
COPY app-flask.py .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3", "app-flask.py" ]
