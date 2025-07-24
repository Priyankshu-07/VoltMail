import requests
def send_email(
    recipientEmail, subject, tone, persona, userContext,
    companyName, productName, customPrompt, targetAudience, emailGoal
):
    payload = {
        "recipientEmail": recipientEmail,
        "subject": subject,
        "tone": tone,
        "persona": persona,
        "userContext": userContext,
        "companyName": companyName,
        "productName": productName,
        "customPrompt": customPrompt,
        "targetAudience": targetAudience,
        "emailGoal": emailGoal
    }
    try:
        response = requests.post("http://localhost:5000/api/send", json=payload)
        response.raise_for_status()

        data = response.json()
        if data.get("success") and data.get("emailBody"):
            return data["emailBody"]
        elif data.get("message"):
            return f" Server responded: {data['message']}"
        else:
            return " Email sent, but no content returned."

    except requests.exceptions.RequestException as e:
        return f" Request failed: {e}"

    except Exception as e:
        return f" Unexpected error: {str(e)}"
