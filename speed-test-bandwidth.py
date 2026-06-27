import speedtest #importação da biblioteca do "speedtest"

def medir_internet(): # O "def" é usado para definir uma função em Python. Ele indica o início da definição da função e é seguido pelo nome da função (medir_internet) e parênteses que podem conter parâmetros (neste caso, não há parâmetros). O código dentro da função é indentado para indicar que pertence à função. Quando a função é chamada, o código dentro dela será executado.
    print("🛰️  Conectando aos servidores de teste... Aguarde.")
    
    # Inicializa o testador de velocidade
    teste = speedtest.Speedtest()
    
    # Encontra o servidor mais próximo para o teste ser preciso
    teste.get_best_server()
    
    print("📥 Testando velocidade de DOWNLOAD...")
    # O resultado vem em bits, dividimos por 1 milhão para virar Mega (Mbps)
    download = teste.download() / 1_000_000
    
    print("📤 Testando velocidade de UPLOAD...")
    upload = teste.upload() / 1_000_000
    
    print("\n" + "="*30) # Imprime uma linha de separação para destacar o resultado. O número 30 indica quantas vezes o caractere "=" será repetido, criando uma linha visualmente agradável para separar o resultado do teste de velocidade da internet.
    print("       RESULTADO DO TESTE       ")
    print("="*30) # Imprime outra linha de separação para destacar o resultado. O número 30 indica quantas vezes o caractere "=" será repetido, criando uma linha visualmente agradável para separar o resultado do teste de velocidade da internet.
    print(f"⚡ Download: {download:.2f} Mbps") # Imprime a velocidade de download formatada com 2 casas decimais. O f antes da string indica que é uma f-string, que permite incluir expressões dentro de chaves {}. O :.2f dentro das chaves indica que o número deve ser formatado como um float com 2 casas decimais.
    print(f"⚡ Upload:   {upload:.2f} Mbps") # Imprime a velocidade de upload formatada com 2 casas decimais. O f antes da string indica que é uma f-string, que permite incluir expressões dentro de chaves {}. O :.2f dentro das chaves indica que o número deve ser formatado como um float com 2 casas decimais.
    print("="*30) # Imprime outra linha de separação para destacar o resultado. O número 30 indica quantas vezes o caractere "=" será repetido, criando uma linha visualmente agradável para separar o resultado do teste de velocidade da internet.

if __name__ == "__main__": # É uma variável especial que verifica se o script está sendo executado diretamente (como o programa principal) e não importado como um módulo em outro script. Se for o caso, a função medir_internet() será chamada para executar o teste de velocidade da internet.
    medir_internet() # Chama a função medir_internet() para executar o teste de velocidade da internet.\ Quando o script é executado, ele verificará se é o programa principal e, se for, chamará a função para realizar o teste e exibir os resultados.


############################################################################################
                            # O QUE ACONTECE, PASSO A PASSO
############################################################################################
# 1. Python lê import speedtest e import time → carrega as bibliotecas
# 2. Python lê o def medir_internet(): → guarda a função na memória (não executa nada ainda)
# 3. Python chega no if __name__ == "__main__": → checa a condição
# 4. Condição é True (porque você rodou o arquivo diretamente) → entra no bloco
# 5. Só agora executa medir_internet() → e aí sim, todo o conteúdo da função roda


################################################################################
                    #EXEMPLIFICANDO "if __name__ == "__main__":"
################################################################################
# Se você roda python medir.py diretamente → __name__ vale "__main__"
# Se outro arquivo faz import medir → __name__ vale "medir" (o nome do arquivo)


                    # CENÁRIO A - RODANDO DIRETO:
# Nome do arquivo: "python medir.py"
# __name__ é "__main__" → Logo a condição é True → medir_internet() executa.


                # CENÁRIO B - IMPORTANDO DE OUTRO ARQUIVO:
# arquivo: app.py
# import medir
# "medir_internet()" NÃO executa automaticamente aqui
# porque __name__ dentro de medir.py virou "medir", não "__main__"
# medir.medir_internet()   # só executa se você chamar explicitamente