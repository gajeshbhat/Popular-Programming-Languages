from tweet_modules import *

def stream_and_close(lang_list,stream_time):
    twit_stream_listner = PlangAnalysis()
    twit_stream_listner.set_auth()
    twit_stream_listner.set_total_stream_minutes(stream_time)
    twit_stream = tweepy.Stream(auth=twit_stream_listner.auth_object,listener=twit_stream_listner)
    twit_stream.filter(track=lang_list,async=True)

def read_lang_input():
    lang_list = list(str(input("Enter List of programming languages. Space Saperated\n")).lower().split())
    return lang_list

def read_stream_time():
    stream_time = int(input("Enter time to stream.(In minutes)\n"))
    return stream_time

def main():
    lang_list = read_lang_input()
    stream_time = read_stream_time()
    stream_and_close(lang_list,stream_time)

if __name__ == '__main__':
    main()
