docker build -t lambdafunction .
docker run -it --name awslambda lambdafunction /bin/bash
# docker cp awslambda:/dist.zip .
