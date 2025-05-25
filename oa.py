
var = int (input("Please give me a number:"))
while var > 0:
    var = var - (len(str(var)) * (len(str(var)) * len(str(var)))) - var % 13 - (12 * (len(str(var)) / 2))
    if var == 5:
        continue
    print (var)

print ("Done!")