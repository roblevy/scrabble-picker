FROM node:15
WORKDIR /home/node/app
ENV NODE_ENV=production
EXPOSE 8080
COPY public ./public/
COPY src ./src/
COPY package.json yarn.lock babel.config.js ./
RUN yarn
USER node
