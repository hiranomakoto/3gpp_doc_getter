import os
import requests
import zipfile

class Filer(object):
    def __init__(self, url, save_path):
        self.url = url
        self.folder = save_path

    def download_zip_file(self):
        response = requests.get(self.url)
        zip_file_name = os.path.basename(self.url)
        zip_file_path = os.path.join(self.folder, zip_file_name)

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        with open(zip_file_path, 'wb') as f:
            f.write(response.content)

    def unzip_file(self):
        zip_file_name = os.path.basename(self.url)
        zip_file_path = os.path.join(self.folder, zip_file_name)

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(self.folder)

        os.remove(zip_file_path)

        return os.path.basename(zip_file_path)

if __name__ == '__main__':
    url = 'https://www.3gpp.org/ftp/Specs/2023-03/Rel-16/21_series/21900-g40.zip'
    file = Filer(url,'test')
    file.download_zip_file()
    file.unzip_file()
