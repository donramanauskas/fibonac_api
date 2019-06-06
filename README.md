REST API that calculates Fibonacci sequence, it supports these
methods:

    GET returns {"success": "Welcome to FibonacciAPI App"}
    POST {"number": 5} returns [0, 1, 1, 2, 3]
    
The easiest way to run app localy is using docker-compose.

You need to have docker and docker-compose installed on your 
local machine. In project root folder run:

docker-compose up

When you want to terminate app:

docker-compose down

After making any code changes, you need to rebuild using:

docker-compose build

To access container fibonaci_api_web container:

docker ps
docker exec -ti <CONTAINER ID> /bin/bash

Deployment pipeline is done using Jenkins.