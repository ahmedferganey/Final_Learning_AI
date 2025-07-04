# ---- 1. Build Stage ----
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy entire project including .env.production
COPY . .

# Copy .env.production to .env so CRA can use it during build
RUN cp .env.production .env

# Build the React app
RUN npm run build || (echo "React build failed!" && cat /app/npm-debug.log || true)



# ---- 2. Serve Stage ----
FROM nginx:alpine

# Copy built files from builder stage to NGINX public folder
COPY --from=builder /app/dist /usr/share/nginx/html

# Custom NGINX config (handles React SPA routing)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Optional runtime environment file (must exist in public/)
COPY public/env-config.js /usr/share/nginx/html/env-config.js

# Optional startup script (e.g., to inject runtime config)
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/docker-entrypoint.sh"]

