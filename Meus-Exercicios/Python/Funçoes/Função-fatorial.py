def titulo(msg):
    print("=" * len(msg))
    print(msg)
    print("=" * len(msg))

def fatorial(num=1, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=" ")  
        f *= c
    return f

titulo("FATORIAL")
n = int(input("Digite um número para calcular o fatorial: "))
print(f"\nO resultado é {fatorial(n, show=True)}")
5