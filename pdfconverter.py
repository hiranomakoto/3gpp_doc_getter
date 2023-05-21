import PyPDF2

class PDFConverter:
    @staticmethod
    def convert_pdf_to_text(input_file, output_file):
        # PDFファイルを開く
        with open(input_file, 'rb') as file:
            # PyPDF2のPdfFileReaderを使用してPDFを読み込む
            pdf_reader = PyPDF2.PdfReader(file)

            # ページ数を取得
            num_pages = len(pdf_reader.pages)

            # 全ページのテキストを格納する変数
            text = ''

            # 各ページに対してテキストを抽出
            for page_number in range(num_pages):
                # ページを取得
                page = pdf_reader.pages[page_number]

                # ページのテキストを抽出してtextに追加
                text += page.extract_text()

        # テキストファイルに結果を書き込む
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(text)

        # 処理完了メッセージを表示
        print('テキストファイルの作成が完了しました。')

if __name__ == '__main__':
    import os

    cwd = os.getcwd()
    target_filename = '38300-gc0.pdf'
    pdffile = os.path.join(cwd, '..', 'docs', 'convert', target_filename)
    outputfile = os.path.join(cwd, '..', 'docs', 'convert', os.path.splitext(target_filename)[0] + ".txt")

    PDFConverter.convert_pdf_to_text(pdffile, outputfile)
