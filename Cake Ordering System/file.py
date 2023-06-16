cakeFile = "cake.txt"

def readCakeDataFromFile(cakeBST):
    file = open(cakeFile, "r")

    for line in file:
        data = line.split("||")
        cakeCode = data[0]
        flavor = data[1]
        weight = data[2]
        unitPrice = data[3]

        cakeBST.add(cakeCode, flavor, weight, unitPrice)

    file.close()