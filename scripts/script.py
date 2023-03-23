from mdutils.mdutils import MdUtils
import json
from pathlib import Path
import os

""" Read json files. """
base_dir = Path(__file__).resolve().parent
def readDB(volume, session):
    filename = str(base_dir) + '/data/' + volume + '/' + session + '.json'
    with open(filename, mode="r", encoding='UTF-8') as jsonFile:
        data = json.load(jsonFile)
    return data

filepath = str(base_dir) + '/data/' + 'Protokolle_BV_14_1822'
filelist = os.listdir(filepath)

for file in filelist:
    data = readDB('Protokolle_BV_14_1822', file[:-5])
    content = ''
    for i in data["database"]["content"]:
        content = content + '<p>' + i + '</p>'
    mdFile = MdUtils(file_name=data["database"]["session"])
    mdFile.new_line('---')
    mdFile.new_line('schema: default')
    mdFile.new_line('title: '+ data["database"]["session"])
    mdFile.new_line('organization: Team Charlie')
    mdFile.new_line('notes: "' + content + '"') 
    mdFile.new_line('resources:')
    filepath_img = str(base_dir) + '/jkan/' + 'Protokolle_BV_14_1822/' + file[:-5]
    filelist_img = os.listdir(filepath_img)
    numdic = {}
    for v in filelist_img:
        right = v.index('[')
        numdic[v] = v[4:right]
    res = dict(sorted(numdic.items(), key=lambda item: int(item[1])))
    filelist_img = res.keys()
    for img in filelist_img:
        mdFile.new_line('- format: png')
        mdFile.new_line('  name: ' + img)
        mdFile.new_line('  url: ../../data_img/Protokolle_BV_14_1822/' + file[:-5] + '/' + img)
    mdFile.new_line('category: ')
    mdFile.new_line('  - ' + 'Protokolle_BV_14_1822')
    mdFile.new_line('maintainer: Frank Chen')
    mdFile.new_line('maintainer_email: t08zc21@abdn.ac.uk')
    mdFile.new_line('---')


    mdFile.create_md_file()

