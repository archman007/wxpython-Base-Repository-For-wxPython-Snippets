import wx
import mariadb

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # Menu
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(wx.ID_ANY, "Hello", "Say Hello")
        exitItem = fileMenu.Append(wx.ID_EXIT, "Exit", "Exit application")
        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        # Status Bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

        # Event Bindings
        self.Bind(wx.EVT_MENU, self.on_hello, helloItem)
        self.Bind(wx.EVT_MENU, self.on_exit, exitItem)

    def on_hello(self, event):
        wx.MessageBox("Hello, World!", "Info", wx.OK | wx.ICON_INFORMATION)

    def on_exit(self, event):
        self.Close(True)

def connect_mariadb():
    try:
        conn = mariadb.connect(
            user="your_username",
            password="your_password",
            host="localhost",
            port=3306,
            database="your_database"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print("MariaDB version:", version)
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, title="Hello World")
    frame.Show()
    connect_mariadb()
    app.MainLoop()
