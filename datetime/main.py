import datetime

def StarOseba(r, enota = "us"):
    r = datetime.datetime(int(r[2]), int(r[1]), int(r[0]))
    t  = datetime.datetime.now()
    a = t-r
    if enota == "s":
        return f"sekunde: {a.total_seconds()}"
    elif enota == "m":
        return f"minute: {a.total_seconds()/60}"
    elif enota == "u":
        return f"ure: {a.total_seconds()/(60*60)}"
    elif enota == "d":
        return f"dnevi: {a.total_seconds()/(60*60*24)}"
    elif enota == "t":
        return f"tedni: {a.total_seconds()/(60*60*24*7)}"
    elif enota == "v":
        return f"vdihi: {a.total_seconds()/(60/18)}"
    elif enota == "us":
        return f"utripi srca: {a.total_seconds()/(60/72)}"

















def NextBD(r, enota="s"):
    g = int(datetime.date.today().year)
    t  = datetime.datetime.now()
    n = datetime.datetime(g+1, int(r[1]), int(r[0]))
    i = n-t
    return i.day
    
def NextPO():
    now  = datetime.datetime.now()
    pocitnice = {
    "jesenske": {
        "začetek": "2024-10-30",
        "konec": "2024-11-03"
    },
    "zimske": {
        "začetek": "2024-12-24",
        "konec": "2025-01-06"
    },
    "spomladanske": {
        "začetek": "2025-04-21",
        "konec": "2025-04-27"
    },
    "poletne": {
        "začetek": "2025-06-24",
        "konec": "2025-09-01"
    }
}
    d = dict()
    for k, v in enumerate(pocitnice):
        a = []
        g = pocitnice[v]['začetek'].split('-')
        for x in range(0, 3):
            a.append(int(g[x]))
        a = datetime.datetime(a[0], a[1], a[2])
        if a > now:
            print(a-now)
            break

def petek(zac=datetime.datetime.now(), kon= datetime.datetime(2026, 12, 31)):
    dan = datetime.datetime.now()
    for i in range((kon-zac).days):
        dan += datetime.timedelta(days=1)
        if dan.day == 13 and dan.strftime("%A") == "Friday":
            print(dan.strftime("%Y-%m-%d") , dan.strftime("%A"))

def arbeit(zac=datetime.datetime.now(), kon= datetime.datetime(2026, 12, 31), izpis = "d"):
    dan = datetime.datetime.now()
    delovnih_dni = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    vikend_dni = ["Sat", "Sun"]
    delovnih_dni_counter = 0
    vikend_dni_counter = 0
    for i in range((kon-zac).days):
        dan += datetime.timedelta(days=1)
        if dan.strftime("%a") in delovnih_dni:
            delovnih_dni_counter += 1
        elif dan.strftime("%a") in vikend_dni:
            vikend_dni_counter += 1
    if izpis =="d":
        print(delovnih_dni_counter)
    else:
        print(vikend_dni_counter)

def cas_cona(ura = 8):
    utc_datetime = datetime.datetime.now(datetime.timezone.utc)
    a = -12
    for x in range(24):
        print(utc_datetime + datetime.timedelta(hours=a))
        print(a)
        a += 1
        






if __name__ == "__main__":
    rojstvo = '27.1.2002'.split('.')
    #print(StarOseba(rojstvo))
    #NextBD(rojstvo)
    #NextPO()
    #petek()
    #arbeit()
    cas_cona()
