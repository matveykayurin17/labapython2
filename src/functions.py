import os
import shutil
import time


import logging
from src.config import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

def cat(now:str,sp:list[list[str]])->str:
    """ Функция получает список, состоящий из двух подсписков, где 1 список содержит в себе команду и файл,
    а второй флаг(тут не нужен). Функция выполняет команду cat"""
    try:
        os.chdir(now)
        file = sp[0][1]
        file1=helper(file)
        if os.path.exists(file1):
            if os.path.isfile(file1):
                if os.access(file1,os.R_OK):
                    with open(file1, "r") as f:
                        return f.read()
                else:
                    return "Недостаточно прав для чтения файла"
            else:
                return "Переданный вами параметр не является файлом"
        else:
            return "Неккоректно указан путь к файлу"
    except OSError as e:
        logger.error(f"Ошибка: {e}")
        return 'Ошибка операционной системы'


def mv(now:str,sp:list[list[str]])->str:
    """ Функция получает список, состоящий из двух подсписков, где 1 список содержит в себе команду и два файла,
    а второй флаг(тут не нужен). Функция выполняет команду mv"""
    try:
        os.chdir(now)
        file=sp[0][1]
        path=sp[0][2]
        file1=helper(file)
        path1=helper(path)
        if os.path.exists(file1):
            shutil.move(file1,path1)
            return "Ваш файл/каталог перемещён/переименован"
        else:
            return "Неккоректно введён путь"
    except FileNotFoundError as e:
        logger.error(f"Ошибка: {e}")
        return 'И где вы это нашли?'
    except PermissionError as e:
        logger.error(f"Ошибка: {e}")
        return "Любопытной варваре на базаре на оторвали(недостаточно прав)"
    except OSError as e:
        logger.error(f"Ошибка: {e}")
        return 'Ошибка операционной системы'




def cd(now:str,sp:list[list[str]])->str:
    """ Функция получает список, состоящий из двух подсписков, где 1 список содержит в себе команду и директорию,
    а второй флаг(тут не нужен). Функция выполняет команду cd"""
    try:
        if len(sp[0])==1:
            os.chdir(now)
            return os.getcwd()
        else:
            os.chdir(now)
            path = sp[0][1]
            absolute_path = helper(path)
            if os.path.exists(absolute_path):
                if os.access(absolute_path,os.R_OK):
                    if os.path.isdir(absolute_path):
                        os.chdir(absolute_path)
                        return os.getcwd()
                    else:
                        return "Каталог указан не верно"
                else:
                    return "Нету прав доступа"
            else:
                return "Неверно указан путь"
    except OSError as e:
        logger.error(f"Ошибка: {e}")
        return 'Ошибка операционной системы'



def ls(now:str,sp:list[list[str]])->str:
    """ Функция получает список, состоящий из двух подсписков, где 1 список содержит в себе команду и пути,
    а второй флаги. Функция выполняет команду ls"""
    try:
        os.chdir(now)
        if len(sp[0]) == 1:
            a = os.listdir(os.getcwd())
            b = ''
            if len(sp[1]) == 0:
                for i in a:
                    b += i + '\n'
                return b
            elif len(sp[1])==1 and sp[1][0]=="-l":
                for i in a:
                    ctime = os.path.getctime(i)
                    size = os.path.getsize(i)
                    rights = os.stat(i).st_mode
                    b += f"{rights} {size:<6} {time.ctime(ctime)} {i}" + "\n"
                return b
            else:
                return "Вы неккоректно ввели флаг/ввели неккоректный флаг"
        else:
            path = sp[0][1]
            path1 = helper(path)
            if os.path.exists(path1):
                if os.access(path1, os.R_OK):
                    a = os.listdir(path1)
                    b = ''
                    if len(sp[1])==0:
                        for i in a:
                            b += i + '\n'
                        return b
                    elif len(sp[1])==1 and sp[1][0]=="-l":
                        for i in a:
                            ctime = os.path.getctime(i)
                            size = os.path.getsize(i)
                            rights = os.stat(i).st_mode
                            b += f"{rights} {size:<6} {time.ctime(ctime)} {i}" + "\n"
                        return b
                    else:
                        return "Неккоректно введён флаг"
                else:
                    return "Нет доступа к данному файлу/каталогу"
            else:
                return "Указан неверный путь"
    except OSError as e:
        logger.error(f"Ошибка: {e}")
        return 'Ошибка операционной системы'

def cp(now:str,sp:list[list[str]])->str:
    """ Функция получает список, состоящий из двух подсписков, где 1 список содержит в себе команду и файлы/каталоги,
        а второй флаги. Функция выполняет команду cp"""
    try:
        os.chdir(now)
        file = sp[0][1]
        path = sp[0][2]
        file1 = helper(file)
        path1 = helper(path)
        if len(sp[1])==0:
            if os.path.exists(file1) and os.path.exists(path1) and os.path.isfile(file1):
                if os.access(file1, os.R_OK) and os.access(path1, os.R_OK):
                    shutil.copy(file1, path1)
                    return "Ваш файл скопирован"
                else:
                    return "У вас нет доступа к данному файлу/каталогу"
            else:
                return "Неправильно указан путь или ваш файл не является файлом"
        elif len(sp[1])==1 and sp[1][0]=='-r':
            if os.path.exists(file1) and os.path.exists(path1):
                if os.access(file1,os.R_OK) and os.access(path1,os.R_OK):
                    if os.path.isdir(path1) and os.path.isdir(file1):
                        shutil.copytree(file1, path1)
                        return 'Ваш каталог скопирован'
                    else:
                        return "Проверьте что вы корректно ввели каталоги"
                else:
                    return "У вас нет доступа к данному(ым) каталогу/каталогам"
            else:
                return "Указан неверный путь"
        else:
            return "Неверно введён флаг"
    except OSError as e:
        logger.error(f"Ошибка: {e}")
        return 'Ошибка операционной системы'


def helper(path1):
    path2=os.path.expanduser(path1)
    path=os.path.abspath(path2)
    return path
