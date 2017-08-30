!#/bin/bash

docker build -t restaurant-service-pyramid . && \
docker run -p 8080:8080 restaurant-service-pyramid gunicorn start:app -w 3 -b :8080
