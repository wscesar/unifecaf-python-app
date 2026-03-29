# Controle de Produção e Qualidade

Este é um projeto simples para simular um sistema de validação de peças de uma linha de produção utilizando Python. O projeto foi desenhado sob o paradigma procedural. Ele roda totalmente em memória usando estruturas de dados simples e não requer banco de dados.

## Fluxo do Programa

1. **Cadastro e Validação**: Assim que uma peça é cadastrada através do console no terminal, uma função de validação (`validar`) julga suas dimensões:
   - **Peso**: Deve estar entre `95.0` e `105.0` gramas;
   - **Cor**: Deve ser exatamente `"azul"` ou `"verde"` (insensível a maiúsculas/minúsculas);
   - **Comprimento**: Deve estar entre `10.0` e `20.0` cm.
2. Com base nessas informações, a peça pode ser **Aprovada** (caso atenda todas as métricas) ou **Reprovada** (caso falhe em pelo menos uma métrica). As informações detalhadas daquela peça e seus motivos de reprovação são mantidas num inventário (`tabela`).
3. **Distribuição em Caixas**: O sistema simula o empacotamento das peças aprovadas estimando o número de caixas necessárias de forma matemática simples, assumindo que cada caixa armazena exatas 10 peças.
4. Pelo menu interativo do sistema, você pode ver um relatório com a quantidade de peças aprovadas e os motivos registrados em cada um dos itens rejeitados.

## Como Executar

O projeto foi projetado para rodar em Python padrão (não necessita de bibliotecas externas). Basta dar play no script central.

```bash
python app.py
```

## Exemplos de Interação

### Exemplo 1: Peça Aprovada
- **ID da peça:** `1`
- **Cor:** `azul`
- **Peso:** `100`
- **Comprimento:** `15`

> **Resultado**: O terminal exibirá um OK aprovando os atributos, e a peça passará a render do cálculo de caixas abertas no relatório final.

### Exemplo 2: Peça Reprovada (fora do padrão)
- **ID da peça:** `2`
- **Cor:** `vermelho`
- **Peso:** `110`
- **Comprimento:** `25`

> **Resultado**: O terminal bloqueará e reprovará essa peça em seguida. Ao acessar o `Relatório`, os 3 defeitos serão exibidos: *"Cor inválida"*, *"Peso fora do limite"* e *"Comprimento fora do limite"*.

## Estrutura dos Dados e Dicionário 

Ao invés de usar classes para abrigar a regra de negócios, o módulo utiliza estruturas chave-valor em `salvar_peca`, em que a chave é a `id_peca` escolhida pelo usuário:
```python
tabela[id_peca] = {
    "cor": cor,
    "peso": peso,
    "comprimento": comprimento,
    "aprovada": aprovada,
    "motivos": motivos
}
```
