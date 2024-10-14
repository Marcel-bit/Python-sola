import datetime
import pytz
import random
import matplotlib.pyplot as plt 
def starOseba(r, enota = "minute"):
    r = datetime.datetime(int(r[2]), int(r[1]), int(r[0]))
    t  = datetime.datetime.now()
    a = t-r
    vred = {
        'sekunde':0,
        'minute':60,
        "ure": (60*60),
        'dnevi': (60*60*24),
        'tedni':(60*60*24*7),
        'vdihi': (60/18),
        'utripi srca':(60/72)
    }
    return f"{enota} : {round(a.total_seconds()/vred[enota], 2)} "



def nextBD(r, enota="minute"):
    g = int(datetime.date.today().year)
    t  = datetime.datetime.now()
    n = datetime.datetime(g+1, int(r[1]), int(r[0]))
    i = n-t
    vred = {
        'sekunde':0,
        'minute':60,
        "ure": (60*60),
        'dnevi': (60*60*24),
        'tedni':(60*60*24*7),
    }
    print(f"{enota} : {round(i.total_seconds()/vred[enota], 2)} ")


def nextPO(cas= datetime.datetime.now(), tip="zimske"):
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
    if tip:
        pocitnice= {tip: pocitnice[tip]}
    d = dict()
    for k, v in enumerate(pocitnice):
        a = []
        g = pocitnice[v]['začetek'].split('-')
        b = pocitnice[v]['konec'].split('-')
        for x in range(0, 3):
            a.append(int(g[x]))
        a = datetime.datetime(a[0], a[1], a[2])
        if a > cas:
            print(a-cas)
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


def cas_cona(ura = 20, minu = 0, sec = 0):
    cilj = datetime.datetime.now()
    zones = pytz.all_timezones
    najbCona = ""
    najmRazlika = float('inf')
    now = datetime.datetime.now(pytz.utc)
    for zone in zones:
        
        timezone = pytz.timezone(zone)
        currTime = now.astimezone(timezone)
        
        cilj = currTime.replace(hour=ura, minute=minu, second=sec)
        razlika = abs((cilj - currTime).total_seconds()) / 60
        if razlika < najmRazlika:
            najmRazlika = razlika
            najbCona = zone
            najbTime = currTime
        print(razlika, zone)
    

    print(najbCona, najmRazlika, najbTime)
        
def bd_paradox(stev_ljudi= 23, rang = 100, iterations = 100):
    leto = 2007
    months = {
    "1": 31,
    "2": 28,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31
}
   
    
    
    final = dict()
    for x in range(rang):
        
        odds = []
        for y in range(iterations):
            bdays = []
            for i in range(x):
                mesec, dan = random.choice(list(months.items()))
                dan = random.randint(1, dan)
                g = str(datetime.datetime(leto, int(mesec), dan))
                if g in bdays:
                    bdays.append(g) 
                    odds.append(True)
                    break
                else:
                    bdays.append(g) 
        final[str(x)] = len(odds)/iterations
    x = list(final.keys())
    y = list(final.values())
    plt.plot(x, y)
    plt.xlabel('X-axis Label', fontsize=5)
    plt.show()

    








if __name__ == "__main__":
    rojstvo = '27.1.2002'.split('.')
    #print(StarOseba(rojstvo))
    #nextBD(rojstvo)
    nextPO()
    #petek()
    #arbeit()
    #cas_cona()
    #print(bd_paradox())
