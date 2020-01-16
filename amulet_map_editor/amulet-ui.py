import wx
from amulet_map_editor.util.world_select import WorldSelectUI
from amulet_map_editor import config, lang


class AmuletMainWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=wx.EmptyString,
            pos=wx.DefaultPosition,
            size=wx.Size(560, 400),
            style=wx.CAPTION
            | wx.CLOSE_BOX
            | wx.MINIMIZE_BOX
            | wx.SYSTEM_MENU
            | wx.TAB_TRAVERSAL
            | wx.CLIP_CHILDREN
            | wx.RESIZE_BORDER,
        )

        # self.sizer = wx.BoxSizer(wx.VERTICAL)
        # self.SetSizer(self.sizer)

        self.world_tab_holder = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0
        )

        self._add_world_tab(WorldSelectUI(self.world_tab_holder), lang.get('main_menu'))

        # self.sizer.Add(self.world_tab_holder, 1, wx.EXPAND | wx.ALL, 5)
        # self.Layout()
        # self.Centre(wx.BOTH)
        self.Show()

    def _add_world_tab(self, obj, obj_name):
        self.world_tab_holder.AddPage(obj, obj_name, True)


if __name__ == "__main__":
    app = wx.App()
    frame = AmuletMainWindow(None)
    app.MainLoop()