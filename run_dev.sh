APPNAME=scrabble-picker
VERSION=0.0.1

FLASK_NAME=$APPNAME-flask
NODE_NAME=$APPNAME-node

FLASK_TAG=$FLASK_NAME:$VERSION
NODE_TAG=$NODE_NAME:$VERSION

NETWORK_NAME=scrabble-net

# Clean up
docker image prune -f
docker stop $FLASK_NAME
docker stop $NODE_NAME
docker network rm $NETWORK_NAME

# Build
docker network create $NETWORK_NAME
docker build --tag $APPNAME-flask:$VERSION api/ 
docker build --tag $APPNAME-node:$VERSION web/

# Run
docker run --rm --name $FLASK_NAME --publish 8000:5000 \
  --mount type=bind,source="$(pwd)"/api,target=/usr/src/app \
  --network $NETWORK_NAME \
  -d \
  $FLASK_TAG
docker run --rm --name $NODE_NAME --publish 8080:8080 \
  --mount type=bind,source="$(pwd)"/web,target=/usr/src/app \
  -d \
  --network $NETWORK_NAME \
  $NODE_TAG
