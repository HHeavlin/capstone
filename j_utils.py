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
        'Authorization': 'Bearer SOMESTRING',
    }

    params = (
        ('id', name),
    )

    response = requests.get('https://api.twitch.tv/helix/users', headers=headers, params=params)

    return None
    
def get_clips(id, num_clip = 10):
    '''
    Parameters: str id, int num_clip
    Returns: list of clips
    Description: Takes a broadcaster ID and gets some number of most recent clips and returns them
    in a list
    '''
    headers = {
        'Client-ID': 'uo6dggojyb8d6soh92zknwmi5ej1q2',
    }

    params = (
        ('broadcaster_id', id),
        ('first', str(num_clip)),
    )

    response = requests.get('https://api.twitch.tv/helix/clips', headers=headers, params=params)
    return None
    