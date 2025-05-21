matriz=[[0,3,2,28],\
        [4,0,2,24],\
        [2,3,0,16]]
# agora, é só fazer o resto do programa
# quando conseguir fazer o programa funcionar com esta matriz,
# mude para outra
# com a mesma, com menos ou com mais equações.

'''-----------------------------------------------'''

matriz=[[4,0,2,24],\
        [2,3,0,16],\
        [0,3,2,28]]
        
def poe1numaLinhaDaRegiaoPreta (nroDaLinha,mat):
    divisor=mat[nroDaLinha][nroDaLinha]
    coluna=0
    while coluna<len(mat)+1:
        mat[nroDaLinha][coluna]/=divisor
        coluna+=1
        
print(matriz[1])
poe1numaLinhaDaRegiaoPreta(1,matriz)
print(matriz[1])

def dividir_coeficientes(linha1, linha2):
    resultados = []
    for i in range(len(linha1)):
        if linha2[i] == 0:
            resultados.append(np.inf)  
        else:
            resultados.append(linha1[i] / linha2[i])
    return resultados

'''-----------------------------------------------'''

def tira0sDaAreaPreta (mat):
    ...
    lin1=0
    while lin1<qtdLinhas-1:
        lin2=lin1+1
        while lin2<qtdLinhas:
            backup=matriz[lin1]
            matriz[lin1]=matriz[lin2]
            matriz[lin2]=backup
            lin2+=1
        lin1+=1
    ...

def poe1numaLinhaDaRegiaoPreta (nroDaLinha,mat):
    divisor=mat[nroDaLinha][nroDaLinha]
    coluna=0
    while coluna<len(mat)+1:
        mat[nroDaLinha][coluna]/=divisor
        coluna+=1