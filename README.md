# PythonHealer
A simple tool to automatically regenerate your health using only Python

## Brief
This tool runs currently without a UI. Configuration is handled purely in code. It is incapable of recognising hotkeys so 
you will need to tell it which hotkey to use using virtual key codes. Currently, execution is based on unittest.py where 
a sample is provided for your browsing. First it will dump a load of data out to console, this data is useful to help you 
work out if there has been a recent client update which has broken the tool. Make sure you check it carefully to ensure 
all values are as you would expect.

## How to run it
I've been running unittest.py as my main point of call for development. It contains some sample stuff to get you started. The 
only pre-requesites are Python 3.5 32-bit and pywin32 which must be installed from sourceforge (no pip package, yet). It's not 
a nice process to install these but it's a requirement to use 32-bit or the module enumeration will be the first thing to fail.

## How safe is it
This will probably be asked if anyone ever visits this project, so my best answer is: I have absolutely no idea. I simulated 
some real world PostMessage calls which I produced using my keyboard, and I used a VK list I took from the internet. Every 
piece of code here has not been tested, and definitely not in anger. The only thing I've done to offer any protection was to 
implement a randomisation on casting spells, you can see this inside healer.py where there is a time.sleep() inside runHeal 
which I hope randomises things enough. The range is currently set to 500,600 which should be as human as is neccessary,
although the values I was getting were fairly close within the range.

## Is that all it does
Yes, right now. I probably won't update this readme for a while so there is a good chance it does more by the time you read 
this. I will do my best to add new features but I'm a busy guy with a lot of stuff to get on with. This project is free as in 
free beer. Right now you're welcome to use it as is or to simply take the code and sell it as if you wrote it yourself. I don't 
recommend doing this as it's probably full of hideous bugs, but the option is there. For a free project, do not expect anything.

## What's all this other stuff
I've tried out a few UI systems, notably Qt. I found it really nice but I did have numerous problems with crashes on exit so 
for the time being I'm not actually using it. I fully intend to add a UI at some point so this tool can be used by simpler minds 
but for the time being this will have to do. I've also added some capacity to do other useful things such as calculating your 
location and experience. This data is basically just there for futureproofing. I didn't add much because I don't want to have to 
update tonnes of addresses, but it would not be difficult to convert this into a full API capable of controlling the client 100%.
