v = {"A": 0, "B": 0, "C": 0}

while True:
    op = input("Voto (A, B, C) ou Sair: ").upper()
    if op not in v: break
    v[op] += 1

total = sum(v.values())
for c, qtd in v.items():
    p = (qtd/total)*100 if total > 0 else 0
    print(f"{c}: {qtd} votos ({p:.1f}%)")

print(f"Vencedor: {max(v, key=v.get)}")