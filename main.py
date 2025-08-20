# cria um dicionário vazio para armazenar o total de entradas
# por linha de ônibus
entradas_por_linha = {}

# abre o arquivo CSV em modo de leitura
with open('out.csv', 'r') as arquivo:

    for linha in arquivo:

# remove espaços e quebras de linha no começo/fim da linha
        linha_limpa = linha.strip()

# lê o primeiro número antes da vírgula (ID da linha)
        id_linha = int(linha_limpa.split(",", 1)[0])

# pega tudo que vem depois da primeira vírgula
        dados = linha_limpa.split(",", 1)[1]

# separa cada par em uma lista, usando a vírgula como separador
        pares = dados.split(",")

# soma todos os valores de entradas (números antes dos ":") na lista de pares
        total_entradas = sum(int(entrada.split(":")[0]) for entrada in pares)

# acumula o total de entradas no dicionário
        entradas_por_linha[id_linha] = entradas_por_linha.get(id_linha, 0) + total_entradas


# gera um ranking temporário das linhas com mais passageiros
# ordena pelo total de entradas, do maior para o menor
        ranking = sorted(entradas_por_linha.items(), key=lambda item: item[1], reverse=True)

# imprime o ranking final no console
# cada item da lista é uma tupla: (ID da linha, total de passageiros)
print(ranking)