'''
Author: Jacob Heller
Date: 02/26/20

Description: utilities for connecting to twitch api
'''
import requests

def get_broadcaster_id(name):
    '''
    Parameters: string for the name of the broadcaster to find
    Returns: str ID of broadcaster
    Description: query the server for the broadcaster name in plaintext to get the id to be used
    later on for getting clips etc
    '''
    headers = {
        'Authorization': 'Bearer ewq8n48deol5mpzmak6cp52cre4h1u',
    }

    params = (
        ('login', name),
    )

    r = requests.get('https://api.twitch.tv/helix/users', headers=headers, params=params)
    r = r.json()
    return r['data'][0]['id']
    
def get_clips(id, num_clip = 10):
    '''
    Parameters: str id, int num_clip
    Returns: list of clips
    Description: Takes a broadcaster ID and gets some number of most recent clips and returns them
    in a list
    '''
    headers = {
        'Client-ID': 'ftag5tm1s9srx33fgz9zg60ebcn0n5',
    }

    params = (
        ('broadcaster_id', id),
        ('first', str(num_clip)),
    )

    r = requests.get('https://api.twitch.tv/helix/clips', headers=headers, params=params)
    return r.json()['data']

