from random import randrange
from funcoes import add_caracter, bem_vindo1, escolhe_palavra_secreta, solicita_chute, incrementa_chute, imprime_mensagem_vencedor, imprime_mensagem_perdedor, desenha_forca

def jogar():
    
    bem_vindo1()
    
    palavra_secreta = escolhe_palavra_secreta()
    letras_acertadas = add_caracter(palavra_secreta)
    print(letras_acertadas) 
    
    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        
        chute = solicita_chute()
        
        if(chute in palavra_secreta):
            incrementa_chute(chute, letras_acertadas, palavra_secreta)   
        else:
            erros += 1
            desenha_forca(erros)
            
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        
        print(letras_acertadas)
        
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()