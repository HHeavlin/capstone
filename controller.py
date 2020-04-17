'''
Author: Jacob Heller
Date: 02/26/20

Description: 
'''
import datetime
from j_utils import *
from sentiment import Chat_reader
from parsingzip import parsing_zip_file
def generate_sentiment(clipdata):
    '''
    input list of clips
    output list of chat_reader objs
    '''
    sentiments = []
    for clip in clipdata:
        d = clip['created_at']
        d = datetime.datetime(int(d[0:4]), int(d[5:7]), int(d[8:10]), int(d[11:13]), int(d[14:16]), int(d[17:19]))
        df = parsing_zip_file(d.day, d.month, d.year)
        sentiments.append(Chat_reader(df['Message']))
    return sentiments
#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    moonid = '121059319'
    ui = int(input('Input int num of top clips to get sentiment for: '))
    clips = get_clips(moonid, ui)
    sentiments = generate_sentiment(clips)
    for i, cr in enumerate(sentiments):
        print('Clip Title: ' + clips[i]['title'])
        print('Clip Views: ' + str(clips[i]['view_count']))
        print('Sentiments: ' + str(cr))
    
if __name__ == '__main__':
    main()
