FROM python:3.8-slim-buster

LABEL maintainer="Mohammed Mwijaa<mm.mwijaa@gmail.com>"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_NO_CACHE_DIR 1
ENV PORT 5000

RUN apt-get update && \
	apt-get -y upgrade && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

RUN groupadd appusers && \
	useradd -mg appusers -s /bin/sh app && \
	mkdir -p /home/app/src && \
	chown -R app:appusers /home/app/src

WORKDIR /home/app/src

COPY requirements.txt .

RUN pip install --upgrade pip && \
	pip install -r requirements.txt

USER app

COPY --chown=app:appusers . .

EXPOSE $PORT

ENTRYPOINT gunicorn \
		   app.main:app \
		   -w 3 \
		   -k uvicorn.workers.UvicornWorker \
		   --max-requests 1024 \
		   --max-requests-jitter 100 \
		   --worker-tmp-dir /dev/shm \
		   --access-logfile=- \
		   --log-file=- \
		   -b 0.0.0.0:$PORT
