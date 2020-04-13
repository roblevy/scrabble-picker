FROM node:12

WORKDIR /usr/src/app
COPY . .
RUN npm install nodemon -g

EXPOSE 3000

CMD [ "nodemon", "index.js" ]
