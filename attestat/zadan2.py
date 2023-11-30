# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
import argparse
import logging
import os
from collections import namedtuple
from pathlib import Path

logging.basicConfig(filename='hw.log',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='{asctime} {levelname} - {msg}',
                    style='{')
logger = logging.getLogger()

PathElements = namedtuple("PathElements", ['name', 'extension', 'directory', 'parent_dir'])

parser = argparse.ArgumentParser()
parser.add_argument('-p', type=str)
args = parser.parse_args()
path = Path(args.p)

path_elements_list = []
file_list = os.listdir(path)
for elem in file_list:
    temp_path = path / elem
    name = temp_path.stem
    suffix = temp_path.suffix or 'directory does not have extension'
    directory = temp_path.is_dir()
    parent_dir = temp_path.parent.stem
    logger.info(f"file/dir name: {name}, suffix: {suffix}, directory: {directory}, parent_dir: {parent_dir}")
    path_elements_list.append(PathElements(name, suffix, directory, parent_dir))

print(*path_elements_list, sep='\n')