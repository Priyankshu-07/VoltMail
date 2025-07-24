const express = require('express');
const cors = require('cors');
require('dotenv').config();
if (!process.env.MONGO_URI) {
  console.error('MONGO_URI not defined in .env');
  process.exit(1);
}
require('./db/mongo.js');
const emailRoutes = require('./routes/emailRoutes.js');
const app = express();
const PORT = process.env.PORT || 5000;
app.use(cors());
app.use(express.json());
app.get('/', (req, res) => res.send('VoltMail'));
app.use('/api', emailRoutes);
app.use((error, req, res, next) => {
  console.error('Error:', error);
  res.status(500).json({ error: 'Something went wrong!' });
});
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});