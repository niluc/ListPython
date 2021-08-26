import numpy as np


def main():
    f = open("DNSList.txt", "r")
    IP_list = []
    Location_list = []
    Status_list = []
    Reliability_list = []
    for e in f:
        if e[:10] == "IP Address":
            IP_list.append(e[12:-1]) if e[-2:-1] != "\t" else IP_list.append(e[12:-2])
        elif e[:8] == "Location":
            Location_list.append(e[10:-1]) if e[-2:-1] != "\t" else Location_list.append(e[10:-2])
    print(IP_list)
    print(Location_list)
    result = []
    i = 0
    for e in Location_list:
        if e == 'France':
            result.append(IP_list[i])
        i += 1
    print(result)
    f.close()

if __name__ == "__main__": main()
