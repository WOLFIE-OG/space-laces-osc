from pythonosc.udp_client import SimpleUDPClient
import time
import os
import ctypes

sender = SimpleUDPClient("127.0.0.1", 9000)

delay = 1.2
text = "It's the mix king!   "
text2 = "SPACE LACES----------"
text7 = " <High Vaultage> "
text8 = "soundcloud.com/space-laces"

while True:
    _a = True
    for i in range(0, 10):
        if _a is True:
            sender.send_message("/chatbox/input", (text8, True))
            ctypes.windll.kernel32.SetConsoleTitleW(text8)
            os.system("cls")
            print(text8)
            _a = False

        else:
            sender.send_message("/chatbox/input", ("_" * len(text8), True))
            ctypes.windll.kernel32.SetConsoleTitleW("_" * len(text8))
            os.system("cls")
            print("_" * len(text8))
            _a = True

        time.sleep(delay)

    for i in range(0, round(len(text7) / 2)):
        __ = text7[:-i][i:]
        if __ != text7:
            sender.send_message("/chatbox/input", (__, True))
            ctypes.windll.kernel32.SetConsoleTitleW(__)
            os.system("cls")
            print(__)
            time.sleep(delay)

    for i in range(0, len(text7)):
        __ = text7[-i:]
        if __ != text7:
            sender.send_message("/chatbox/input", (__, True))
            ctypes.windll.kernel32.SetConsoleTitleW(__)
            os.system("cls")
            print(__)
            time.sleep(delay)

    for i in range(0, 10):
        sender.send_message("/chatbox/input", (text, True))
        ctypes.windll.kernel32.SetConsoleTitleW(text)
        os.system("cls")
        print(text)
        for i in range(0, 4):
            text = text[1:] + text[0]
        time.sleep(delay)

    for i in range(0, 2):
        for i in range(0, 5):
            sender.send_message("/chatbox/input", (text2, True))
            ctypes.windll.kernel32.SetConsoleTitleW(text2)
            os.system("cls")
            print(text2)
            text2 = text2[:-2]
            text2 = "-" + text2
            text2 = "-" + text2
            time.sleep(delay)

        for i in range(0, 5):
            sender.send_message("/chatbox/input", (text2, True))
            ctypes.windll.kernel32.SetConsoleTitleW(text2)
            os.system("cls")
            print(text2)
            text2 = text2[2:]
            text2 = text2 + "-"
            text2 = text2 + "-"
            time.sleep(delay)

    sender.send_message("/chatbox/input", (text2, True))
    ctypes.windll.kernel32.SetConsoleTitleW(text2)
    os.system("cls")
    print(text2)
    time.sleep(delay)

    for i in range(0, 4):
        i += 1
        if i == 4:
            text3 = "VAULTAGE ???"
        else:
            text3 = f"VAULTAGE 00{i}"
        sender.send_message("/chatbox/input", (text3, True))
        ctypes.windll.kernel32.SetConsoleTitleW(text3)
        os.system("cls")
        print(text3)
        time.sleep(delay)

    text5 = [
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

    for i in text5:
        sender.send_message("/chatbox/input", (i, True))
        ctypes.windll.kernel32.SetConsoleTitleW(i)
        os.system("cls")
        print(i)
        time.sleep(delay)

    text6 = [
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
    for i in text6:
        sender.send_message("/chatbox/input", (i, True))
        ctypes.windll.kernel32.SetConsoleTitleW(i)
        os.system("cls")
        print(i)
        time.sleep(delay)
