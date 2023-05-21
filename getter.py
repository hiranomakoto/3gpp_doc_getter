import os
import time

from soup import Soup
from filer import Filer


# Rel16のファイルを取得する
baseurl = 'https://www.3gpp.org/ftp/Specs/2023-03/Rel-16/38_series'
savepath = os.path.join(os.pardir, 'docs', 'Rel-16', '38_series')
print('savepath : ', savepath)

# release = Soup(baseurl, 'series', None)
# links = release.get_links()
links = [baseurl]
for link in links:
    ts_series = Soup(link, 'zip', None)
    zip_links = ts_series.get_links()
    for zip_path in zip_links:
        file = Filer(zip_path, savepath)
        file.download_zip_file()
        print(file.unzip_file())
        # time.sleep(0.05)

