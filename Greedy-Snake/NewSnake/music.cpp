#include "music.h"

Music::Music(QObject *parent) : QThread(parent)
{
   playlist = new QMediaPlaylist;
   player.setVolume(30);//音量
   playlist->addMedia(QUrl::fromLocalFile("image\\music\\开场.m4a"));
   playlist->addMedia(QUrl::fromLocalFile("image\\music\\游戏.mp3"));
   playlist->addMedia(QUrl::fromLocalFile("image\\music\\死亡.mp3"));
   playlist->setPlaybackMode(QMediaPlaylist::CurrentItemInLoop);
   currentIndex = playlist->currentIndex();
   player.setPlaylist(playlist);
}


void Music::chose(int type)
{
       musictype = type;
      // qDebug()<<"开始播放音乐";
       switch (musictype) {
       case 1://开场
            playlist->setCurrentIndex(0);
            player.play();
           break;
       case 2://游戏
            playlist->setCurrentIndex(1);
            player.play();
           break;
       case 3://死亡
            playlist->setCurrentIndex(2);
            player.play();
           break;
       case 4://减一
            playlist->setCurrentIndex(3);
            player.play();
           break;
       default:
           break;
       }
}
