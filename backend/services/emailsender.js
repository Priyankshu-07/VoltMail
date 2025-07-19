const nodemailer = require('nodemailer');
async function sendEmail(email, subject, message) {
  try {
    if (!email || !subject || !message) {
      throw new Error('Please provide email, subject, and message');
    }
    if (!email.includes('@')) {
      throw new Error('Please enter a valid email address');
    }
    if (!process.env.SENDER_EMAIL || !process.env.SENDER_PASS) {
      throw new Error('Email credentials not configured');
    }
    const transporter = nodemailer.createTransporter({
      service: 'gmail',
      auth: {
        user: process.env.SENDER_EMAIL,
        pass: process.env.SENDER_PASS
      }
    });
    await transporter.verify();
    const emailOptions = {
      from: process.env.SENDER_EMAIL,
      to: email,
      subject: subject,
      text: message
    };
    const result = await transporter.sendMail(emailOptions);   
    console.log('Email sent successfully!');
    return { success: true, id: result.messageId };
  } catch (error) {
    console.log('Failed to send email:', error.message);
    return { success: false, error: error.message };
  }
}
module.exports = sendEmail;