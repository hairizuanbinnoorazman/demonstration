FROM golang:1.9.1 as builder
ADD ./app/src ./src
RUN go test server
# The net package kind of uses c bindings which may link different on the golang docker container as compared to the
# alpine package that we intend to finally move to
RUN CGO_ENABLED=0 GOOS=linux go build server

FROM alpine:latest
COPY --from=builder go/server .
CMD ./server
