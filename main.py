#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    import requests,colorama,os,threading,sys,time
except ModuleNotFoundError:
    print('Failed to import required modules, installing them for you...')
    import os
    os.system('pip install requests colorama')
colorama.init(convert=True)
session = requests.session()
cookie_name = 'sessionid'
def cookienigga(cookie_value):
    cookies = {
        cookie_name: cookie_value
    }
    session.cookies.update(cookies)
    status = session.get('https://www.instagram.com/accounts/edit/', allow_redirects=False)
    if status.status_code == 200:
        c = time.ctime() 
        print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3]+ colorama.Fore.BLUE + "]" +colorama.Fore.RED +  ' ' + "[SUCCESS] WORKING COOKIE: " + colorama.Fore.GREEN + str(cookie_value))
        c = time.ctime() 
        print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3]+ colorama.Fore.BLUE + "]" +colorama.Fore.RED +  ' ' + "[DATA] SAVING WORKING COOKIE: " + colorama.Fore.GREEN + str(cookie_value))
        time.sleep(3)
        with open('success.txt', 'a', encoding='UTF-8') as filee:
            filee.write(cookie_value + '\n')
        sys.exit(1)
    else:
        c = time.ctime() 
        print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3]+ colorama.Fore.BLUE + "]" +colorama.Fore.RED +  ' ' + "[ATTEMPT] INVALID COOKIE: " + colorama.Fore.GREEN + str(cookie_value))
        c = time.ctime() 
        print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3]+ colorama.Fore.BLUE + "]" +colorama.Fore.RED +  ' ' + "[DATA] Deleting Invalid Cookie From Wordlist " + colorama.Fore.GREEN + str(cookie_value))
        c = time.ctime() 
        with open('cookies.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open('cookies.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                if line.strip() != cookie_value:
                    file.write(line)
try:
    with open('cookies.txt', 'r', encoding='utf-8') as file:
        cookie_values = file.read().splitlines()
    for cookie_value in cookie_values:
        thread = threading.Thread(target=cookienigga, args=(cookie_value,))
        thread.start()
        thread.join()
except KeyboardInterrupt:
    try:
        c = time.ctime()        
        print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3]+ colorama.Fore.BLUE + "]" +colorama.Fore.GREEN +  ' ' + 'Ctrl + C detected. Do you really want to stop? [y/n]')
        c = time.ctime() 
        b = input(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3]+ colorama.Fore.BLUE + "]" +  ' ' + colorama.Fore.RED+'[>] ')
        c = time.ctime() 
        if b.lower() == 'yes' or b.lower() == 'ye' or b.lower() == 'y':
            print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3]+ colorama.Fore.BLUE + "]"  ' '  +'Exiting...')
            sys.exit(1)
        else:
             print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3]+ colorama.Fore.BLUE + "]" +colorama.Fore.GREEN +  ' ' + 'Restarting program...')
             os.system('python main.py')
    except KeyboardInterrupt:
        time.sleep(1)
        print(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3]+ colorama.Fore.BLUE + "]" +colorama.Fore.GREEN +  ' ' + 'Restarting program...')
        os.system('python main.py')