import requests

user_message = "can you tell me about black holes in 1 to 2 lines"
requests_message = {"message": user_message}
url = "http://localhost:5678/webhook-test/4ae603a2-5a7f-4d5d-9d43-1d7f6fc4df53"

response = requests.post(url, json=requests_message)
print(f"Status Code: {response.status_code}")

# Print the FULL response to see what we're getting
print("\nFull Response:")
print(response.json())