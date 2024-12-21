

#!/bin/bash
echo "Installing Dependencies..."

if [ -f "src/backend/requirements.txt" ]; then
  pip install -r src/backend/requirements.txt
elif [ -f "src/frontend/package.json" ]; then
  yarn install --cwd src/frontend/
elif [ -f "src/ruby-app/Gemfile" ]; then
  bundle install --gemfile=src/ruby-app/Gemfile
elif [ -f "src/go-app/go.mod" ]; then
  cd src/go-app && go mod tidy
else
  echo "No dependencies to install."
fi



#!/bin/bash
# Script for installing dependencies automatically for Django project

echo "Installing Python dependencies..."
pip install -r requirements.txt

# Additional installation for Django Channels if needed
pip install channels

echo "Dependencies installed."
