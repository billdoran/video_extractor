import yaml
import argparse
import time
import logging, logging,handlers
from __future__ import unicode_literals
import youtube_dl
import os

YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

CLIENT_SECRETS_FILE = "client_secrets.json"
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the Developers Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))




#download videos for each channel since previous download date

def populate_channel_meta_data(channel_list):
    for channel in channel_list:
        options = {
                    "channelID": channel['name']
                }
        channel_item = youtube_channel_ids(options)
        if channel_item not None:
            #insert result
            item = Channel(channel_item['id']).save()
#autoset lastpubdate on initialisation

def youtube_get_channel_ids(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
    
    search_response = youtube.search().list(
        part="id,snippet"
        forUsername=options.channelName
    ).execute()
    if len(search_response) > 0:
        return search_response['items'][0]
    else:
        return None 

def youtube_get_channel_videos_data(channel):

    search_response = youtube.search().list(
        part="id,snippet"
        maxResult=50,
        order="date",
        publishedAfter=channel['lastPubData']
        channelId=options.channel['id']
    ).execute()


def retrieve_channel_videos():

    ydl_opts = {
               "simulate": True,
               "daterange":,
               "age_limit": 100,
                }

    with youtube_dl.YoutubeDL(ydl)opts as ydl:
        ydl.download

def retrieve_new_videos():


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Manage retrieval of Youtube feeds for Syrian Archive project.')
    parser.add_argument("--config", "-c", dest="config_path", action="store",
                        help="Path to configuration file (defaults to %s)" % const.CONFIG_PATH,
                        default=const.CONFIG_PATH)
    parser.add_argument("--verbose", "-v", dest="verbose", action="store_true",
                        help="Verbose output", default=False)
    args = parser.parse_args()

    with open(args.config_path) as config_f:
        config = load.safe_load(config_f.read())

    if args.verbose:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler() # log to STDERR
        handler.setFormatter(logging.Formatter('SYARC_youtube_retriever (%(process)d): %(levelname)s %(message)s'))
        logger.addHandler(handler)

    else:
        # Set up logging
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logfile_handler = logging.handlers.WatchedFileHandler(config["logpath"])
        logfile_handler.setFormatter(logging.Formatter('SYARC_youtube_retriever (%(process)d): %(levelname)s %(message)s'))
        #TODO setup logging for error level in another file
        logger.addHandler(logfile_handler)

