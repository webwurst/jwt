FROM python:3.6-alpine3.6

RUN apk --no-cache add tini \
  && apk --no-cache add --virtual .build-deps \
    make gcc python-dev musl-dev \
  && pip install --no-cache-dir \
    "Sanic~=0.6.0" \
  && apk del .build-deps

WORKDIR /usr/src/app
COPY . /usr/src/app

CMD ["/sbin/tini", "--", "python", "server.py"]
