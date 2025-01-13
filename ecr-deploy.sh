#!/bin/bash

# Configuration Variables
REPO_NAME="gradio-app"
REGION="us-east-1"
ACCOUNT_ID="163980781550"
IMAGE_TAG="latest"

# Authenticate Docker with ECR
echo "Authenticating Docker with ECR..."
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com
if [ $? -ne 0 ]; then
  echo "Error: Failed to authenticate Docker with ECR."
  exit 1
fi
echo "Docker authenticated with ECR."

# Check if Repository Exists, Create If Not
echo "Checking if repository '$REPO_NAME' exists..."
REPO_CHECK=$(aws ecr describe-repositories --region $REGION --repository-names $REPO_NAME 2>&1)
if [[ $? -ne 0 ]]; then
  if echo "$REPO_CHECK" | grep -q "RepositoryNotFoundException"; then
    echo "Repository '$REPO_NAME' does not exist. Creating it..."
    aws ecr create-repository --repository-name $REPO_NAME --region $REGION
    if [ $? -ne 0 ]; then
      echo "Error: Failed to create repository '$REPO_NAME'."
      exit 1
    fi
    echo "Repository '$REPO_NAME' created successfully."
  else
    echo "Error: Unable to describe repository '$REPO_NAME'."
    exit 1
  fi
else
  echo "Repository '$REPO_NAME' already exists."
fi

# Build Docker Image
echo "Building Docker image '$REPO_NAME'..."
docker build -t $REPO_NAME .
if [ $? -ne 0 ]; then
  echo "Error: Failed to build Docker image."
  exit 1
fi
echo "Docker image built successfully."

# Tag Docker Image
IMAGE_URI="$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:$IMAGE_TAG"
echo "Tagging Docker image as '$IMAGE_URI'..."
docker tag $REPO_NAME:$IMAGE_TAG $IMAGE_URI
if [ $? -ne 0 ]; then
  echo "Error: Failed to tag Docker image."
  exit 1
fi
echo "Docker image tagged successfully."

# Push Docker Image to ECR
echo "Pushing Docker image to ECR..."
docker push $IMAGE_URI
if [ $? -ne 0 ]; then
  echo "Error: Failed to push Docker image to ECR."
  exit 1
fi
echo "Docker image pushed successfully to '$IMAGE_URI'."

echo "ECR deployment complete."
