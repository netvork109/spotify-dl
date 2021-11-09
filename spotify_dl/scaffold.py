import logging
from os import getenv

__all__ = ['log', 'check_for_tokens']

logging.basicConfig(level=logging.INFO,
                    format='%(message)s')


def check_for_tokens():
    """
    Checks if the required API keys for Spotify has been set.
    :param name: Name to be cleaned up
    :return string containing the cleaned name
    """
    log.debug('Checking for tokens')
    CLIENT_ID = getenv('SPOTIPY_CLIENT_ID')
    CLIENT_SECRET = getenv('SPOTIPY_CLIENT_SECRET')
    log.debug("Tokens fetched: {} {}".format(CLIENT_ID, CLIENT_SECRET))

    if CLIENT_ID is None or CLIENT_SECRET is None:
        print('''
            You need to set your Spotify API credentials. You can do this by
            setting environment variables like so:
            Linux:
            export SPOTIPY_CLIENT_ID='your-spotify-client-id'
            export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
            Windows Powershell:
            $env:SPOTIPY_CLIENT_ID='your-spotify-client-id'
            $env:SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
            Windows CMD:
            set SPOTIPY_CLIENT_ID='your-spotify-client-id'
            set SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'

            Get your credentials at
                https://developer.spotify.com/my-applications
        ''')
        return False
    return True
