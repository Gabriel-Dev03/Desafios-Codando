def titulo(msg):
    print("-=" * (len(msg)//2 ))
    print(msg)
    print("-=" * (len(msg)//2 ))

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano 
    if idade == 18:
        print(f"A idade é {idade}, OBRIGADO VOTAR. ")
    elif 16 <= idade < 18 or idade >= 65:
        print(f"A idade é {idade}, VOTO OPCIONAL. ")
    else:
        print(f"A idade é {idade}, VOTO NEGADO. ")

titulo("  Função de Voto  ")
ano_nasc = int(input("Digite o ano do seu nascimento: "))
voto(ano_nasc)
