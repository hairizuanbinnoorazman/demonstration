virtualenv temp
source temp/bin/activate
pip install -r requirements.txt

mkdir dist
cp lambda_function.py ./dist/lambda_function.py
cp -r ./temp/lib/python2.7/site-packages/* ./dist/

cd dist
zip -r lol.zip .
cd ..
