# Create the distribution folder
rm -rf dist
rm -f dist.zip
mkdir dist

# Build the go application
env GOOS=linux GOARCH=amd64 go build main.go

# Copy lambda files in
cp lambda_function.py ./dist/lambda_function.py
cp main ./dist/main

# Generate the distribution zip
cd dist
zip -r dist.zip .
cd ..
cp dist/dist.zip dist.zip
