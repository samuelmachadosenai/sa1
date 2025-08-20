# Algoritmo Contador de Passageiros

## Justificativa
O presente algoritmo foi desenvolvido para atender à necessidade da prefeitura e da empresa de transporte do município em identificar as linhas de ônibus com maior volume de passageiros.  

Em horários de pico, algumas linhas ficam sobrecarregadas, causando desconforto para os usuários e comprometendo a eficiência do sistema de transporte público. A proposta é fornecer uma ferramenta confiável que utilize os dados coletados por sensores e câmeras instalados nos ônibus para contabilizar o fluxo de passageiros.  

Com base nesses dados, será possível gerar um **ranking das linhas mais movimentadas**, fornecendo à gestão informações seguras para direcionar o investimento em novas unidades de transporte. Dessa forma, evita-se gastos desnecessários e garante-se que os recursos públicos sejam aplicados de forma eficiente e estratégica.

### Pontos Fundamentais
- **Necessidade de dados confiáveis para decisões de investimento**: garante que a escolha das linhas a receber novos ônibus seja feita com base em evidências concretas.  
- **Apoio à mobilidade urbana inteligente**: contribui para um transporte público mais eficiente, moderno e integrado às demandas reais da população.



## Fluxograma do Algoritmo

Abaixo está o fluxograma que representa as etapas do algoritmo:

![Fluxograma do algoritmo](fluxograma.jpg)


## Algoritmo

A seguir está o código-fonte principal do algoritmo desenvolvido (`main.py`):

```python
# main.py
# Descrição: Algoritmo para contabilizar passageiros em linhas de ônibus,
# identificar quais linhas possuem maior demanda e gerar um ranking.

entradas_por_linha = {}  

with open('out.csv', 'r') as arquivo:
    for linha in arquivo:
        linha_limpa = linha.strip()
        id_linha = int(linha_limpa.split(",", 1)[0])
        dados = linha_limpa.split(",", 1)[1]
        pares = dados.split(",")
        total_entradas = sum(int(pass_.split(":")[0]) for pass_ in pares)
        entradas_por_linha[id_linha] = entradas_por_linha.get(id_linha, 0) + total_entradas

ranking = sorted(entradas_por_linha.items(), key=lambda item: item[1], reverse=True)
print(ranking)