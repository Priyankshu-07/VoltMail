import requests
def send_to_backend(query, context, backend_url="http://localhost:5000/api/emails/send"):
    payload = {
        "tone": "friendly",
        "persona": "college student",
        "companyName": "the company",
        "productName": "the role",
        "userContext": context,
        "customPrompt": query,
        "targetAudience": "hiring managers",
        "emailGoal": "job application"
    }   
    try:
        response = requests.post(backend_url, json=payload)
        response.raise_for_status()       
        data = response.json()
        return data.get("email", "No email generated.")      
    except requests.exceptions.RequestException as err:
        return f"Error: {err}"