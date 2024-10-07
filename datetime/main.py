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
        f"dnevi: {a.total_seconds()/(60*60*24)}"
    elif enota == "t":
        return f"tedni: {a.total_seconds()/(60*60*24*7)}"
    elif enota == "v":
        f"vdihi: {a.total_seconds()/(60/18)}"
    elif enota == "us":
        return f"utripi srca: {a.total_seconds()/(60/72)}"


















def NextBD(r, enota="s"):
    g = int(datetime.date.today().year)
    t  = datetime.datetime.now()
    n = datetime.datetime(g+1, int(r[1]), int(r[0]))
    i = n-t
    return i.day
    
def NextPO():
    t  = datetime.datetime.now()
    poc = {"jes":"28.10"}
    g = poc['jes'].split('.')
    a = [t.year]
    for x in range(0, 2):
        a.append(int(g[x]))
    print(a)










if __name__ == "__main__":
    rojstvo = '27.1.2002'.split('.')
    #print(StarOseba(rojstvo))
    #NextBD(rojstvo)
    NextPO()
