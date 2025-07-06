birthaday ={
    "chandan" : "07-06-2002",
    "darshan" : "27-09-2004",
    "virat": "05-10-1988"
}

meaning = {"bat" : "used to hit",
    " ball":"this is also hit",
    "wicket":"to be protected"
}

print(birthaday.get("chandan"))
print(birthaday.get("sudeep", "Not found"))
print(birthaday)

birthaday["sudeep"] = "02-09-1973"

print(birthaday)

x = birthaday.pop("chandan")
print(x)

#del birthaday["chandan"]

print(birthaday)

print(birthaday.keys())
print(birthaday.values())
print(birthaday.items())