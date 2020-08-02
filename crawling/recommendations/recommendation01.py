from bs4 import BeautifulSoup
class Recommendation01:
    
    """
    Recomendação 1: Fornecer alternativa em texto para as imagens do sítio 
    Descrição da recomendação se houver

    :param name - Recebe o nome da Recomendação
    """

    def __init__(self, nome):
        self.nome = nome

    def print_name(self):
        print('teste')

    def Avaliacao(self, contents):
        self.contents = contents
        soap = BeautifulSoup(self.contents,'html.parser')
        imagens = soap.find_all('img')

        for imagem in imagens:
            if not imagem['alt'] :
                print('Erro :'+str(imagem)+'| Não possui atributo "Alt"' )



        
