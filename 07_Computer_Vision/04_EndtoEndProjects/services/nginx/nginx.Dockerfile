# Use official NGINX base image
FROM nginx:stable-alpine

# Remove default NGINX config
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom NGINX config into the container
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy static frontend build (optional, if using NGINX to serve UI files)
# COPY ./services/ui_frontend/dist/ /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

