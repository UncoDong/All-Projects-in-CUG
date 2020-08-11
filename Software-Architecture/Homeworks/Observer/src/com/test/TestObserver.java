package com.test;

import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Map;
import java.util.Vector;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextArea;

public class TestObserver extends JFrame  {
	Map<String,Observer>Name2Observer = new HashMap<String, Observer>();
	Vector<String>DelName = new Vector<String>();
	static ConcreteSubject sbj = new ConcreteSubject();
	
	int index = 0;
	JTextArea textarea = new JTextArea();
	JButton send = new JButton("发送");
	JButton new_ = new JButton("新建一个观察者");
	JPanel jp = new JPanel();
	
	public TestObserver() {
		textarea.setFont(new Font("黑体",Font.BOLD,20));
		this.setLayout(new GridLayout(2, 1));
		this.add(textarea);
		jp.add(send);
		 send.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				for(String key:DelName)
				{
					sbj.detach(Name2Observer.get(key));
					Name2Observer.remove(key);
				}
				DelName.clear();
				sbj.notifyObservers(textarea.getText());
			}
		});
		
		jp.add(new_);
		new_.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				index+=1;
				Observer co = new WindowObserver(Integer.toString(index),DelName);
				sbj.attcah(co);
				Name2Observer.put(Integer.toString(index), co);
			}
		});
		
		this.add(jp);
		 this.setSize(400, 150);
	     this.setTitle("发布者");
	     this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	     this.setVisible(true);
		
	}
	public static void main(String[] args) {

		TestObserver t = new TestObserver();
	}
}
