import wx
import os
import re

def main_func(path):
    file_name = path
    with open(os.path.join(os.getcwd(), file_name), 'r') as f:
        lines: list = f.readlines()

    found: list = []
    for i, line in enumerate(lines):
        elem: list = re.findall(r'\(\d{3}\)\d{3}\-?\d{2}\-?\d{2}', line), i + 1
        if elem: found.append(elem)
    res = []
    for elem, i in found:
        for x in elem:
            res.append(f'Строка {i}, позиция {lines[i - 1].find(x)} : найдено {x}')
    return res


def print_to_lb(list_, list_box):
    for item in list_:
        list_box.Append(item)


def check_log_file(app):
    if not os.path.isfile('./script18.log'):
        dlg = wx.MessageBox('Файл лога не найден. Файл будет создан автоматически', 'Внимание!', \
                            wx.OK | wx.ICON_EXCLAMATION, app)
        with open('./script18.log', 'w') as f:
            print('File Created')


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        vbox = wx.BoxSizer()
        self.list_box = wx.ListBox(self, wx.ID_ANY, style=wx.LB_SINGLE)
        vbox.Add(self.list_box, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(vbox)


class MyMenu(wx.MenuBar):
    def __init__(self):
        super().__init__()

        file_menu = wx.Menu()
        log_menu = wx.Menu()

        open_b = file_menu.Append(wx.ID_ANY, 'Открыть\tCtrl+O')
        export_b = log_menu.Append(wx.ID_ANY, 'Экспорт\tCtrl+E')
        add_b = log_menu.Append(wx.ID_ANY, 'Добавить в лог\tCtrl+A')
        look_b = log_menu.Append(wx.ID_ANY, 'Просмотр\tCtrl+S')

        self.Append(file_menu, 'Файл')
        self.Append(log_menu, 'Лог')

        self.Bind(wx.EVT_MENU, self.open_file, open_b)
        self.Bind(wx.EVT_MENU, self.add_to_log, add_b)
        self.Bind(wx.EVT_MENU, self.export_to_file, export_b)
        self.Bind(wx.EVT_MENU, self.look_log, look_b)

    def look_log(self, e):
        dlg = wx.MessageDialog(frame, 'Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!', \
                               'Внимание!', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_EXCLAMATION)
        res = dlg.ShowModal()
        if res == wx.ID_YES:
            frame.panel.list_box.Clear()
            with open('./script18.log', 'r') as f:
                lines = f.readlines()
            for line in lines:
                frame.panel.list_box.Append(line[:len(line) - 1])
        frame.status_bar.SetStatusText('Открыт лог')
        if res == wx.ID_NO:
            return 'NO'

    def add_to_log(self, e):
        with open('./script18.log', 'a') as f:
            for line in frame.panel.list_box.GetStrings():
                f.write(f'{line}\n')

    def open_file(self, e):
        with wx.FileDialog(self, 'Открыть файл…', style=wx.FD_OPEN) as fd:
            if fd.ShowModal() == wx.ID_CANCEL:
                return 'cancel'
            path_name = fd.GetPath()
            text = main_func(path_name)
            frame.panel.list_box.Clear()
            print_to_lb(text, frame.panel.list_box)
            frame.status_bar.SetStatusText(f'Обработан файл {os.path.basename(path_name)}')
            frame.status_bar.SetStatusText('{0:,} байт'.format(os.path.getsize(path_name)).replace(',', ' '), 1)

    def export_to_file(self, e):
        with wx.FileDialog(self, 'Экспорт в…', style=wx.FD_OPEN) as fd:
            if fd.ShowModal() == wx.ID_CANCEL:
                return 'cancel'
            path_name = fd.GetPath()
            with open(path_name, 'w') as f:
                for line in frame.panel.list_box.GetStrings():
                    f.write(f'{line}\n')


class MyFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super().__init__(parent, size=size, title=title)

        menubar = MyMenu()
        self.SetMenuBar(menubar)

        self.panel = MyPanel(self)

        self.status_bar = self.CreateStatusBar(2)
        self.status_bar.SetStatusWidths([-6, -4])

        self.Show()
        check_log_file(self)


app = wx.App()
frame = MyFrame(None, 'Искатель строк', size=(600, 400))
app.MainLoop()