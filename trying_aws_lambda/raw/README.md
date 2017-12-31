# Using Serverless without any frameworks

A quick test on using the AWS Lambda service without going using the frameworks or other tooling out there

# Requests Example

All the required files to get the lambda running is available there.
However, the commands to get the aws lambda and aws endpoints started is not available. Will available in the future.

To create the dist zip for the lambda function
```
sh deploy.sh
```

With that, a `dist.zip` file will be generated. This can be added into lambda.

On GUI

- Create a lambda function in region desired. Permissions for this as `lambda execute`
- Upload the zip as required
- Create the API Endpoint to trigger the lambda
