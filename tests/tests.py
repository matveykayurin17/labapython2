import os
import unittest
from src.functions import cat,mv,cd,cp,ls,helper
from unittest.mock import patch,MagicMock
from src.parse import parse

class TestFunctions(unittest.TestCase):
    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('builtins.open')
    def test_cat(self,mock_open,mock_access,mock_isfile,mock_exists,mock_abspath,mock_expanduser,mock_chdir):
        mock_expanduser.return_value="file1"
        mock_abspath.return_value="folder_1/file_1"
        mock_exists.return_value=True
        mock_isfile.return_value=True
        mock_access.return_value=True
        mock_open.return_value=MagicMock()
        cat("folder_1",[["cat","file_1"],[]])
        mock_open.assert_called_once_with("folder_1/file_1","r")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('builtins.open')
    def test_cat1(self, mock_open, mock_access, mock_isfile, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.return_value = "file1"
        mock_abspath.return_value = "folder_1/file_1"
        mock_exists.return_value = False
        self.assertEqual(cat("folder_1", [["cat", "file_1"], []]),"Неккоректно указан путь к файлу")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('builtins.open')
    def test_cat2(self, mock_open, mock_access, mock_isfile, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.return_value = "file1"
        mock_abspath.return_value = "folder_1/file_1"
        mock_exists.return_value = True
        mock_isfile.return_value = False
        self.assertEqual(cat("folder_1", [["cat", "file_1"], []]), "Переданный вами параметр не является файлом")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('builtins.open')
    def test_cat3(self, mock_open, mock_access, mock_isfile, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.return_value = "file1"
        mock_abspath.return_value = "folder_1/file_1"
        mock_exists.return_value = True
        mock_isfile.return_value = True
        mock_access.return_value = False
        self.assertEqual(cat("folder_1", [["cat", "file_1"], []]), "Недостаточно прав для чтения файла")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('builtins.open')
    def test_cat4(self,mock_open,mock_access,mock_isfile,mock_exists,mock_abspath,mock_expanduser,mock_chdir):
        mock_expanduser.return_value="file1"
        mock_abspath.return_value="folder1/file_1"
        mock_exists.return_value=True
        mock_isfile.return_value=True
        mock_access.return_value=True
        mock_open.side_effect=OSError
        self.assertEqual(cat("folder1",[["cat","file_1"],[]]),'Ошибка операционной системы')

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('shutil.move')
    def test_mv(self,mock_move, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect=["file1","folder2"]
        mock_abspath.side_effect=["folder1/file1","folder1/folder2"]
        mock_exists.return_value = True
        mock_move.side_effect=PermissionError
        self.assertEqual(mv("folder1",[["mv","file1","folder2"],[]]),"Любопытной варваре на базаре на оторвали(недостаточно прав)")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('shutil.move')
    def test_mv1(self,mock_move,mock_exists,mock_abspath,mock_expanduser,mock_chdir):
        mock_expanduser.side_effect=["file1","folder2"]
        mock_abspath.side_effect=["folder1/file1","folder1/folder2"]
        mock_exists.return_value=True
        mv("folder1",[[mv,"file1","folder2"],[]])
        mock_move.assert_called_once_with("folder1/file1","folder1/folder2")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('shutil.move')
    def test_mv2(self,mock_move,mock_exists,mock_abspath,mock_expanduser,mock_chdir):
        mock_expanduser.side_effect = ["file1", "folder2"]
        mock_abspath.side_effect = ["folder1/file1", "folder1/folder2"]
        mock_exists.return_value = True
        self.assertEqual(mv("folder1",[["mv","file1","folder2"],[]]),"Ваш файл/каталог перемещён/переименован")
        mock_move.assert_called_once_with("folder1/file1", "folder1/folder2")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('shutil.move')
    def test_mv3(self,mock_move,mock_exists,mock_abspath,mock_expanduser,mock_chdir):
        mock_expanduser.side_effect = ["file1","folder2"]
        mock_abspath.side_effect = ["folder1/file1","folder1/folder2"]
        mock_exists.return_value = False
        self.assertEqual(mv("folder1",[["mv","file1","folder2"],[]]),"Неккоректно введён путь")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('shutil.move')
    def test_mv4(self,mock_move,mock_exists,mock_abspath,mock_expanduser,mock_chdir):
        mock_expanduser.side_effect=["file1","folder2"]
        mock_abspath.side_effect=["folder1/file1","folder1/folder2"]
        mock_exists.return_value=True
        mock_move.side_effect=FileNotFoundError
        self.assertEqual(mv("folder1",[["mv","file1","folder2"],[]]),'И где вы это нашли?')

    @patch('os.chdir')
    @patch('os.getcwd')
    def test_cd(self,mock_getcwd,mock_chdir):
        cd("folder1",[["cd"],[]])
        mock_getcwd.assert_called_once_with()

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('os.getcwd')
    def test_cd1(self,mock_getcwd,mock_isdir,mock_access,mock_exists,mock_abspath,mock_expanduser,mock_chdir):
        mock_expanduser.return_value="path1"
        mock_abspath.return_value="folder1/path1"
        mock_exists.return_value=True
        mock_access.return_value = True
        mock_isdir.return_value = True
        cd("folder1", [["cd","path1"], []])
        mock_getcwd.assert_called_once_with()

    @patch('os.chdir')
    @patch('os.getcwd')
    def test_cd2(self, mock_getcwd, mock_chdir):
        mock_getcwd.side_effect=OSError
        self.assertEqual(cd("folder1", [["cd"], []]),'Ошибка операционной системы')


    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('os.getcwd')
    def test_cd4(self, mock_getcwd, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.return_value = "path1"
        mock_abspath.return_value = "folder1/path1"
        mock_exists.return_value = False
        self.assertEqual(cd("folder1", [["cd", "path1"], []]),"Неверно указан путь")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('os.getcwd')
    def test_cd5(self, mock_getcwd, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.return_value = "path1"
        mock_abspath.return_value = "folder1/path1"
        mock_exists.return_value = True
        mock_access.return_value = False
        self.assertEqual(cd("folder1", [["cd", "path1"], []]), "Нету прав доступа")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('os.getcwd')
    def test_cd6(self, mock_getcwd, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.return_value = "path1"
        mock_abspath.return_value = "folder1/path1"
        mock_exists.return_value = True
        mock_access.return_value = True
        mock_isdir.return_value = False
        self.assertEqual(cd("folder1", [["cd", "path1"], []]), "Каталог указан не верно")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('os.getcwd')
    def test_cd7(self, mock_getcwd, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.return_value = "path1"
        mock_abspath.return_value = "folder1/path1"
        mock_exists.return_value = True
        mock_access.return_value = True
        mock_isdir.return_value = True
        mock_getcwd.side_effect = OSError
        self.assertEqual(cd("folder1", [["cd", "path1"], []]), 'Ошибка операционной системы')

    @patch('os.chdir')
    @patch('os.listdir')
    @patch('os.getcwd')
    @patch('os.path.getctime')
    @patch('os.path.getsize')
    @patch('os.stat')
    def test_ls(self, mock_stat, mock_getsize, mock_getctime, mock_getcwd, mock_listdir, mock_chdir):
        self.assertEqual(ls("folder1", [["ls"], ["-l", "-p"]]), "Вы неккоректно ввели флаг/ввели неккоректный флаг")

    @patch('os.chdir')
    @patch('os.listdir')
    @patch('os.getcwd')
    @patch('os.path.getctime')
    @patch('os.path.getsize')
    @patch('os.stat')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    def test_ls1(self, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_stat, mock_getsize, mock_getctime,
                 mock_getcwd, mock_listdir, mock_chdir):
        mock_expanduser.return_value = 'path1'
        mock_abspath.return_value = "folder1/path1"
        mock_exists.return_value = True
        mock_access.return_value = True
        self.assertEqual(ls("folder1", [["ls", "path1"], ["-l", "-p"]]), "Неккоректно введён флаг")

    @patch('os.chdir')
    @patch('os.listdir')
    @patch('os.getcwd')
    @patch('os.path.getctime')
    @patch('os.path.getsize')
    @patch('os.stat')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    def test_ls2(self, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_stat, mock_getsize, mock_getctime,
                 mock_getcwd, mock_listdir, mock_chdir):
        mock_expanduser.return_value = 'path1'
        mock_abspath.return_value = "folder1/path1"
        mock_exists.return_value = True
        mock_access.return_value = False
        self.assertEqual(ls("folder1", [["ls", "path1"], ["-l"]]), "Нет доступа к данному файлу/каталогу")

    @patch('os.chdir')
    @patch('os.listdir')
    @patch('os.getcwd')
    @patch('os.path.getctime')
    @patch('os.path.getsize')
    @patch('os.stat')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    def test_ls3(self, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_stat, mock_getsize, mock_getctime,
                 mock_getcwd, mock_listdir, mock_chdir):
        mock_expanduser.return_value = 'path1'
        mock_abspath.return_value = "folder1/path1"
        mock_exists.return_value = False
        self.assertEqual(ls("folder1", [["ls", "path1"], ["-l"]]), "Указан неверный путь")

    @patch('os.chdir')
    @patch('os.listdir')
    @patch('os.getcwd')
    @patch('os.path.getctime')
    @patch('os.path.getsize')
    @patch('os.stat')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    def test_ls4(self, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_stat, mock_getsize, mock_getctime,
                 mock_getcwd, mock_listdir, mock_chdir):
        mock_expanduser.return_value = 'path1'
        mock_abspath.return_value = "folder1/path1"
        mock_exists.return_value = True
        mock_access.return_value = True
        mock_listdir.side_effect = OSError
        self.assertEqual(ls("folder1", [["ls", "path1"], ["-l"]]), 'Ошибка операционной системы')

    @patch('os.chdir')
    @patch('os.listdir')
    @patch('os.getcwd')
    @patch('os.path.getctime')
    @patch('os.path.getsize')
    @patch('os.stat')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    def test_ls5(self, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_stat, mock_getsize, mock_getctime,
                 mock_getcwd, mock_listdir, mock_chdir):
        mock_expanduser.return_value = 'path1'
        mock_abspath.return_value = "folder1/path1"
        mock_exists.return_value = True
        mock_access.return_value = True
        mock_getsize.return_value = 4096
        mock_listdir.return_value = ["file1", "dir1"]
        ls("folder1", [["ls", "path1"], ["-l"]])

    @patch('os.chdir')
    @patch('os.listdir')
    @patch('os.getcwd')
    @patch('os.path.getctime')
    @patch('os.path.getsize')
    @patch('os.stat')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    def test_ls6(self, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_stat, mock_getsize, mock_getctime,
                 mock_getcwd, mock_listdir, mock_chdir):
        mock_expanduser.return_value = 'path1'
        mock_abspath.return_value = "folder1/path1"
        mock_exists.return_value = True
        mock_access.return_value = True
        mock_listdir.return_value = ["file1", "dir1"]
        ls("folder1", [["ls", "path1"], []])

    @patch('os.chdir')
    @patch('os.listdir')
    @patch('os.getcwd')
    @patch('os.path.getctime')
    @patch('os.path.getsize')
    @patch('os.stat')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    def test_ls7(self, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_stat, mock_getsize, mock_getctime,
                 mock_getcwd, mock_listdir, mock_chdir):
        mock_expanduser.return_value = 'path1'
        mock_abspath.return_value = "folder1/path1"
        mock_exists.return_value = True
        mock_access.return_value = True
        mock_listdir.return_value = ["file1", "dir1"]
        ls("folder1", [["ls"], []])

    @patch('os.chdir')
    @patch('os.listdir')
    @patch('os.getcwd')
    @patch('os.path.getctime')
    @patch('os.path.getsize')
    @patch('os.stat')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    def test_ls8(self, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_stat, mock_getsize, mock_getctime,
                 mock_getcwd, mock_listdir, mock_chdir):
        mock_expanduser.return_value = 'path1'
        mock_abspath.return_value = "folder1/path1"
        mock_exists.return_value = True
        mock_access.return_value = True
        mock_getsize.return_value = 4096
        mock_listdir.return_value = ["file1", "dir1"]
        ls("folder1", [["ls"], ["-l"]])

    def test_parse(self):
        self.assertEqual(parse("cat main.py"),[["cat","main.py"],[]])
    def test_parse1(self):
        self.assertEqual(parse("ls -l"),[["ls"],["-l"]])
    def test_parse2(self):
        self.assertEqual(parse("ls -l /Users/macbookair13/Desktop/labapython2/labapython2/src"),[["ls","/Users/macbookair13/Desktop/labapython2/labapython2/src"],["-l"]])

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('shutil.copy')
    def test_cp(self,mock_copy,moke_access,mock_isfile,mock_exists,mock_abspath,mock_expanduser,mock_chdir):
        mock_expanduser.side_effect=["file1","path1"]
        mock_abspath.side_effect=["folder1/file1","folder1/path1"]
        mock_exists.side_effect=[True,True]
        mock_isfile.return_value=True
        moke_access.side_effect=[True,True]
        cp("folder1",[["cp","file1","path1"],[]])
        mock_copy.assert_called_once_with("folder1/file1","folder1/path1")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('shutil.copy')
    def test_cp1(self,mock_copy,moke_access,mock_isfile,mock_exists,mock_abspath,mock_expanduser,mock_chdir):
        mock_expanduser.side_effect=["file1","path1"]
        mock_abspath.side_effect=["folder1/file1","folder1/path1"]
        mock_exists.side_effect=[False,True]
        self.assertEqual(cp("folder1",[["cp","file1","path1"],[]]),"Неправильно указан путь или ваш файл не является файлом")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('shutil.copy')
    def test_cp2(self, mock_copy, moke_access, mock_isfile, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["file1", "path1"]
        mock_abspath.side_effect = ["folder1/file1", "folder1/path1"]
        mock_exists.side_effect = [True, False]
        self.assertEqual(cp("folder1", [["cp", "file1", "path1"], []]),"Неправильно указан путь или ваш файл не является файлом")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('shutil.copy')
    def test_cp3(self, mock_copy, moke_access, mock_isfile, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["file1", "path1"]
        mock_abspath.side_effect = ["folder1/file1", "folder1/path1"]
        mock_exists.side_effect = [False, False]
        self.assertEqual(cp("folder1", [["cp", "file1", "path1"], []]),"Неправильно указан путь или ваш файл не является файлом")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('shutil.copy')
    def test_cp4(self, mock_copy, moke_access, mock_isfile, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["file1", "path1"]
        mock_abspath.side_effect = ["folder1/file1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_isfile.return_value = False
        self.assertEqual(cp("folder1", [["cp", "file1", "path1"], []]),"Неправильно указан путь или ваш файл не является файлом")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('shutil.copy')
    def test_cp5(self,mock_copy,moke_access,mock_isfile,mock_exists,mock_abspath,mock_expanduser,mock_chdir):
        mock_expanduser.side_effect=["file1","path1"]
        mock_abspath.side_effect=["folder1/file1","folder1/path1"]
        mock_exists.side_effect=[True,True]
        mock_isfile.return_value=True
        moke_access.side_effect=[False,True]
        self.assertEqual(cp("folder1", [["cp", "file1", "path1"], []]),"У вас нет доступа к данному файлу/каталогу")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('shutil.copy')
    def test_cp6(self, mock_copy, moke_access, mock_isfile, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["file1", "path1"]
        mock_abspath.side_effect = ["folder1/file1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_isfile.return_value = True
        moke_access.side_effect = [True, False]
        self.assertEqual(cp("folder1", [["cp", "file1", "path1"], []]), "У вас нет доступа к данному файлу/каталогу")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('shutil.copy')
    def test_cp7(self, mock_copy, moke_access, mock_isfile, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["file1", "path1"]
        mock_abspath.side_effect = ["folder1/file1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_isfile.return_value = True
        moke_access.side_effect = [False, False]
        self.assertEqual(cp("folder1", [["cp", "file1", "path1"], []]), "У вас нет доступа к данному файлу/каталогу")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('shutil.copy')
    def test_cp8(self, mock_copy, moke_access, mock_isfile, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["file1", "path1"]
        mock_abspath.side_effect = ["folder1/file1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_isfile.return_value = True
        moke_access.side_effect = [True, True]
        self.assertEqual(cp("folder1", [["cp", "file1", "path1"], []]), "Ваш файл скопирован")
        mock_copy.assert_called_once_with("folder1/file1", "folder1/path1")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('shutil.copytree')
    def test_cp9(self,mock_copytree,mock_isdir,mock_access,mock_exists,mock_abspath,mock_expanduser,mock_chdir):
        mock_expanduser.side_effect=["catalog1","path1"]
        mock_abspath.side_effect=["folder1/catalog1","folder1/path1"]
        mock_exists.side_effect=[True,True]
        mock_access.side_effect=[True,True]
        mock_isdir.side_effect=[True,True]
        cp("folder1",[["cp","catalog1","path1"],["-r"]])
        mock_copytree.assert_called_once_with("folder1/catalog1","folder1/path1")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('shutil.copytree')
    def test_cp10(self, mock_copytree, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["catalog1", "path1"]
        mock_abspath.side_effect = ["folder1/catalog1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_access.side_effect = [True, True]
        mock_isdir.side_effect = [True, True]
        self.assertEqual(cp("folder1", [["cp", "catalog1", "path1"], ["-r"]]),'Ваш каталог скопирован')
        mock_copytree.assert_called_once_with("folder1/catalog1", "folder1/path1")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('shutil.copytree')
    def test_cp11(self, mock_copytree, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["catalog1", "path1"]
        mock_abspath.side_effect = ["folder1/catalog1", "folder1/path1"]
        mock_exists.side_effect = [False, True]
        self.assertEqual(cp("folder1", [["cp", "catalog1", "path1"], ["-r"]]), "Указан неверный путь")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('shutil.copytree')
    def test_cp12(self, mock_copytree, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["catalog1", "path1"]
        mock_abspath.side_effect = ["folder1/catalog1", "folder1/path1"]
        mock_exists.side_effect = [True,False]
        self.assertEqual(cp("folder1", [["cp", "catalog1", "path1"], ["-r"]]), "Указан неверный путь")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('shutil.copytree')
    def test_cp13(self, mock_copytree, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["catalog1", "path1"]
        mock_abspath.side_effect = ["folder1/catalog1", "folder1/path1"]
        mock_exists.side_effect = [False, False]
        self.assertEqual(cp("folder1", [["cp", "catalog1", "path1"], ["-r"]]), "Указан неверный путь")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('shutil.copytree')
    def test_cp14(self, mock_copytree, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["catalog1", "path1"]
        mock_abspath.side_effect = ["folder1/catalog1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_access.side_effect = [False,True]
        self.assertEqual(cp("folder1", [["cp", "catalog1", "path1"], ["-r"]]), "У вас нет доступа к данному(ым) каталогу/каталогам")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('shutil.copytree')
    def test_cp15(self, mock_copytree, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["catalog1", "path1"]
        mock_abspath.side_effect = ["folder1/catalog1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_access.side_effect = [True, False]
        self.assertEqual(cp("folder1", [["cp", "catalog1", "path1"], ["-r"]]),"У вас нет доступа к данному(ым) каталогу/каталогам")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('shutil.copytree')
    def test_cp16(self, mock_copytree, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["catalog1", "path1"]
        mock_abspath.side_effect = ["folder1/catalog1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_access.side_effect = [False, False]
        self.assertEqual(cp("folder1", [["cp", "catalog1", "path1"], ["-r"]]),"У вас нет доступа к данному(ым) каталогу/каталогам")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('shutil.copytree')
    def test_cp17(self, mock_copytree, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["catalog1", "path1"]
        mock_abspath.side_effect = ["folder1/catalog1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_access.side_effect = [True, True]
        mock_isdir.side_effect=[False,True]
        self.assertEqual(cp("folder1", [["cp", "catalog1", "path1"], ["-r"]]),"Проверьте что вы корректно ввели каталоги")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('shutil.copytree')
    def test_cp18(self, mock_copytree, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["catalog1", "path1"]
        mock_abspath.side_effect = ["folder1/catalog1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_access.side_effect = [True, True]
        mock_isdir.side_effect = [True, False]
        self.assertEqual(cp("folder1", [["cp", "catalog1", "path1"], ["-r"]]),"Проверьте что вы корректно ввели каталоги")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('shutil.copytree')
    def test_cp19(self, mock_copytree, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["catalog1", "path1"]
        mock_abspath.side_effect = ["folder1/catalog1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_access.side_effect = [True, True]
        mock_isdir.side_effect = [False, False]
        self.assertEqual(cp("folder1", [["cp", "catalog1", "path1"], ["-r"]]),"Проверьте что вы корректно ввели каталоги")

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.path.isfile')
    @patch('os.access')
    @patch('shutil.copy')
    def test_cp20(self, mock_copy, moke_access, mock_isfile, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["file1", "path1"]
        mock_abspath.side_effect = ["folder1/file1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_isfile.return_value = True
        moke_access.side_effect = [True, True]
        mock_copy.side_effect=OSError
        self.assertEqual(cp("folder1", [["cp", "file1", "path1"], []]),'Ошибка операционной системы')

    @patch('os.chdir')
    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    @patch('os.path.exists')
    @patch('os.access')
    @patch('os.path.isdir')
    @patch('shutil.copytree')
    def test_cp21(self, mock_copytree, mock_isdir, mock_access, mock_exists, mock_abspath, mock_expanduser, mock_chdir):
        mock_expanduser.side_effect = ["catalog1", "path1"]
        mock_abspath.side_effect = ["folder1/catalog1", "folder1/path1"]
        mock_exists.side_effect = [True, True]
        mock_access.side_effect = [True, True]
        mock_isdir.side_effect = [True, True]
        mock_copytree.side_effect = OSError
        self.assertEqual(cp("folder1", [["cp", "catalog1", "path1"], ["-r"]]), 'Ошибка операционной системы')

    @patch('os.path.expanduser')
    @patch('os.path.abspath')
    def test_helper(self,mock_abspath,mock_expanduser):
        mock_expanduser.return_value="file1"
        mock_abspath.return_value="folder1/file1"
        self.assertEqual(helper("file1"),"folder1/file1")




