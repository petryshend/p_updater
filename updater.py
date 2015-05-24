import wget, os.path, zipfile, glob, shutil, sys

EXTRACTED_FOLDER = 'extracted/'

def downloadZipRepo():
    url = 'https://github.com/petryshend/udacityfullstack/archive/master.zip'
    filename = wget.download(url)
    return filename        

def removeFiles():
    for f in glob.glob('*'):
        if f in ['updater.py', 'extracted', 'girls-conf']:
            continue
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)

ARCHIVE_NAME = 'udacityfullstack-master.zip'

if os.path.isfile(ARCHIVE_NAME):
    os.remove(ARCHIVE_NAME)

removeFiles()
filename = downloadZipRepo()
print filename + ' downloaded'

downloadedZip = zipfile.ZipFile(ARCHIVE_NAME)

downloadedZip.extractall(EXTRACTED_FOLDER)

repoFolder = os.path.splitext(ARCHIVE_NAME)[0]

for ent in glob.glob(EXTRACTED_FOLDER + repoFolder + '/*'):
    shutil.move(ent, '.')
