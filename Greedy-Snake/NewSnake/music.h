#ifndef MUSIC_H
#define MUSIC_H

#include <QObject>
#include<QDebug>
#include<QMediaPlayer>
#include<QThread>
#include<QMediaPlaylist>
class Music : public QThread
{
    Q_OBJECT
    int musictype;
    QMediaPlaylist *playlist;
     QMediaPlayer player;
     int currentIndex;
public:

    explicit Music(QObject *parent = nullptr);

    void chose(int type);//切歌


protected:


signals:


public slots:
};

#endif // MUSIC_H
