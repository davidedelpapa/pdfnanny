import unittest
import PyPDF2
import os
from pdfnanny import extract


class TestExtract(unittest.TestCase):

    pdfFileObj = open('data/test.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    def test_get_text_output(self):
        #currentDirectory = os.getcwd()
        self.assertEqual(extract.get_text(
            self.pdfReader)[0:35], "Little Women  \n2 of 861 CHAPTER ONE")
        #self.assertEqual(currentDirectory, "Hello World!")
