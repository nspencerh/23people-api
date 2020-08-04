#!/bin/bash

echo "****************************"
echo "** Building Docker Image ***"
echo "****************************"

docker-compose docker-compose.yml build --no-cache
