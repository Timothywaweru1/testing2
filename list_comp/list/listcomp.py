squares = [x**2 for x in range(10)]
print(squares)
cubes = [y**3 for y in range(10)]
print(cubes)
fours = [z**4 for z in range(10)]
print(fours)
fives = [a**5 for a in range(10)]
print(fives)
sixs = [b**6 for b in range(10)]
print(sixs)
sevens = [c**7 for c in range(10)]
print(sevens)

#even no's
evn = [s for s in range(10) if s % 2 is 0]
print(evn)
#convert to uppercase
txt = ["apple", "banana", "cherry"]
cap = [w.upper() for w in txt]
print(cap)
#convert to lowercase
wrds = ['APPLE', 'BANANA', 'CHERRY']
lwr = [l.lower() for l in wrds]
print(lwr)
#nested list comp
pairs = [(x,y) for x in (1,2) for y in ("a","b")]
print(pairs)


grps = [(b,s) for b in ("Brian" , "Thomas") for s in (23,40)]
print(grps)