#Degree of profanity in a Twitter tweet
import sys
import os

def length_of_tweet(tweet_sentence):                                            #FUNCTION TO GET THE WORDS IN A SENTENCE OF TWEET
    tweet_sentence = tweet_sentence.split()
    return len(tweet_sentence)

def calculate_dop(tweets):                                                      #DEGREE OF PROFANITY = DOP
    count = 0                                                                   #FUNCTION TO GET THE DOP VALUE OF A TWEET
    found = 0
    for tweet in tweets:
        if tweet!='':                                                           #ASSUMING EVERY TWEET IS SEPERATED BY EMPTY LINE
            print(tweet)
            count += length_of_tweet(tweet)                                     #GETTING TOTAL LENGTH OF THE TWEET IF IT'S MULTI-LINE TWEET
            for word in slur_words:                                             #COMPARING EVERY SLUR_WORD IN TWEET
                if word in tweet:
                    found += 1
        else:                                                                   #DOP = SUM OF SLUR_WORDS FOUND IN TWEET / TOTAL WORDS IN TWEET
            print('Degree of Profanity Found in Twitter Tweet is {0:.2f}'.format(found/count),'\n\n')
            count = 0                                                           #RESETTING VARIABLES FOR NEXT TWITTER TWEET
            found = 0

tweet_file_name = input('Enter Twitter tweet file name :')
if (len(tweet_file_name)<1): tweet_file_name = 'tweet.txt'                      #DEFAULT TO ENTER FILE NAME IF IN CASE NO INPUT IS GIVEN

slur_file_name = input('Enter racial slur file name :')
if (len(slur_file_name)<1): slur_file_name = 'slur_words.txt'

try:
    open_tweet = open(tweet_file_name)                                          #TO ELIMINATE THE FILE I/O ERROR TRY-EXCEPT METHOD IS USED
    open_rs = open(slur_file_name)
except:
    print('File name not Found!!! Please re-enter file name')
    quit()

twitter_comments = [i.strip().upper() for i in open_tweet]                      #STORING TWITTER TWEETS IN A LIST
slur_words = [i.strip().upper() for i in open_rs]

calculate_dop(twitter_comments)                                                 #FUNCTION TO GET THE DEGREE OF PROFANITY OF TWITTER TWEETS
