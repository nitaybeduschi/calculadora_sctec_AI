# AGENTS.md

# Contexto do projeto

Repositório didático de uma calculadora simples em Python, usado em aulas do SENAI para demonstrar comandos de Git e workflows com agentes de IA.

Este é um projeto educacional.
Priorize clareza e simplicidade acima de sofisticação arquitetural.

---

## Stack

- Python 3 (stdlib)
- pytest para testes

---

## Estrutura do projeto

- `src/calculadora.py` — funções da calculadora
- `main.py` — entrypoint de demonstração
- `tests/test_calculadora.py` — suíte de testes
- `pyproject.toml` — configuração do pytest

---

## Comandos de execução

Sempre use estes comandos ao validar alterações:

```bash
python main.py
python -m pytest
python -m pytest -v
```

Sempre rode os testes após alterar arquivos em `src/` ou `tests/`.

---

## Convenções obrigatórias

### Idioma
- nomes de funções em português
- comentários em português
- mensagens de commit em português

### Commits
Use Conventional Commits:

- `feat:`
- `fix:`
- `test:`
- `docs:`
- `chore:`
- `refactor:`

Formato:
- prefixo semântico
- mensagem curta
- imperativo
- minúsculas

Exemplo:

```text
feat: adiciona operação de porcentagem
```

### Branches

Para novas funcionalidades:

```text
feature/<nome-curto>
```

Para correções:

```text
fix/<nome>
```

---

## Regras de implementação

Ao implementar uma nova feature, siga obrigatoriamente esta sequência:

1. identificar os arquivos que serão alterados
2. explicar a abordagem técnica antes de alterar
3. implementar a função em `src/calculadora.py`
4. expor em `main.py` se fizer sentido
5. adicionar testes em `tests/test_calculadora.py`
6. cobrir caminho feliz e ao menos um edge case
7. executar `python -m pytest`
8. reportar resultado dos testes

---

## Estilo de código

Seguir Python idiomático e direto.

Regras:
- código simples
- legível em aula
- sem abstrações desnecessárias
- evitar engenharia excessiva
- clareza > sofisticação

Não fazer:
- refactor oportunista
- reorganização estrutural sem pedido
- introdução de novas dependências sem necessidade

---

## Regras do agente

- não executar commit sem solicitação explícita
- não executar merge sem solicitação explícita
- não abrir PR sem solicitação explícita
- se pedirem commit, retornar apenas a mensagem sugerida
- manter mudanças mínimas e focadas
- preservar o fluxo didático do projeto

Antes de finalizar qualquer alteração, sempre informar:
- arquivos modificados
- resumo do que mudou
- resultado dos testes
- possíveis próximos passos