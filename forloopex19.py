Degree = ["BCA", "BCOM", "BBA", "BA", "BE"]

Fees =[45000, 50000, 60000, 80000, 90000]

Admisssion_History={}


for i in range(len(Degree)):
    Admisssion_History[Degree[i]] = Fees[i]

print(Admisssion_History)




Tution = ["BA", "BE", "ITI"]

fees =[1000, 2000, 3000]

fees_history={}

for j in range(len(Tution)):
    fees_history[Tution[j]] = fees[j]

print(fees_history)




Cloths = ["ready matireal", "Selwar comizz", "top and bottom set", "tshirt"]

Cloths.sort()

price = [500,  800, 400, 600]

price.sort()

cloths_stocks={}

for i in range(len(Cloths)):
    cloths_stocks[Cloths[i]] = price[i]


print(cloths_stocks)