# -*- coding: utf-8 -*-
import re
class Desafio:    
    # matriz_palavra= []
    def troca(self, palavra):
        tamanho_palavra = len(palavra)
        indice = 0
        matriz_palavra = []
        i = 0
        while i < tamanho_palavra:
            palavra = palavra[-1] + palavra[:-1]
            matriz_palavra.append(palavra)
            i = i + 1
        
        # for i in range(0, 11):
        #     for j in range(0, 11):
        #         # if palavra[j] == list_concat_alternate[i][j]:
        #             # linha = i
        #             print (f'[{matriz_palavra[i][j]}]', end='')
        #     print()
        
        palavra = list(palavra)
        matriz_palavra = sorted(matriz_palavra) #ordena  a lista em ordem alfabética
        matriz_palavra = [list(palavra) for palavra in matriz_palavra] #coloca a lista de palavras em uma matriz de letras
        for i in range (tamanho_palavra):
            if(palavra == matriz_palavra[i]):
                indice = i
        self.encoder(matriz_palavra, indice)
        # if tipo == 'decode':
        #     print('hi')
        #     # self.decoder(matriz_palavra, palavra)
        # if tipo == 'encode':
        #     print('hi')
        #     # self.encoder(matriz_palavra, indice)
        # else:
        #     print('arquivo não suportado')

        # return matriz_palavra

    # def teste1(self, matriz_palavra, palavra):
    #     tamanho  = int(len(matriz_palavra))
    #     for i in range (tamanho):
    #         if palavra == matriz_palavra[i]:
    #             arquivo = open("testando.out", 'w')
    #             texto = [palavra, i]
    #             arquivo.write(str(texto))

    #encoder    
    def encoder(self, matriz_palavra, indice):
        tamanho  = int(len(matriz_palavra))
        matriz_palavra = sorted(matriz_palavra)
        list_res_fin = []       
        for i in range(tamanho):
            list_res_fin.append(matriz_palavra[i][tamanho-1])

        resultado = str(list_res_fin) + ',' + str(indice)
        arquivo = open('encoder.out', 'w+')
        arquivo.write(str(resultado))

    #decoder
    def decoder(self, palavra, indice):
        list_res_fin = list(palavra)       
        list_primordial = list_res_fin
        list_concat_alternate = list_res_fin
        list_res_fin = sorted(list_res_fin)
        list_concat_alternate = zip(list_concat_alternate, list_res_fin)
        
        # print(list_res_fin, list(list_concat_alternate))
        for i in range(1, 10):
            list_concat_alternate = sorted(list_concat_alternate)
            list_concat_alternate = zip(list_primordial, list_concat_alternate)
        
        list_concat_alternate = list(list_concat_alternate)
        list_concat_alternate = sorted(list_concat_alternate)
        string =  str(list_concat_alternate[int(indice)])
        resultado = re.findall("([a-zA-Z0-9])", string)
        # resultado = re.findall("([a-zA-Z0-9])", str(resultado))
        arquivo = open('decoder.out', 'w+')
        arquivo.write(str(resultado))


    def ler_arquivo(self, nome_arquivo):

        # nome_arquivo = 'decode.in'
        posicao_resultado = 0

        # arquivo = open('opa.in', 'r')
        # text = arquivo.read()
        # print(text)
        # arquivo.close()

        try:
            arquivo = open(nome_arquivo , 'r')
            text = arquivo.read()
        except FileNotFoundError:
            print('erro ao abrir o arquivo')    
        # nome_arquivo=list(nome_arquivo)
        # print (palavra)
        # posicao_resultado = str(posicao_resultado)
        if 'encode' in nome_arquivo:
            tipo = 'encode' 
            # palavra = list(text)
            # posicao_resultado = re.findall('[^"]+$', text)
            # posicao_resultado = re.findall("[0-9]", str(posicao_resultado))
            # posicao_resultado = posicao_resultado[0]
            self.troca(str(text))
        if 'decode' in nome_arquivo:
            tipo = 'decode'
            # palavra = list(text)
            posicao_resultado = re.findall('[^"]+$', text)
            posicao_resultado = re.findall("[0-9]", str(posicao_resultado))
            palavra = re.findall('"([A-Za-z0-9]*)"', text)
            palavra = palavra[0]
            posicao_resultado = posicao_resultado[0]
            self.decoder(palavra, posicao_resultado)

        else:
            pass
        arquivo.seek(0)
        arquivo.close()
        # palavra = list(text)
        # print(text)
        # # print (palavra)
        # print(tipo)
        # # posicao_resultado = str(posicao_resultado)
        # posicao_resultado = posicao_resultado[0]
        # print(posicao_resultado)
        # arquivo.seek(0)
        # arquivo.close()
        # self.troca(text, tipo, posicao_resultado)