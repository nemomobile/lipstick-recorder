
#include <QGuiApplication>

#include "recorder.h"

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    Recorder recorder;
    return app.exec();
}
