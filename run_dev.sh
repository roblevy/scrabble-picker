APPNAME=scrabble-picker
VERSION=0.0.1

API_NAME=$APPNAME-api
WEB_NAME=$APPNAME-web

API_TAG=$API_NAME:$VERSION
WEB_TAG=$WEB_NAME:$VERSION

API_PORT=5000
NETWORK_NAME=scrabble-net

# Clean up
docker image prune -f
docker stop $API_NAME
docker stop $WEB_NAME
docker network rm $NETWORK_NAME

# Build
docker network create $NETWORK_NAME
docker build --tag $APPNAME-api:$VERSION api/ 
docker build --tag $APPNAME-web:$VERSION web/

# Run
docker run --rm --name $API_NAME \
  --mount type=bind,source="$(pwd)"/api,target=/usr/src/app \
  --network $NETWORK_NAME \
  -d \
  $API_TAG
docker run --rm --name $WEB_NAME --publish 8080:8080 \
  --mount type=bind,source="$(pwd)"/web,target=/usr/src/app \
  -d \
  --env API=$API_NAME \
  --env API_PORT=$API_PORT \
  --network $NETWORK_NAME \
  $WEB_TAG
