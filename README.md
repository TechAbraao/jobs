# Jobs CLI

<div align="center"><pre>                       
     ██╗ ██████╗ ██████╗ ███████╗     ██████╗██╗     ██╗
     ██║██╔═══██╗██╔══██╗██╔════╝    ██╔════╝██║     ██║
     ██║██║   ██║██████╔╝███████╗    ██║     ██║     ██║
██   ██║██║   ██║██╔══██╗╚════██║    ██║     ██║     ██║
╚█████╔╝╚██████╔╝██████╔╝███████║    ╚██████╗███████╗██║
 ╚════╝  ╚═════╝ ╚═════╝ ╚══════╝     ╚═════╝╚══════╝╚═╝
</pre></div>


## 1. Sobre
### 1.1. Informações Gerais
- CLI em Python para buscar vagas de emprego diretamente pelo terminal, consumindo a API da Gupy.
- Projeto de cunho acadêmico e open-source, com o objetivo de ajudar a comunidade a filtrar e encontrar oportunidades de emprego com mais facilidade.

### 1.2. Tecnologias
- Python
- Httpx
- Typer
- Rich

### 1.3. Documentação
#### 1.3.1. Comando `search`

Busca vagas de emprego na plataforma Gupy com filtros de cidade, tipo de contrato e palavra-chave.

```bash
jobs-cli search [OPTIONS]
```

| Opção | Tipo | Padrão | Descrição |
|---|---|---|---|
| `--city` | `str` | `São Paulo` | Filtra vagas por cidade. |
| `--limit` | `int` | `10` | Quantidade de resultados retornados. |
| `--keyword` | `str` | `Tecnologia` | Palavra-chave para buscar no título e na descrição das vagas. |
| `--type` | `str` | `Efetivo` | Tipo de vaga a ser filtrada. Opções: `Efetivo`, `Estagiário`, `Jovem Aprendiz`. |

- Busca padrão (vagas de Tecnologia em São Paulo)

```bash
$ jobs-cli search
```
- Exemplo de retorno

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Empresa                       ┃ Cargo                                                               ┃ Cidade    ┃ URL        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ Vivo Digital                  │ Gerente de Tecnologia                                               │ São Paulo │ Abrir Vaga │
│ Vem Pra Vivo!                 │ Consultor Tecnológico 6H | AV ARICANDUVA  - SP                      │ São Paulo │ Abrir Vaga │
│ Vivo Digital                  │ Consultor de Tecnologias Martech (Hands On)                         │ São Paulo │ Abrir Vaga │
│ iugu                          │ Executivo de Contas - Vertical Tecnologia                           │ São Paulo │ Abrir Vaga │
│ BIP Brasil                    │ Gerente de Produtos de Tecnologia e Dados - Serviços Financeiros    │ São Paulo │ Abrir Vaga │
│ Núclea                        │ Analista de Riscos e Controles Internos BP | Segurança e Tecnologia │ São Paulo │ Abrir Vaga │
│ COPASTUR VIAGENS E TURISMO    │ Tecnologia | UX/UI Designer Júnior - RJ e SP                        │ São Paulo │ Abrir Vaga │
│ Motiva                        │ MOTIVA I ANALISTA DE SOLUÇÕES DE TECNOLOGIA PLENO                   │ São Paulo │ Abrir Vaga │
│ Lopes Consultoria Imobiliária │ [LOPES] ANALISTA ADMINISTRATIVO JUNIOR - área Tecnologia            │ São Paulo │ Abrir Vaga │
│ Software.com.br               │ Executivo de Contas Enterprise - Tecnologia                         │ São Paulo │ Abrir Vaga │
└───────────────────────────────┴─────────────────────────────────────────────────────────────────────┴───────────┴────────────┘
```

- Busca por vagas de Estágio no Rio de Janeiro
```bash
$ jobs-cli search --city="Rio de Janeiro" --type="Estagiário"
```

- Exemplo de retorno

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Empresa                     ┃ Cargo                                                                                                   ┃ Cidade         ┃ URL        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ Estácio                     │ PROFESSOR INGRESSANTE - TECNOLOGIA - ESTÁCIO PRESIDENTE VARGAS - EXCLUSIVA PARA PESSOAS PRETAS E PARDAS │ Rio de Janeiro │ Abrir Vaga │
│ Page Outsourcing Brasil     │ Gerente - Tecnologia e Arquitetura – Bradesco                                                           │ Rio de Janeiro │ Abrir Vaga │
│ Globo                       │ Analista de Processos Pleno | Processos de Tecnologia                                                   │ Rio de Janeiro │ Abrir Vaga │
│ Ambev                       │ TÉCNICO(A) ADMINISTRATIVO (Centro de Inovações e Tecnologia | Ilha do Fundão/ Rio de Janeiro)           │ Rio de Janeiro │ Abrir Vaga │
│ Globo                       │ Especialista Parceiro de Recursos Humanos | Tecnologia                                                  │ Rio de Janeiro │ Abrir Vaga │
│ Fragata e Antunes Advogados │ Estágio em Tecnologia da Informação                                                                     │ Rio de Janeiro │ Abrir Vaga │
│ Globo                       │ Especialista em Arquitetura Soluções | Infra e Telecom -  Arquitetura de Tecnologia                     │ Rio de Janeiro │ Abrir Vaga │
│ Ambev                       │ Operador (a) de Utilidades (Centro Tecnológico - Ilha do Fundão/RJ)                                     │ Rio de Janeiro │ Abrir Vaga │
│ Ambev                       │ AMBEV I Técnico(a) em Tecnologia da Informação (TI) e Analytics - Rio de Janeiro (Supply)               │ Rio de Janeiro │ Abrir Vaga │
│ Lefosse                     │ Advogado(a) Pleno - Tecnologia, Proteção de Dados e Propriedade Intelectual.                            │ Rio de Janeiro │ Abrir Vaga │
└─────────────────────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────┴────────────────┴────────────┘
```

## 2. Executando localmente
### 2.1. Pré-requisitos
- ...
- ...
- ...


