function buildEmailPrompt(tone, persona, company, product, situation, notes, audience, purpose) {
  tone = tone || 'friendly';
  persona = persona || 'college student';
  let prompt = `Write a ${tone} email from a ${persona}.\n\nDetails:\n`;
  if (purpose) prompt += `- Purpose: ${purpose}\n`;
  if (audience || company) {
    const recipient = audience || 'recipient';
    prompt += `- To: ${company ? `${recipient} at ${company}` : recipient}\n`;
  }
  if (product) prompt += `- About: ${product}\n`;
  if (situation) prompt += `- Your situation: ${situation}\n`;
  if (notes?.trim()) prompt += `- Extra notes: ${notes.trim()}\n`;
  return prompt + '\nWrite just the subject line and email body. Keep it natural and genuine.';
}
module.exports = buildEmailPrompt;