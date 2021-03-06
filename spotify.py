from __future__ import absolute_import

__kupfer_name__ = _("Spotify")
__kupfer_sources__ = ("SpotifySource", )
__description__ = _("Control spofity media player.")
__version__ = "0.1"
__author__ = "Stephen Johnson <steve@thatbytes.co.uk>"

import dbus

from kupfer.objects import RunnableLeaf, Source
from kupfer.obj.apps import AppLeafContentMixin
from kupfer import utils, icons, pretty

import pynotify

def get_player():
    session = dbus.SessionBus.get_session()
    spotify = session.get_object("org.mpris.MediaPlayer2.spotify","/org/mpris/MediaPlayer2")
    return dbus.Interface(spotify, dbus_interface = 'org.mpris.MediaPlayer2.Player')

class PlayPause (RunnableLeaf):
    def __init__(self):
        RunnableLeaf.__init__(self, name=_("Play/Pause"))
    def run(self):
        get_player().PlayPause() 
    def get_description(self):
        return _("Resume/Pause playback in Spotify")
    def get_icon_name(self):
        return "media-playback-start"
class Next (RunnableLeaf):
    def __init__(self):
        RunnableLeaf.__init__(self, name=_("Next"))
    def run(self):
        get_player().Next()
    def get_description(self):
        return _("Jump to next track in Spotify")
    def get_icon_name(self):
        return "media-skip-forward"

class Previous (RunnableLeaf):
    def __init__(self):
        RunnableLeaf.__init__(self, name=_("Previous"))
    def run(self):
        get_player().Previous()
    def get_description(self):
        return _("Jump to previous track in Spotify")
    def get_icon_name(self):
        return "media-skip-backward"

class SpotifySource (AppLeafContentMixin, Source):
    appleaf_content_id = 'spotify'
    def __init__(self):
        Source.__init__(self, _("Spotify"))
    def get_items(self):
        yield PlayPause()
        yield Next()
        yield Previous()
    def provides(self):
        yield RunnableLeaf
    def get_description(self):
        return __description__
    def get_icon_name(self):
        return "spotify"
