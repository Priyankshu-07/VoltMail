function buildEmailPrompt(tone, persona, company, product, situation, notes, audience, purpose) {
  if (!tone) tone = 'friendly';
  if (!persona) persona = 'college student';
  let prompt = 'Write a ' + tone + ' email from a ' + persona + '.\n\nDetails:\n';
  if (purpose) {
    prompt += '- Purpose: ' + purpose + '\n';
  }
  if (audience || company) {
    let recipient = audience;
    if (!recipient) recipient = 'recipient'; 
    prompt += '- To: ' + recipient;
    if (company) {
      prompt += ' at ' + company;
    }
    prompt += '\n';
  }
  if (product) {
    prompt += '- About: ' + product + '\n';
  }
  if (situation) {
    prompt += '- Your situation: ' + situation + '\n';
  }
  if (notes && notes.trim()) {
    prompt += '- Extra notes: ' + notes.trim() + '\n';
  }
  prompt += '\nWrite just the subject line and email body. Keep it natural and genuine.';
  return prompt;
}
module.exports = buildEmailPrompt;