def get_input(tipo_palavra: str):
    user_input: str = input(f"Insira um {tipo_palavra}: ")
    return user_input


def main():
    nome = get_input("nome")
    profissao = get_input("profissão")
    adjetivo = get_input("adjetivo")
    verbo1 = get_input("verbo no passado")
    substantivo1 = get_input("substantivo")
    verbo2 = get_input("verbo no infinitivo")
    animal = get_input("animal")
    cor = get_input("cor")
    substantivo2 = get_input("substantivo no plural")
    verbo3 = get_input("verbo no infinitivo")
    lugar = get_input("lugar")
    objeto = get_input("objeto mágico")
    frase = get_input("frase de efeito")

    story = f"""
    O explorador {nome}, um(a) renomado(a) {profissao}, sempre sonhou em encontrar 
    a lendária Selva Proibida. 
    Um dia, com seu chapéu {adjetivo} e sua mochila repleta de mapas 
    antigos, ele(a) {verbo1} sem olhar para trás. Mal sabia que enfrentaria um(a) 
    {substantivo1} logo na entrada da floresta.

    Com coragem e um pouco de sorte, conseguiu {verbo2} por entre os cipós e 
    escapar de um ataque de {animal} selvagens com pelos {cor}. 
    Mais adiante, encontrou uma aldeia abandonada, onde só restavam {substantivo2} 
    espalhados pelo chão, como pistas de um mistério antigo.

    Determinado(a) a {verbo3} até o fim, {nome} seguiu em direção ao {lugar}. 
    Lá, encontrou o {objeto}, o artefato sagrado que todos diziam ser apenas uma lenda. 
    Ao segurá-lo, sentiu um poder indescritível e disse em voz alta: "{frase}!". 
    A selva inteira pareceu responder, como se reconhecesse o verdadeiro guardião do segredo.
    """
    
    print(story)

if __name__ == '__main__':
    main()














