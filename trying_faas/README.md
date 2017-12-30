# Trying out FAAS in Kubernetes

Run the following commands:

Create the container cluster
```
gcloud container clusters create test-cluster --zone us-central1-a --num-nodes 1
```

Login and access the cluster
```
gcloud container clusters get-credentials test-cluster --zone us-central1-a
```

Install the helm toolkit
```
brew install kubernetes-helm
```

Run the command to initialize and get helm working both on client and on the cluster
```
helm init
```
