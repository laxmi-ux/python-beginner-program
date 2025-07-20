details={
    "name":"laxmi",
    "Since":2004,
    "course":["python","Java","etc"]
}
print(type(details))
print(details)

print(details.get("course"))
print(details.values())
print(details.keys())

details.update({"phone no":576567897654})
print(details)
details.update({"Since":2005})
print(details)


dict1=details.copy()
print("dictionary-2",dict1)

dict1.clear()
print(dict1)