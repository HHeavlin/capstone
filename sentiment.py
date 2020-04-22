'''
sentiment.py
By: Joseph Chan
Sentiment Analysis for Chatlogs

'''
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Chat_reader():
    '''
    Assuming that there is a chat entity or iterable for chat sentences.
    '''
    def __init__(self,chatEntity):
        '''
        Sets up an analyzer object to get an average sentiment
        '''
        self.chat_sentences = []
        self.sentiment = []
        self.avgsent = 0
        self.analyzer = SentimentIntensityAnalyzer()
        self.update_dict()
        for line in chatEntity:
            self.chat_sentences.append(line)

        for sentence in self.chat_sentences:
            self.sentiment.append(self.analyzer.polarity_scores(sentence))

        for sent in self.sentiment:
            self.avgsent += sent['compound']

        if len(self.sentiment):
            self.avgsent /= len(self.sentiment)

    def update_dict(self):
        '''
        call file s1.csv
        '''
        nd = {} 
        df = pd.read_csv('s1.csv', index_col = 0)
        for col in df.columns:
            nd[col] = df.loc['AVERAGE RATING', col]
        self.analyzer.lexicon.update(nd)

    def parse_comment(self, comment):
        '''
        This will take apart the log line with a timestamp, content, and username
        '''
        colonpos = comment.find(":")
        timestmpUser = comment[:colonpos]
        content = comment[colonpos+1:]
        timestamp = timestmpUser[:24]
        username = timestmpUser[25:]

        return (content, timestamp, username)

    def __repr__(self):
        '''
        Incase print
        '''
        numchats = len(self.chat_sentences)
        return "Average sentiment for chatlog: " + str(self.avgsent) + "\n" + "Total number of Chat entries: " + str(numchats)
        



