#!/bin/bash
echo "Detecting Application Framework..."

if [ -f "src/backend/manage.py" ]; then
  echo "Django application detected."
elif [ -f "src/frontend/package.json" ]; then
  echo "Node.js application detected."
elif [ -f "src/ruby-app/Gemfile" ]; then
  echo "Ruby application detected."
elif [ -f "src/php-app/index.php" ]; then
  echo "PHP application detected."
elif [ -f "src/go-app/main.go" ]; then
  echo "Go application detected."
else
  echo "No supported application framework detected."
  exit 1
fi
