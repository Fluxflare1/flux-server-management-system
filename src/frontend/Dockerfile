
# Base image
FROM node:14

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
COPY package-lock.json .
RUN npm install

# Copy project files
COPY . .

# Expose port and start application
EXPOSE 3000
CMD ["npm", "start"]
