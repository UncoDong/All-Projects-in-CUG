#include "music.h"

Music::Music(QObject *parent) : QThread(parent)
{
   playlist = new QMediaPlaylist;
   player.setVolume(100);//音量
   playlist->addMedia(QUrl::fromLocalFile("happy.mp3"));
   playlist->setPlaybackMode(QMediaPlaylist::CurrentItemInLoop);
   currentIndex = playlist->currentIndex();

   player.setPlaylist(playlist);
   playlist->setCurrentIndex(0);
   player.play();
}


void Music::chose(int type)
{
       musictype = type;

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
