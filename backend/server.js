const express = require('express');
const cors = require('cors');
const path = require('path');

// ✅ Load environment variables from backend/.env
require('dotenv').config({ path: path.resolve(__dirname, './.env') });

console.log("🔗 MONGO_URI:", process.env.MONGO_URI);

// ❗ Optional safety check to prevent silent failure
if (!process.env.MONGO_URI) {
  console.error('❌ MONGO_URI not defined in .env');
  process.exit(1);
}

// ✅ MongoDB connection setup
require('./db/mongo.js');

// ✅ Route imports
const emailRoutes = require('./routes/emailRoutes.js');

// ✅ Create Express app
const app = express();
const PORT = process.env.PORT || 5000;

// ✅ Middleware
app.use(cors());
app.use(express.json());

// ✅ API Routes
app.use('/api', emailRoutes); // /api/send, /api/status, etc.

// ✅ Health Check
app.get('/', (req, res) => {
  res.send('⚡ VoltMail Backend is Running!');
});

// ✅ Error Handler
app.use((error, req, res, next) => {
  console.error('Error:', error);
  res.status(500).json({ error: 'Something went wrong!' });
});

// ✅ Launch Server
app.listen(PORT, () => {
  console.log(`🚀 Server running at http://localhost:${PORT}`);
});
