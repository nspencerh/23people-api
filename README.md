# 23people-api
This repository contains all the source code used to develop an API that connects to Datastore to get, post, put and delete information. The API was build using Flask, Python, Docker and the asociated files to build a Jenkins Pipeline for CI/CD.
# Prerequisites
- GCP Datastore instance 
- GCP VM with a Container-Optimized OS (provided and maintain by Google)
- Service account with appopiated permission to push Docker images to the GCP Container Registry
- Service account with read/write permission to Datastore 
- Public key in the VM so that Jenkins can connect to the server
- SSH agent Jenkins plugin to connect to the remote server (GCP VM)
- SSH Username with private key in Jenkins credential
- GCLOUD SDK Jenkins plugin 
# Files
- src/api.py: python app that contains the source code from the API. Each Flask App routing is used to map a specific URL with the associated function.
- docker-compose.yml: Use to define and run the docker container
- Dockerfile: Use to build the Docker image. Its build with a python base image, Flask and google-cloud-datastore package installed. Env GOOGLE_APPLICATION_CREDENTIALS with the service account path key must be created.
- Jenkinsfile: To build the pipeline. It contains 3 stages (Build, Push, Deploy) plus the checkout stage configured in Jenkins. Each stage points to a bash script.
- Scripts Folder: Bash scripts (build, push, deploy) that are executed in the corresponding stages of the pipeline.


