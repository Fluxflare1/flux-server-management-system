

# Use official Node.js image as the base
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package.json yarn.lock ./
RUN yarn install

# Copy the rest of the application files
COPY . .

# Expose the app port
EXPOSE 3000

# Start the frontend server
CMD ["yarn", "start"]




# Base image for Node.js
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy application code
COPY . .

# Expose port for the React app
EXPOSE 3000

# Run the application
CMD ["npm", "start"]






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
