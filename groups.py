from libqtile.config import Group
from libqtile.config import Match
groups = [                                                                 
    Group("1", label = 'WWW',   matches=[Match(wm_class="google-chrome"), Match(wm_class="Yandex-browser")], layout="monadtall"),
    Group("2", label = "CODE",  matches=[Match(wm_class="code-oss")]),
    Group("3", label = "CHAT",  matches=[Match(wm_class="Telegram")]),
    Group("4", label = "MEDIA", matches=[Match(wm_class="vlc")], layout="max"),
    Group("5", label = "DOC",   matches=[Match(wm_class="Libreoffice")]),
    Group("6", label = "VM"),
    Group("7", label = "ETC"),
]