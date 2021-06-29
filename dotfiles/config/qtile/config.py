# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# Configuration file modified by MSun

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile import hook
import os
import subprocess

mod = "mod4"
mod1 = "mod1"   # Alt
terminal = "alacritty"

# Color scheme
colors = ["#1c2b2d",
          "#1f6f8b",
          "#99a8b2",
          "e6d5b8"]

# Layout theme
layout_theme = {
        "border_width": 12,
        "border_focus": colors[1],
        "border_normal": colors[0],
        }

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    KeyChord(
        [mod], "r", [
            Key([], "j", lazy.layout.shrink(),
                desc="Reduce window size dwon"),
            Key([], "k", lazy.layout.grow(),
                desc="Grow window size up"),
            Key([], "n", lazy.layout.normalize(),
                desc="Reset all window sizes"),
            ],
        mode="Resize"
        ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod], "s", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle the current window to/from floating mode"),
    Key([mod], "f", lazy.window.toggle_maximize(),
        desc="Toggle the current window to/from fullscreen mode"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


layouts = [
    # layout.Columns(
    #     **layout_theme,
    #     grow_amount=5,
    #     insert_position=1,
    #     border_normal_stack=colors[2],
    #     border_focus_stack=colors[1],
    #     ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        **layout_theme,
        ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(),
    layout.Max(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# ##### WIDGET SETTING ########
widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=20,
    padding=4,
    background=colors[0],
    foreground=colors[-1],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    background=colors[0],
                    foreground=colors[2],
                    scale=0.7,
                    ),
                widget.Chord(
                    background=colors[2],
                    foreground=colors[0],
                    ),
                widget.GroupBox(
                    active=colors[-1],
                    font="Ubuntu Bold",
                    highlight_method='block',
                    ),
                widget.Prompt(),
                widget.Sep(
                    linewidth=4,
                    padding=10,
                    background=colors[0],
                    foreground=colors[2],
                    ),
                widget.WindowName(
                    background=colors[1],
                    foreground=colors[3],
                    ),
                widget.Sep(
                    linewidth=4,
                    padding=10,
                    background=colors[0],
                    foreground=colors[2],
                    ),
                widget.TextBox(
                    text=" Cpu:",
                    foreground=colors[2],
                    background=colors[0],
                    padding=0
                    ),
                widget.CPU(
                    foreground=colors[3],
                    background=colors[0],
                    ),
                widget.TextBox(
                    text=" Mem:",
                    foreground=colors[2],
                    background=colors[0],
                    padding=0
                    ),
                widget.Memory(
                    foreground=colors[3],
                    background=colors[0],
                    padding=5,
                    ),
                widget.TextBox(
                    text=" Net:",
                    foreground=colors[2],
                    background=colors[0],
                    padding=0
                    ),
                widget.Net(
                    interface="wlp0s20f3",
                    frequency=5,
                    format='{down}/{up}',
                    ),
                widget.TextBox(
                    text=" Vol:",
                    foreground=colors[2],
                    background=colors[0],
                    padding=0
                    ),
                widget.Volume(
                    foreground=colors[3],
                    background=colors[0],
                    padding=5
                    ),
                widget.Clock(
                    format='%a-%Y-%m-%d  %H:%M',
                    fontsize=22,
                    foreground=colors[-1],
                    background=colors[0],
                    ),
                widget.Systray(
                    padding=5,
                    icon_size=24,
                    ),
                widget.Spacer(
                    length=10,
                    ),
            ],
            32,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], **layout_theme)
auto_fullscreen = True
focus_on_window_activation = "smart"


# Hooks
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
