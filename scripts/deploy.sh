#!/bin/bash

echo "***************************************"
echo "** Deploying image into GCP VM  *******"
echo "***************************************"

#Pulling the new builed image to the VM
echo ">>>> Pulling the new image from the registry..."
docker pull gcr.io/nicolaspencer/api-server-image:latest
#Remove the previous container
echo ">>>> Removing previous contaniner..."
docker rm -fv api-container
#Run the new contaniner with the latest image from the registry
echo ">>>> Runing the container....."
docker run -d -p 5000:5000 --name api-container gcr.io/nicolaspencer/api-server-image:latest
