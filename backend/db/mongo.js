const mongoose = require('mongoose');
const path = require('path');
require('dotenv').config({ path: path.resolve(__dirname, '../.env') }); 
const mongoURI = process.env.MONGO_URI;
console.log(" MONGO_URI:", mongoURI);
if (!mongoURI) {
  console.error('MONGO_URI is undefined. Please check your .env file and its path.');
  process.exit(1); 
}
mongoose.connect(mongoURI)
  .then(() => console.log('✅ Connected to MongoDB'))
  .catch((err) => console.error('❌ MongoDB connection error:', err));
module.exports = mongoose;
