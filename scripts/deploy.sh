#!/bin/bash

echo "***************************************"
echo "** Deploying image into GCP VM  *******"
echo "***************************************"


echo ">>>> Removing previous image..."
docker rm -fv api-container
#Run the new contaniner
echo ">>>> Runing the container....."
docker run -d -p 5000:5000 --name api-container gcr.io/nicolaspencer/api-server-image
