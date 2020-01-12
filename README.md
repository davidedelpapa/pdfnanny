# PDFNanny

pdf2mp3 using gTTS

## Versions

The first commit was unsuccessful. The package `pdftotext` was unable to reliably extract text from the pdf page in _test/_. Got to find some other package.

From the second commit, we changed the tet extraction library, using `PyPDF2`: things are starting to work.

### TODO

This for now is a **proof of concept**. This is what I wish to have in the next releases:

- TOC extraction, so to divide the audio in multiple mp3's. A failback system when TOC extractions fails. Considering also not to fill up allotted shares for gTTS
- autodetecting text language, prior to passing it to gTTS
