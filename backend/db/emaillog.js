const mongoose = require('mongoose');
const emailLogSchema = new mongoose.Schema({
  recipientEmail: { type: String, required: true },
  subject: { type: String, required: true },
  name: { type: String, default: 'Unknown' },
  company: { type: String, default: 'Unknown' },
  role: { type: String, default: 'Unknown' },
  product: { type: String, default: 'Unknown' },
  body: { type: String, required: true },
  embedding: { type: Array, default: [] },
  status: { type: String, enum: ['Success', 'Failed'], default: 'Success' },
  timestamp: { type: Date, default: Date.now }
});
const EmailLog = mongoose.model('EmailLog', emailLogSchema);
module.exports = EmailLog;
