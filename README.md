# Python_Chat_Bot
Python Chat Bot

Este projeto utiliza o **LangChain**, a integração com o **Groq** e a extração de informações de vídeos do YouTube para fornecer detalhes sobre animais e suas características, além de permitir a visualização de vídeos relacionados. O sistema consulta um modelo de linguagem para responder a perguntas sobre animais e também permite assistir a vídeos do YouTube sobre o animal selecionado.

## Funcionalidades

- **Consulta de Informações sobre Animais**: O usuário pode inserir o nome de um animal e a região onde ele é encontrado, e o sistema retorna as informações detalhadas sobre o animal usando o modelo **Groq**.
- **Exibição de Vídeos do YouTube**: O usuário pode escolher se deseja visualizar um vídeo relacionado ao animal escolhido. O vídeo é extraído diretamente do YouTube utilizando o `YoutubeLoader` da LangChain.

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o seguinte instalado:

- Python 3.x
- Chave de API do Groq (necessária para o modelo de IA)
- Pacotes:
  - `langchain-community` para o `YoutubeLoader`
  - `langchain-groq` para o `ChatGroq`
  - `yt-dlp` para carregar vídeos do YouTube

## Instalação

### Passo 1: Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu_usuario/nome_do_repositorio.git
cd nome_do_repositorio 
```

### Passo 2: Criar e Ativar Ambiente Virtual

Recomenda-se criar um ambiente virtual para isolar as dependências do projeto.

#### Criando o ambiente virtual:

```bash
python -m venv venv
```

Ativando o ambiente virtual:
Windows:

```bash
venv\Scripts\activate
```
Linux/macOS:

```bash
source venv/bin/activate
```

### Passo 3: Instalar Dependências

Instale as dependências necessárias com o seguinte comando:

```bash
pip install langchain-community langchain-groq yt-dlp
```

### Passo 4: Configuração da API Groq

Para usar o modelo Groq, é necessário configurar a chave da API. Obtenha a chave de API diretamente no site do Groq. Após obtê-la, defina a chave da API no seu ambiente:

```bash
import os
os.environ["GROQ_API_KEY"] = 'SUA_CHAVE_API_AQUI'
```

### Passo 5: Rodando o Projeto
Execute o script Python com o comando:

```bash
python seu_script.py
```

### Passo 6: Interação com o Sistema
Quando o script rodar, ele pedirá as seguintes informações:

Nome do animal (ex: "Leão")
Região do animal (ex: "África")
Deseja ver um vídeo? (Digite "S" para sim ou "N" para não)
O script irá retornar as informações sobre o animal e, caso o usuário escolha "S", exibirá um vídeo relacionado ao animal (se disponível).

## Deploy
Para realizar o deploy do projeto em um servidor ou ambiente de produção, basta garantir que todas as dependências estejam instaladas e a chave da API Groq esteja configurada no ambiente do servidor.

### Passo 1: Configuração no Servidor
Crie um ambiente virtual no servidor e instale as dependências da mesma forma que no ambiente local.

### Passo 2: Rodar o Projeto em Background
Em servidores de produção, você pode rodar o script em background utilizando ferramentas como tmux ou screen, ou configurar um cron job para rodá-lo em intervalos.

## Licença
Este projeto está licenciado sob a Licença MIT

### Instruções para Usar:

1. **Crie um arquivo `README.md`** no seu repositório do GitHub.
2. **Cole este conteúdo** dentro do arquivo `README.md`.
3. **Faça um commit** e envie para o seu repositório no GitHub:

```bash
git add README.md
git commit -m "Adicionando README formatado"
git push origin main
