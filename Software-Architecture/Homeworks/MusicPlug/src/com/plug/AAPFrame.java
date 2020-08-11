package com.plug;


import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class AAPFrame extends JFrame {
	
	JPanel jp1, jp2, jp3,jp4;
	JLabel jlb1, jlb2,jlb3;
	JTextField jtf1,jtf2,jtf3;
	JButton jb;
	JComboBox xiala;
	public AAPFrame() {
		this.setLayout(new GridLayout(4, 1));
		jp1 = new JPanel();
	    jp2 = new JPanel();
	    jp3 = new JPanel();
	    jp4 = new JPanel();
	    
	    jlb1 = new JLabel("插件包名");
	    jlb2 = new JLabel("插件地址");
	    jlb3 = new JLabel("文件地址");
	    
	    
	    jtf1 = new JTextField(40);
	    jtf1.setText("com.mp3.MP3PlayerPlugin");
	    jtf2 = new JTextField(40);
	    jtf2.setText("D:\\myjava\\MP3PlayerPlugin\\MP3PlayerPlugin.jar");
	    jtf3 = new JTextField(40);
	    jtf3.setText("C:/Users/UncleDong/Desktop/TestFile/1234567.mp3");
	    
	    jp1.add(jlb1);
	    jp1.add(jtf1);
	    jp2.add(jlb2);
	    jp2.add(jtf2);
	    jp3.add(jlb3);
	    jp3.add(jtf3);
	    
	    jb = new JButton("播放");
	       
	    jb.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				try {
				// TODO Auto-generated method stub
				Plugin p = new Plugin();
				
				//p.setClassName("com.mp3.MP3PlayerPlugin");
				//p.setJar("D:\\myjava\\MP3PlayerPlugin\\MP3PlayerPlugin.jar");
				
				//p.setClassName("com.wav.WAVPlayerPlugin2");
				//p.setJar("D:\\myjava\\WAVPlayerPlugin\\WAVPlayerPlugin2.jar");
				
				p.setClassName(jtf1.getText());
				p.setJar(jtf2.getText());
				IPlayerPlugin player;
				player = p.getInstance();
				player.play(jtf3.getText());
				} catch (Exception e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
					 //JOptionPane.showMessageDialog(hi, "你的内容");
					JOptionPane.showMessageDialog(null, "路径配置有误", "警告", JOptionPane.ERROR_MESSAGE);
				}
				
			}
		});
	    jp4.add(jb);
	    
	    this.add(jp1);
	    this.add(jp2);
	    this.add(jp3);
	    this.add(jp4);
	        
		
		// TODO Auto-generated constructor stub
		this.setSize(350, 250);
	     this.setTitle("音乐播放");
	     this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	     this.setVisible(true);
	}
public static void main(String[] args) throws Exception  {
	
	AAPFrame a = new AAPFrame();
//	Plugin p = new Plugin();
//	//p.setClassName("com.wav.WAVPlayerPlugin2");
//	//p.setJar("D:\\myjava\\WAVPlayerPlugin\\WAVPlayerPlugin2.jar");
//	p.setClassName("com.mp3.MP3PlayerPlugin");
//	p.setJar("D:\\myjava\\MP3PlayerPlugin\\MP3PlayerPlugin.jar");
//	IPlayerPlugin player = p.getInstance();
//	
//	try {
//		player.play("C:\\Users\\UncleDong\\Desktop\\TestFile\\1234567.mp3");
//	} catch (Exception e) {
//		// TODO: handle exception
//		System.out.println(e);
//	}
//	
}

}
