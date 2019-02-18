# -*- coding: utf-8 -*-
class Desafio:    

# my_string[-1] selects the last character in the string ('o'), and my_string[:-1] selects all of the string excluding the last character ('hell').

# To move by x amount you could use:

# my_string = my_string[-x:] + my_string[:-x]
# my_string[-x:] selects the last x characters in the string, and my_string[:-x] selects all of the string excluding the last x characters.
    def troca(self, palavra):
        tamanho_palavra = len(palavra)
        matriz_palavra = []
        i = 0
        while i < tamanho_palavra - 1:
            palavra = palavra[-1] + palavra[:-1]
            matriz_palavra.append(palavra)
            # print(palavra)
            i = i + 1
        
        print (matriz_palavra)

    def change_to_matriz(self, matriz_palavra):
        matriz_palavra = sorted(matriz_palavra) #ordena  a lista em ordem alfabética
        matriz_palavra = [list(palavra) for palavra in matriz_palavra] #coloca a lista de palavras em uma matriz de letras
        print (matriz_palavra)
        # pega_elementos_colunas(matriz_palavra)

    def pega_elementos_colunas(self, matriz_palavra):
        tamanho  = int(len(matriz_palavra))
        list_res_prim = []
        nu = 0  #nu = variavel que indica a coluna que é pra pegar o elementos
        while nu < len(matriz_palavra):
            for i in range(tamanho):
                list_res_prim.append(matriz_palavra[i][nu])
                nu = nu + 1  

    def pega_ultima_coluna(self, matriz_palavra):
        tamanho  = int(len(matriz_palavra))
        list_res_fin = []
        for i in range(tamanho):
            list_res_fin.append(matriz_palavra[i][tamanho-1])
    

    def list_concat(self, list_res_fin, list_res_prim):
        list_concat_alternate = list(''.join(map(''.join, zip(list_res_fin, list_res_prim))))
        # nu = list_concat() + 1
        # return nu
        
    # def list_sort(self, list_concat_alternate):
    #     list_concat_alternate = sorted(list_concat_alternate)

    
    # def list_verify(self, list_concat_alternate, palavra):
    # TRABALAHR NESSE FOR POIS list_concat_alternate É UMA MATRIZ E PALAVRA É UMA STRING, TENHO DUAS OPÇÕES:
            #list(palavra), aí o for seria duplo(i,j)
            #fazer com que o for percorra as linhas e as colunas individualmente, e comparar o conjunto de colunas com a PALAVRA
    #     for i in range(len(palavra)):
    #         if list_concat_alternate[i] == palavra:
    #             print ("Words Matched"+ list_concat_alternate[i], palavra)
    
    def teste(self, matriz_palavra): 
        tamanho  = int(len(matriz_palavra))
        palavra = 'abracadabraa'
        matriz_palavra = sorted(matriz_palavra) #ordena  a lista em ordem alfabética
        matriz_palavra = [list(palavra) for palavra in matriz_palavra] #coloca a lista de palavras em uma matriz de letras
        # maior =  matriz_palavra[0][0]
        
        #PEGA OS PRIMEIROS ELEMENTOS DAS RESPECTIVAS LINHAS 
        list_res_prim = []
        nu = 0
        for i in range(tamanho):
            list_res_prim.append(matriz_palavra[i][nu])
            # nu = nu + 1

        print (list_res_prim)
        
        list_res_sec = []
        for i in range(tamanho):
            list_res_sec.append(matriz_palavra[i][1])

        print(list_res_sec)
        
        
        list_res_terc = []
        for i in range(tamanho):
            list_res_terc.append(matriz_palavra[i][2])

        print(list_res_terc)
        
        list_res_quar = []
        for i in range(tamanho):
            list_res_quar.append(matriz_palavra[i][3])

        print(list_res_quar)
        
        list_res_qui = []
        for i in range(tamanho):
            list_res_qui.append(matriz_palavra[i][4])

        print(list_res_qui)
        
        list_res_sext = []
        for i in range(tamanho):
            list_res_sext.append(matriz_palavra[i][5])

        print(list_res_sext)
        
        list_res_set = []
        for i in range(tamanho):
            list_res_set.append(matriz_palavra[i][6])

        print(list_res_set)
        
        list_res_oct = []
        for i in range(tamanho):
            list_res_oct.append(matriz_palavra[i][7])

        print(list_res_oct)
        
        list_res_nin = []
        for i in range(tamanho):
            list_res_nin.append(matriz_palavra[i][8])

        print(list_res_nin)
        
        list_res_ten = []
        for i in range(tamanho):
            list_res_ten.append(matriz_palavra[i][9])

        print(list_res_ten)
        
        list_res_ele = []
        for i in range(tamanho):
            list_res_ele.append(matriz_palavra[i][10])

        print(list_res_ele)


        #PEGA O ULTIMO ELEMENTO DAS RESPECTIVAS LINHAS
        list_res_fin = []
        for i in range(tamanho):
            list_res_fin.append(matriz_palavra[i][tamanho-1])

        print(list_res_fin)    


        #TODA VEZ QUE CHAMAR O METODO CONCAT VAI ACRESCENTAR 1 AO N
        # list_concat_alternate = list(''.join(map(''.join, zip(list_res_fin, list_res_prim))))
        list_concat_alternate = zip(list_res_fin, list_res_prim, list_res_sec, list_res_terc, list_res_quar, list_res_qui, list_res_sext, list_res_set, list_res_oct, list_res_nin, list_res_ten, list_res_ele)
        # list_concat_alternate = zip(list_concat_alternate, list_res_sec )
        # list_concat_alternate = zip(list_concat_alternate, list_res_terc )
        # QUANDO EU USO ESSE METODO DUAS VEZES, ELE ACABA NÃO FUNCIONANDO CORRETAMENTE
        # list_concat_alternate = list(''.join(map(''.join, zip(list_concat_alternate, list_res_sec ))))
        # n = 3
        list_concat_alternate = list(list_concat_alternate)
        # list_concat_alternate = [list_concat_alternate[i:i+n] for i in range(0, len(list_concat_alternate), n)]
        list_concat_alternate = sorted(list_concat_alternate)
        # palavra = list(palavra)
        # for i in range(tamanho):
        #     for j in range(tamanho):
        #         if palavra[j] == list_concat_alternate[i][j]:
        #             linha = i
        #             print('palavra na lista: ', list_concat_alternate[linha][j], 'palavra:', palavra )

        palavra = list(palavra)
        #IMPRIME BONITINHO
        for i in range(0, 11):
            for j in range(0, 11):
                # if palavra[j] == list_concat_alternate[i][j]:
                    # linha = i
                    print (f'[{list_concat_alternate[i][j]}]', end='')
            print()
                
        # print(matriz_palavra)


    def ler_arquivo(self):
        try:
            arquivo = open('arquivo.txt', 'a+')
            text = arquivo.read()
        except FileNotFoundError:
            print('erro ao abrir o arquivo')    
        
        
        palavra = list(text)
        print(text)
        print (palavra)
        arquivo.seek(0)
        arquivo.close()


