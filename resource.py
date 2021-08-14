with open("file.log", "r") as f:
    while f:
        d = dict()
        line = f.readline()
        if not line:
            break
        for i in line.split("?")[1].split("&"):
            key, value = i.split("=")
            d[key] = value
        print(d["resourceVersion"], end="")
