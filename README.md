**Fibonacci API**

REST API that calculates Fibonacci sequence, it supports these
methods:

    GET returns {"success": "Welcome to FibonacciAPI App"}
    POST {"number": 5} returns [0, 1, 1, 2, 3]
    
The App includes Django REST framework GUI, so you can make POST request from the browser.
    
**Running Application Locally**
    
The easiest way to run app locally is using docker compose.

You need to have docker and docker-compose installed on your 
local machine. In project root folder run:

_docker-compose build && docker-compose up_

When you want to terminate app:

_docker-compose down_

To access container fibonaci_api_web container:

_docker ps_

docker exec -ti <CONTAINER ID> /bin/bash

**Deployment Pipeline**

Deployment pipeline is done using Jenkins. It consists of  1 Jenkins server,
1 kubernetes master and 1 kubernetes node server. Jenkins is pulling from
github repository deploys to canary deployment first, that is defined in 
fibonacci-api-canary.yml if smoke tests passes, code is promoted to production 
kubernetes deployment defined in fibonacci-api-kube.yml

**Jenkins Configuration steps:**

I'm planning to add script for Jenkins server configuration shortly.

At the moment, I did configuration via GUI.

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

Add the Kubeconfig from the Kubernetes master as a credential in Jenkins.

From kubernetes master display the contents of our Kubeconfig:
                      
                      cat ~/.kube/config
                      
Click Add Credentials in the menu on the left of the page.

Add credentials with the following information:

Kind: Kubernetes configuration (kubeconfig)
ID: kubeconfig
Description: Kubeconfig
Kubeconfig: Enter directly
Content: Paste the contents of ~/.kube/config
Click OK.

In the GitHub section, click Add GitHub Server and then click 
GitHub Server.

Name: GitHub
Credentials: Click Add and then click Jenkins
Kind: Secret text
Secret: Paste the GitHub API token from the earlier step
ID: github_secret
Description: GitHub Secret
Click Add. Click the dropdown next to Credentials and select the 
GitHub Secret we just added. Click Save.

**Set Up Project**

Back in the Jenkins tab in our browser, click New Item. Use a Name of "fibonacci-api" and select 
Multibranch Pipeline as the type. Click OK.

In the Branch Sources section, click Add source, and then click GitHub.

Credentials: Select the GitHub Key
Owner: Enter your GitHub username
Repository: Select repository, where you forked the project

Click save.