def validador(personas):
    
    añonaci = personas[1]
    altura = personas[2]
    cumple = añonaci >= 2010
    alt = altura >= 180
    return [cumple, alt]