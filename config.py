import random,string,time,colorama
#Generate custom wordlist to bruteforce a user id
def generate_custom_cookie():
    c = time.ctime()
    ig_id = input(colorama.Fore.BLUE + "[" + colorama.Fore.GREEN + c.split(" ")[3] + colorama.Fore.BLUE + "]"  + ' ' + 'USER ID: [>] ')
    def random_string(n):
        return ''.join(random.choices(string.ascii_letters + string.digits + '-' + "_", k=n))
    with open('cookies.txt', 'a',encoding='UTF-8') as f:
         for i in range(9000):
            s = f"{ig_id}%3A{random_string(14)}%3A{random.randint(10, 99)}%3AAY{random_string(random.randint(42, 43))}\n"
            f.write(s)

#Generate default Wordlist
def generate_default_cookies():
    def random_string(n):
     return ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    with open('cookies.txt', 'a',encoding='UTF-8') as f:
        for i in range(9000):
            s = f"{random.randint(10000000000, 99999999999)}%3A{random_string(14)}%3A{random.randint(10, 99)}%3AAY{random_string(random.randint(42, 43))}\n"
            f.write(s)
