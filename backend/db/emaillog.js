const mongoose = require('mongoose');
const emailLogSchema = new mongoose.Schema({
  recipientEmail: { type: String, required: true },
  subject: { type: String, required: true },
  body: { type: String, required: true },
  status: { type: String, enum: ['Success', 'Failed'], default: 'Success' },
  timestamp: { type: Date, default: Date.now }
});
const EmailLog = mongoose.model('EmailLog', emailLogSchema);
module.exports = EmailLog;
