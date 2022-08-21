import requests
import random
import string
import numpy
from colorama import Fore



num = int(input('how many codes?: -> '))

chars = []
chars[:0] = string.ascii_letters + string.digits
c = numpy.random.choice(chars, size=[num, 23])
for s in c:  
    code = ''.join(x for x in s)
    nitro = f"https://discord.gift/{code}"  
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
    
    response = requests.get(url)
    if response.status_code == 200:  
            print(Fore.GREEN,("Valid",nitro))
    else:
        print(Fore.RED,("not valid",nitro))
      
