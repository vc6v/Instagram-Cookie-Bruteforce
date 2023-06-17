#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import colorama,time,os,webbrowser
from config import *
colorama.init(convert=True)
version = 1.0
author = "opw#"
user = os.getenv('USERNAME')
cpath = os.getcwd()
url = "https://www.instafollowers.co/find-instagram-user-id"
time.sleep(1)
from sys import platform
if platform == 'win64' or platform == 'win32':
    os.system(f'title [Instagram Cookie Bruteforce] Version: {version}')
    os.system('cls')
    os.system('color 4')
else:
    os.system('clear')
print(f'''
 _____           _                                  ____             _        __                   
|_   _|         | |                                |  _ \           | |      / _|                  
  | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___ | |_) |_ __ _   _| |_ ___| |_ ___  _ __ ___ ___ 
  | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \|  _ <| '__| | | | __/ _ \  _/ _ \| '__/ __/ _ \\
 _| |_| | | \__ \ || (_| | (_| | | | (_| | | | | | | |_) | |  | |_| | ||  __/ || (_) | | | (_|  __/
|_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|____/|_|   \__,_|\__\___|_| \___/|_|  \___\___|
                           __/ |                                                                   
                          |___/        

                                                                  
Welcome {user} to Instagram Cookie Bruteforce!                      Made by {author}

Version = {version}                                                 PATH {cpath}
''')

print()
c = time.ctime()
print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3] + colorama.Fore.BLUE + "]" + ' ' + 'Do you want to use a custom wordlist (custom target) or try to found any working instagram cookie? [y/n]')
c = time.ctime()
g = input(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3] + colorama.Fore.BLUE + "]" ' ' + '[>] ')
if g.lower() == 'yes' or g.lower() == 'ye' or g.lower() == 'y':
    c = time.ctime()
    print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3]+ colorama.Fore.BLUE + "]" + ' ' + 'Input the Instagram username on the website to get the ID and then put it here. (IT WON\'T WORK WITH A USERNAME)')
    webbrowser.open(url)
    generate_custom_cookie()
else:
    c = time.ctime()
    print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3] + colorama.Fore.BLUE + "]" + ' ' + 'Using the default wordlist...')
    generate_default_cookies()
c = time.ctime()
print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3]+ colorama.Fore.BLUE + "]" + ' ' +'All done, running main.py to start bruteforcing! please wait..')
time.sleep(1)
os.system('python main.py')
