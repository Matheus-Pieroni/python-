perg1 = """
    .--.              .--.
   : (\ ". _......_ ." /) :
    '.    `        `    .'
     /'   _        _   '
    /     0}      {0     \.
   |       /      \       |
   |     /'        `\     |
    \   | .  .==.  . |   /
     '._ \.' \__/ './ _.'
jgs \/  ``'._-''-_.'``  \/
"""
perg2 = """
                    _,,......_
                 ,-'          `'--.
              ,-'  _              '-.
     (`.    ,'   ,  `-.              `.
      \ \  -    / )    \               \
       `\`-^^^, )/      |     /         :
         )^ ^ ^V/            /          '.
         |      )            |           `.
         9   9 /,--,\    |._:`         .._`.
         |    /   /  `.  \    `.      (   `.`.
         |   / \  \    \  \     `--\   )    `.`.___
-hrr-   .;;./  '   )   '   )       ///'       `-"'
        `--'  ////    ////
"""
perg3 = """
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \.  W  ./           <
      ./             /~---~\             \.
     ./_            |       |            _\.
         ~-.        |       |        .-~
            ;        \     /        i
          ./___      /\   /\      ___\.
                ~-. /  \_/  \ .-~
                   V         V
"""
perg4 = """
   ___     ___
  (o o)   (o o)
 (  V  ) (  V  )
/--m-m- /--m-m-
"""
perg5 = """
                                                       _...--.
                                       _____......----'     .'
                                 _..-''                   .'
                               .'                       ./
                       _.--._.'                       .' |
                    .-'                           .-.'  /
                  .'   _.-.                     .  \   '
                .'  .'   .'    _    .-.        / `./  :
              .'  .'   .'  .--' `.  |  \  |`. |     .'
           _.'  .'   .' `.'       `-'   \ / |.'   .'
        _.'  .-'   .'     `-.            `      .'
      .'   .'    .'          `-.._ _ _ _ .-.    :
     /    /o _.-'     LGB       .--'   .'   \   |
   .'-.__..-'                  /..    .`    / .'
 .'   . '                       /.'/.'     /  |
`---'                                   _.'   '
                                      /.'    .'
                                       /.'/.'
"""


print("<< Jogo do Advinhe o Desenho! >>")

def resposta(respostaCorreta, pergunta):
    print("O que é isso?")
    print(f"{pergunta}")
    resp = ""
    while (resp == ""):
        #A ideia é fazer tipo 20 perguntas 5 sobre cada topico e jogar elas em ordem depois verificar quais letras da resposta (do usuario), tem na resposta correta!
        resp = str(input(" >>> "))
        if (resp.lower() == respostaCorreta):
            print(f"Parabéns! Você acertou! a resposta era '{respostaCorreta}'! ")
        else:
            print("Resposta Incorreta! Tente denovo!")
            resp = ""

print(f"Bem vindo a este jogo! Você terá uma imagem em ASCII, e deverá dizer o que é.\n")
#print("O que é isso?")
#print(f"{perg1}")
print("Vamos à primeira pergunta!")
resposta('urso', perg1)
print("Muito Bem! Agora para a segunda pergunta!")
resposta('tamandua', perg2)
print("Continue Assim! Agora para a terceira pergunta!")
resposta('morcego', perg3)
print("Isso aí! Vamos para a quarta pergunta!")
resposta('coruja', perg4)
print("Bora Lá! Vamos para a quinta pergunta!")
resposta('ganso', perg5)