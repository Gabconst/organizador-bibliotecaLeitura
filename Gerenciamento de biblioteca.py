import pickle

class Livro:
    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero

class Biblioteca:
    def __init__(self):
        self.livros = {}

    def cadastrar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def consultar_livro(self, titulo):
        if titulo in self.livros:
            livro = self.livros[titulo]
            print(f"Título: {livro.titulo}\nAutor: {livro.autor}\nAno: {livro.ano}\nGênero: {livro.genero}")
        else:
            print(f"Livro com título '{titulo}' não encontrado.")

    def listar_livros_por_autor(self, autor):
        livros_autor = [livro for livro in self.livros.values() if livro.autor == autor]
        if livros_autor:
            for livro in livros_autor:
                print(f"Título: {livro.titulo}\nAutor: {livro.autor}\nAno: {livro.ano}\nGênero: {livro.genero}")
        else:
            print(f"Nenhum livro encontrado para o autor '{autor}'.")

    def listar_livros_por_genero(self, genero):
        livros_genero = [livro for livro in self.livros.values() if livro.genero == genero]
        if livros_genero:
            for livro in livros_genero:
                print(f"Título: {livro.titulo}\nAutor: {livro.autor}\nAno: {livro.ano}\nGênero: {livro.genero}")
        else:
            print(f"Nenhum livro encontrado para o gênero '{genero}'.")

    def salvar_dados(self, nome_arquivo):
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.livros, arquivo)
        print("Dados salvos com sucesso!")

    def carregar_dados(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as arquivo:
                self.livros = pickle.load(arquivo)
            print("Dados carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado. Nenhuma informação carregada.")

# Função para exibir o menu
def exibir_menu():
    print("\n===== Menu =====")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Listar Livros por Autor")
    print("4. Listar Livros por Gênero")
    print("5. Salvar Dados")
    print("6. Carregar Dados")
    print("0. Sair")

# Exemplo de uso
biblioteca = Biblioteca()

while True:
    exibir_menu()
    escolha = input("Escolha a operação (0-6): ")

    if escolha == "0":
        print("Saindo do programa. Até mais!")
        break
    elif escolha == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano de publicação do livro: "))
        genero = input("Digite o gênero do livro: ")

        livro = Livro(titulo, autor, ano, genero)
        biblioteca.cadastrar_livro(livro)
        print("Livro cadastrado com sucesso!")
    elif escolha == "2":
        titulo = input("Digite o título do livro a ser consultado: ")
        biblioteca.consultar_livro(titulo)
    elif escolha == "3":
        autor = input("Digite o nome do autor para listar os livros: ")
        biblioteca.listar_livros_por_autor(autor)
    elif escolha == "4":
        genero = input("Digite o gênero para listar os livros: ")
        biblioteca.listar_livros_por_genero(genero)
    elif escolha == "5":
        nome_arquivo = input("Digite o nome do arquivo para salvar os dados: ")
        biblioteca.salvar_dados(nome_arquivo)
    elif escolha == "6":
        nome_arquivo = input("Digite o nome do arquivo para carregar os dados: ")
        biblioteca.carregar_dados(nome_arquivo)
    else:
        print("Escolha inválida. Tente novamente.")

