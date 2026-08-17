import random
import wx


class text_glitch(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent, style=wx.NO_BORDER)

        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)

        self.timer = wx.Timer(self)

        self.Bind(wx.EVT_TIMER, self._update_glitch)
        self.Bind(wx.EVT_PAINT, self._on_paint)
        self.Bind(wx.EVT_WINDOW_DESTROY, self._on_destroy)

        self.duration = 150
        self.frame_interval = 40
        self.elapsed = 0

        self.Hide()

    def start(self):
        if self.IsBeingDeleted():
            return

        parent = self.GetParent()

        if not parent or parent.IsBeingDeleted():
            return

        label = parent.label

        self.SetPosition(label.GetPosition())
        self.SetSize(label.GetSize())

        self.elapsed = 0

        self.Show()
        self.Raise()
        self.Refresh()

        if not self.timer.IsRunning():
            self.timer.Start(self.frame_interval)

    def _update_glitch(self, event):
        if self.IsBeingDeleted():
            return

        self.elapsed += self.frame_interval

        if self.elapsed >= self.duration:
            self.timer.Stop()
            self.Hide()

            parent = self.GetParent()

            if parent and not parent.IsBeingDeleted():
                parent.label.Refresh()

            return

        self.Refresh()

    def _on_destroy(self, event):
        if self.timer.IsRunning():
            self.timer.Stop()

        event.Skip()

    def _on_paint(self, event):
        dc = wx.PaintDC(self)

        width, height = self.GetClientSize()

        dc.SetBackground(wx.Brush(wx.BLACK))
        dc.Clear()

        for _ in range(250):
            x = random.randrange(max(1, width))
            y = random.randrange(max(1, height))

            size = random.choice((1, 1, 2, 3, 4))

            brightness = random.randint(40, 255)

            colour = wx.Colour(brightness, brightness, brightness)

            dc.SetBrush(wx.Brush(colour))
            dc.DrawRectangle(x, y, size, size)

        dc.SetPen(wx.Pen(wx.Colour(80, 80, 80), 1))

        for y in range(0, height, 4):
            dc.DrawLine(0, y, width, y)

        for _ in range(12):
            y = random.randrange(max(1, height))

            bar_height = random.randint(1, 6)
            x = random.randint(-50, 50)
            bar_width = random.randint(20, max(21, width))

            brightness = random.randint(80, 255)

            colour = wx.Colour(brightness, brightness, brightness)

            dc.SetBrush(wx.Brush(colour))
            dc.DrawRectangle(x, y, bar_width, bar_height)
