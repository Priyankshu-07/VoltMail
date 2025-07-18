function buildEmailPrompt(
  tone = 'friendly',
  persona = 'college student',
  companyName = '',
  productName = '',
  userContext = '',
  customPrompt = '',
  targetAudience = '',
  emailGoal = ''
) {
  let prompt = `Write a ${tone} email from a ${persona}.\n\n`;
  prompt += `Details:\n`;

  if (emailGoal) prompt += `- Purpose: ${emailGoal}\n`;
  if (targetAudience || companyName) {
    prompt += `- To: ${targetAudience}${companyName ? ` at ${companyName}` : ''}\n`;
  }
  if (productName) prompt += `- About: ${productName}\n`;
  if (userContext) prompt += `- Your situation: ${userContext}\n`;
  if (customPrompt && customPrompt.trim()) {
    prompt += `- Extra notes: ${customPrompt.trim()}\n`;
  }

  prompt += `\nWrite just the subject line and email body. Keep it natural and genuine.`;

  return prompt;
}

module.exports = buildEmailPrompt;
