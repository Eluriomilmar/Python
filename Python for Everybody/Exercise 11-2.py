import re


with open("mbox-short.txt", "r") as arquivo:
    average = 0
    count = 0
    for linha in arquivo:
        coisa = re.findall("^New Revision: ([0-9.]+)", linha)
        if len(coisa) > 0:
            coisa = float(coisa[0])
            average += coisa
            count += 1
    average = average/count
print(average)
