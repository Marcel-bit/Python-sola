def main():
    file = open("files/input1.txt", "r") 

    content = file.read()
    lines = content.split("\n")

    le = []
    ri = []

    for l in lines:
        if l != "":
            co = l.split()
            le.append(int(co[0]))
            ri.append(int(co[1]))

    tot = 0

    for i in range(len(le)):
        simScore = 0
        for x in range(len(ri)):
            if le[i] == ri[x]:
                simScore += 1
        tot += simScore*le[i]
    print(tot)




if __name__ == "__main__":
    main()