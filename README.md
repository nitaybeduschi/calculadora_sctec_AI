# Exemplo Git

Repositorio de exemplo para aulas de Git e workflows com agentes de IA. Implementa uma calculadora simples em Python.

## Operacoes disponiveis

- `somar(a, b)`
- `subtrair(a, b)`
- `multiplicar(a, b)`
- `dividir(a, b)` - lanca `ValueError` ao dividir por zero
- `potencia(base, expoente)`
- `raiz_quadrada(x)` - lanca `ValueError` se `x < 0`
- `fatorial(n)` - lanca `ValueError` para numero negativo

## Como executar

```bash
python main.py
```

## Como rodar os testes

```bash
python -m pytest
```
