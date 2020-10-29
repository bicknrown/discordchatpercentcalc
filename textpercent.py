def percent(textfile,namesfile):
    text = open(textfile)
    names = open(namesfile)
    namemap = {}
    percentmap = {}
    acc = 0
    total = 0
    for line in names:
        namemap[line.strip()] = 0
    for line in text:
        for key in namemap:
            if key in line:
                namemap[key] += 1
    percentmap = namemap
    for key in namemap:
        total += int(namemap[key])
    for key in percentmap:
        percentmap[key] = round(((int(percentmap[key]) / total) * 100),3)
        print(str(key) + " : " + str(percentmap[key]) + "%")
