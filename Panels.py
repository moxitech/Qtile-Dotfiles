from qtile_extras.widget.decorations  import PowerLineDecoration
from qtile_extras.widget import UPowerWidget
from libqtile import bar, widget
from Strings import *
keyboard = widget.KeyboardLayout(configured_keyboards=['us', 'ru'])


def spawnSpacer():
    return widget.Spacer(length=5)
borderline = {
    
}



panel_top = bar.Bar(
    [
        
        widget.GroupBox(
                borderwidth=2, 	  # Толщина рамки
			    highlight_method='block', # Метод выделения активного воркспейса
			    block_highlight_text_color= TEAL_COLOR_ACTIVE,# Цвет текста активного воркспейса
                this_current_screen_border= GREEN_THEME_COLOR, # Цвет фона активного воркспейса
                inactive="#FFFFFF",
                rounded=True,
        ),

        widget.Spacer(length=5),
        widget.LaunchBar(progs=[
                                ('/usr/share/icons/Obsidian/apps/48/code.png', 'code-oss', 'start code'),
                                ("/usr/share/icons/Obsidian/apps/48/pycharm.png", "flatpak run com.jetbrains.PyCharm-Community"),
                                ("telegram", "telegram-desktop", "start tg"),

                                
                                ]),
        widget.WindowName(max_chars=30),
        #widget.TaskList(border = '#000011'),
        
        widget.Systray(),            
        
        widget.Wlan(format='({percent:2.0%} 📶)', **borderline,),
        spawnSpacer(),
        
        widget.KeyboardLayout(configured_keyboards=['us', 'ru'], fmt="[ {} ⌨️]", update_interval=1, **borderline,),
		spawnSpacer(),
        
        widget.PulseVolume(fmt="[{} 🔊]", padding=5,**borderline,), # emoji='🔈', emoji_list=['🔇', '🔈', '🔉', '🔊']		
        spawnSpacer(),
        
        
        
        UPowerWidget(),
        spawnSpacer(),


        spawnSpacer(),
		widget.Clock(format="%Y.%m.%d  %H:%M %p", padding=10, **borderline,),
		
  

        spawnSpacer(),
        widget.QuickExit(default_text=" Выход 🔐  ", **borderline,),
        ],
        40,
            #sborder_width=[0, 30, 5, 30],  # Draw top and bottom borders
            #border_color=["#00000000", "#00000000", "#00000000", "#00000000"],  # Borders are magenta
	    background="#111111", # 253238    
)