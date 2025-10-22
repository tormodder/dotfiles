from libqtile import bar
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from colors import colors
from keybinds import defaultApps
from functions import powerMenu

#----------------------------------------------------------------------------
# Defaults and theming settings
#----------------------------------------------------------------------------

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

decoration_group =  {
    #"background": colors[0],
    #"foreground": colors[1],
    "decorations": [
        RectDecoration(
            colour=colors[-2],
            radius=9, 
            filled=True, 
            padding_y=3,
            padding_x=1,
        )
    ],
}

widgetDecorations = {
    "background": colors[0],
    "foreground": colors[1],
    "decorations": [
        RectDecoration(use_widget_background = True, radius = 12, filled = True, group = True),
    ],
}

groupBoxTheme = dict(
    highlight_method="block",
    this_current_screen_border=colors[0],
    other_current_screen_border=colors[0], #45b3e0,
    other_screen_border=colors[4], #215578, # same color when unfocused on both screens
    this_screen_border=colors[4],
    hide_unused=True,
)

barConfig = {
    'size':         28,
    'background':   colors[-1], # 90% opacity
    "margin":       [3, 0, 5, 0]
}

#----------------------------------------------------------------------------
# Bar templates
#----------------------------------------------------------------------------
leftWidgets = [
    widget.CurrentLayout(
        **decoration_group, 
        **widget_defaults
    ),
    widget.Spacer(length=10),
    widget.GroupBox(
        **groupBoxTheme,
        **decoration_group,
        **widget_defaults,
        ),
    widget.Spacer(length=10),
    widget.Prompt(**decoration_group),
]

middleWidgets = [
    widget.Spacer(),
    widget.TextBox(
        font = "Font Awesome 6 Free Regular",
        fmt = "",
	    mouse_callbacks = {"Button1": lazy.spawn(defaultApps["calendar"])},
    ),
    widget.Clock(width=bar.CALCULATED ,format="%H:%M"),
    widget.Spacer(
        length = 10,
    ),
    widget.TextBox(
        font = "Font Awesome 6 Free Regular",
        fmt = "",
	    mouse_callbacks = {"Button1": lazy.spawn(defaultApps["calendar"])},
        #**widget_defaults,
    ),
    widget.Clock(
        format = "%d.%m.%Y",
	    mouse_callbacks = {"Button1": lazy.spawn(defaultApps["calendar"])},
        #**widgetDecorations,
    ),
    widget.Spacer(),

]

rightWidgets = [
    widget.Chord( # keeping this here because idk what if I decide to use chords later
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    widget.Systray(),
    widget.Spacer(length=10),
    widget.Volume(
        font = "Font Awesome 6 Free Regular",
        emoji = True,
        emoji_list = ['', '', '', ''],
        volume_app = defaultApps["sound"],
        #**decoration_group,
    ),
    widget.Spacer(
        length = -6,
        padding = 0,
        mouse_callbacks = {"Button3": lazy.spawn(defaultApps["sound"])},
        #**decoration_group
    ),
    widget.Volume(
        mute_foreground = colors[1] + "90",
        mute_format = "Muted",
        volume_app = defaultApps["sound"],
        #**decoration_group,
    ),
    widget.Spacer(length=5),
    widget.TextBox(
        font = "Font Awesome 6 Free Regular",
        fmt = "",
        **widgetDecorations,
    ),
    widget.Memory(
        format = '{MemPercent}%',
        update_interval = 5.0,
        #    **widgetDecorations
    ),
    widget.TextBox(
        font = "Font Awesome 6 Free Regular",
        fmt = "",
        #**widgetDecorations,
    ),    
    widget.CPU(
        format = '{load_percent}%',
        update_interval = 5.0,
        #**widgetDecorations,
    ),
    widget.CheckUpdates(
        font = 'Font Awesome 6 Free Regular',
        distro = 'Arch_checkupdates',
        display_format = ' ! ',
        no_update_string = '',
        update_interval = 30,
        mouse_callbacks = {"Button1": lazy.spawn(defaultApps["terminal"] + ' --hold --title "Available updates" checkupdates')},
        #**widgetDecorations,
    ),
    widget.TextBox(
        font = "Font Awesome 6 Free Regular",
        fmt = "",
	    mouse_callbacks = {"Button1": lazy.function(powerMenu)},
        #**widgetDecorations,
    ),
    widget.Spacer(length=5),
]

#----------------------------------------------------------------------------
# Declaration of the bars
#----------------------------------------------------------------------------
mainBar = bar.Bar(leftWidgets + middleWidgets + rightWidgets, **barConfig)

