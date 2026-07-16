from flask import Flask, request, redirect, session, jsonify
import requests
import os
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'  # Change this to a random secret key

# --- SET THESE FROM YOUR GOOGLE CLOUD CONSOLE ---
CLIENT_ID = '449188330073-f1kmlamcpg47ldbeijt8o99h3ambn7mp.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REDIRECT_URI = 'http://localhost:5678/webhook-test/4ae603a2-5a7f-4d5d-9d43-1d7f6fc4df53'

@app.route('/')
def home():
    if 'access_token' in session:
        return f'''
        <h1>Welcome! You are logged in ✅</h1>
        <p>Access Token: {session['access_token'][:50]}...</p>
        <a href="/calendar">View Calendar Events</a><br>
        <a href="/logout">Logout</a>
        '''
    return '<a href="/login">Login with Google Calendar</a>'

@app.route('/login')
def login():
    # Redirect user to Google to get permission
    google_auth_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code"
        f"&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
        f"&scope=https://www.googleapis.com/auth/calendar.readonly"
        f"&access_type=offline"
    )
    return redirect(google_auth_url)

@app.route('/rest/oauth2-credential/callback')
def callback():
    code = request.args.get('code')
    
    if not code:
        return 'Error: No authorization code received', 400
    
    # Exchange code for access token
    token_url = 'https://oauth2.googleapis.com/token'
    data = {
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    
    try:
        response = requests.post(token_url, data=data)
        token_data = response.json()
        
        if 'error' in token_data:
            return f"Error: {token_data['error_description']}", 400
        
        # Store tokens in session
        session['access_token'] = token_data.get('access_token')
        session['refresh_token'] = token_data.get('refresh_token')
        session['token_expiry'] = (datetime.now() + timedelta(seconds=token_data.get('expires_in', 3600))).isoformat()
        
        return redirect('/')
    
    except Exception as e:
        return f"Error during token exchange: {str(e)}", 500

@app.route('/calendar')
def get_calendar():
    if 'access_token' not in session:
        return redirect('/login')
    
    try:
        # Get calendar events from Google
        headers = {
            'Authorization': f'Bearer {session["access_token"]}'
        }
        
        # Get next 5 events
        response = requests.get(
            'https://www.googleapis.com/calendar/v3/calendars/primary/events?maxResults=5&orderBy=startTime&singleEvents=true',
            headers=headers
        )
        
        events = response.json().get('items', [])
        
        html = '<h1>Your Calendar Events</h1>'
        html += '<a href="/">Home</a> | <a href="/logout">Logout</a><br><br>'
        
        if events:
            html += '<ul>'
            for event in events:
                title = event.get('summary', 'Untitled Event')
                start = event['start'].get('dateTime', event['start'].get('date'))
                html += f'<li>{title} - {start}</li>'
            html += '</ul>'
        else:
            html += '<p>No upcoming events found.</p>'
        
        return html
    
    except Exception as e:
        return f"Error fetching calendar: {str(e)}", 500

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# --- TELEMETRY ROUTES (Handle n8n tracking) ---
@app.route('/rest/telemetry/proxy/v1/page', methods=['POST', 'OPTIONS'])
def telemetry_page():
    return {'status': 'ok'}, 200

@app.route('/rest/telemetry/proxy/v1/track', methods=['POST', 'OPTIONS'])
def telemetry_track():
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run(port=3000)