def es_primo(x):

    cuenta = 0
    recursivo = x
    
    while cuenta <= 2 and recursivo > 0:

        if x%recursivo==0:
            
                cuenta += 1
                recursivo -= 1
        else:
                recursivo -= 1

    if cuenta ==2:
        print(f"El número {x}: Es primo")
    else:
        print(f"El número {x}: No es primo")

es_primo(7)
