export function connectSocket() {
  return new WebSocket('ws://localhost:9000/ws');
}

