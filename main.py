import requests

# Replace <your_access_token> with the actual token
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNjY0MjQ2LCJpYXQiOjE3MzE2NjM5NDYsImp0aSI6IjQ3ZjI5N2I3NzJiODQ4MzBiMGY2NDg2YTQyNDJiNzA3IiwidXNlcl9pZCI6MX0.zn_zIs2tDvFiRU5q6n_zRM9WmZpdCwjHdi5s3U-C_gI"
url = "http://127.0.0.1:8000/api/events/10/register/"

# Data to be sent in the request body
data = {
    "title": "test2",
    "description": "test2",
    "date": "2024-11-15T08:47:43.391Z",
    "location": "London",
    "organizer": 2
}

# Headers, including the Authorization header with the Bearer token
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

# URL to create a new event
create_event_url = "http://127.0.0.1:8000/api/events/"

# Data for creating a new event
new_event_data = {
    "title": "Test Event",
    "description": "This is a test event.",
    "date": "2024-11-15T08:47:43.391Z",
    "location": "Kyiv",
    "organizer": 1
}

# Create the event
response = requests.post(create_event_url, headers=headers, json=new_event_data)
print("Create Event Status:", response.status_code)
print("Create Event Response:", response.json())

# Retrieve the event ID from the response if successful
if response.status_code == 201:  # 201 Created
    event_id = response.json().get("id")
    print("New Event ID:", event_id)

    # Then use this event_id to register for the event
