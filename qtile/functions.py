import os
import subprocess

from libqtile import qtile, hook 
from libqtile.lazy import lazy
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupImage, PopupText

from colors import colors

#----------------------------------------------------------------------------
# Defaults
#----------------------------------------------------------------------------

# Change if you want to choose your own brightness levels for brightness popup 
# It MUST be a string. DON'T SET ANYTHING UNDER 0.1. YOU WILL PROBABLY NOT SEE ANYTHING


imageDefaults = {
    "mask": True,
    "colour": colors[1],
    "highlight_radius": 10,
    "highlight_border": -10,
}

textDefaults = {
    "font": "Hack Nerd Font",
    "fontsize": 14,
    "h_align": "center",
    "foreground": colors[1],
}

layoutDefaults = {
    "border_width": 2,
    "border": colors[1],
    "background": colors[0],
    "hide_on_mouse_leave": True,
}

#----------------------------------------------------------------------------
# Functions
#----------------------------------------------------------------------------

def powerMenu(qtile):
    controls = [
        PopupImage(
            filename = "~/.config/qtile/images/terminal.svg",
            pos_x = 0.15,
            pos_y = 0.15,
            width = 0.1,
            height = 0.5,
            **imageDefaults,
            highlight = colors[3],
            mouse_callbacks = {
                "Button1": lazy.shutdown()
            },
        ),
        PopupImage(
            filename = "~/.config/qtile/images/reboot.svg",
            pos_x = 0.45,
            pos_y = 0.15,
            width = 0.1,
            height = 0.5,
            **imageDefaults,
            highlight = colors[3],
            mouse_callbacks = {
                "Button1": lazy.spawn("reboot")
            }
        ),
        PopupImage(
            filename = "~/.config/qtile/images/shutdown.svg",
            pos_x = 0.75,
            pos_y = 0.15,
            width = 0.1,
            height = 0.5,
            **imageDefaults,
            highlight = "A00000",
            mouse_callbacks = {
                "Button1": lazy.spawn("shutdown now")
            }
        ),
        PopupText(
            text = "Quit Qtile",
            pos_x = 0.1,
            pos_y = 0.75,
            width = 0.2,
            height = 0.2,
            **textDefaults,
        ),
        PopupText(
            text = "Reboot",
            pos_x = 0.4,
            pos_y = 0.75,
            width = 0.2,
            height = 0.2,
            **textDefaults,
        ),
        PopupText(
            text = "Shutdown",
            pos_x = 0.7,
            pos_y = 0.75,
            width = 0.2,
            height = 0.2,
            **textDefaults,
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width = 1000,
        height = 200,
        controls = controls,
        initial_focus = 1,
        opacity = 0.8,
        **layoutDefaults,
    )

    layout.show(centered=True)

#----------------------------------------------------------------------------
# Hooks
#----------------------------------------------------------------------------
@hook.subscribe.startup_once
def autostart():
    autostartScript = os.path.expanduser("~/.config/qtile/autostart.sh")
    
    subprocess.run(["/bin/sh", autostartScript])

@hook.subscribe.startup_once
def setup_monitors():
    qtile.screens[0].set_group(qtile.groups_map["1"])
    qtile.screens[1].set_group(qtile.group_map["2"])

@hook.subscribe.client_new
def float_calendar(window):
    if window.name == "Calendar":
        window.floating = True
        # Example: Centered with 40% width and 40% height of the screen
        window.togroup(qtile.current_group.name)
        #        screen = window.qtile.current_screen
        #screen = window.qtile.screens[1]
        screen = qtile.screens[1]
        group_name = screen.group.name
        window.togroup(group_name)
        sw = screen.width
        sh = screen.height
        ww = int(sw * 0.4)
        wh = int(sh * 0.4)
        wx = int((sw - ww) / 2)
        wy = int((sh - wh) / 4)  # Below the bar
        window.place(wx, wy, ww, wh, 0, None)
