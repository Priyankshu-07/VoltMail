const nodemailer = require('nodemailer');

async function sendEmail(recipientEmail, subject, body) {
  try {
    // Input validation
    if (!recipientEmail || !subject || !body) {
      throw new Error('Missing required parameters: recipientEmail, subject, and body are required');
    }

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(recipientEmail)) {
      throw new Error('Invalid recipient email format');
    }

    // Check for required environment variables
    if (!process.env.SENDER_EMAIL || !process.env.SENDER_PASS) {
      throw new Error('Missing environment variables: SENDER_EMAIL and SENDER_PASS must be set');
    }

    // Create transporter with improved configuration
    const transporter = nodemailer.createTransporter({
      service: 'gmail',
      auth: {
        user: process.env.SENDER_EMAIL,
        pass: process.env.SENDER_PASS  // Gmail App Password
      },
      // Additional security options
      secure: true,
      tls: {
        rejectUnauthorized: false
      }
    });

    // Verify transporter configuration
    await transporter.verify();

    const mailOptions = {
      from: process.env.SENDER_EMAIL,
      to: recipientEmail,
      subject: subject,
      text: body,
      // Optional: Add HTML version
      html: `<p>${body.replace(/\n/g, '<br>')}</p>`
    };

    const info = await transporter.sendMail(mailOptions);
    console.log("📬 Email sent successfully:", info.response);
    console.log("📧 Message ID:", info.messageId);
    
    return {
      success: true,
      messageId: info.messageId,
      response: info.response
    };

  } catch (error) {
    console.error("❌ Email sending failed:", error.message);
    
    // Return error info instead of throwing (optional approach)
    return {
      success: false,
      error: error.message,
      code: error.code || 'UNKNOWN_ERROR'
    };
    
    // Alternative: Re-throw the error for caller to handle
    // throw error;
  }
}

module.exports = sendEmail;