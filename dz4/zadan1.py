import os

def rename(directory: str, name: str, digits: int, extension: str, out_extension: str,
           range_file_name: tuple[int, int]):


    files = os.listdir(directory)  # список названий файлов и папок в директории

    # for file in files:
    #     file_path = os.path.join(directory, file) # путь к файлу или папке
    #     if os.path.isfile(os.path.join(directory, file)): #проверка файл или папка (передаем путь к файлу)
    #         if os.path.splitext(file_path)[1] == extension:

    files = [file for file in files if os.path.isfile(os.path.join(directory, file)) and os.path.splitext(file)[
        1] == extension]  # список имен файлов

    for number, file in enumerate(files, 1):  # x, y = (1, 2)
        start, end = range_file_name
        new_file_name = os.path.splitext(file)[0][start - 1:end]  # формируем имя нового файла
        new_file_name += name
        new_file_name += f'{number:>0{digits}}'  # Формирование нужного номера файла
        new_file_name += out_extension
        file_path = os.path.join(directory, file)  # путь к файлу(изначальному)
        new_file_path = os.path.join(directory, new_file_name)
        os.rename(file_path, new_file_path)  # передаем старый путь к файлу и путь к нофому файлу(с новым именем)


rename('hw_seminar7/rename', 'test', 3, '.txt', '.py', (1, 3))