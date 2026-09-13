def es_valido(s):
    pila = []
    for caracter in s:
        if caracter == '(' or caracter == '[' or caracter == '{':
            pila.append(caracter)
        else:
            if len(pila) == 0:
                return False
            ultimo = pila.pop()
            if caracter == ')' and ultimo != '(':
                return False
            if caracter == ']' and ultimo != '[':
                return False
            if caracter == '}' and ultimo != '{':
                return False
    return len(pila) == 0


# Problema: 20 - Valid Parentheses
# Enlace: https://leetcode.com/problems/valid-parentheses/
# Complejidad temporal: O(n)
# Complejidad espacial: O(n)