import time
import re
import requests
import sqlite3

WEBHOOK_Link = "https://discordapp.com/api/webhooks/1505949031849922610/Xu6SiEnjlPfV9d7V3vsyuMAP_nIK36LmSzsrGFV22BGj5-6441DYMr_PStHjTDqX7sAE"
with open("server_logs.txt", "r") as plik:


    con = sqlite3.connect('SQL_SIEM.db')
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS alerty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_nr TEXT,
    attempts int,
    czas TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    con.commit()


    licznik_prob = {}
    while (True):
        linia = plik.readline()
        if not linia:
            time.sleep(0.5)
            continue
        wynik = re.search(r"(Failed password|Accepted password).*from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", linia)
        if wynik:
            status = wynik.group(1)
            ip = wynik.group(2)
            if status == "Failed password":
                if ip in licznik_prob:
                    licznik_prob[ip] += 1  
                else:
                    licznik_prob[ip] = 1
                if licznik_prob[ip] >= 3:
                    cur.execute("INSERT INTO alerty (ip_nr, attempts) VALUES (?,?)", (ip, licznik_prob[ip]))
                    con .commit()
                    wiadomosc = {
                        "content": f"🚨 **[ALERT]** Brute Force wykryty z IP: {ip}! Liczba prób: {licznik_prob[ip]}"
                    }
                    requests.post(WEBHOOK_Link, json=wiadomosc)


