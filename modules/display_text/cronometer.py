import time
import wx


class cronometer:

    def __init__(self, parent):
        self.parent = parent

        self.display = wx.StaticText(parent, label="00:00.000")

        self.display.SetForegroundColour(wx.WHITE)
        self.display.SetBackgroundColour(wx.BLACK)

        font = self.display.GetFont()
        font.SetPointSize(14)
        self.display.SetFont(font)

        self.start_time = None
        self.finished = False

        self.timer = wx.Timer(parent)
        parent.Bind(wx.EVT_TIMER, self._update, self.timer)
        parent.Bind(wx.EVT_SIZE, self._on_parent_resize)

        self._update_position()

    def _update_position(self):
        parent_width, parent_height = self.parent.GetClientSize()

        display_width, display_height = self.display.GetBestSize()

        margin = 20

        x = (parent_width - display_width) // 2
        y = parent_height - display_height - margin

        self.display.SetPosition((x, y))

    def _on_parent_resize(self, event):
        self._update_position()
        event.Skip()

    def start(self):
        if self.start_time is not None or self.finished:
            return

        self.start_time = time.perf_counter()

        self.timer.Start(10)
        self._update(None)

    def stop(self):
        if self.start_time is None or self.finished:
            return

        self._update(None)

        self.finished = True
        self.timer.Stop()

    def _update(self, event):
        if self.start_time is None:
            return

        elapsed = time.perf_counter() - self.start_time

        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed % 1) * 1000)

        self.display.SetLabel(f"{minutes:02}:{seconds:02}.{milliseconds:03}")

        self._update_position()
