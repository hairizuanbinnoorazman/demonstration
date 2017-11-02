# Scaling in Kubernetes

Includes the following points:
- Deployment of Go application that does work of calculating a fibonacci sequence (Pseudo introduce load)
- Application has an endpoint to receive input and then running the fibonacci function
- Prepare a deployment, service, horizontal scaling

# Understanding performance

One possible tool: Vegeta

```
# Mac command
brew install vegeta
```

Command to run:
```
echo "GET http://localhost:3000/fibonacci?n=12" | vegeta attack -duration=10s -rate=100  | tee results.bin | vegeta report -reporter plot > report.html
```
