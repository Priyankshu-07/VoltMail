const express = require('express');
const cors = require('cors');
const path = require('path');
require('dotenv').config();

console.log("🔗 MONGO_URI:", process.env.MONGO_URI);

// MongoDB connection setup
require('./db/mongo.js');

// Route imports
const emailRoutes = require('./routes/emailRoutes.js');

// Create Express app
const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Fix this line 👇 to match frontend expectations
app.use('/api', emailRoutes);

// Health Check
app.get('/', (req, res) => {
  res.send('⚡ VoltMail Backend is Running!');
});

// Error Handler
app.use((error, req, res, next) => {
  console.error('Error:', error);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Launch
app.listen(PORT, () => {
  console.log(`🚀 Server running at http://localhost:${PORT}`);
});
