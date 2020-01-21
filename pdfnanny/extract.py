def get_text(pdfReader):
    """ 
    Returns text extracted from the PDF.

    in:     pdfReader object
    out:    string representing the text extracted from the PDF file
    """
    pdf_text = ""
    pages = pdfReader.numPages
    for page in range(0, pages):
        pdf_text += pdfReader.getPage(page).extractText()
    return pdf_text
