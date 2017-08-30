!#/bin/bash
docker build --no-cache -t restaurant-service-pyramid . && docker run restaurant-service-pyramid pact-test verify consumers
