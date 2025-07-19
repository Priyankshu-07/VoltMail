function buildEmailPrompt(tone, persona, company, product, situation, notes, audience, purpose) {
  tone = tone || 'friendly';
  persona = persona || 'college student';
  let prompt = `Write a ${tone} email from a ${persona}.\n\n`;
  prompt += 'Details:\n';
  if (purpose) {
    prompt += `- Purpose: ${purpose}\n`;
  }
  if (audience || company) {
    let recipient = audience || 'recipient';
    if (company) {
      recipient += ` at ${company}`;
    }
    prompt += `- To: ${recipient}\n`;
  }
  if (product) {
    prompt += `- About: ${product}\n`;
  }
  if (situation) {
    prompt += `- Your situation: ${situation}\n`;
  }
  if (notes && notes.trim()) {
    prompt += `- Extra notes: ${notes.trim()}\n`;
  }
  prompt += '\nWrite just the subject line and email body. Keep it natural and genuine.';
  return prompt;
}
module.exports = buildEmailPrompt;