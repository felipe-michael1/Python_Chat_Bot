import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import YoutubeLoader

#classe do reino animal
class ReinoAnimal:
    # Instancia e inicia a classe e o método construct
    def __init__(self, chat, nome_animal, regiao_animal, video):

        self.chat = chat
        self.nome_animal = nome_animal
        self.regiao_animal = regiao_animal
        self.video = video

    #retorn o animal correspondente
    def retorna_animal(self):
        # Entrada com f string
        resposta_animal = f"Olá tudo bem? Preciso saber tudo sobre as características deste animal: {self.nome_animal} e {self.regiao_animal} será que você poderia me passar?"
        resposta = chat.invoke(resposta_animal)
        print(resposta)

    # retorna video a respeito de determinado animal
    def retorna_video(self):
        # Verifica se o video for sim
        if self.video == 'S':
            # pega o video do animal e retorna
            if nome_animal == 'Lambari':
                loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=CCU7L6shn94", language=['pt'])
                lista_documento = loader.load()
                documento = ''
                for doc in lista_documento:
                    documento = documento + doc.page_content
                print(documento)
            else:
                print('Nenhum vídeo encontrado')
        else:
            print('Operação cancelada pelo usuário') # Mensagem de operação cencelada pelo usuário


# Definir a chave da API corretamente
api_key = '' # COLOQUE A SUA CHAVE DE API AQUI
os.environ["GROQ_API_KEY"] = api_key  # Definindo a chave da API no ambiente

# Criando a instância do ChatGroq
chat = ChatGroq(model='llama-3.3-70b-versatile')

# retorna as variaveis correspondentes
# primeiro retornamos o nosso animal
nome_animal = input('Digite o nome do animal. Pode ser um peixe, uma ave, um réptil ou qualquer outro : ')
regiao_animal = input('Digite qual a região do animal. Ex: Brasil, África : ')  
animal = ReinoAnimal(chat,nome_animal,regiao_animal,'')
animal.retorna_animal()
# segundo retornamos o nosso video - leitura completa do video
video = input('Você deseja verificar as informações de um vídeo?. Digite S para sim e N para não : ')
video = ReinoAnimal(chat,nome_animal, regiao_animal, video)
video.retorna_video()
