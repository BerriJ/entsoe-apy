#!/bin/sh

echo "Fetching Postman collection..."
curl -v "https://documenter.getpostman.com/api/collections/7009892/2s93JtP3F6" | jq > ./misc/TransparencyPlatformRestfulAPI.postman_collection.json
echo "Response received. File size:"
ls -lh ./misc/TransparencyPlatformRestfulAPI.postman_collection.json
echo "First 500 characters of response:"
head --lines=50 ./misc/TransparencyPlatformRestfulAPI.postman_collection.json