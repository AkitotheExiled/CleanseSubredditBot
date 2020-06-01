# CleanseSubredditBot

### Description
Removes every post from your subreddit and locks them

### Preqs
* PRAW
* configparser
* requests
* time

```
pip install praw 
```
(Everything else included in Python library)

### Installing Python
* Download Python 3.7: https://www.python.org/downloads/release/python-370/
* Add Python to Path by selecting box during installation or manually adding to Path(https://datatofish.com/add-python-to-windows-path/)
* Open up Command Prompt and type "python", it should tell you the version if its installed correctly.

## Setting up Config.ini

### Secret and Client_ID
* Go to reddit.com and select user settings
* Select Privacy & Security
* At the very bottom, select Manage third-party app authorization
* At the very bottom again, select create another app..
* In the name, type "CleanseSubredditBot by ScoopJr"
* Select the bubble: script
* In description, type "Bot that cleans up the subreddit"
* For about url, type "http://localhost"
* For redirect url, type "http://localhost"
* Select create app

**Secret**
* look next to the text, "Secret", and copy this text down somewhere

*mysecret*
```
daklfanlfkanl392r29neorfjs
```

**Client_ID**
* Look at CleanseSubredditBot by ScoopJr, and right under Personal Use Script, is our client_id
* Copy the text and save it somewhere

*myclient_id*
```
ddMaksjJsuyeb
```


## Running on Home PC
* Open up your Command Prompt again, type 
```
pip install praw
```
* Download the ZIP file and extract the contents to your desktop
* Open the config.ini file and place your information inside and save the file

```
[main]
USER =example
PASSWORD=ex_password
CLIENT_ID=ddMaksjJsuyeb
SECRET=daklfanlfkanl392r29neorfjs
SUBREDDIT=mysubredditexample
DELAY=15
```


### NOTE BEFORE RUNNING
* The account that you are running the script on must be a moderator in the subreddit you are running!

*I.E. ScoopJr is a moderator of Kgamers, where I test all my scripts.*

### Running the bot
* Open up your command prompt
* Navigate to the directory your bot is in
```
cd desktop/CleanseSubredditBot
```
* Type the following
```
python cleansebot.py
```
* Press the enter key

*The bot is now running!*

### Contributing
Issue Tracker: https://github.com/AkitotheExiled/CleanseSubredditBot/issues

### Contact
https://www.reddit.com/user/ScoopJr
