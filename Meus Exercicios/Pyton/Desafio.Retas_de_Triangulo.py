print("-="*30)

n1 = float(input("qual é o comprimento da primeira reta? "))
n2 = float(input("qual é o comprimento da segunda reta? ")) 
n3 = float(input("qual é o comprimento da terceira reta? "))

if n1 and n2 > n3:
    print("As retas podem formar um triângulo.")
elif n1 and n3 > n2:
    print("As retas podem formar um triângulo.")
elif n2 and n3 > n1:
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")
print("-="*30)