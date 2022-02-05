from ast import Match
from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-fa-firefox, 
# nf-fae-python, 
# nf-dev-terminal, 
# nf-fa-code, 
# nf-oct-git_merge, 
# nf-linux-docker,
# nf-mdi-image, 
# nf-mdi-layers

# Qtile workspaces 1
#groups = [Group(i) for i in [
#    " ", " ", " ", " ", " ", "", "", " ", " ",
    #"   ", "   ", "   ", "   ", "  ", "   ", "   ",
#]]

#for i, group in enumerate(groups):
#    actual_key = str(i + 1)
#    keys.extend([
#        # Switch to workspace N
#        Key([mod], actual_key, lazy.group[group.name].toscreen()),
#        # Send window to workspace N
#        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
#    ])


# Qtile workspaces 2
# Groups with matches
workspaces = [
    {"name": " ₁", "key": "1", "matches": [Match(wm_class='firefox')], "layout": "monadtall"},
    {"name": " ₂", "key": "2", "matches": [Match(wm_class='kitty'), Match(wm_class='ranger')], "layout": "monadtall"},
    {"name": " ₃", "key": "3", "matches": [Match(wm_class='vim')], "layout": "monadtall"},
    {"name": " ₄", "key": "4", "matches": [Match(wm_class='telegram-desktop'), Match(wm_class='weechat')], "layout": "monadtall"},
    {"name": " ₅", "key": "5", "matches": [Match(wm_class='gimp-2.10')], "layout": "monadtall"},
    {"name": " ₆", "key": "6", "matches": [Match(wm_class='spotify')], "layout": "monadtall"},
    {"name": " ₇", "key": "7", "matches": [Match(wm_class='libreoffice')], "layout": "monadtall"},
    {"name": " ₈", "key": "8", "matches": [Match(wm_class='newsboat')], "layout": "monadtall"},
    {"name": " ₉", "key": "9", "matches": [Match(wm_class='neomutt')], "layout": "monadtall"},
]

#workspaces = [
#    {"name": " ₁", "key": "1", "matches": [Match(wm_class='firefox')], "layout": "monadtall"},
#    {"name": " ₂", "key": "2", "matches": [Match(wm_class='kitty'), Match(wm_class='ranger')], "layout": "monadtall"},
#    {"name": " ₃", "key": "3", "matches": [Match(wm_class='vim')], "layout": "monadtall"},
#    {"name": " ₄", "key": "4", "matches": [Match(wm_class='telegram-desktop'), Match(wm_class='weechat')], "layout": "monadtall"},
#    {"name": " ₅", "key": "5", "matches": [Match(wm_class='gimp-2.10')], "layout": "monadtall"},
#    {"name": "阮 ₆", "key": "6", "matches": [Match(wm_class='spotify')], "layout": "monadtall"},
#    {"name": " ₇", "key": "7", "matches": [Match(wm_class='libreoffice')], "layout": "monadtall"},
#    {"name": " ₈", "key": "8", "matches": [Match(wm_class='newsboat')], "layout": "monadtall"},
#    {"name": " ₉", "key": "9", "matches": [Match(wm_class='neomutt')], "layout": "monadtall"},
#]

groups = []
for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    layouts = workspace["layout"] if "layout" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout=layouts))
    keys.append(Key([mod], workspace["key"], lazy.group[workspace["name"]].toscreen()))
    keys.append(Key([mod, "shift"], workspace["key"], lazy.window.togroup(workspace["name"])))    