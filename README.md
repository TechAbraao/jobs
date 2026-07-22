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

- Busca vagas de emprego na plataforma Gupy com filtros de cidade, tipo de contrato e palavra-chave.

```bash
jobs-cli search [OPTIONS]
```
##### 1.3.1.1. Tabela

| Opção | Atalho | Tipo | Padrão | Descrição |
|---|---|---|---|---|
| `--city` | `-c` | `str` | `None` | Filtra vagas por cidade. |
| `--limit` | `-l` | `int` | `10` | Quantidade de resultados retornados. |
| `--keyword` | `-k` | `str` | `None` | Palavra-chave para buscar no título e na descrição das vagas. |
| `--type` | `-t` | `str` | `Efetivo` | Tipo de vaga a ser filtrada. Opções: `Efetivo`, `Estágio`, `Jovem Aprendiz`. |
| `--state` | `-s` | `str` | `None` | Filtra vagas por estado. |
| `--output` | `-o` | `str` | `None` | Nome do arquivo `.txt` para salvar os resultados (salvo em `jobs/data/`). |
| `--enterprise` | `-e` | `str` | `None` | Filtra vagas por empresa. |
- Busca padrão

```bash
$ jobs-cli search
```
- Exemplo de retorno:

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Empresa                       ┃ Cargo                                                                                 ┃ Cidade ┃ Estado ┃ URL        ┃ Publicado em           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Ourofino Saúde Animal         │ Coordenador(a) de Demanda Nacional | Animais de Companhia                             │        │        │ Abrir Vaga │ 2026-07-21 às 15:10:59 │
│ VENHA SER #SANGUELARANJA 🧡🚀 │ Desenvolvedor Fullstack .NET + Angular ou React - Pleno                               │        │        │ Abrir Vaga │ 2026-07-21 às 15:02:38 │
│ Vagas Inmetrics               │ ANALISTA DE ENGENHARIA DE DADOS SR - Remoto                                           │        │        │ Abrir Vaga │ 2026-07-21 às 15:02:14 │
│ Strattner                     │ Executivo Comercial Sênior | CME (Porto Alegre/RS)                                    │        │        │ Abrir Vaga │ 2026-07-21 às 14:48:41 │
│ Caju                          │ Pessoa Desenvolvedora Front-End Sênior                                                │        │        │ Abrir Vaga │ 2026-07-21 às 14:44:10 │
│ Escalada                      │ ATENTO ESCALADA - Instrutor de Treinamento Jr (Pluxee) - Unidade São Bento            │        │        │ Abrir Vaga │ 2026-07-21 às 14:42:43 │
│ Caju                          │ Pessoa Desenvolvedora Front-End Plena | Vaga Afirmativa para Pessoas com Deficiência  │        │        │ Abrir Vaga │ 2026-07-21 às 14:34:52 │
│ Asaas                         │ Assistente de Atendimento ao Cliente                                                  │        │        │ Abrir Vaga │ 2026-07-21 às 14:27:24 │
│ Strattner                     │ Executivo Comercial Sênior | Diagnóstico por Imagem (Recife/PE)                       │        │        │ Abrir Vaga │ 2026-07-21 às 14:25:04 │
│ #sejaveriter                  │ Frontend Developer Sênior - REMOTO                                                    │        │        │ Abrir Vaga │ 2026-07-21 às 14:21:11 │
└───────────────────────────────┴───────────────────────────────────────────────────────────────────────────────────────┴────────┴────────┴────────────┴────────────────────────┘
```

- Busca por vagas de Estágio no Rio de Janeiro
```bash
$ jobs-cli search --city="Rio de Janeiro" --type="Estágio"
```

- Exemplo de retorno:

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Empresa                                 ┃ Cargo                                                  ┃ Cidade         ┃ Estado         ┃ URL        ┃ Publicado em           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Oportunidades Petros                    │ Estágio no Setor de Relacionamento com Participantes   │ Rio de Janeiro │ Rio de Janeiro │ Abrir Vaga │ 2026-07-21 às 14:13:16 │
│ AZZAS 2154 FASHION & LIFESTYLE          │ AZZAS F&L | Estagio em Mídia Paga | Digital            │ Rio de Janeiro │ Rio de Janeiro │ Abrir Vaga │ 2026-07-21 às 13:12:36 │
│ Supergasbras                            │ Estágio em Análise e Métricas | Rio de Janeiro - RJ.   │ Rio de Janeiro │ Rio de Janeiro │ Abrir Vaga │ 2026-07-21 às 13:04:36 │
│ Energisa Estágio                        │ ESTAGIARIO NIVEL SUP. - M                              │ Rio de Janeiro │ Rio de Janeiro │ Abrir Vaga │ 2026-07-21 às 13:01:57 │
│ Programa de Estágio de Obras Tenda 2026 │ ESTAGIO - JURÍDICO IMOBILIÁRIO                         │ Rio de Janeiro │ Rio de Janeiro │ Abrir Vaga │ 2026-07-21 às 13:00:40 │
│ LENNY NIEMEYER                          │ Estagiário(a) | Jurídico                               │ Rio de Janeiro │ Rio de Janeiro │ Abrir Vaga │ 2026-07-20 às 20:01:38 │
│ Grupo Trigo                             │ Estágio em Marketing | China in Box                    │ Rio de Janeiro │ Rio de Janeiro │ Abrir Vaga │ 2026-07-20 às 19:59:13 │
│ Cury Construtora                        │ Pessoa Estagiária de Engenharia Civil - Niterói/ RJ    │ Rio de Janeiro │ Rio de Janeiro │ Abrir Vaga │ 2026-07-20 às 14:33:15 │
│ Cury Construtora                        │ Pessoa Estagiária de Engenharia Civil - Niterói/ RJ    │ Rio de Janeiro │ Rio de Janeiro │ Abrir Vaga │ 2026-07-20 às 14:26:15 │
│ Trabalhe com a RSM                      │ Programa de Estágio de Auditoria 2026 - Rio de Janeiro │ Rio de Janeiro │ Rio de Janeiro │ Abrir Vaga │ 2026-07-20 às 14:17:52 │
└─────────────────────────────────────────┴────────────────────────────────────────────────────────┴────────────────┴────────────────┴────────────┴────────────────────────┘
```

- Busca através dos atalhos
```bash
$ jobs-cli search -s "São Paulo" -c "São Paulo" -l 5 -t "Efetivo"
```

- Exemplo de retorno:

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Empresa                                                                ┃ Cargo                                                 ┃ Cidade    ┃ Estado    ┃ URL        ┃ Publicado em           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ McDonald's Restaurante - Arcos Dorados                                 │ ATENDENTE DE RESTAURANTE ( LIBERDADE - SAO PAULO/SP)  │ São Paulo │ São Paulo │ Abrir Vaga │ 2026-07-21 às 15:10:31 │
│ GPA                                                                    │ Operador(a) de E-commerce I - Santa Cecilia (575742)  │ São Paulo │ São Paulo │ Abrir Vaga │ 2026-07-21 às 15:07:36 │
│ Vivo Digital                                                           │ Analista Sistemas Senior                              │ São Paulo │ São Paulo │ Abrir Vaga │ 2026-07-21 às 15:07:11 │
│ McDonald's Restaurante - Arcos Dorados                                 │ ATENDENTE DE RESTAURANTE ( BRAS - SAO PAULO/SP)       │ São Paulo │ São Paulo │ Abrir Vaga │ 2026-07-21 às 15:05:21 │
│ Assaí Atacadista - O atacadista com 50 anos de tradição! #VemserAssaí  │ Operador(a) de Caixa                                  │ São Paulo │ São Paulo │ Abrir Vaga │ 2026-07-21 às 15:04:34 │
└────────────────────────────────────────────────────────────────────────┴───────────────────────────────────────────────────────┴───────────┴───────────┴────────────┴────────────────────────┘
```

- Busca usando filtro da empresa
```bash
$ jobs-cli search -e "Safra" -l 15
```

- Exemplo de retorno:

```bash
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Empresa ┃ Cargo                                                                                       ┃ Cidade         ┃ Estado       ┃ URL        ┃ Publicado em           ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Safra   │ Riscos  Mercado & Operacional                                                               │ São Paulo      │ São Paulo    │ Abrir Vaga │ 2026-07-20 às 18:01:28 │
│ Safra   │ Analista de Projetos de Cobrança - Sênior                                                   │ São Paulo      │ São Paulo    │ Abrir Vaga │ 2026-07-17 às 19:32:21 │
│ Safra   │ Especialista - Jurídico Asset                                                               │ São Paulo      │ São Paulo    │ Abrir Vaga │ 2026-07-10 às 12:18:25 │
│ Safra   │ Analista de CRM Sr - CRM                                                                    │ São Paulo      │ São Paulo    │ Abrir Vaga │ 2026-07-08 às 20:57:55 │
│ Safra   │ Distribuição de Investimentos | Investor Advisor - Empresas                                 │ S�o Paulo      │ São Paulo    │ Abrir Vaga │ 2026-07-07 às 19:10:55 │
│ Safra   │ Analista Middle Office | Asset                                                              │ S�o Paulo      │ São Paulo    │ Abrir Vaga │ 2026-07-07 às 18:36:38 │
│ Safra   │ Especialista em data science                                                                │ São Paulo      │ São Paulo    │ Abrir Vaga │ 2026-07-07 às 12:58:42 │
│ Safra   │ Operador de Computador – Turno III (23h15 às 07h00) - Vaga exclusiva PCD                    │ S�o Paulo      │ São Paulo    │ Abrir Vaga │ 2026-07-03 às 15:08:00 │
│ Safra   │ Analista de Suporte Jr - Vaga exclusiva PCD                                                 │ S�o Paulo      │ São Paulo    │ Abrir Vaga │ 2026-07-01 às 18:55:13 │
│ Safra   │ Especialista Comercial (Hunter) | Consignado Privado | Safra Financeira (Belo Horizonte/MG) │ Belo Horizonte │ Minas Gerais │ Abrir Vaga │ 2026-06-29 às 13:00:16 │
│ Safra   │ Especialista Comercial (Hunter) | Consignado Privado | Safra Financeira (Recife/PE)         │ Recife         │ Pernambuco   │ Abrir Vaga │ 2026-06-29 às 12:55:28 │
│ Safra   │ Especialista Comercial (Hunter) | Consignado Privado | Safra Financeira (Curitiba/PR)       │ Curitiba       │ Paraná       │ Abrir Vaga │ 2026-06-29 às 12:51:50 │
│ Safra   │ Executivo Vendas Cartorio                                                                   │ São Paulo      │ São Paulo    │ Abrir Vaga │ 2026-06-26 às 18:57:59 │
│ Safra   │ Executivo de Contas Safrapay - RJ (Capital e Niterói)                                       │                │              │ Abrir Vaga │ 2026-06-23 às 18:10:06 │
│ Safra   │ Executivo de Contas Safrapay - MG (Belo Horizonte, Juiz de Fora e Uberlândia)               │                │              │ Abrir Vaga │ 2026-06-23 às 18:04:28 │
└─────────┴─────────────────────────────────────────────────────────────────────────────────────────────┴────────────────┴──────────────┴────────────┴────────────────────────┘
```

#### 1.3.2. Comando `match` (beta)
- Busca vagas de emprego na plataforma Gupy utilizando os filtros disponíveis e calcula a porcentagem de compatibilidade de cada vaga com as palavras-chave definidas pelo usuário no arquivo `KEYWORDS.md`.

```bash
$ jobs-cli match [OPTIONS]
```

- Para utilizar o comando `match`, renomeie o arquivo `KEYWORDS_TEMPLATE.md` para `KEYWORDS.md`. O arquivo está localizado na raiz do projeto e deve permanecer nesse diretório. Em seguida, preencha-o com as palavras-chave que representam seus conhecimentos, tecnologias ou competências de interesse. Utilize o modelo abaixo como referência:

```text
Python
Java
Flask
FastAPI
Spring Boot
AWS
Amazon Web Services
Docker
Linux
Bash Script
```

##### 1.3.2.1. Tabela

| Opção | Atalho | Tipo | Padrão | Descrição |
|---|---|---|---|---|
| `--file` | `-f` | `KeywordsType` | `KEYWORDS.md` | Arquivo de palavras-chave. |
| `--city` | `-c` | `str` | `None` | Filtra vagas por cidade. |
| `--limit` | `-l` | `int` | `15` | Quantidade de resultados retornados. |
| `--keyword` | `-k` | `str` | `None` | Palavra-chave para buscar no título e na descrição das vagas. |
| `--state` | `-s` | `str` | `None` | Filtra vagas por estado. |
| `--enterprise` | `-e` | `str` | `None` | Filtra vagas por empresa. |

- Busca vagas em São Paulo pela palavra-chave `Java` com cálculo de compatibilidade.

```bash
$ jobs-cli match -f KEYWORDS.md -s "São Paulo" -l 15 -k "Java"
```

- Exemplo de retorno

```bash
┏━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Porcentual ┃ Empresa                       ┃ Cargo                                                                  ┃ Cidade          ┃ Estado    ┃ URL        ┃ Palavras                              ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 50%        │ PagBank                       │ Engenheiro de Software Jr. (Java)                                      │ São Paulo       │ São Paulo │ Abrir Vaga │ java, spring boot, aws, docker, linux │
│ 50%        │ PagBank                       │ Engenheiro de Software Sr. (Java)                                      │ São Paulo       │ São Paulo │ Abrir Vaga │ java, spring boot, aws, docker, linux │
│ 50%        │ Firedev IT                    │ SkillHunter - Desenvolvedor Java com React                             │ São Paulo       │ São Paulo │ Abrir Vaga │ java, spring boot, aws, docker, linux │
│ 40%        │ VENHA SER #SANGUELARANJA 🧡🚀 │  Pessoa Desenvolvedor(a) Java / Microsserviços - Pleno                 │ São Paulo       │ São Paulo │ Abrir Vaga │ java, spring boot, aws, docker        │
│ 40%        │ Porto                         │ Pessoa Desenvolvedora Java Pleno                                       │ São Paulo       │ São Paulo │ Abrir Vaga │ python, java, spring boot, aws        │
│ 30%        │ PagBank                       │ Engenheiro de Software Sr. (Java)                                      │ Sao Paulo       │ São Paulo │ Abrir Vaga │ java, aws, docker                     │
│ 30%        │ PagBank                       │ Engenheiro de Software Sr. (Java)                                      │ Sao Paulo       │ São Paulo │ Abrir Vaga │ java, aws, docker                     │
│ 30%        │ Brasilprev                    │ ANALISTA DE SISTEMAS JAVA PLENO                                        │ São Paulo       │ São Paulo │ Abrir Vaga │ python, java, aws                     │
│ 30%        │ Minsait an Indra Company      │ Desenvolvedor Java Fullstack com Angular Pleno                         │ São Paulo       │ São Paulo │ Abrir Vaga │ java, spring boot, docker             │
│ 30%        │ Itaú Unibanco                 │ Engenharia de Software Fullstack Pleno - Java/Angular | Recuperação PF │ São Paulo       │ São Paulo │ Abrir Vaga │ java, aws, docker                     │
│ 20%        │ Minsait an Indra Company      │ Desenvolvedor Java Backend Pleno                                       │ São Paulo       │ São Paulo │ Abrir Vaga │ java, spring boot                     │
│ 20%        │ Minsait an Indra Company      │ Desenvolvedor Java Backend Pleno                                       │ São Paulo       │ São Paulo │ Abrir Vaga │ java, spring boot                     │
│ 20%        │ PagBank                       │ Engenheiro de Software Pl. (Java)                                      │ Sao Paulo       │ São Paulo │ Abrir Vaga │ java, aws                             │
│ 20%        │ PagBank                       │ Engenheiro de Software Sr. (Java)                                      │ Sao Paulo       │ São Paulo │ Abrir Vaga │ java, aws                             │
│ 10%        │ ADMINISTRADOR DE REDES        │ Analista Desenvolvedor Java Pl                                         │ Taboão da Serra │ São Paulo │ Abrir Vaga │ java                                  │
└────────────┴───────────────────────────────┴────────────────────────────────────────────────────────────────────────┴─────────────────┴───────────┴────────────┴───────────────────────────────────────┘
```

#### 1.3.3. Comando `history` 

- Permite visualizar o histórico de comandos utilizados, com a opção de limitar a quantidade exibida.

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

- Com o ambiente ativado, o comando `jobs-cli` fica disponível no terminal:

```bash
$ jobs-cli --help
```

```bash                                                                                                                                
 Usage: jobs-cli [OPTIONS] COMMAND [ARGS]...                                                                                                                                                                                                  
                                                                                                                                                                                                                                              
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                                                                                                                    │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                                                                                                             │
│ --help                        Show this message and exit.                                                                                                                                                                                  │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ match                                                                                                                                                                                                                                      │
│ search                                                                                                                                                                                                                                     │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

- Comandos disponíveis em `search`

```bash
$ jobs-cli search --help
```

```bash
 Usage: jobs-cli search [OPTIONS]                                                                                                                                                                                                             
                                                                                                                                                                                                                                              
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --city        -c      <str>                             Filtra vagas por cidade.                                                                                                                                                           │
│ --limit       -l      <int>                             Quantidade de resultados. [default: 10]                                                                                                                                            │
│ --keyword     -k      <str>                             Palavra-chave para buscar no título e na descrição das vagas.                                                                                                                      │
│ --state       -s      <str>                             Filtra vagas por estado.                                                                                                                                                           │
│ --type        -t      <Efetivo|Estágio|Jovem Aprendiz>  Tipo de vaga a ser filtrada. [default: Efetivo]                                                                                                                                    │
│ --output      -o      <str>                             Nome do arquivo .txt para salvar os resultados (salvo em jobs/data/).                                                                                                              │
│ --enterprise  -e      <str>                             Filtra vagas por empresa.                                                                                                                                                          │
│ --help                                                  Show this message and exit.                                                                                                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

- Comandos disponíveis em `match`

```bash
$ jobs-cli match --help
```

```bash
 Usage: jobs-cli match [OPTIONS]                                                                                                                                                                                                              
                                                                                                                                                                                                                                              
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --file        -f      <KEYWORDS.md>  Arquivo de palavras-chave. [default: KEYWORDS.md]                                                                                                                                                     │
│ --keyword     -k      <str>          Palavra-chave para buscar no título e na descrição das vagas.                                                                                                                                         │
│ --limit       -l      <int>          Quantidade de resultados. [default: 15]                                                                                                                                                               │
│ --enterprise  -e      <str>          Filtra vagas por empresa.                                                                                                                                                                             │
│ --state       -s      <str>          Filtra vagas por estado.                                                                                                                                                                              │
│ --city        -c      <str>          Filtra vagas por cidade.                                                                                                                                                                              │
│ --help                               Show this message and exit.                                                                                                                                                                           │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
