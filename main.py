from test import Desafio

print('digite o nome do arquivo:\n')
nome_arquivo = input()
des = Desafio()
# palavra = ['abracadabra','aabracadabr', 'raabracadab', 'braabracada', 'abraabracad', 'dabraabraca', 'adabraabrac', 'cadabraabra', 'acadabraabr', 'racadabraab', 'bracadabraa']
# des.troca('abracadabra', 'encode', 2)
# des.change_to_matriz(palavra)
des.ler_arquivo(nome_arquivo)
# des.encoder(palavra, 2)
# des.decoder('rdarcaaaabb', 2)

# des.decoder(palavra, 2)