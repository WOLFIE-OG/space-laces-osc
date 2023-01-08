from pythonosc.udp_client import SimpleUDPClient
import time
import os
import ctypes
import random

sender = SimpleUDPClient("127.0.0.1", 9000)

chars = ["▓", "▒", "░", "█"]

delay = 1.6
mix_king = "It's the mix king!   "
space_laces = "SPACE LACES----------"
high_vaultage = " <High Vaultage> "
url = "soundcloud.com/space-laces"

while True:
    
    inc = 0
    bar = ""
    sender.send_message("/chatbox/input", ("Loading RUN.dll", True))
    ctypes.windll.kernel32.SetConsoleTitleW("Loading RUN.dll")
    os.system("cls")
    print("Loading RUN.dll")
    time.sleep(delay)
    
    for i in range(0, 10):
        bar += "▒"
        inc += 10
        sender.send_message("/chatbox/input", (f"{bar} {inc}%", True))
        ctypes.windll.kernel32.SetConsoleTitleW("Loading RUN.dll")
        os.system("cls")
        print("Loading RUN.dll")
        time.sleep(delay)

    _a = True
    for i in range(0, 10):
        if _a is True:
            sender.send_message("/chatbox/input", (url, True))
            ctypes.windll.kernel32.SetConsoleTitleW(url)
            os.system("cls")
            print(url)
            _a = False

        else:
            _p = []
            for i in range(0, int(len(url) / 2)):
                _p.append(random.choice(chars))

            sender.send_message("/chatbox/input", ("".join(_p), True))
            ctypes.windll.kernel32.SetConsoleTitleW("".join(_p))
            os.system("cls")
            print("".join(_p))
            _a = True

        time.sleep(delay)

    for i in range(0, round(len(high_vaultage) / 2)):
        __ = high_vaultage[:-i][i:]
        if __ != high_vaultage:
            sender.send_message("/chatbox/input", (__, True))
            ctypes.windll.kernel32.SetConsoleTitleW(__)
            os.system("cls")
            print(__)
            time.sleep(delay)

    for i in range(0, len(high_vaultage)):
        __ = high_vaultage[-i:]
        if __ != high_vaultage:
            sender.send_message("/chatbox/input", (__, True))
            ctypes.windll.kernel32.SetConsoleTitleW(__)
            os.system("cls")
            print(__)
            time.sleep(delay)

    for i in range(0, 10):
        sender.send_message("/chatbox/input", (mix_king, True))
        ctypes.windll.kernel32.SetConsoleTitleW(mix_king)
        os.system("cls")
        print(mix_king)
        for i in range(0, 4):
            mix_king = mix_king[1:] + mix_king[0]
        time.sleep(delay)

    for i in range(0, 2):
        for i in range(0, 5):
            sender.send_message("/chatbox/input", (space_laces, True))
            ctypes.windll.kernel32.SetConsoleTitleW(space_laces)
            os.system("cls")
            print(space_laces)
            space_laces = space_laces[:-2]
            space_laces = "-" + space_laces
            space_laces = "-" + space_laces
            time.sleep(delay)

        for i in range(0, 5):
            sender.send_message("/chatbox/input", (space_laces, True))
            ctypes.windll.kernel32.SetConsoleTitleW(space_laces)
            os.system("cls")
            print(space_laces)
            space_laces = space_laces[2:]
            space_laces = space_laces + "-"
            space_laces = space_laces + "-"
            time.sleep(delay)

    sender.send_message("/chatbox/input", (space_laces, True))
    ctypes.windll.kernel32.SetConsoleTitleW(space_laces)
    os.system("cls")
    print(space_laces)
    time.sleep(delay)

    for i in range(0, 4):
        i += 1
        if i == 4:
            vautlage = "VAULTAGE ???"
        else:
            vautlage = f"VAULTAGE 00{i}"
        sender.send_message("/chatbox/input", (vautlage, True))
        ctypes.windll.kernel32.SetConsoleTitleW(vautlage)
        os.system("cls")
        print(vautlage)
        time.sleep(delay)

    lyrics_vautlage = [
        "He's been away a long time...",
        "Once a man,",
        "he is now something more than human...",
        "Indestructible, ever-changing...",
        "varying powers of black magic from deep space...",
        "His mission;",
        "To avenge,",
        "to possess,",
        "to destroy!",
    ]

    for i in lyrics_vautlage:
        sender.send_message("/chatbox/input", (i, True))
        ctypes.windll.kernel32.SetConsoleTitleW(i)
        os.system("cls")
        print(i)
        time.sleep(delay)

    random_quotes = [
        "I got choppaz in the trunk",
        "Gimme some room, I'm throwing elbows",
        "Let's get ready to rumble!",
        "1 on 1, toe-to-toe, bring your clique witcha",
        "Woah, no, not the bees",
        "I'm going a step back",
        "My name is.",
        "My name is..",
        "My name is...",
        "Chika-chika",
        "<SPACE LACES>",
    ]
    for i in random_quotes:
        sender.send_message("/chatbox/input", (i, True))
        ctypes.windll.kernel32.SetConsoleTitleW(i)
        os.system("cls")
        print(i)
        time.sleep(delay)
