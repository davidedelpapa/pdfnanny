def get_text(pdfReader):
    """ 
    Returns text extracted from the PDF.

    in:     pdfReader object
    out:    list of strings representing the text extracted from the PDF file
    """
    pdf_text = []
    pages = pdfReader.numPages
    for page in range(0, pages):
        pdf_text.append(pdfReader.getPage(page).extractText())
    return pdf_text


def tokenize(text):
    """ 
    Returns tokenized text, as list of lists.

    in:     pdfReader extracted text
    out:    list of list of strings representing the text
    """
    tokenized = []
    for page in text:
        page_list = []
        for sentence in page.split("\n"):
            page_list.append(sentence)
        tokenized.append(page_list)
    return tokenized
