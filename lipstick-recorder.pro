TEMPLATE = app
TARGET = lipstick-recorder
VERSION = 0.0.1

target.path += /usr/bin
INSTALLS += target

CONFIG += wayland-scanner link_pkgconfig
QT += platformsupport-private
PKGCONFIG += wayland-client
WAYLANDCLIENTSOURCES += protocol/lipstick-recorder.xml

SOURCES += \
    src/main.cpp \
    src/recorder.cpp \

HEADERS += \
    src/recorder.h \
