const sendEmail = require('../services/emailsender.js');
const EmailLog = require('../db/emaillog.js');
const buildPrompt = require('../services/promptBuilder.js');
const callGroqAPI = require('../services/groqService.js');

async function handleEmailSend(req, res) {
  const {
    recipientEmail,
    subject,
    tone,
    persona,
    userContext,
    companyName,
    productName,
    customPrompt,
    targetAudience,
    emailGoal
  } = req.body;

  console.log("🟢 Incoming request body:", req.body);

  try {
    console.log("🧠 Building prompt...");
    const prompt = buildPrompt(
      tone,
      persona,
      companyName,
      productName,
      userContext,
      customPrompt,
      targetAudience,
      emailGoal
    );
    console.log("✅ Prompt built:", prompt);

    console.log("📡 Calling Groq API...");
    const emailContent = await callGroqAPI(prompt);
    console.log("✅ Groq returned:", emailContent);

    console.log("📤 Sending email...");
    await sendEmail(recipientEmail, subject, emailContent);
    console.log("✅ Email sent.");

    console.log("🗃️ Saving to MongoDB...");
    await EmailLog.create({
      recipientEmail,
      subject,
      body: emailContent,
      embedding: [],
      status: 'Success'
    });
    console.log("✅ Mongo entry saved.");

    res.status(200).json({
      success: true,
      message: 'Email sent successfully!',
      emailBody: emailContent
    });
  } catch (error) {
    console.error("❌ [FAILURE] Error caught:", error.message);
    console.error("🧨 Stack Trace:", error.stack);

    // Try saving the failure in logs (optional)
    try {
      await EmailLog.create({
        recipientEmail: recipientEmail || 'unknown',
        subject: subject || 'no subject',
        body: 'email generation or sending failed',
        embedding: [],
        status: 'Failed'
      });
    } catch (mongoError) {
      console.error("❌ Failed to log error in MongoDB:", mongoError.message);
    }

    res.status(500).json({
      success: false,
      message: 'Email sending failed',
      error: error.message
    });
  }
}

module.exports = handleEmailSend;
