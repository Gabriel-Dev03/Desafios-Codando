import math 

angulo = float(input("Digite um angulo em graus: "))

angulo_rad = math.radians(angulo)

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print(f"O grau digitado foi {angulo}, seu seno é de {seno:.2f}, seu cosseno é de {cosseno:.2f} e sua tangente de {tangente:.2f}")