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

You can then proceed to follow some of the instructions or you can just continue to follow the commands here

Run the following commands to get faas in. This involves creating additional workspaces before installing it.
This would reduce confusion when running it.
```
git clone https://github.com/openfaas/faas-netes && \
  cd faas-netes
kubectl create ns openfaas
kubectl create ns openfaas-fn
helm upgrade --install --debug --namespace openfaas \
  --reset-values --set async=false --set rbac=false --set serviceType=LoadBalancer --set functionNamespace=openfaas-fn openfaas openfaas/
```

To delete the openfaas from the cluster
```
helm delete --purge openfaas
```

# Difficulties

- Using a private repository - not really supported in faas-cli yet
- Not too sure what kind of apis available to operate and manipulate the faas service
