import wx

class DroneFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        super(DroneFrame, self).__init__(*args, **kw)

        # panel in the frame
        pn = wx.Panel(self)

        # main text
        st = wx.StaticText(pn, -1, "An Shallah My Brothers", style=wx.ALIGN_CENTRE)
        font = st.GetFont()
        font.PointSize += 40
        font = font.Underlined()
        font = font.Bold()
        st.SetFont(font)

        # create a sizer to manage widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 100))
        pn.SetSizer(sizer)

        # set menu bar
        self.makeMenuBar()

        # set status bar
        self.CreateStatusBar()
        self.SetStatusText("Property of CNU UAS")


    def makeMenuBar(self):

        fileMenu = wx.Menu()

        item = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()

        exit = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        about = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.HelpBar, item)
        self.Bind(wx.EVT_MENU, self.Exit,  exit)
        self.Bind(wx.EVT_MENU, self.About, about)


    def Exit(self, event):
        self.Close(True)


    def HelpBar(self, event):
        wx.MessageBox("أنا أحب الصحراء", "Pandora's Box")


    def About(self, event):
        wx.MessageBox("الله أكبر", "Cry About It")


if __name__ == '__main__':
    app = wx.App()
    fr = DroneFrame(None, title="Station Tester")
    fr.Show()
    app.MainLoop()