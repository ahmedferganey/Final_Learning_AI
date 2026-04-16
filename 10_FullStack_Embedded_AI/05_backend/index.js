// index.js
const express = require('express');
const app = express();
const PORT = 7777;

app.get('/', (req, res) => {
  res.send('Hello from port 7777!');
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});

