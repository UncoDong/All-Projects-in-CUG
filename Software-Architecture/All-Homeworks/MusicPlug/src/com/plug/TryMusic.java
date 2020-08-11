package com.plug;
import java.io.FileInputStream;
import sun.audio.AudioPlayer;
import sun.audio.AudioStream;
public class TryMusic {
	
	static public void PlayMusic(String s)
	{
		try {
			FileInputStream fileau=new FileInputStream(s);
			AudioStream as=new AudioStream(fileau);
			AudioPlayer.player.start(as);
			}
			catch (Exception e) {
				System.out.println(e);
			}
		}
	
	public static void main(String[] args) {
		//TryMusic.PlayMusic("C:\\Users\\UncleDong\\Music\\Toby Fox - Power of NEO.mp3");
		TryMusic.PlayMusic("C:\\Users\\UncleDong\\Desktop\\lab\\“∆∂Øº∆À„\\FFT√‘Àº\\1234567.wav");
	}


}
