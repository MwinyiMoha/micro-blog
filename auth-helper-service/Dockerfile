ARG APP_NAME=auth_helper


FROM golang:1.15-alpine as builder

WORKDIR $GOROOT/src/${APP_NAME}

COPY go.* ./

RUN go mod download

COPY . .

RUN go build -ldflags="-s -w" -o build/app ./app

CMD ["go", "run", "app/main.go"]


FROM alpine

ENV GIN_MODE=release

LABEL maintainer="Mohammed Mwijaa<mm.mwijaa@gmail.com>"

RUN apk -U --no-cache upgrade

RUN addgroup app && adduser -D -h /home/app -G app app

WORKDIR /home/app

COPY --chown=app:app --from=builder $GOROOT/src/${APP_NAME}/build/ .

USER app

EXPOSE 5000

ENTRYPOINT [ "./app" ]
