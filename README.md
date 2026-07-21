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
- Pytest

### 1.3. Documentação
#### 1.3.1. Comando `search`

Busca vagas de emprego na plataforma Gupy com filtros de cidade, tipo de contrato e palavra-chave.

```bash
jobs-cli search [OPTIONS]
```
##### 1.3.1.1. Tabela

| Opção | Tipo | Padrão | Descrição |
|---|---|---|---|
| `--city` | `str` | `São Paulo` | Filtra vagas por cidade. |
| `--limit` | `int` | `10` | Quantidade de resultados retornados. |
| `--keyword` | `str` | `N/A` | Palavra-chave para buscar no título e na descrição das vagas. |
| `--type` | `str` | `Efetivo` | Tipo de vaga a ser filtrada. Opções: `Efetivo`, `Estágio`, `Jovem Aprendiz`. |

- Busca padrão (vagas em São Paulo)

```bash
$ jobs-cli search
```
- Exemplo de retorno:

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Empresa                                                                ┃ Cargo                                                     ┃ Cidade    ┃ URL        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ Comgás                                                                 │ Pessoa Engenheira Sênior - Prevenção a Danos              │ São Paulo │ Abrir Vaga │
│ Rede Américas                                                          │ ANALISTA OPERACOES UNIDADE                                │ São Paulo │ Abrir Vaga │
│ Assaí Atacadista - O atacadista com 50 anos de tradição! #VemserAssaí  │ Operador(a) de Caixa - Frente de caixa                    │ São Paulo │ Abrir Vaga │
│ Minsait an Indra Company                                               │ Analista de Dados PL                                      │ São Paulo │ Abrir Vaga │
│ DC-DinsmoreCompass                                                     │ Gerente de Projetos Sênior - Presencial (Vila Olimpia/SP) │ São Paulo │ Abrir Vaga │
│ Minsait an Indra Company                                               │ Analista de dados PL                                      │ São Paulo │ Abrir Vaga │
│ Minsait an Indra Company                                               │  Desenvolvedor Fullstack                                  │ São Paulo │ Abrir Vaga │
│ Minsait an Indra Company                                               │ Analista de Dados JR                                      │ São Paulo │ Abrir Vaga │
│ Minsait an Indra Company                                               │ Desenvolvedor Fullstack                                   │ São Paulo │ Abrir Vaga │
│ DC-DinsmoreCompass                                                     │ Gerente de Projetos Senior | Reforma Tributária - SP      │ São Paulo │ Abrir Vaga │
└────────────────────────────────────────────────────────────────────────┴───────────────────────────────────────────────────────────┴───────────┴────────────┘
```

- Busca por vagas de Estágio no Rio de Janeiro
```bash
$ jobs-cli search --city="Rio de Janeiro" --type="Estágio"
```

- Exemplo de retorno:

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Empresa                                   ┃ Cargo                               ┃ Cidade         ┃ URL        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ Fragata e Antunes Advogados               │ Estágio em Tecnologia da Informação │ Rio de Janeiro │ Abrir Vaga │
│ Estágio em Tecnologia do Instituto Infnet │ Estágio em Tecnologia               │ Rio de Janeiro │ Abrir Vaga │
└───────────────────────────────────────────┴─────────────────────────────────────┴────────────────┴────────────┘
```

## 2. Executando localmente
### 2.1. Pré-requisitos
- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- `pip` atualizado

### 2.2. Instalação

- Clone o repositório:

```bash
$ git clone git@github.com:TechAbraao/jobs.git
$ cd jobs
```

- Crie e ative um ambiente virtual:

```bash
$ python -m venv .venv
$ source .venv/bin/activate  # Linux/Mac
```

- Instale o projeto (via `pip`):

```bash
$ pip install -e .
```

- Ou via `Makefile`:

```bash
$ make install
```

### 2.3. Utilização

Com o ambiente ativado, o comando `jobs-cli` fica disponível no terminal:

```bash
$ jobs-cli search --help
```

```bash
Usage: jobs-cli search [OPTIONS]                                                                                                                                                             
                                                                                                                                                                                              
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --city           <str>                             Filtra vagas por cidade. [default: São Paulo]                                                                                           │
│ --limit          <int>                             Quantidade de resultados. [default: 10]                                                                                                 │
│ --keyword        <str>                             Palavra-chave para buscar no título e na descrição das vagas.                                                                           │
│ --type           <Efetivo|Estágio|Jovem Aprendiz>  Tipo de vaga a ser filtrada. [default: Efetivo]                                                                                         │
│ --help                                             Show this message and exit.                                                                                                             │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Veja a seção [1.3.1. Comando `search`](#131-comando-search) para todas as opções disponíveis.


