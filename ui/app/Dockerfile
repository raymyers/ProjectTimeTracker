# Stage 1: Compile and Build angular codebase
# Use official node image as the base image
# cd ui/app
# docker build -f Dockerfile -t tylerm007/timetracker_frontend --rm .
# docker tag tylerm007/timetracker_frontend tylerm007/timetracker_frontend:1.0.0
# docker push tylerm007/timetracker_frontend:1.0.11  # requires docker login
#
# docker tag tylerm007/timetracker_frontend tylerm007/timetracker_frontend:latest
# docker push tylerm007/timetracker_frontend:latest  

# curl -X POST http://apilogicserver:5656/ontimizeweb/services/rest/users/login -H 'Authorization: Basic YWRtaW46cA=='
# curl -X POST http://192.168.80.1:5655/ontimizeweb/services/rest/users/login -H 'Authorization: Basic YWRtaW46cA=='
#  curl -X POST http://localhost:5655/ontimizeweb/services/rest/users/login -H 'Authorization: Basic YWRtaW46cA=='
#  curl -X POST http://apilogicserver:5655/ontimizeweb/services/rest/users/login -H 'Authorization: Basic YWRtaW46cA=='
FROM node:18.10.0-alpine as build
USER root

# Set the working directory
WORKDIR /usr/local/app

COPY package*.json .

# Install all the dependencies
RUN npm install

COPY . .

#RUN apt-get clean
#RUN echo 'Acquire::http::Pipeline-Depth 0;\nAcquire::http::No-Cache true;\nAcquire::BrokenProxy true;\n' > /etc/apt/apt.conf.d/99fixbadproxy

# Generate the build of the application
RUN npm run production
#RUN apt-get update && apt-get install -y nano

# Stage 2: Serve app with nginx server

# Use official nginx image as the base image
FROM nginx:latest

# Copy the build output to replace the default nginx contents.
COPY --from=build /usr/local/app/dist /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY /setenv.sh /opt
RUN chmod +x /opt/setenv.sh
EXPOSE 80
CMD ["sh", "-c", "/opt/setenv.sh && nginx -g 'daemon off;'"]



