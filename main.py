import os
import wx

from modules.TextField.TextField import TextField

os.system("cls")

app = wx.App()

window = wx.Frame(None, title="Stupid Typing Game", size=(800, 600))

panel = TextField(window)


sizer = wx.BoxSizer(wx.VERTICAL)
sizer.Add(panel, 1, wx.EXPAND)
window.SetSizer(sizer)
window.SetBackgroundColour(wx.BLACK)

window.Show()

app.MainLoop()
