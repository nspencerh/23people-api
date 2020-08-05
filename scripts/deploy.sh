#!/bin/bash

echo "***************************************"
echo "** Deploying image into GCP VM  *******"
echo "***************************************"

#Pulling the image from the registry
echo ">>>> Pulling image from the registry..."
docker pull gcr.io/nicolaspencer/api-server-image
#Remove the previous container
echo ">>>> Removing previous image..."
docker rm -fv api-container
#Sleep for 6 seconds to give time to remove the old container before running the new one
sleep 6
#Run the new contaniner
echo ">>>> Runing the container....."
docker run -d -p 5000:5000 --name api-container gcr.io/nicolaspencer/api-server-image
