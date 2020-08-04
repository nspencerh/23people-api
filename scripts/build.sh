#!/bin/bash

echo "****************************"
echo "** Building Docker Image ***"
echo "****************************"

docker-compose build --no-cache
