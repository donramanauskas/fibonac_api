REST API that calculates Fibonacci sequence, it supports these
methods:

    GET returns {"success": "Welcome to FibonacciAPI App"}
    POST {"number": 5} returns [0, 1, 1, 2, 3]
    
The easiest way to run app locally is using docker-compose.

You need to have docker and docker-compose installed on your 
local machine. In project root folder run:

docker-compose build && docker-compose up

When you want to terminate app:

docker-compose down

To access container fibonaci_api_web container:

docker ps
docker exec -ti <CONTAINER ID> /bin/bash

Deployment pipeline is done using Jenkins. 

I'm planning to add script for Jenkins configuration shortly.

At the moment, I did configuration via GUI.

Jenkins Configuration steps:

Navigate to the GitHub tab in your browser. Click your profile picture in the top right of the page, 
click Settings, click Developer settings, click Personal access tokens, and finally click Generate new token.

Name this token "jenkins" and be sure to click the checkbox next to admin:repo_hook. Click Generate token at the bottom 
of the page. Copy the token to your clipboard.

Back in the Jenkins tab in your browser, click Credentials in the menu on the left of the page and then click global. 

Click Add Credentials in the menu on the left of the page. 
Provide the following information:

Username: Provide your GitHub username
Password: Paste the API token from your clipboard.
ID: github_key
Description: GitHub Key
Click OK.

Click Add Credentials in the menu on the left of the page.

Add Docker Hub Credentials in Jenkins
Note: You will need a DockerHub account for this step.

Username: Provide your DockerHub username
Password: Provide your DuckerHub password
ID: docker_hub_login
Description: Docker Hub Login
Click OK.

