#!/bin/bash

echo "****************************"
echo "** Building Docker Image ***"
echo "****************************"

#Build the new image
docker-compose build --no-cache
#Tag the builded docker image with the GCP registry
docker tag api-server-image gcr.io/nicolaspencer/api-server-image
