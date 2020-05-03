'''
Author: Jacob Heller
Date: 02/26/20

Description: 
'''
import datetime, json
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
        td = datetime.timedelta(minutes=1)
        d1 = d - td
        d2 = d + td
        df = parsing_zip_file(d.day, d.month, d.year)
        chat = df[(df.Date >= d1) & (df.Date <= d2)]['Message']
        if len(chat) <= 1:
            continue
        sentiments.append(Chat_reader(chat))
    return sentiments

def generate_json(sentiments, clipdata):
    data = []
    for i, s in enumerate(sentiments):
        score = s.avgsent
        d = {
            'score' : round(score, 2),
            'url' : clipdata[i]['url'],
            'thumbnail_url' : clipdata[i]['thumbnail_url'],
            'title' : clipdata[i]['title'],
            'view_count' : clipdata[i]['view_count'],
            'clipped_by' : clipdata[i]['creator_name'],
            'created_at' : clipdata[i]['created_at'],
            'broadcaster' : clipdata[i]['broadcaster_name'], 
            'emote' : s.freqd.max(), 
            'emote_score' : s.emotescore
        }
        data.append(d)
    with open(str(len(sentiments)) + '_clipdata.json', 'w') as fp:
        json.dump(data, fp)

#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    moonid = '121059319'
    ui = int(input('Press 1 for clip data and a diff int for saving json: '))
    if ui == 1:
        ui = int(input('Input int num of top clips to get sentiment for: '))
        clips = get_clips(moonid, ui)
        sentiments = generate_sentiment(clips)
        for i, cr in enumerate(sentiments):
            print('Clip Title: ' + clips[i]['title'])
            print('Clip Views: ' + str(clips[i]['view_count']))
            print('Sentiments: ')
            print(str(cr[0]))
            print(str(cr[1]))
    else:
        ui = int(input('Input int num of top clips to save data for: '))
        clips = get_clips(moonid, ui)
        sentiments = generate_sentiment(clips)
        generate_json(sentiments, clips)
if __name__ == '__main__':
    main()
