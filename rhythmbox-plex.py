from gi.repository import GObject, RB, Peas


class PlexPlugin (GObject.Object, Peas.Activatable):
    object = GObject.property(type=GObject.Object)

    def __init__(self):
        super(PlexPlugin, self).__init__()

    def do_activate(self):
        self.string = "Hello World"
        print(self.string)

    def do_deactivate(self):
        del self.string