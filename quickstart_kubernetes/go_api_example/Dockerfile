FROM golang:1.9.1 as builder
ADD server.go server.go
# The net package kind of uses c bindings which may link different on the golang docker container as compared to the
# alpine package that we intend to finally move to
RUN CGO_ENABLED=0 GOOS=linux go build server.go

FROM alpine:latest
COPY --from=builder go/server .
RUN echo $(ls) 
CMD ./server