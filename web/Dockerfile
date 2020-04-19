FROM node:12
WORKDIR /usr/src/app
# Add package.json and package-lock.json
COPY package*.json ./

RUN npm install

# Copy the app source
COPY . .

EXPOSE 8080
CMD [ "npm", "run", "start" ]
