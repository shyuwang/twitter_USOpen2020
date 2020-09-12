#!/usr/bin/env python3
import socket
import twitter
from keys import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

TCP_IP = 'localhost'
TCP_PORT = 9904
KEYWORD = 'USOpen'


def get_tweets_and_send(TCP_IP=TCP_IP, TCP_PORT=TCP_PORT, KEYWORD=KEYWORD):
    my_api = twitter.Api(consumer_key=API_KEY,
                         consumer_secret=API_KEY_SECRET,
                         access_token_key=ACCESS_TOKEN,
                         access_token_secret=ACCESS_TOKEN_SECRET,
                         sleep_on_rate_limit=True)

    LANGUAGES = ['en']

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(6)
    print("Waiting for TCP connection at PORT {}...".format(TCP_PORT))

    conn, addr = s.accept()
    print("Connected... Starting getting tweets.")

    for line in my_api.GetStreamFilter(track=[KEYWORD], languages=LANGUAGES):
        conn.send(line['text'].encode('utf-8'))
        print("Tweet text: {}".format(line['text']))
        print("--------------------------------------------------------------")


if __name__ == "__main__":
    get_tweets_and_send(TCP_IP, TCP_PORT, KEYWORD)
