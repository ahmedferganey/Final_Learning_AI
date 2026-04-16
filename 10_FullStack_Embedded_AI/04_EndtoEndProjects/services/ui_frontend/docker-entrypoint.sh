#!/bin/sh
set -e

# Replace placeholders with actual env vars from container runtime
sed -i "s|%%VITE_BACKEND_API_URL%%|${VITE_BACKEND_API_URL}|g" /usr/share/nginx/html/env-config.js
sed -i "s|%%VITE_WEBSOCKET_URL%%|${VITE_WEBSOCKET_URL}|g" /usr/share/nginx/html/env-config.js

# Start nginx
exec nginx -g "daemon off;"

