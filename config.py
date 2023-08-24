import os
import subprocess
from libqtile import layout,  hook
from libqtile.config import Click, Drag,Key, Match, Screen
from groups import groups
from libqtile.lazy import lazy
from keys import keys, mod

from mouse import mouse
from screens import screens


## АВТОЗАПУСК ----------------------------------------------------------------------
@hook.subscribe.startup_once
def autostart():
    os.system("/home/moxitech/.config/qtile/autostart.sh")


## ОБОИ ----------------------------------------------------------------------------
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
    layout.Bsp(border_focus = "#01ffef", border_normal = "#263238", border_width=1, margin = 5),
    layout.Matrix(border_focus = "#01ffef", border_normal = "#263238", border_width=1, margin = 5),
    layout.Max(),
    #layout.Floating(),
]

widget_defaults = dict(
    font="JetBrainsMono",
    fontsize=16,
    padding=5,
)
extension_defaults = widget_defaults.copy()
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
        Match(wm_class="vlc"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wl_input_rules = None
wmname = "LG3D"
