**Evidência 01 – SCA** 



Arquivo: 01-sca-vulnerabilidades-dependencias.png




Durante a execução da etapa de Software Composition Analysis (SCA), a ferramenta pip-audit identificou vulnerabilidades conhecidas em dependências Python utilizadas pela aplicação.



Foram detectadas vulnerabilidades associadas às bibliotecas requests, python-dotenv e starlette, demonstrando que o pipeline é capaz de identificar automaticamente componentes potencialmente inseguros antes da implantação da aplicação.



**Ação Tomada**



As dependências vulneráveis foram atualizadas para versões corrigidas e compatíveis com o projeto. A etapa foi executada novamente até que as vulnerabilidades críticas fossem eliminadas ou mitigadas.



\-------------------------------------------------------------------------------------------------------



**Evidência 02 – Validação de Dependências**



Arquivo: 02-validacao-conflito-dependencias.png



Durante o processo de atualização das bibliotecas, o pipeline identificou um conflito de dependências entre as versões do FastAPI e Starlette.



A falha ocorreu durante a instalação dos pacotes e impediu a continuidade da execução do pipeline, evitando a utilização de uma configuração inconsistente do ambiente.



**Ação Tomada**



Foi realizada a revisão das dependências da aplicação e a substituição da stack inicial por uma implementação baseada em Flask, eliminando o conflito identificado e permitindo a continuidade das validações de segurança.





\----------------------------------------------------------------------------------------------------





**Evidência 03 – Trivy Image Scan**



Arquivo: 03-trivy-container-scan.png



Após a construção da imagem Docker da aplicação, a ferramenta Trivy executou uma análise de vulnerabilidades na imagem gerada.



A análise identificou vulnerabilidades de alta severidade presentes em componentes da imagem base do sistema operacional, demonstrando a capacidade do pipeline de avaliar riscos não apenas no código da aplicação, mas também na infraestrutura utilizada para execução.



**Ação Tomada**



A etapa foi mantida como mecanismo de auditoria contínua. O pipeline foi configurado para registrar e reportar vulnerabilidades encontradas, permitindo a visibilidade dos riscos identificados durante a fase acadêmica do projeto.





\----------------------------------------------------------------------------------------------------





**Conclusão**



As evidências apresentadas demonstram a aplicação prática dos conceitos de DevSecOps no projeto EcoSaúde. O pipeline implementado foi capaz de identificar vulnerabilidades em dependências, detectar inconsistências de configuração e analisar riscos presentes em imagens de contêineres, reforçando a adoção do princípio de Security by Design e promovendo maior segurança ao ciclo de desenvolvimento da solução.

