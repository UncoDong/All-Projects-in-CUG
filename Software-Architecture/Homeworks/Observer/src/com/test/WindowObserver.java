package com.test;

import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import java.util.Vector;
import sun.awt.WindowIDProvider;

public class WindowObserver extends JFrame implements Observer {

	String name = null;
	JTextArea textarea = new JTextArea();
	JButton detach = new JButton("取消链接");
	JPanel jp = new JPanel();
	Vector<String>DelName = null;
	
	public WindowObserver(String n,Vector<String>DN) {
		// TODO Auto-generated constructor stub
		textarea.setFont(new Font("黑体",Font.BOLD,20));
		DelName = DN;
		name = n;
		this.setLayout(new GridLayout(2, 1));
		this.add(textarea);
		
		jp.add(detach);
		detach.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				DelName.add(name);
				System.out.println(DelName.size());
				//dispose();
			}
		});
		this.add(jp);
		 this.setSize(350, 150);
	     this.setTitle("观察者"+name);
	     this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	     this.setVisible(true);
	}
	
	@Override
	public void update(String s) {
		// TODO Auto-generated method stub
		textarea.setText(s);
	}
	
	public static void main(String[] args) {
		System.out.println("hello");
		//WindowObserver w = new WindowObserver("1");
	}

}
