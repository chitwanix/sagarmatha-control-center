#!/usr/bin/python

DOMAIN = "sagarmatha-control-center"
PATH = "/usr/share/sagarmatha/locale"

import os, gettext, sys
sys.path.append('/usr/lib/chitwanix/common')
import additionalfiles

os.environ['LANG'] = "en_US.UTF-8"
gettext.install(DOMAIN, PATH)

prefix = """[Desktop Entry]
Exec=sagarmatha-control-center screen
Icon=cs-screensaver
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Settings;DesktopSettings;X-Sagarmatha-Settings-Panel;X-Sagarmatha-PersonalSettings
OnlyShowIn=X-Sagarmatha;
X-Sagarmatha-Settings-Panel=screen
# Translators: those are keywords for the brightness and lock control-center panel
_Keywords=Brightness;Lock;Dim;Blank;Monitor;
NoDisplay=true
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/screen/sagarmatha-screen-panel.desktop.in.in", prefix, _("Brightness & Lock"), _("Screen brightness and lock settings"), "")

prefix = """[Desktop Entry]
Exec=sagarmatha-settings sound
Icon=cs-sound
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Settings;HardwareSettings;X-Sagarmatha-Settings-Panel;
OnlyShowIn=X-Sagarmatha;
X-Sagarmatha-Settings-Panel=sound-nua
# Translators: those are keywords for the sound control-center panel
_Keywords=Card;Microphone;Volume;Fade;Balance;Bluetooth;Headset;
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/sound-nua/data/sagarmatha-sound-nua-panel.desktop.in.in", prefix, _("Sound"), _("Change sound volume and sound events"), "")

prefix = """[Desktop Entry]
Exec=sagarmatha-settings color
Icon=cs-color
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Settings;X-Sagarmatha-Settings-Panel;HardwareSettings
OnlyShowIn=X-Sagarmatha;
X-Sagarmatha-Settings-Panel=color
# Translators: those are keywords for the color control-center panel
_Keywords=Color;ICC;Profile;Calibrate;Printer;Display;
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/color/sagarmatha-color-panel.desktop.in.in", prefix, _("Color"), _("Color management settings"), "")

prefix = """[Desktop Entry]
Exec=sagarmatha-control-center sound
Icon=cs-sound
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Settings;HardwareSettings;X-Sagarmatha-Settings-Panel;
OnlyShowIn=X-Sagarmatha;
NoDisplay=true
X-Sagarmatha-Settings-Panel=sound
# Translators: those are keywords for the sound control-center panel
_Keywords=Card;Microphone;Volume;Fade;Balance;Bluetooth;Headset;Audio;
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/sound/data/sagarmatha-sound-panel.desktop.in.in", prefix, _("Sound"), _("Change sound volume and sound events"), "")

prefix = """[Desktop Entry]
Icon=cs-sound
Exec=sagarmatha-sound-applet
Terminal=false
Type=Application
Categories=
NoDisplay=true
X-GNOME-Autostart-Notify=true
AutostartCondition=GNOME3 if-session gnome-fallback
OnlyShowIn=X-Sagarmatha;
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/sound/data/sagarmatha-sound-applet.desktop.in", prefix, _("Volume Control"), _("Show desktop volume control"), "")

prefix = """[Desktop Entry]
Exec=sagarmatha-settings power
Icon=cs-power
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Settings;DesktopSettings;X-Sagarmatha-Settings-Panel;HardwareSettings
OnlyShowIn=X-Sagarmatha;
X-Sagarmatha-Settings-Panel=power
NoDisplay=true
# Translators: those are keywords for the power control-center panel
_Keywords=Power;Sleep;Suspend;Hibernate;Battery;
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/power/sagarmatha-power-panel.desktop.in.in", prefix, _("Power"), _("Power management settings"), "")

prefix = """[Desktop Entry]
Exec=sagarmatha-settings region
Icon=cs-language
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Settings;DesktopSettings;X-Sagarmatha-Settings-Panel;X-Sagarmatha-PersonalSettings
OnlyShowIn=X-Sagarmatha;
X-Sagarmatha-Settings-Panel=region
# Translators: those are keywords for the region control-center panel
_Keywords=Language;Layout;Keyboard;
NoDisplay=true
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/region/sagarmatha-region-panel.desktop.in.in", prefix, _("Region & Language"), _("Change your region and language settings"), "")

prefix = """[Desktop Entry]
Exec=sagarmatha-settings display
Icon=cs-display
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Settings;HardwareSettings;X-Sagarmatha-Settings-Panel;
OnlyShowIn=X-Sagarmatha;
X-Sagarmatha-Settings-Panel=display
# Translators: those are keywords for the display control-center panel
_Keywords=Panel;Projector;xrandr;Screen;Resolution;Refresh;
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/display/sagarmatha-display-panel.desktop.in.in", prefix, _("Displays"), _("Change resolution and position of monitors and projectors"), "")

prefix = """[Desktop Entry]
Exec=sagarmatha-settings network
Icon=cs-network
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Settings;HardwareSettings;X-Sagarmatha-Settings-Panel;
OnlyShowIn=X-Sagarmatha;
X-Sagarmatha-Settings-Panel=network
# Translators: those are keywords for the network control-center panel
_Keywords=Network;Wireless;IP;LAN;Proxy;
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/network/sagarmatha-network-panel.desktop.in.in", prefix, _("Network"), _("Network settings"), "")

prefix = """[Desktop Entry]
Exec=sagarmatha-settings universal-access
Icon=cs-universal-access
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Settings;X-Sagarmatha-SystemSettings;X-Sagarmatha-Settings-Panel;
OnlyShowIn=X-Sagarmatha;
X-Sagarmatha-Settings-Panel=universal-access
# Translators: those are keywords for the universal access control-center panel
_Keywords=Keyboard;Mouse;a11y;Accessibility;Contrast;Zoom;Screen Reader;text;font;size;AccessX;Sticky Keys;Slow Keys;Bounce Keys;Mouse Keys;
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/universal-access/sagarmatha-universal-access-panel.desktop.in.in", prefix, _("Universal Access"), _("Universal Access Preferences"), "")

prefix = """[Desktop Entry]
Exec=sagarmatha-control-center datetime
Icon=cs-date-time
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Settings;X-sagarmatha-SystemSettings;X-Sagarmatha-Settings-Panel;
OnlyShowIn=X-Sagarmatha;
X-Sagarmatha-Settings-Panel=datetime
# Translators: those are keywords for the date and time control-center panel
_Keywords=Clock;Timezone;Location;
"""

additionalfiles.generate(DOMAIN, PATH, "./panels/datetime/sagarmatha-datetime-panel.desktop.in", prefix, _("Date & Time"), _("Date and Time preferences"), "")
