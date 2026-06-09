# Registro de Riscos - EcoSaúde DevSecOps

| Risco | Impacto | Controle | Evidência |
|---|---|---|---|
| Segredo exposto | Acesso indevido a APIs | Gitleaks + GitHub Secrets | Workflow falha |
| Dependência vulnerável | Exploração da aplicação | pip-audit | Log do pipeline |
| Imagem vulnerável | Container comprometido | Trivy | Relatório do scan |
| Permissão excessiva | Escalada de privilégio | RBAC | Manifesto Kubernetes |
| Dado adulterado | Forecast incorreto | Validação de integridade | Logs auditáveis |
