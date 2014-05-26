# This is used in PANEL_CFLAGS
cappletname = region

INCLUDES =						\
	$(PANEL_CFLAGS)					\
	$(REGION_PANEL_CFLAGS)				\
	-DLOCALE_DIR="\"$(datadir)/locale\""	\
	-DCINNAMONCC_DATA_DIR="\"$(pkgdatadir)\""		\
	-DCINNAMONCC_UI_DIR="\"$(uidir)\""			\
	-I$(srcdir)/../common/				\
	$(NULL)

ccpanelsdir = $(PANELS_DIR)
ccpanels_LTLIBRARIES = libregion.la

libregion_la_SOURCES =	\
	region-module.c \
	cc-region-panel.c \
	cc-region-panel.h \	
	sagarmatha-region-panel-xkb.c \
	sagarmatha-region-panel-xkblt.c \
	sagarmatha-region-panel-xkbltadd.c \
	sagarmatha-region-panel-xkbot.c \
	sagarmatha-region-panel-xkbpv.c \
	sagarmatha-region-panel-xkb.h

libregion_la_LIBADD = $(PANEL_LIBS) $(REGION_PANEL_LIBS) $(builddir)/../common/liblanguage.la

libregion_la_LDFLAGS = $(PANEL_LDFLAGS)

@INTLTOOL_DESKTOP_RULE@

uidir   = $(pkgdatadir)/ui
ui_DATA = \
	sagarmatha-region-panel.ui \
	sagarmatha-region-panel-layout-chooser.ui \
	sagarmatha-region-panel-options-dialog.ui

desktopdir = $(datadir)/applications
Desktop_in_files = sagarmatha-region-panel.desktop.in
desktop_DATA = $(Desktop_in_files:.desktop.in=.desktop)

CLEANFILES = $(Desktop_in_files) $(desktop_DATA)
EXTRA_DIST = $(ui_DATA)


-include $(top_srcdir)/git.mk
