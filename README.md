# EcoSaúde DevSecOps


Módulo DevSecOps integrado ao projeto EcoSaúde, desenvolvido para a Global Solution FIAP 2026.


## Integrantes

Lucas Reis Diniz - RM552838

Thiago Araújo Vieira - RM553477

Vitor de Moura Nascimento - RM553806


## Sobre o Projeto

O EcoSaúde é uma plataforma de inteligência socioambiental baseada em dados espaciais, inteligência artificial e computação de borda, desenvolvida para transformar informações provenientes de satélites, APIs climáticas e bases geoespaciais em indicadores capazes de apoiar ações de saúde pública, saneamento básico e sustentabilidade.

A solução foi concebida para monitorar fatores ambientais diretamente relacionados à qualidade de vida da população, como qualidade da água, qualidade do ar, emissões de CO₂, queimadas, saneamento básico e condições favoráveis à disseminação de doenças. Os dados coletados são processados por serviços especializados que geram análises, alertas preventivos e previsões de tendência para regiões monitoradas.

Por depender da integridade e disponibilidade dessas informações, a segurança foi incorporada desde o início do desenvolvimento através da adoção de práticas DevSecOps. O objetivo é reduzir riscos operacionais, proteger credenciais e garantir que apenas componentes validados sejam promovidos para ambientes de execução.

---

## Objetivo

Proteger o ciclo de desenvolvimento da plataforma, considerando:

* Dados espaciais e geoespaciais;
* APIs ambientais e climáticas;
* Serviços críticos de forecast;
* Contêineres e infraestrutura em nuvem;
* Gestão segura de credenciais;
* Automação de verificações de segurança;
* Ambientes orquestrados com Kubernetes e K3s.

---

## Arquitetura da Solução

A implementação considera uma arquitetura baseada em microsserviços, permitindo que diferentes domínios da solução sejam processados de forma independente.

```text
Satélites e APIs Externas
            │
            ▼
      EcoSaúde Core
            │
 ┌──────────┼──────────┐
 │          │          │
 ▼          ▼          ▼
Forecast  Saúde   Saneamento
Service   Pública   Ambiental
            │
            ▼
      APIs Internas
            │
            ▼
      Docker/Kubernetes
            │
            ▼
      Pipeline DevSecOps
```

---

## Pipeline de Segurança

O pipeline é executado automaticamente a cada Push ou Pull Request através do GitHub Actions.

As validações ocorrem antes da disponibilização da aplicação e seguem o conceito de Security by Design.

### Fluxo

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
 ┌──┼───────────────┐
 │  │               │
 ▼  ▼               ▼
Gitleaks      Bandit     pip-audit
 │              │            │
 └───────┬──────┴────────────┘
         ▼
    Docker Build
         ▼
 Trivy Filesystem Scan
         ▼
   Trivy Image Scan
         ▼
      Deploy
```

---

## Controles Implementados

| Controle             | Ferramenta              | Finalidade                    |
| -------------------- | ----------------------- | ----------------------------- |
| Secret Scan          | Gitleaks                | Detectar credenciais expostas |
| SAST                 | Bandit                  | Analisar código Python        |
| SCA                  | pip-audit               | Auditar dependências          |
| Filesystem Scan      | Trivy                   | Verificar arquivos do projeto |
| Container Scan       | Trivy                   | Verificar imagem Docker       |
| Container Hardening  | Docker Security Options | Reduzir superfície de ataque  |
| Kubernetes Hardening | RBAC / Security Context | Aplicar mínimo privilégio     |

---

## Gestão de Credenciais

Nenhuma credencial é armazenada diretamente no código-fonte.

As informações sensíveis são gerenciadas através de GitHub Secrets.

Secrets utilizados:

```text
SATELLITE_API_KEY
CLIMATE_API_KEY
DATABASE_URL
```

Essa abordagem reduz riscos de exposição acidental e permite a separação entre código e configuração.

---

## Hardening Implementado

Os contêineres da aplicação foram configurados seguindo práticas básicas de segurança:

* Sistema de arquivos somente leitura (`read_only`)
* Restrição de escalonamento de privilégios (`no-new-privileges`)
* Remoção de capacidades Linux desnecessárias (`cap_drop: ALL`)
* Execução sem privilégios administrativos
* Diretório temporário isolado (`tmpfs`)
* Isolamento de processos dentro do contêiner

---

## Estrutura do Projeto

```text
.
├── .github/
│   └── workflows/
│       └── security-pipeline.yml
├── app/
│   └── main.py
├── infrastructure/
├── security/
├── docs/
│   └── evidencias/
│       ├── 01-sca-vulnerabilidades-dependencias.png
│       ├── 02-validacao-conflito-dependencias.png
│       ├── 03-trivy-container-scan.png
│       └── README_EVIDENCIAS.md
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Execução Local

Instalação das dependências:

```bash
pip install -r requirements.txt
```

Inicialização da aplicação:

```bash
flask --app app.main run --host 0.0.0.0 --port 8000
```

---

## Execução com Docker

Build da imagem:

```bash
docker build -t ecosaude-forecast-service .
```

Execução:

```bash
docker run -p 8000:8000 ecosaude-forecast-service
```

Docker Compose:

```bash
docker compose up -d
```

```

## GitHub Secrets necessários

- SATELLITE_API_KEY
- CLIMATE_API_KEY
- MAPS_TOKEN
- DATABASE_URL
- JWT_SECRET

```

---

## Scans Locais

### Bandit

```bash
bandit -r app
```

### pip-audit

```bash
pip-audit -r requirements.txt
```

### Trivy Filesystem

```bash
trivy fs .
```

### Trivy Image

```bash
trivy image ecosaude-forecast-service
```

---

## Endpoints

### Health Check

```http
GET /health
```

Resposta:

```json
{
  "status": "ok",
  "service": "ecosaude-forecast-service"
}
```

### Consulta de Risco

```http
GET /risk/{region_id}
```

Resposta:

```json
{
  "region_id": "SP001",
  "risk_index": 82,
  "trend": "crescente"
}
```

---

## Evidências da Implementação

As evidências da implementação encontram-se no diretório:

```text
docs/evidencias
```

O diretório contém capturas de tela, logs e documentação das principais validações executadas durante a implementação:

* Identificação de vulnerabilidades em dependências;
* Correção de conflitos entre bibliotecas;
* Análise de imagens Docker;
* Execução do pipeline GitHub Actions;
* Registro das ações corretivas realizadas.

Esses artefatos servem como comprovação prática da aplicação das práticas DevSecOps ao projeto EcoSaúde.

---

## Tecnologias Utilizadas

* Python
* Flask
* Docker
* Docker Compose
* GitHub Actions
* Gitleaks
* Bandit
* pip-audit
* Trivy
* Kubernetes
* K3s

---

## Global Solution FIAP 2026

Projeto desenvolvido como complemento da solução EcoSaúde para demonstrar a integração de práticas DevSecOps, automação de segurança e proteção de infraestrutura em aplicações baseadas em dados espaciais.



