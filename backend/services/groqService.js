const axios = require('axios');
function callGroqAPI(prompt) {
  return new Promise((resolve, reject) => {
    const requestData = {
      model: 'llama3-8b-8192',
      messages: [
        {
          role: 'system',
          content: 'You are an expert email copywriter.'
        },
        {
          role: 'user',
          content: prompt
        }
      ],
      temperature: 0.7,
      max_tokens: 512
    };
    const headers = {
      'Authorization': 'Bearer ' + process.env.GROQ_API_KEY,
      'Content-Type': 'application/json'
    };
    axios
      .post('https://api.groq.com/openai/v1/chat/completions', requestData, { headers })
      .then((response) => {
        const message = response.data.choices[0].message.content.trim();
        resolve(message);
      })
      .catch((error) => {
        console.error(' Groq API Error:', error.response ? error.response.data : error.message);
        reject(new Error('Failed to get email from Groq'));
      });
  });
}
module.exports = callGroqAPI;