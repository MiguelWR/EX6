#Exercício 6

def W(s):
    if len(s) == 0:
        return True  # Uma cadeia vazia pertence a W

    if s[0] != 'a' or s[-1] != 'c':
        return False

    pilha = []
    for simbolo in s[1:-1]:
        if simbolo == 'a':
            pilha.append(simbolo)
        elif simbolo == 'b' and pilha:
            pilha.pop()
        else:
            return False

    return len(pilha) == 0


print(W("a(b)c"))
print(W("a(a(b)c)c"))
print(W("a(abc)c"))
print(W("a(a(a(a)c)c)c"))
print(W("a(aacc)c"))