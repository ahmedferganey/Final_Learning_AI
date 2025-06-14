# Step 1: Build the app
FROM node:20 AS builder
WORKDIR /app

COPY package.json vite.config.js ./
COPY package-lock.json ./
COPY index.html ./
COPY src ./src
COPY public ./public

RUN npm install && npm run build

# Step 2: Serve with Nginx
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

