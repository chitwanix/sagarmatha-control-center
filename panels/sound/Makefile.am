SUBDIRS = data

# This is used in PANEL_CFLAGS
cappletname = sound
NULL =

bin_PROGRAMS =					\
	sagarmatha-sound-applet			\
	$(NULL)

AM_CPPFLAGS =					\
	$(PANEL_CFLAGS) 			\
	$(SOUND_PANEL_CFLAGS)			\
	-DLOCALE_DIR=\""$(datadir)/locale"\"	\
	-DLIBEXECDIR=\"$(libexecdir)\"		\
	-DGLADEDIR=\""$(pkgdatadir)"\"		\
	-DICON_DATA_DIR="\"$(pkgdatadir)/icons\"" \
	$(NULL)

noinst_LTLIBRARIES = libsagarmathavolumecontrol.la \
                     libsound.la
libsagarmathavolumecontrol_la_SOURCES =		\
	gvc-mixer-card.h			\
	gvc-mixer-card.c			\
	gvc-mixer-card-private.h		\
	gvc-mixer-stream.h			\
	gvc-mixer-stream.c			\
	gvc-mixer-stream-private.h		\
	gvc-channel-map.h			\
	gvc-channel-map.c			\
	gvc-channel-map-private.h		\
	gvc-mixer-ui-device.h			\
	gvc-mixer-ui-device.c			\
	gvc-mixer-sink.h			\
	gvc-mixer-sink.c			\
	gvc-mixer-source.h			\
	gvc-mixer-source.c			\
	gvc-mixer-sink-input.h			\
	gvc-mixer-sink-input.c			\
	gvc-mixer-source-output.h		\
	gvc-mixer-source-output.c		\
	gvc-mixer-event-role.h			\
	gvc-mixer-event-role.c			\
	gvc-mixer-control.h			\
	gvc-mixer-control.c			\
	gvc-mixer-control-private.h		\
	gvc-channel-bar.h			\
	gvc-channel-bar.c			\
	gvc-pulseaudio-fake.h			\
	$(NULL)

sagarmatha_sound_applet_LDADD =			\
	-lm					\
	libsagarmathavolumecontrol.la		\
	$(SOUND_PANEL_LIBS)			\
	$(NULL)

sagarmatha_sound_applet_SOURCES =			\
	gvc-stream-status-icon.h		\
	gvc-stream-status-icon.c		\
	gvc-applet.h				\
	gvc-applet.c				\
	gvc-log.h				\
	gvc-log.c				\
	applet-main.c				\
	$(NULL)

libsound_la_LIBADD =				\
	-lm					\
	libsagarmathavolumecontrol.la		\
	$(PANEL_LIBS)				\
	$(SOUND_PANEL_LIBS)			\
	$(NULL)

libsound_la_LDFLAGS =				\
	$(PANEL_LDFLAGS)			\
	$(NULL)

libsound_la_SOURCES =				\
	gvc-balance-bar.h			\
	gvc-balance-bar.c			\
	gvc-mixer-dialog.h			\
	gvc-mixer-dialog.c			\
	gvc-level-bar.h				\
	gvc-level-bar.c				\
	gvc-combo-box.h				\
	gvc-combo-box.c				\
	gvc-speaker-test.h			\
	gvc-speaker-test.c			\
	cc-sound-panel.c			\
	cc-sound-panel.h			\
	$(NULL)

BUILT_SOURCES =				\
	$(NULL)

CLEANFILES =				\
	$(BUILT_SOURCES)		\
	$(NULL)

MAINTAINERCLEANFILES =                  \
        *~                              \
        Makefile.in

-include $(top_srcdir)/git.mk
