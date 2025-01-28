import json
import os
import telegram
import asyncio

def medojedka():

    async def send(msg, chat_id, token=muj_token):
        bot = telegram.Bot(token=token)
        await bot.sendMessage(chat_id=chat_id, text=msg)
        print('Zpráva odeslána.')

    vypisy = sorted(os.listdir("data")) # sorted je nutné, linux to řadil naopak

    if len(vypisy) < 2:
        print("Ještě jsem neposbíral dost dat.")
        quit()

    naskladneno = []
    with open(os.path.join("data",vypisy[-2]), "r", encoding="utf-8") as f:
        predposledni = json.loads(f.read())
    with open(os.path.join("data",vypisy[-1]), "r", encoding="utf-8") as f:
        posledni = json.loads(f.read())
    for odkaz, status in posledni.items():
        try:
            if (status == True) and (predposledni[odkaz] == False):
                naskladneno.append(odkaz)
        except Exception as e: 
            if status == True: # kdyby náhodou naskladnili knihu před prvním scrapováním
                naskladneno.append(odkaz)
            print(e)

    if len(naskladneno) > 0:
        zprava = "Čerstvě naskladněno: " + " ".join(naskladneno)
    else:
        zprava = None

    try:
        with open(os.path.join("config","telegram.json"), 'r') as f:
            konfigurace = json.loads(f.read())
            muj_token = konfigurace['token']
            muj_kontakt = konfigurace['kontakt']
    except:
        pass

    if zprava:
        print(zprava)
        asyncio.run(send(msg=zprava, chat_id=muj_kontakt, token=muj_token))
    else:
        print("Nic nového pod sluncem.")

if __name__ == "__main__":
    medojedka()