# Task

Now, we want to get the same app from the docker-compose example running on K8s.

1. We need the same Dockerfile as in the docker-compose example.
2. I have already provided the deployment files in the deploy folder. Familiarize with them. In the web deployment, the image is taken from docker.io/gauss71248/webapi_k8s, i.e., from a page on dockerhub. Push your own image to dockerhub (create your own account) and rewrite the deployment accordingly.
3. Run the app in K8s.
4. Now, we want to scale out the web deployment to 5 replicas. Do it. 
5. The out scaling works like a load balancer. How can we make the load balancing transparent? Can you modify the code that we can see the hostname of the requested pod?
6. Modify the source code accordingly, deploy with 5 replicas, and verify the different hostnames after multiple accesses.
7. Remove the deployment.