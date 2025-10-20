"""
Leitor de .PDF, classificando as palavras mais comuns
"""

import re
from collections import Counter
from PyPDF2 import PdfReader


def extrair_texto_pdf(pdf_arquivo: str) -> list[str]:
    """
    Recebe um arquivo .pdf e retorna o texto contido no arquivo em uma lista
    Args:
        pdf_arquivo(str): caminho do arquivo .pdf a ser lido
    Returns:
        list[str]: lista com as palavras do arquivo .pdf
    """
    with open(pdf_arquivo, "rb") as pdf:
        reader = PdfReader(pdf, strict=False)

        print("Páginas", len(reader.pages))
        print("-" * 10)

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text


def contar_palavras(text_list: list[str]) -> Counter:
    """
    Conta a frequência das palavras presentes em uma lista
    Args:
        text_list(list[str]): lista com as palavras
    """
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r"\s+|[,;?!.-]\s*", text.lower())

        all_words += [word for word in split_text if word]

    return Counter(all_words)


def main():
    extracted_text: list[str] = extrair_texto_pdf("sample.pdf")
    counter: Counter = contar_palavras(text_list=extracted_text)

    for page in extracted_text:
        print(page)

    for word, mention in counter.most_common(10):
        print(f"{word:10}: {mention} vezes")


if __name__ == "__main__":
    main()
