cappletname = info

INCLUDES = 						\
	$(PANEL_CFLAGS)					\
	$(INFO_PANEL_CFLAGS)				\
	-DSAGARMATHACC_UI_DIR="\"$(uidir)\""			\
	-DSAGARMATHALOCALEDIR="\"$(datadir)/locale\""	\
	-DSAGARMATHACC_DATA_DIR="\"$(pkgdatadir)\""		\
	-DDATADIR="\"$(datadir)\""			\
	-DLIBEXECDIR="\"$(libexecdir)\""		\
	$(NULL)

noinst_PROGRAMS = test-hostname
test_hostname_SOURCES = hostname-helper.c hostname-helper.h test-hostname.c
test_hostname_LDADD = $(PANEL_LIBS) $(INFO_PANEL_LIBS)
test_hostname_CFLAGS = $(INCLUDES)

all-local: check-local

check-local: test-hostname
	$(builddir)/test-hostname $(srcdir)/hostnames-test.txt > /dev/null

ccpanelsdir = $(PANELS_DIR)
ccpanels_LTLIBRARIES = libinfo.la

libinfo_la_SOURCES =		\
	info-module.c		\
	cc-info-panel.c		\
	cc-info-panel.h		\
	hostname-helper.c	\
	hostname-helper.h	\
	gsd-disk-space-helper.h	\
	gsd-disk-space-helper.c

libinfo_la_LIBADD = $(PANEL_LIBS) $(INFO_PANEL_LIBS)
libinfo_la_LDFLAGS = $(PANEL_LDFLAGS)

uidir = $(pkgdatadir)/ui
dist_ui_DATA = info.ui sagarmatha.png

@INTLTOOL_DESKTOP_RULE@

desktopdir = $(datadir)/applications
desktop_in_files = sagarmatha-info-panel.desktop.in
desktop_DATA = $(desktop_in_files:.desktop.in=.desktop)

SPACEDIR=$(top_srcdir)/../gnome-settings-daemon/plugins/housekeeping/
SPACEFILES=gsd-disk-space-helper.c gsd-disk-space-helper.h
update-from-gsd:
	FILES="$(SPACEFILES)" DIR="$(SPACEDIR)" $(top_srcdir)/update-from-gsd.sh && changed=true ; \
	git commit -m "info: Update from gnome-settings-daemon" $(SPACEFILES)

CLEANFILES = $(desktop_in_files) $(desktop_DATA)
EXTRA_DIST = hostnames-test.txt

-include $(top_srcdir)/git.mk
