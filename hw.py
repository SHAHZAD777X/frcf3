
a=1
b=0
c=0

aANDb = a & b
bXORc = b ^ c
b0Rc = b | c
g = bXORc & bXORc
final = aANDb ^ g

print("q=", final)