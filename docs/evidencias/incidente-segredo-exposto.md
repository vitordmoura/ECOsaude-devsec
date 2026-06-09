# Evidência - Incidente de Segredo Exposto

## Cenário
Um desenvolvedor adiciona acidentalmente uma chave diretamente no código.

```python
SATELLITE_API_KEY = "abc123-secret"
```

## Resultado esperado
O Gitleaks detecta o segredo e interrompe o pipeline.

## Correção
A chave é removida do código e cadastrada no GitHub Secrets.

```python
SATELLITE_API_KEY = os.getenv("SATELLITE_API_KEY")
```
