from libqtile.config import Screen
from Strings import WALLPAPER_STRING
from Panels import panel_top
screens = [
    Screen(
        wallpaper=WALLPAPER_STRING,
        wallpaper_mode="stretch",
        top=panel_top,
    ),
]

