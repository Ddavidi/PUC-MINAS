import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
dados = pd.read_csv('resultados_ordenacao.csv')

# Configurações gerais
algoritmos = ['SelectionSort', 'InsertionSort', 'BubbleSort', 'QuickSort']
tamanhos = [100, 1000, 10000, 100000]
cores = {'SelectionSort': 'blue', 'InsertionSort': 'green', 'BubbleSort': 'red', 'QuickSort': 'purple'}

# Gráfico de Tempo de Execução
plt.figure(figsize=(10, 6))
for algoritmo in algoritmos:
    dados_algo = dados[dados['Algoritmo'] == algoritmo]
    plt.plot(dados_algo['Tamanho'], dados_algo['Tempo_ms'], marker='o', color=cores[algoritmo], label=algoritmo)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo de Execução (ms)')
plt.title('Comparação de Tempo de Execução')
plt.legend()
plt.grid(True)
plt.savefig('tempo_execucao.png')

# Gráfico de Comparações
plt.figure(figsize=(10, 6))
for algoritmo in algoritmos:
    dados_algo = dados[dados['Algoritmo'] == algoritmo]
    plt.plot(dados_algo['Tamanho'], dados_algo['Comparacoes'], marker='o', color=cores[algoritmo], label=algoritmo)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Número de Comparações')
plt.title('Comparação de Número de Comparações')
plt.legend()
plt.grid(True)
plt.savefig('comparacoes.png')

# Gráfico de Movimentações
plt.figure(figsize=(10, 6))
for algoritmo in algoritmos:
    dados_algo = dados[dados['Algoritmo'] == algoritmo]
    plt.plot(dados_algo['Tamanho'], dados_algo['Movimentacoes'], marker='o', color=cores[algoritmo], label=algoritmo)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Número de Movimentações')
plt.title('Comparação de Número de Movimentações')
plt.legend()
plt.grid(True)
plt.savefig('movimentacoes.png')