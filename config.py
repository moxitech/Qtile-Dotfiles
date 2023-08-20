import os
import subprocess
from libqtile.log_utils import logger
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget as qtile_extras_widget

TEAL_COLOR = '#01FFEF'          # Цвет блока
TEAL_COLOR_ACTIVE = '#000000'
TEAL_COLOR_UNACTIVE = '#A4A4A4'

WALLPAPER_STRING = "~/wallpaper/210902.jpg" # "~/wallpaper/far.jpg"

## АВТОЗАПУСК ----------------------------------------------------------------------
@hook.subscribe.startup_once
def autostart():
    os.system("/home/moxitech/.config/qtile/autostart.sh")

@hook.subscribe.startup
def autostart():
    wallpaper()


## СДЕЛАТЬ ДИАЛОГОВЫЕ ОКНА ПЛАВАЮЩИМИ ----------------------------------------------
@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True
    
mod = "mod4"
terminal = guess_terminal()
keyboard = widget.KeyboardLayout(configured_keyboards=['us', 'ru'])

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
    Key([mod], "f", lazy.spawn("pcmanfm")),                         # filemanager
    Key([mod], "d", lazy.spawn("alacritty -e btop")),                            # dispatcher
    Key([mod], "m", lazy.spawn("rambox")),                # telegram
    Key([mod], "y", lazy.spawn("flatpak run ru.yandex.Browser")),   # yandex
    Key([mod], "b", lazy.spawn("google-chrome-stable")),            # google
    Key([mod, "control"], "b", lazy.spawn("bluedevil-wizard")),     # bluetooth
    
    Key([mod], "p", lazy.spawn("flatpak run com.jetbrains.PyCharm-Community")),             # PyCharm IDE
    Key([mod], "k", lazy.spawn("krita")),                                                   # Krita graphical
    Key([mod], "l", lazy.spawn("qbittorrent")),                                             # Torrent
    Key([mod], "c", lazy.spawn("code")),                                                    # Code IDE
    Key([mod], "a", lazy.spawn("flatpak run com.google.AndroidStudio")),                    # Android IDE
    Key([mod], "u", lazy.spawn("flatpak run org.gnome.Boxes")),                             # Boxes emu
    Key([mod], "o", lazy.spawn("flatpak run com.wps.Office")),                              # WPS office
    Key([mod, "control"], "c", lazy.spawn("code /home/moxitech/.config/qtile/config.py")),  # code -> config.py [qtile]
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),                     # Terminal spawn
    # Клавиши Fn
    Key([mod], "F11", lazy.spawn("brightnessctl -d intel_backlight set 10%- -q")),
    Key([mod], "F12", lazy.spawn("brightnessctl -d intel_backlight set +10% -q")),
    Key([mod], "F1", lazy.spawn("amixer -q set Master toggle")),
    Key([mod], "F2", lazy.spawn("amixer -c 0 sset Master 11%- unmute")),
    Key([mod], "F3", lazy.spawn("amixer -c 0 sset Master 11%+ unmute")),

    #Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
   
    # Создать скриншот	
    Key([], "Print", lazy.spawn("scrot 'ArcoLinux-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f /home/moxitech/screenshoots/'")),
    Key([mod], "Print", lazy.spawn('xfce4-screenshooter')),
    
    
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),                                    # Закрыть выбранное окно
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),                         # Перезагрузить конфиг
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),                                 # Выход из Qtile
    Key([mod], "r", lazy.spawn("rofi -show run "), desc="Spawn a command using a prompt widget"),       # Promt менеджер ( standart -> spawncmd() )
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout"),    # Изменить раскладку клавиатуры
]


groups = [                                                                 
    Group("1", label = "1"),
    Group("2", label = "2"),
    Group("3", label = "3"),
    Group("4", label = "4"),
    Group("5", label = "5"),
    Group("6", label = "6"),
    Group("7", label = "7"),
]

for i in groups:
    keys.extend(
        [
            # Переместить фокус на другой рабочий стол
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # Переместить окно с фокусом на другой рабочий стол
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),        # switch_togroup=True --> switch focus to group
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
)

layouts = [
    layout.Bsp(border_focus = "#01ffef", border_normal = "#263238", border_width=2, margin = 6),
    #TODO : layout.Floating(),
]

widget_defaults = dict(
    font="JetBrainsMono",
    fontsize=16,
    padding=6,
)

extension_defaults = widget_defaults.copy()
panel_top = bar.Bar(
    [
            widget.GroupBox(
                borderwidth=1, 	  # Толщина рамки
			    highlight_method='block', # Метод выделения активного воркспейса
			    block_highlight_text_color=TEAL_COLOR_ACTIVE,# Цвет текста активного воркспейса
                this_current_screen_border=TEAL_COLOR, # Цвет фона активного воркспейса
                inactive=TEAL_COLOR_UNACTIVE,
                rounded=True,
        ),
        widget.Spacer(length=20),
        #widget.LaunchBar(progs=[('', 'com.jetbrains.PyCharm-Community', 'start code'), ("telegram", "telegram-desktop", "start tg")]),
        widget.Prompt(),
        widget.WindowName(max_chars=30),
        widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
        ),
        widget.Systray(),
		widget.Spacer(length=5), # Виджет пробела                
        widget.Wlan(format=' {percent:2.0%} 🌐'),
        widget.Spacer(length=5), # Виджет пробела
        widget.KeyboardLayout(configured_keyboards=['us', 'ru'], fmt="{}", update_interval=1),
		widget.Spacer(length=5),
        widget.Bluetooth(),
		
        widget.PulseVolume(fmt=" {} 🔈", padding=5,), # emoji='🔈', emoji_list=['🔇', '🔈', '🔉', '🔊']		

        widget.Spacer(length=5),
        qtile_extras_widget.UPowerWidget(text_diplaytime=3, text_charging='({percentage:.0f}%) {ttf} до полной зарядки', text_discharging='({percentage:.0f}%)'),
        widget.Battery(battery=0, format='{percent:2.0%}'),
        widget.Spacer(length=5),
		widget.CPUGraph(graph_color=TEAL_COLOR),
		widget.Spacer(length=5),
		widget.Clock(format="[ %Y.%m.%d  %H:%M %p ]", padding=10),
		widget.QuickExit(default_text=" Выход 🔐   ", countdown_format='{} 🔑'),
        ],
        30,
            border_width=[0, 30, 5, 30],  # Draw top and bottom borders
            #border_color=["#00000000", "#00000000", "#00000000", "#00000000"],  # Borders are magenta
	    margin=1,
	    background="#00000055", # 253238    
)

screens = [
    Screen(
        wallpaper=WALLPAPER_STRING,
        wallpaper_mode="stretch",
        top=panel_top,
    ),
]
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]



dgroups_key_binder = None
dgroups_app_rules = []  
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(title="pinentry"),                    # GPG key password entry
        Match(wm_class="firefox"), # firefox    
        Match(wm_class="glava"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wl_input_rules = None
wmname = "LG3D"
