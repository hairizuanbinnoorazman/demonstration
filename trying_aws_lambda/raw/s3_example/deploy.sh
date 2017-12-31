# Create the virtual environment
rm -rf temp
virtualenv temp
source temp/bin/activate
pip install -r requirements.txt

# Create the distribution folder
rm -rf dist
mkdir dist

# Copy lambda files in
cp lambda_function.py ./dist/lambda_function.py
cp -r ./temp/lib/python2.7/site-packages/* ./dist/

# Generate the distribution zip
cd dist
zip -r dist.zip .
cd ..
cp dist/dist.zip dist.zip

# Deactivate virtual environment
deactivate
