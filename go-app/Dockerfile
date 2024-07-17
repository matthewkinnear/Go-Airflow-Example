FROM golang:1.16

WORKDIR /app

COPY . .

RUN go mod init go-app
RUN go get -d -v ./...
RUN go build -o main .

CMD ["/app/main"]
