def gcd(a, b):
    if(b == 0):
        return a
    else:
        a = a % b
        return gcd(b , a)

#a = int(input("Give a:"))
#b = int(input("Give b:"))
a = int(input())
b = int(input())
#print("Gcd(", a, " , ", b , ") : ", gcd(a,b))
print(gcd(a, b))

