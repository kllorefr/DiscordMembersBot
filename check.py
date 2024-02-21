
import requests, colorama, os, threading
from datetime import datetime
from colorama import Fore
colorama.init()

class Check:
    def checker(token, amount):
        current_time = datetime.now().strftime('%H:%M:%S')
        response = requests.get(
            f"https://discord.com/api/v9/users/@me/guilds",
            headers={"Authorization": token},
        )

        if response.status_code == 200:
            server_ids = [server["id"] for server in response.json()]
            server_amount = len(server_ids)
            print(f'[{Fore.LIGHTBLUE_EX}{current_time}{Fore.RESET}]> Token is in {server_amount} Servers!')
            if server_amount <= (int(amount)):
                with open('tokens.txt', 'a') as db_file:
                    db_file.write(f'{token}\n')
        
        else:
            # print(f'Invalid token: {token}')
            print(f'[{Fore.LIGHTBLUE_EX}{current_time}{Fore.RESET}]> Token is Invalid')


def start():
    amount = input('Amount Of Servers The Tokens CANNOT Go Over? ')
    with open('tokens.txt', 'r') as db_file:
        tokens = db_file.read().splitlines()
    threads = []
    for token in tokens:
        thread = threading.Thread(target=Check.checker, args=(token, amount)).start()
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

start()