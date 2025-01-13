FROM gitpod/workspace-full:latest

# Install AWS CLI
RUN sudo apt-get update && sudo apt-get install -y awscli

# Configure AWS CLI using environment variables
RUN mkdir -p ~/.aws && \
    echo "[default]" > ~/.aws/credentials && \
    echo "aws_access_key_id=$AWS_ACCESS_KEY_ID" >> ~/.aws/credentials && \
    echo "aws_secret_access_key=$AWS_SECRET_ACCESS_KEY" >> ~/.aws/credentials && \
    echo "[default]" > ~/.aws/config && \
    echo "region=$AWS_DEFAULT_REGION" >> ~/.aws/config

# Clean up
RUN sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*
