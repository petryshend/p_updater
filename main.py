import wget
import os.path


def downloadZipRepo():
    url = 'https://github.com/petryshend/udacityfullstack/archive/master.zip'
    filename = wget.download(url)
    return filename        

ARCHIVE_NAME = 'udacityfullstack-master.zip'

if os.path.isfile(ARCHIVE_NAME):
    os.remove(ARCHIVE_NAME)

filename = downloadZipRepo()
print filename + ' downloaded'
