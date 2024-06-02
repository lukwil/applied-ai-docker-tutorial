#!/bin/sh

echo "Downloading Git repository..."
git clone https://github.com/lukwil/applied-ai-docker-tutorial.git

echo "Updating dependencies..."
apk update

echo "Installing editor..."
apk add nano

echo "Installing syntax highlighting for editor..."
source <(curl https://raw.githubusercontent.com/scopatz/nanorc/master/install.sh)