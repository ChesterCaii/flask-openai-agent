#!/bin/bash

# Create a temporary directory for the release
RELEASE_DIR="flask-openai-agent-release"
mkdir -p $RELEASE_DIR

# Copy necessary files
cp -r agent api frontend tests app.py config.py requirements.txt README.md CHANGELOG.md .env.example $RELEASE_DIR/

# Create zip file
zip -r flask-openai-agent-v1.0.0.zip $RELEASE_DIR

# Clean up
rm -rf $RELEASE_DIR

echo "Release package created: flask-openai-agent-v1.0.0.zip" 