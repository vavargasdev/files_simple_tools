# Files Simple Tools
Coleção de ferramentas simples para executar tarefas rotineiras em arquivos e pastas.

***Necessário Python 3 instalado***

## search_file_folder.py
Classe para localizar rapidamente arquivos ou pastas localmente.

Você pode definir a extensão, pesquisar pastas ou arquivos, recursivamente ou apenas na raiz do diretório fornecido.


### Atributos:
- target_dir (str): O diretório onde a pesquisa será realizada.
- dir_or_file (str): 'dir' para pesquisar diretórios ou 'file' para arquivos.
- keyword (str): A palavra-chave a ser pesquisada dentro de nomes de arquivo/pasta.
- extension (str): A extensão de arquivo a ser filtrada (aplica-se somente ao pesquisar arquivos).
- recursive (bool): Se deve pesquisar recursivamente em subdiretórios.


### Exemplo de uso:
```
new_search = SearchFilesFolder("D:/ImageFiles", "file", "test", "jpg", True)
new_search.start()
```
Fará a busca na pasta D:/ImageFiles por arquivos de imagem jpg, tendo "test" no nome.
