import os
import shutil
import logging
import time
from os import access

from src.config import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)
logger=logging.getLogger(__name__)
def cat(now:str,sp:list[list[str]])->str:
    """ Функция получает список, состоящий из двух подсписков, где 1 список это сама команда и файл,
    а второй флаг(тут не нужен). Функция выполняет команду cat"""
    try:
        os.chdir(now)
        file = sp[0][1]
        file2=os.path.expanduser(file)
        file1=os.path.abspath(file2)
        if os.path.exists(file1):
            if os.path.isfile(file1):
                if os.access(file1,os.R_OK):
                    with open(file1, "r") as f:
                        return f.read()
                else:return "Недостаточно прав для чтения файла"
            else:
                return "Переданный вами параметр не является файлом"
        else: return "Неккоректно указан путь к файлу"
    except OSError as e:
        logging.error(f"Ошибка: {e}")
        return 'Что-то рухнуло всё, почему не знаю'
    except Exception as e:
        logging.error(f"Ошибка : {e}")
        return 'Что-то всё рухнуло, почему не знаю'

def mv(now:str,sp:list[list[str]])->str:
    """Функция получает на вход список, состоящий из двух подсписков, где первый содержит в себе саму функцию mv и файлы и каталоги,
    а во втором флаги(здесь не нужны). Функция выполняет команду mv"""
    try:
        os.chdir(now)
        file=sp[0][1]
        path=sp[0][2]
        file2=os.path.expanduser(file)
        path2=os.path.expanduser(path)
        file1=os.path.abspath(file2)
        path1=os.path.abspath(path2)
        if os.path.exists(file1):
            return shutil.move(file1,path1)
        else:"Неккоректно введён путь"
    except FileNotFoundError as e:
        logging.error(f"Ошибка: {e}")
        return 'И где вы это нашли?'
    except PermissionError as e:
        logging.error(f"Ошибка: {e}")
    except Exception as e:
        logging.error(f"Ошибка : {e}")
        return 'Что-то всё рухнуло, почему не знаю'


def cd(now:str,sp:list[list[str]])->str:
    """Функция получает на вхож список, состоящий из двух подсписков, где первый содержит в себе саму функцию mv и файлы и каталоги,
        а во втором флаги(здесь не нужны). Функция выполняет команду cd"""
    try:
        os.chdir(now)
        if len(sp[0])==1:
            return os.getcwd()
        else:
            path = sp[0][1]
            exp_path = os.path.expanduser(path)
            absolute_path = os.path.abspath(exp_path)
            if os.path.exists(absolute_path):
                if access(absolute_path,os.R_OK):
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
        logging.error(f"Ошибка: {e}")
        return 'Что-то рухнуло всё, почему не знаю'
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        return 'Что-то рухнуло всё, почему не знаю'


def ls(now:str,sp:list[list[str]])->str:
    """Функция получает на вход список, состоящий из двух подсписков, где первый содержит саму команду ls и пути к файлам/каталогам,
        а во втором флаги(-l). Функция выполняет команду ls"""
    try:
        os.chdir(now)
        if len(sp[1]) == 0:
            if len(sp[0]) == 1:
                a = os.listdir(os.getcwd())
                b = ''
                for i in a:
                    b += i + '\n'
                return b
            else:
                path = sp[0][1]
                path2 = os.path.expanduser(path)
                path1 = os.path.abspath(path2)
                if os.path.exists(path1):
                    if os.access(path1,os.R_OK):
                        a = os.listdir(path1)
                        b = ''
                        for i in a:
                            b += i + '\n'
                        return b
                    else:
                        return "Указан неверный путь"
                else:
                    return "Нет доступа к данному файлу/каталогу"
        else:
            if len(sp[1]) == 1 and sp[1][0] == '-l':
                if len(sp[0]) == 1:
                    a = os.listdir(os.getcwd())
                    b = ''
                    for i in a:
                        ctime = os.path.getctime(i)
                        size = os.path.getsize(i)
                        rights = os.stat(i).st_mode
                        b += f"{rights} {size:<6} {time.ctime(ctime)} {i}" + "\n"
                    return b
                if len(sp[0]) == 2:
                    path = sp[0][1]
                    path2 = os.path.expanduser(path)
                    path1 = os.path.abspath(path2)
                    if os.path.exists(path1):
                        if os.access(path1,os.R_OK):
                            a = os.listdir(path1)
                            b = ''
                            for i in a:
                                ctime = os.path.getctime(i)
                                size = os.path.getsize(i)
                                rights = os.stat(i).st_mode
                                b += f"{rights} {size:<6} {time.ctime(ctime)} {i}" + "\n"
                            return b
                        else: return "Нет доступа к данному файлу/каталогу"
                    else:
                        return "Указан неверный путь"
            else:
                return "Введён неверный флаг или он введён не один"
    except OSError as e:
        logging.error(f"Ошибка: {e}")
        return 'Что-то рухнуло всё, почему не знаю'
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        return 'Что-то рухнуло всё, почему не знаю'

def cp(now:str,sp:list[list[str]])->str:
    try:
        os.chdir(now)
        if len(sp[1])==0:
            file=sp[0][1]
            path=sp[0][2]
            file2=os.path.expanduser(file)
            path2=os.path.expanduser(path)
            file1= os.path.abspath(file2)
            path1=os.path.abspath(path2)
            if os.path.exists(file1) and os.path.exists(path1) and os.path.isfile(file1):
                if os.access(file1,os.R_OK) and os.access(path1,os.R_OK):
                    return shutil.copy(file1, path1)
                else:return "У вас нет доступа к данному файлу/каталогу"
            else:return "Неправильно указан путь или ваш файл не является файлом"
        elif len(sp[1])==1 and sp[1][0]=='-r':
            catalog=sp[0][1]
            path=sp[0][2]
            catalog2=os.path.expanduser(catalog)
            path2=os.path.expanduser(path)
            catalog1=os.path.abspath(catalog2)
            path1=os.path.abspath(path2)
            if os.path.exists(catalog1) and os.path.exists(path1):
                if os.access(catalog1,os.R_OK) and os.access(path1,os.R_OK):
                    if os.path.isdir(path1) and os.path.isdir(catalog1):
                        shutil.copytree(catalog1, path1)
                    else:
                        return "Проверьте что вы корректно ввели каталоги"
                else:
                    return "У вас нет доступа к данноум каталогу/каталогам"
            else:
                return "Указан неверный путь"
        else:
            return "Неверно введён флаг"
    except OSError as e:
        logging.error(f"Ошибка : {e}")
        return 'Что-то всё рухнуло, почему не знаю'
    except Exception as e:
        logging.error(f"Ошибка : {e}")
        return 'Что-то всё рухнуло, почему не знаю'
