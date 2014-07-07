INCLUDES =					\
	-I$(top_srcdir)				\
	$(SHELL_CFLAGS)

bin_PROGRAMS = sagarmatha-control-center

MARSHAL_FILES = cc-shell-marshal.c cc-shell-marshal.h
BUILT_SOURCES = $(MARSHAL_FILES)

cc-shell-marshal.h: cc-shell-marshal.list
	$(AM_V_GEN) $(GLIB_GENMARSHAL) --prefix=cc_shell_marshal $< --header > $@

cc-shell-marshal.c: cc-shell-marshal.list
	$(AM_V_GEN) $(GLIB_GENMARSHAL) --prefix=cc_shell_marshal $< --body --header > $@

sagarmatha_control_center_SOURCES =			\
	control-center.c			\
	cc-shell-log.c				\
	cc-shell-log.h				\
	sagarmatha-control-center.c			\
	sagarmatha-control-center.h			\
	cc-shell-category-view.c		\
	cc-shell-category-view.h		\
	cc-shell-item-view.c			\
	cc-shell-item-view.h			\
	cc-shell-model.c			\
	cc-shell-model.h			\
	cc-shell-nav-bar.c			\
	cc-shell-nav-bar.h			\
	$(MARSHAL_FILES)

sagarmatha_control_center_LDADD =			\
	libsagarmatha-control-center.la		\
	$(SHELL_LIBS)

sagarmatha_control_center_LDFLAGS = -export-dynamic

lib_LTLIBRARIES = libsagarmatha-control-center.la

libsagarmatha_control_center_include_HEADERS =      \
	cc-panel.h                              \
	cc-shell.h                              \
	cc-editable-entry.h			\
	$(NULL)

libsagarmatha_control_center_la_SOURCES =		\
	cc-panel.c				\
	cc-panel.h				\
	cc-shell.c				\
	cc-shell.h				\
	cc-editable-entry.c			\
	cc-editable-entry.h			\
	$(NULL)

libsagarmatha_control_center_la_LDFLAGS =		\
	-no-undefined				\
	-version-info $(LIBSAGARMATHACONTROLCENTER_CURRENT):$(LIBSAGARMATHACONTROLCENTER_REVISION):$(LIBSAGARMATHACONTROLCENTER_AGE) \
	$(NULL)

libsagarmatha_control_center_la_LIBADD = 		\
	$(LIBSAGARMATHA_CONTROL_CENTER_LIBS)		\
	$(NULL)

libsagarmatha_control_center_la_LIBTOOLFLAGS = --tag=disable-static

libsagarmatha_control_center_includedir = $(includedir)/sagarmatha-control-center-1/libsagarmatha-control-center

pkgconfigdir=$(libdir)/pkgconfig
pkgconfig_DATA=libsagarmatha-control-center.pc

AM_CPPFLAGS =							\
	-DSAGARMATHALOCALEDIR="\"$(datadir)/locale\""		\
	-DUIDIR="\"$(uidir)\""					\
	-DMENUDIR="\"$(menudir)\""				\
	-DPANELS_DIR="\"$(PANELS_DIR)\""

menudir = $(sysconfdir)/xdg/menus
menu_DATA = sagarmathacc.menu

sagarmathacc.menu: sagarmathacc.menu.in
	$(AM_V_GEN) cat $< | sed 's,@applicationsdir@,$(datadir)/applications/,' > $@

uidir = $(pkgdatadir)/ui
ui_DATA = shell.ui

sysdir = $(datadir)/applications
sys_in_files = sagarmatha-control-center.desktop.in
sys_DATA = $(sys_in_files:.desktop.in=.desktop)
@INTLTOOL_DESKTOP_RULE@

directorydir = $(datadir)/desktop-directories
directory_in_files = sagarmathacc.directory.in
directory_DATA = $(directory_in_files:.directory.in=.directory)
@INTLTOOL_DIRECTORY_RULE@

EXTRA_DIST =					\
	$(ui_DATA)				\
	sagarmatha-control-center.desktop.in.in	\
	sagarmathacc.directory.in			\
	sagarmathacc.menu.in				\
	libsagarmatha-control-center.pc.in  \
	cc-shell-marshal.list

DISTCLEANFILES = sagarmatha-control-center.desktop sagarmatha-control-center.desktop.in sagarmathacc.directory sagarmathacc.menu

-include $(top_srcdir)/git.mk
