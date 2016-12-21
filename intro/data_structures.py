# A data structure is just a structure for your data

party_list = ["dip","chips","wine","beer","hats"]

print("1st element of party list is",party_list[0])
print("2nd element of party list is",party_list[1])
print("5th element of party list is",party_list[4])

print("let's look at the party list, in it's entirety", ", ".join(party_list))

print("let's look at the party list, in it's entirety, a different way")

for element in party_list:
    print(element)
    if element == "wine":
        break

