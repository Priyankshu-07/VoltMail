const express = require('express');
const handleEmailSend = require('../controllers/emailController.js'); 
const router = express.Router();
router.post('/send', handleEmailSend); 
module.exports = router;
