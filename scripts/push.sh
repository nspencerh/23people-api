#!/bin/bash

echo "***************************************************"
echo "** Pushing image to the GCP contaniner Registry  **"
echo "***************************************************"

#Authenticate to the registry. Prerequisites:
# - gcloud SDK must be installed in Jenkins server
# - service account with write/permission to the registry must be created in GCP
# - the key file must be in the Jenkins server
$GCLOUD_PATH/gcloud auth activate-service-account registry@nicolaspencer.iam.gserviceaccount.com --key-file=registry-key.json
#Adding credentials to the docker config file
gcloud auth configure-docker -q
#Push the image to the GCP Registry
docker push gcr.io/nicolaspencer/api-server-image
