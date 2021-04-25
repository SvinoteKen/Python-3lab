import wx
from Formatter import StringFormatter

class StringFrame(wx.Frame):
    ''' Класс окна работы со строками '''

    def __init__(self):
        wx.Frame.__init__(
            self, None, -1, "Обработка строк", size=(400, 320))

        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, "Строка:", pos=(5, 20))
        self.entry_text = wx.TextCtrl(
            panel, -1, "", size=(300, -1), pos=(70, 20))
        self.res_text = wx.StaticText(panel, -1, "Результат:", pos=(5, 230))
        self.result_text = wx.TextCtrl(
            panel, -1, "", size=(300, -1), pos=(70, 230))

        self.len_sc = wx.SpinCtrl(panel, -1, "", (295, 55), (40, -1), min=1, max=20)

        self.dell_less_cb = wx.CheckBox(panel, -1, "Удалить слова размером меньше",(70, 60), (210, 20))
        self.count_dell = wx.StaticText(panel, -1, "букв", pos=(340, 62))
        self.convert_cb = wx.CheckBox(panel, -1, "Заменить все цифры на *", (70, 80), (220, 20))
        self.space_cb = wx.CheckBox(panel, -1, "Вставить пробелы между символами",
                    (70, 100), (280, 20))
        self.sort_cb = self.sort_checkbox = wx.CheckBox(panel, -1, "Сортировать слова в строке",
                                         (70, 120), (220, 20))

        self.radio_by_size = wx.RadioButton(
            panel, -1, "По размеру", (100, 140), (150, 20))
        self.radio_by_lex = wx.RadioButton(
            panel, -1, "Лексикографически", (100, 160), (150, 20))
        self.radio_by_size.Disable()
        self.radio_by_lex.Disable()

        format_button = wx.Button(panel, -1, "Форматирование",
                                  size=(300, 30), pos=(70, 190))

        self.Bind(wx.EVT_BUTTON, self.on_format_click, format_button)
        self.Bind(wx.EVT_CHECKBOX, self.on_check, self.sort_checkbox)

    def on_format_click(self, event):
        text = self.entry_text.GetValue()
        format_text = StringFormatter(text)
        if self.dell_less_cb.IsChecked():
            format_text.del_less(self.len_sc.GetValue())
        if self.convert_cb.IsChecked():
            format_text.change_num()
        if self.space_cb.IsChecked():
            format_text.set_spaces()
        if self.sort_cb.IsChecked():
            if self.radio_by_size.GetValue():
                format_text.sort_by_len()
            elif self.radio_by_lex.GetValue():
                format_text.sort_by_alph()
        self.result_text.SetValue(format_text.string)

    def on_check(self, event):
        if self.sort_checkbox.IsChecked():
            self.radio_by_size.Enable()
            self.radio_by_lex.Enable()
        else:
            self.radio_by_size.Disable()
            self.radio_by_lex.Disable()


if __name__ == '__main__':

    app = wx.App()

    string_frame = StringFrame()

    string_frame.Show()

    app.MainLoop()