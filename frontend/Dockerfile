# Use an official Node.js runtime as a parent image
FROM node:alpine AS build
WORKDIR '/app'
COPY ./package.json ./
RUN npm config set strict-ssl false
RUN npm install
COPY . /app
RUN npm run build
# Copy the rest of the app's code into the container

# Use a lightweight server to serve the build folder
FROM nginx:alpine

# Copy the React build files from the 'build' stage to the Nginx container
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 to access the React app
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
