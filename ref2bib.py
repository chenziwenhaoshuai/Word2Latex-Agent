from get_bibtex.process_words_to_bibtex import process_words_to_bibtex


def ref2bib(words_path, result_bibtex_path='./result_bibtex.txt', result_cite_path='./result_cite.txt',done_path='./done.txt'):
    """
    Convert references in a text file to BibTeX format.

    :param words_path: Path to the text file containing references.
    """
    process_words_to_bibtex(words_path, result_bibtex_path=result_bibtex_path, result_cite_path=result_cite_path, done_path=done_path)
    print("BibTeX conversion completed. Results saved in 'result_bibtex.txt' and 'result_cite.txt'.")