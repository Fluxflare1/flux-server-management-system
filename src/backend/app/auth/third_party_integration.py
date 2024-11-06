# src/backend/auth/third_party_integration.py

from authlib.integrations.flask_client import OAuth
from flask import redirect, url_for

oauth = OAuth()
google = oauth.register(
    name='google',
    client_id='YOUR_GOOGLE_CLIENT_ID',
    client_secret='YOUR_GOOGLE_CLIENT_SECRET',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    client_kwargs={
        'scope': 'openid profile email'
    }
)

def google_login():
    """
    Initiates login via Google OAuth.
    """
    return google.authorize_redirect(url_for('auth.google_authorize', _external=True))

def google_authorize():
    """
    Handles authorization and user session creation.
    """
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token)
    # Create or update user session in the system
    return redirect(url_for('dashboard'))
