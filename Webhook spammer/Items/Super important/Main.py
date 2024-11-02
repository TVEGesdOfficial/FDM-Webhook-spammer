import discord
import requests
from colorama import Fore

print(Fore.YELLOW + '███████╗██████╗ ███╗   ███╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗')
print(Fore.YELLOW + '██╔════╝██╔══██╗████╗ ████║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗')
print(Fore.YELLOW + '█████╗  ██║  ██║██╔████╔██║    ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝')
print(Fore.YELLOW + '██╔══╝  ██║  ██║██║╚██╔╝██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗')
print(Fore.YELLOW + '██║     ██████╔╝██║ ╚═╝ ██║    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║')
print(Fore.YELLOW + '╚═╝     ╚═════╝ ╚═╝     ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝')



webhook = input(Fore.WHITE + "Whats your webhook URL?: ")
amount = int(input(Fore.WHITE + "Amount you want to spam: "))
message = input(Fore.WHITE + "Whats the message you want to spam?: ")
username = input(Fore.WHITE + "What do you want to name the webhook: ")


payload = {
    "content": message,
    "username": username
}

for i in range(amount):
    requests.post(webhook, json=payload)
    print("Sending Messages...")
