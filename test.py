# -*- coding: utf-8 -*-
import re
class Desafio:    
    def troca(self, palavra, nome_arquivo):
        tamanho_palavra = len(palavra)
        indice = 0
        matriz_palavra = []
        i = 0
        while i < tamanho_palavra:
            palavra = palavra[-1] + palavra[:-1]
            matriz_palavra.append(palavra)
            i = i + 1
        
        palavra = list(palavra)
        matriz_palavra = sorted(matriz_palavra) #ordena  a lista em ordem alfabética
        matriz_palavra = [list(palavra) for palavra in matriz_palavra] #coloca a lista de palavras em uma matriz de letras
        for i in range (tamanho_palavra):
            if(palavra == matriz_palavra[i]):
                indice = i
        self.encoder(matriz_palavra, indice, nome_arquivo)

    #encoder    
    def encoder(self, matriz_palavra, indice, nome_arquivo):
        tamanho  = int(len(matriz_palavra))
        matriz_palavra = sorted(matriz_palavra)
        list_res_fin = []       
        for i in range(tamanho):
            list_res_fin.append(matriz_palavra[i][tamanho-1])

        resultado = str(list_res_fin) + ',' + str(indice)
        nome_arquivo_saida = str(nome_arquivo.replace('in', 'out'))
        arquivo = open(nome_arquivo_saida, 'w+')
        arquivo.write(str(resultado))

    #decoder
    def decoder(self, palavra, indice, nome_arquivo):

        list_res_fin = list(palavra)       
        list_primordial = list_res_fin
        list_concat_alternate = list_res_fin
        list_res_fin = sorted(list_res_fin)
        list_concat_alternate = zip(list_concat_alternate, list_res_fin)
        
        for i in range(1, 10):
            list_concat_alternate = sorted(list_concat_alternate)
            list_concat_alternate = zip(list_primordial, list_concat_alternate)
        
        list_concat_alternate = list(list_concat_alternate)
        list_concat_alternate = sorted(list_concat_alternate)
        string =  str(list_concat_alternate[int(indice)])
        resultado = re.findall("([a-zA-Z0-9])", string)
        nome_arquivo_saida = str(nome_arquivo.replace('in', 'out'))
        arquivo = open(nome_arquivo_saida, 'w+')
        arquivo.write(str(resultado))


    def ler_arquivo(self, nome_arquivo):

        posicao_resultado = 0
        try:
            arquivo = open(nome_arquivo , 'r')
            text = arquivo.read()
        except FileNotFoundError:
            print('erro ao abrir o arquivo')    

        if 'encode' in nome_arquivo:
            self.troca(str(text), nome_arquivo)
        elif 'decode' in nome_arquivo:
                posicao_resultado = re.findall('[^"]+$', text)
                posicao_resultado = re.findall("[0-9]", str(posicao_resultado))
                palavra = re.findall('"([A-Za-z0-9 ]*)"', text)
                palavra = palavra[0]
                posicao_resultado = posicao_resultado[0]
                self.decoder(palavra, posicao_resultado, nome_arquivo)

        else:
            print('\nFORMATO INVÁILDO')
        arquivo.seek(0)
        arquivo.close()