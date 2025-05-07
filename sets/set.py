set_1 = {1,4,9}
set_2 = {9,3,6}
reslut1 = set_1 & set_2
reslut2 = set_1 - set_2
print(reslut1)
print(reslut2)

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
up = {u.upper() for u in sentence if u not in "aeiou"}
print(up)