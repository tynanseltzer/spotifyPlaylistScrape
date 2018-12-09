import sys
import spotipy
import spotipy.util as util

def authenticate(username, scope = None):
    # clientID = 'SET TO ENV VARIABLE'
    # clientSecret = 'ENV VARIABLE'
    redirectURI = 'http://127.0.0.1/'
    token = util.prompt_for_user_token(username, scope, client_id=clientID,
                                       client_secret=clientSecret,
                                       redirect_uri=redirectURI)
    return token


