def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write('\nTeXTO')
    arquivo.close()


def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()
    if __name__ == '__main__':
        escrever_arquivo('primeira linha.\n')
        # atualizar_arquivo('Terceira linha.\n')
