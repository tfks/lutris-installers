#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf
from lutris.util.downloader import Downloader

wnd = None
img_header = None
destfile = ""
downloader = None

def handlerOk(self):
    wnd.destroy()

def loadHeaderImage():
    global destfile
    global downloader
    url = "https://lutris.net/media/cache/52/dd/52ddbf4b6a59ab9af346ff50f7576ec6.jpg"
    destfile = "/tmp/dune-2000.jpg"
    downloader = Downloader(url, destfile, True, None, loadHeaderImageCallBack)
    downloader.start()

def loadHeaderImageCallBack():
    img_header.set_from_pixbuf(Pixbuf.new_from_file(destfile))

def createDialog():
    global wnd
    global img_header

    wnd = Gtk.Window()
    wnd.set_default_size(400, 400)
    wnd.set_position(Gtk.WindowPosition.CENTER)
    wnd.connect("destroy", Gtk.main_quit)

    wnd.set_title("Dune 2000")

    wnd.set_resizable(False)

    wnd.set_icon_from_file("/usr/share/lutris/media/logo.png")

    vbox = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL,
        spacing=12,
        visible=True
    )

    vbox.set_margin_top(18)
    vbox.set_margin_bottom(18)
    vbox.set_margin_right(18)
    vbox.set_margin_left(18)

    wnd.add(vbox)

    img_header = Gtk.Image()
    loadHeaderImage()

    vbox.pack_start(img_header, False, False, 0)

    label = Gtk.Label()
    label.set_alignment(0, 0)
    label.set_text("This installer will install Dune 2000 and the cut scenes on your machine. ")

    vbox.pack_start(label, False, False, 0)

    label2 = Gtk.Label()
    label2.set_alignment(0, 0)
    label2.set_text("The game will ask for your preferred language, will set the game to this language, and download the cut scenes for this language.")

    vbox.pack_start(label2, False, False, 0)

    action_buttons = Gtk.Box(spacing=6)
    vbox.pack_start(action_buttons, False, False, 0)

    action_buttons_alignment = Gtk.Alignment.new(0, 0, 1, 1)
    action_buttons_alignment.add(action_buttons)
    vbox.pack_start(action_buttons_alignment, False, True, 50)

    ok_button = Gtk.Button("Install Dune 2000")
    ok_button.set_property("width-request", 75)
    ok_button.set_hexpand(True)
    ok_button.connect("clicked", handlerOk)

    action_buttons.add(ok_button)

    wnd.show_all()

createDialog()

Gtk.main()

