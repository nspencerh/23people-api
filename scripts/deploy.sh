#!/bin/bash

echo "***************************************"
echo "** Deploying image into GCP VM  *******"
echo "***************************************"

#Pulling the image from the registry
docker pull gcr.io/nicolaspencer/api-server-image
#Remove the previous container
docker rm -fv api-container
#Run the contaniner
docker run -d -p 5000:5000 --name api-container gcr.io/nicolaspencer/api-server-image
