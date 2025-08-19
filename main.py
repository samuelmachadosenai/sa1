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

        total_entradas = sum(int(entrada.split(":")[0]) for entrada in pares)
        entradas_por_linha[id_linha] = entradas_por_linha.get(id_linha, 0) + total_entradas
        ranking = sorted(entradas_por_linha.items(), key=lambda item: item[1], reverse=True)


print(ranking)

# print(sorted(nome_do_dic, key=lambda x: nome_do_dic["passageiros"], reverse=True))