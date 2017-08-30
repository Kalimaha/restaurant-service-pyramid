!#/bin/bash
docker build -t restaurant-service-pyramid . && docker run restaurant-service-pyramid python setup.py test
