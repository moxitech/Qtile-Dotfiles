from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
terminal = guess_terminal()
mod = "mod4"

keys = [
    # Переместить Фокус между окнами
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Изменить позицию окна
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Изменение размера окна
    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Запуск|Спавн программ 
    Key([mod], "f", lazy.spawn("nautilus"), desc="Запуск файлового менеджера"),
    Key([mod, "control"], "f", lazy.spawn("pcmanfm"), desc="Запуск дополнительного файлового менеджера"),                                                 # filemanager
    Key([mod], "a", lazy.spawn("alacritty -e btop"), desc="Запуск диспетчера задач"),                                       # dispatcher
    Key([mod], "t", lazy.spawn("telegram-desktop"), desc='Запуск телеграмма'),                                        # telegram
    Key([mod, "control"], "t", lazy.spawn("gedit /home/moxitech/Moxitech_Binarity/todo.txt"), desc="Открыть Todo-шку"),

    Key([mod], "y", lazy.spawn("flatpak run ru.yandex.Browser"), desc='Запуск Яндекса'),                           # yandex
    Key([mod], "b", lazy.spawn("google-chrome-stable"), desc='Запуск гугл хрома'),                                    # google
    Key([mod, "control"], "b", lazy.spawn("blueberry"), desc='Запустить блютуз'),                                    # bluetooth
    Key([mod], "v", lazy.spawn("vlc"), desc='Запуск медиаплеера'),                                                     # vlc player
    Key([mod], "p", lazy.spawn("flatpak run com.jetbrains.PyCharm-Community"), desc='Запустить Pycharm python IDE'),             # PyCharm IDE
    Key([mod], "k", lazy.spawn("krita"), desc='Запуск графического редактора'),                                                   # Krita graphical
    Key([mod], "d", lazy.spawn("qbittorrent"), desc='Запустить торрент'),                                             # Torrent
    Key([mod], "c", lazy.spawn("code"), desc='Запустить VS code'),                                                    # Code IDE
    Key([mod], "s", lazy.spawn("flatpak run com.google.AndroidStudio"), desc='Запуск Андроид студио'),                    # Android IDE
    Key([mod], "e", lazy.spawn("virtualbox"), desc='Запустить эмулятор x86'),                             # Boxes emu
    Key([mod], "l", lazy.spawn("libreoffice"), desc='Запуск Офиса'),                                             # WPS office
    Key([mod, "control"], "c", lazy.spawn("code /home/moxitech/.config/qtile/")),  # code -> config.py [qtile]
    Key([mod], "Return", lazy.spawn(terminal), desc="Запуск Терминала"),                     # Terminal spawn
    Key([mod], "Tab", lazy.next_layout(), desc="ПЕРЕКЛЮЧЕНИЕ МЕЖДУ ЛАЙАУТАМИ"),
    # Клавиши Fn
    Key([mod], "F11", lazy.spawn("brightnessctl -d intel_backlight set 5%- -q"), desc='Уменьшить яркость'),
    Key([mod], "F12", lazy.spawn("brightnessctl -d intel_backlight set +5% -q"), desc='Увеличить яркость'),
    Key([mod], "F1", lazy.spawn("amixer -q set Master toggle"), desc='Выключить микрофон'),
    Key([mod], "F2", lazy.spawn("amixer -c 0 sset Master 5%- unmute"), desc='Уменьшить громкость'),
    Key([mod], "F3", lazy.spawn("amixer -c 0 sset Master 5%+ unmute"), desc='Увеличить громкость'),

    #Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
   
    # Создать скриншот	
    Key([], "Print", lazy.spawn("grim /home/moxitech/screenshoots/screen.png "), desc='Сделать скриншот'),
    Key([mod], "Print", lazy.spawn('xfce4-screenshooter'), desc='Сделать скриншот с мастером скриншотов'),
    
    
    Key([mod], "q", lazy.window.kill(), desc="Закрыть выбранное окно"),                                    # Закрыть выбранное окно
    Key([mod, "control"], "r", lazy.reload_config(), desc="Перезагрузка qtile"),                         # Перезагрузить конфиг
    Key([mod, "control"], "q", lazy.shutdown(), desc="Выключить Qtile"),                                 # Выход из Qtile
    Key([mod], "r", lazy.spawn("fuzzel"), desc="Запуск программы из под менеджера"),       # Promt менеджер ( standart -> spawncmd() || rofi -show run )
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Следующая раскладка клавиатуры"),    # Изменить раскладку клавиатуры
]
