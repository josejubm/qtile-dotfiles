from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-3
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),
    separator(),

    widget.Notify(),

    widget.Systray(**base(bg='dark'),padding=5),

    powerline('color2', 'dark'),
    icon(bg="color2", text=' '),

    powerline('color4', 'color2'),
    icon(bg="color4", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color3', 'color4'),
    icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    widget.Net(**base(bg='color3'), interface='wlo1'),

    powerline('color2', 'color3'),
    icon(bg="color2", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
    
    powerline('color1', 'color2'),
    icon(bg="color1", text=' '),
    widget.Backlight(
        background = colors['color1'],
        foreground = colors['text'],
        backlight_name = 'amdgpu_bl0',
        format = '{percent:2.0%} ',
        update_interval = 0.2,
    ),
    
    icon(bg="color1", text='墳 '),
    widget.Volume(
        background = colors['color1'],
        foreground = colors['text'],
        fmt = '{}',
        update_interval = 0.2, 
    ),

    widget.Battery(
        background = colors['color1'],
        foreground = colors['text'],
        charge_char = '',
        discharge_char = ' ',
        empty_char = '  ',
        format = ' {char} {percent:2.0%} ',
        full_char = ' ',
        update_interval = 0.2,
	),
    
    powerline('dark', 'color1'),
    widget.CurrentLayoutIcon(**base(bg='dark'), scale=0.65),
    widget.CurrentLayout(**base(bg='dark', fg='active'), padding=5),

]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color3', 'dark'),
    widget.ThermalSensor(
        background = colors['color3'],
        foreground = colors['text'],
        threshold = 90,
        fmt = '  {} ',
        padding = 5
    ),

    powerline('color1', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
