FROM python:3.8.4-alpine3.12

WORKDIR /usr/src/app/

RUN apk add --no-cache gcc \
    libc-dev \
    linux-headers \
    postgresql-dev

COPY requirements.txt /usr/src/app/

RUN pip install uwsgi 

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "/usr/src/app/docker-entrypoint.sh"]