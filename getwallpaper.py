#!/usr/bin/python3
print("\n\n\nstarting getwallpaper")
#
from sys import argv
import subprocess
import praw
import datetime

t = "{}\n".format(str(datetime.datetime.now()).split('.')[0])
open('last_exec.txt','a').write(t)
print("@ {}".format(t))
#sub = "wallpapers"
#sub = "WQHD_Wallpaper"
#sub = "blender"
#sub = "space"

if(argv[1:]):
    sub = argv[1]
else:
    sub = "wallpapers"

if(len(argv)>2):
    top = int(argv[2])
else:
    top = 1

rootpath = open("path.txt").read()
image = f"{rootpath}/downloaded.jpg"

# bot setup
print("setting up")
reddit = praw.Reddit('moriartieBot')
subreddit = reddit.subreddit(sub)

# get the top n hottest post:
values = [v for v in subreddit.hot(limit=200)]

# filtering posts that arent images
print("filtering posts for image")
print("size before: {}".format(len(values)))
values = [v for v in values if v.url[-4:]=='.jpg']
print("size after : {}".format(len(values)))
url = values[0+(top-1)].url

# downloading image from url
str_to_exec = "rm *.jpg;wget {};mv *.jpg {}".format(url,image)
print("executing: \n{}".format(str_to_exec))
subprocess.getoutput(str_to_exec)

# change wallpaper
str_to_exec = "feh --bg-fill downloaded.jpg"
print("executing: \n{}".format(str_to_exec))
subprocess.getoutput(str_to_exec)
print("done")
