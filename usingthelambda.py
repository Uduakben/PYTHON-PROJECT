items = [
    ("Prodcut1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# prices = []
# for item in items:
#     prices.append(item[1])
# prices = list(map(lambda item: item[1], items))
# print(prices)
filter = list(filter(lambda item:item[1] >= 10, items))
print(filter)