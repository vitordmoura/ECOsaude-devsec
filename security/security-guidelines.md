# Diretrizes de Segurança - EcoSaúde

Credenciais devem ser armazenadas em GitHub Secrets ou Kubernetes Secrets. Arquivos `.env` não devem ser versionados.

Contêineres devem usar usuário não-root, remover capabilities desnecessárias, definir limites de recursos e passar por scan Trivy antes do deploy.
