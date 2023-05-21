# 参考URL https://cduck.tech/2022/02/python-doc-to-docx/

import os
import time
import win32com.client

class Converter(object):
    def convert(self, docfile, docxfile):

        WordApp = win32com.client.Dispatch("Word.Application") # "Word.Application"を引数にすることでWordのインスタンスを作成します。 
        WordApp.Visible = 0 # Visibleが1 or Trueの場合、Wordが立ち上がります。0にすることでバックグラウンドで実行可能に
        WordApp.DisplayAlerts = 0 # DisplayAlerts も上記と同様アラートを表示させないように。

        doc = WordApp.Documents.Open(str(docfile))
        time.sleep(3)
        # doc.SaveAs(str(docxfile), 17, False, "", True, "", False, False, False, False) # １番目の引数に新しいファイルのパスを指定
        doc.SaveAs(str(docxfile), FileFormat=17) #17=PDF

if __name__ == '__main__':

    import glob
    import multiprocessing

    cwd = os.getcwd()

    docfiledir = os.path.join(cwd, '..', 'docs', 'Rel-16', '38_series')
    target_dir = os.path.join(cwd, '..', 'docs', 'convert')
    file_extension = ".doc"

    files = glob.glob(os.path.join(docfiledir, "*" + file_extension + "*"))

    for docfile in files:
        pdffile = os.path.join(target_dir, os.path.splitext(os.path.basename(docfile))[0] + ".pdf")
        print(docfile, pdffile)
        converter = Converter()
        converter.convert(docfile, pdffile)





#ネットから拾っていろいろ施行

"""
正攻法でdocxを使ったが、word形式ではないといわれた
from docx import Document
import docx2txt

def convert_doc_to_docx(filename, target_dir):
    doc = Document(filename)
    docx_filename = os.path.join(target_dir, os.path.splitext(os.path.basename(filename))[0] + ".docx")
    doc.save(docx_filename)
    return docx_filename

# docxfile = convert_doc_to_docx(docfile, target_dir)

"""

"""
asposeを使った場合
import aspose.words as aw

doc = aw.Document(docfile)
docx_filename = os.path.join(target_dir, os.path.splitext(os.path.basename(docfile))[0] + ".docx")
doc.save(docx_filename)
print(type(doc))
"""

