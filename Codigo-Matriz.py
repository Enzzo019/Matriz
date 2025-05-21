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

# Está função é responsavel por dividir a linha por o número pivo e fazer que os numeros virem 1 ou proximo disso, tirando só a parte preta para que 0.
def resolverSistema(mat):
    qtdLinhas = len(mat)

    # Colocando 1 nas linhas da região preta
    for i in range(qtdLinhas):
        poe1numaLinhaDaRegiaoPreta(i, mat)
        print(f"Após normalizar linha {i+1}: {mat[i]}")

    # Eliminando zeros abaixo da diagonal principal
    tira0sDaAreaPreta(mat)
    
    print("\nMatriz após troca de linhas e normalização:")
    for linha in mat:
        print(linha)

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
