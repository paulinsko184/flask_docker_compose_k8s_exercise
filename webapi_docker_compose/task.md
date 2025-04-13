# Task

1. Use the Dockerfile from the webapi_flask folder. It will work here as well (even though the source code is slightly different and comprises also a backend, a redis database)
2. Write a docker-compose file that contains two services: web and redis. The web (frontend) part should build the image based on the Dockerfile, then reroute the container port 8080 to the local 80 port, the redis service should run the redis image (image: redis:alpine). Don't worry about the ports here. Docker will take care of networking between the services.
3. Run the app via docker-compose and access it locally via port 80.
4. Inspect the networks (docker network ls, docker network inspect network_name); what are the service's IP addresses?
5. Shut down the app.