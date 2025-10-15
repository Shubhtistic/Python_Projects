# How Hackers Really Work: The Problem of Password Re-use The biggest threat to your online accounts is not a hacker guessing your password. 
# It's password re-use. Hackers use lists of passwords leaked from major data breaches to try the same email/password combinations on other websites. 
# This is called credential stuffing. Our goal is to check if a password has appeared in one of these breaches.

# The Solution: The "Have I Been Pwned" API, We will use the Have I Been Pwned (HIBP) Pwned Passwords API. 
# It's a free, secure, and anonymous service that allows you to check if a password has been compromised without ever sending the full password over the internet.

import requests
import hashlib

def check_pwned_api(password):

    # hash our password with SHA-1
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_chars, tail = sha1_password[:5], sha1_password[5:]
    ## we will send the first 5 fro sha1 password
    
    # query api with the first 5 characters
    url = f"https://api.pwnedpasswords.com/range/{first_5_chars}"

    response = requests.get(url)
    response.raise_for_status() 
        ## we get an status code it rases exception it is an bad code


    # split our response into lines of hashes
    hashes = (line.split(':') for line in response.text.splitlines())

    # locally check if the tail of our hash is in the response
    for h, count in hashes:
        if h == tail:
            return int(count)
    
    return 0

