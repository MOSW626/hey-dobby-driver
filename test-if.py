# a, b, c, d, e, f = map(float, input('% 6개를 입력하세요: ').split())
 
 
# if a > (b and c and d and e and f):
#     print("winner is a")
# elif b > (a and c and d and e and f):
#     print("winner is b")
# elif c > (a and b and d and e and f):
#     print("winner is c")
# elif d > (a and b and c and e and f):
#     print("winner is d")
# elif e > (a and b and c and d and f):
#     print("winner is e")
# else:
#     print("winner is f")

labels = ["A", "b", "c", "d", "e", "f"]
probas = [1,5,2,6,2,7]

pl = list(zip(probas, labels))
print(pl)

pl.sort(reverse=True)

print(pl)

proba = pl[0][0]
label = pl[0][1]

print(f"proba = {proba}, label = {label}")

# l = [a,b,c,d,e,f]
# print(max(l))