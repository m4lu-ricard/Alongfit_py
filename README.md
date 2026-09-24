# AlongFit

O **AlongFit** é uma aplicação desktop desenvolvida para auxiliar trabalhadores em regime de *home office* a combater o sedentarismo e prevenir lesões ocupacionais (como LER e DORT). O sistema monitora a rotina de trabalho e emite alertas ativos sugerindo pausas para alongamentos guiados, personalizados de acordo com desconfortos físicos relatados pelo usuário.

## 🚀 Funcionalidades

* **Gestão de Tarefas e Jornada:** Configuração personalizada do tempo de foco e intervalos de descanso.
* **Cronômetro e Alertas Ativos:** Notificações visuais e sonoras em tempo real indicando o momento exato de realizar uma pausa.
* **Guia Ergonômico Inteligente:** Sugestão de exercícios de alongamento específicos com base na dor relatada (ex: Cervicalgia, Lombalgia).
* **Dashboard de Estatísticas:** Acompanhamento do progresso e taxa de conclusão de exercícios através de gráficos visuais interativos.
* **Inicialização Autônoma:** O sistema constrói e popula seu próprio banco de dados local no primeiro uso, sem exigir configurações complexas de infraestrutura.

## 🛠️ Tecnologias Utilizadas

* **Python 3:** Linguagem principal, com forte aplicação de Orientação a Objetos.
* **Tkinter:** Biblioteca nativa utilizada para o desenvolvimento da Interface Gráfica (GUI), garantindo que o software seja leve.
* **SQLite3:** Banco de dados relacional embutido para persistência de históricos e catálogos de forma segura e local.
* **Matplotlib:** Utilizada para a geração analítica e renderização dos gráficos de estatísticas na interface.

## 🏗️ Arquitetura do Projeto

O código-fonte foi estruturado seguindo o padrão de projeto **Model-View-Controller (MVC)**, garantindo a separação clara de responsabilidades:

* `model/`: Contém as classes que representam as entidades do domínio (Usuário, Alongamento, HistoricoAlon, JornadaTrabalho, etc.).
* `view/`: Abriga todas as telas da aplicação (Login, Home, Timer, Configurações, Estatísticas), operando de forma desacoplada.
* `controller/`: Centraliza as regras de negócio, lógica de sessão, comunicação com o banco e o motor do cronômetro (utilizando o padrão *Observer*).
* `dao/`: Scripts SQL utilizados pelo sistema para a criação automatizada das tabelas e inserção dos dados essenciais.
* `assets/`: Arquivos estáticos de mídia, como imagens, ícones e alertas em áudio (`.mp3`).

## ⚙️ Como Instalar e Executar

### 1. Pré-requisitos

Certifique-se de ter o **Python 3** instalado em sua máquina. Para o pleno funcionamento da tela de estatísticas, é necessário instalar a biblioteca externa responsável pelos gráficos.

### 2. Instalação das Dependências

Abra o seu terminal e instale o Matplotlib utilizando o gerenciador de pacotes do Python:

```bash
pip install matplotlib

```

*(Caso o comando acima não seja reconhecido, utilize `python -m pip install matplotlib`).*

### 3. Execução

No terminal, navegue até a pasta raiz do projeto clonado e execute o arquivo principal da aplicação:

```bash
python view/app.py

```

> **Aviso sobre o Banco de Dados:** Não é necessário instalar nenhum servidor de banco de dados (como MySQL ou Postgres). Ao rodar o `app.py` pela primeira vez, o controlador do sistema executará os scripts da pasta `dao/` silenciosamente e criará o arquivo físico `alongfit.db` na raiz do seu projeto, já pronto para uso.

## 👥 Equipe de Desenvolvimento

Software desenvolvido como projeto acadêmico para o curso de Engenharia de Software da Universidade Católica de Brasília (UCB).

* Leticia Delmilio Soares
* Marcos Vinicius Nunes Moreira
* Maria Luiza Ricardo Fernandes
* Mariana Cardoso Honorato
* Paulo Vinícius Sousa Lima
