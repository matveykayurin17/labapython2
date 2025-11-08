
import os

from src.functions import cat,cd,mv,ls,cp
import logging
from src.config import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)




def parse(cin: str) -> list[list[str]]:
    """В функцию подаётся строка введённая пользователем
    Функция возвращает список, состоящий из двух списков. Один для хранения команд и путей/файлов/каталогов,
    другой для хранения флагов"""
    args:list[list[str]] = [[], []]
    token = ''
    for i in range(len(cin)):
        if len(token)==0:
            if cin[i]!=' ':
                token+=cin[i]
        else:
            if token[0]=='"':
                token+=cin[i]
                if cin[i]=='"':
                    args[0].append(token[1:-1])
                    token=''
            elif token[0]=="'":
                    token += cin[i]
                    if cin[i] == "'":
                        args[0].append(token[1:-1])
                        token = ''
            else:
                if cin[i]!=' ':
                    token+=cin[i]
                else:
                    if token[0]=='-':
                        args[1].append(token)
                        token=''
                    else:
                        args[0].append(token)
                        token=''
    if len(token)>0:
        if token[0]=='-':
            args[1].append(token)
        else:
            args[0].append(token)
    args[1]=list(set(args[1]))
    for k in range(len(args[1])):
        flag=list(set(list(args[1][k])))
        str_flag='-'
        for p in flag:
            str_flag+=p if p!='-' else''
        args[1][k]=str_flag
    args[1] = list(set(args[1]))
    return args



def parse_1(cin:str)->None:
    """На вход подаётся строка, введённая пользователем
    Функция вызывает предыдущий парсес, определяет какая команда была выполнена и вызывает функцию самой команды"""
    try:
        args = parse(cin)
        if len(args[0])==2 and args[0][0]=='cat' and len(args[1])==0:
            res=cat(os.getcwd(),args)
            if res=="Переданный вами параметр не является файлом" or res=="Недостаточно прав для чтения файла" or res=="Неккоректно указан путь к файлу":
                logger.error(f"Команда:{cin}, результат:\n{res}")
            else:
                logger.info(f"Команда:{cin}, результат:\n{res}")
        elif (len(args[0])==2 or len(args[0])==1) and args[0][0]=='cd' and len(args[1])==0:
            res=cd(os.getcwd(),args)
            logger.info(f"Команда:{cin}, результат:\n{res}")
        elif len(args[0])==3 and args[0][0]=='mv' and len(args[1])==0:
            res=mv(os.getcwd(),args)
            logger.info(f"Команда:{cin}, результат:\n{res}")
        elif (len(args[0])==2 or len(args[0])==1) and args[0][0]=='ls':
            res=ls(os.getcwd(),args)
            logger.info(f"Команда:{cin}, результат:\n{res}")
        elif len(args[0])==3 and args[0][0]=="cp":
            res=cp(os.getcwd(),args)
            if res=="Неправильно указан путь или ваш файл не является файлом" or res=="У вас нет доступа к данному файлу/каталогу" or res=="Проверьте что вы корректно ввели каталоги" or res=="У вас нет доступа к данноум каталогу/каталогам" or res=="Указан неверный путь" or res=="Неверно введён флаг":
                logger.error(f"Команда:{cin}, результат:\n{res}")
            else:
                logger.info(f"Команда:{cin}, результат:\n{res}")
        else:
            res="Ваша команда введена неправильно или её не существует"
            logger.error(f"Команда:{cin}, результат:\n{res}")
    except OSError as e:
        print('Ошибка операционной системы')
        logger.error(f"Ошибка : {e}")
    except Exception as e:
        print('Непредвиденная ошибка')
        logger.error(f"Ошибка : {e}")
