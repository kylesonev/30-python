"""
Organiza arquivos dado um path
Utiliza a extensão dos arquivos existentes no path para criar diretórios baseados em suas extensões
"""

import os
import shutil


def criar_diretorio(path: str, extension: str) -> str:
    """
    Cria uma pasta que é nomeada baseada na extenção do arquivo que é passado
    Args:
        path(str): caminho onde será criado o diretório
        extension(str): extensão do arquivo para nomear diretório
    """
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def organizar_arquivos(source_path: str) -> None:
    """
    Organiza arquivos baseado no caminho dado
    Args:
        source_path(str): caminho de origem onde serão organizados os arquivos
    """

    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extension: str = os.path.splitext(filename)[1]

            if extension:
                target_folder: str = criar_diretorio(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)

                shutil.move(file_path, target_path)


def remover_diretorio_vazio(source_path: str) -> None:
    """
    Remove todos as pastas vazias
    Args:
        source_path(str): caminho de origem onde serão removidas as pastas vazias

    """

    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        for current_dir in sub_dir:
            folder_path: str = os.path.join(root_dir, current_dir)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)


def main():
    """
    Executa a lógica do programa
    1. Solicita ao usuário o path onde serão organizados os arquivos
    2. Verifica se o path existe
    3. Organiza os arquivos
    """
    user_input: str = input("Informe o path do arquivo para organizar: ")

    if os.path.exists(path=user_input):
        organizar_arquivos(user_input)
        remover_diretorio_vazio(user_input)
        print("Arquivos organizados")
    else:
        print("Caminho inválido!")


if __name__ == "__main__":
    main()
