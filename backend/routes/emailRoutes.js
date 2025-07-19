const express = require('express');
const { handleEmailSend, getEmailLogs } = require('../controllers/emailController.js');
const router = express.Router();
router.post('/send', handleEmailSend);      
router.get('/email-logs', getEmailLogs);   
module.exports = router;
