package com.sample;

import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Vector;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

import org.kie.api.KieServices;
import org.kie.api.runtime.KieContainer;
import org.kie.api.runtime.KieSession;

/**
 * This is a sample class to launch a rule.
 */
public class DroolsTest extends JFrame {
	String name = null;
	JLabel testscore = new JLabel("输入成绩");
	JLabel testshow = new JLabel("输出等级");
	JTextField score = new JTextField(10);
	JTextField show = new JTextField(10);
	JButton search = new JButton("查询");
	JPanel jp1 = new JPanel();
	JPanel jp2 = new JPanel();
	JPanel jp3 = new JPanel();
	public void init()
	{
		testscore.setFont(new Font("黑体",Font.BOLD,20));
		testshow.setFont(new Font("黑体",Font.BOLD,20));
		score.setFont(new Font("黑体",Font.BOLD,20));
		show.setFont(new Font("黑体",Font.BOLD,20));
		
		this.setLayout(new GridLayout(3, 1));
		
		jp1.add(testscore);
		jp1.add(score);
		
		jp2.add(testshow);
		jp2.add(show);
		
		jp3.add(search);
		
		this.add(jp1);
		this.add(jp2);
		this.add(jp3);
		
		
		
		
		}
	
	public DroolsTest() {
		init();
		KieServices ks = KieServices.Factory.get();
	    KieContainer kContainer = ks.getKieClasspathContainer();
    	KieSession kSession = kContainer.newKieSession("ksession-rules");
		search.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				try {
					System.out.println(Integer.parseInt( score.getText()));
				Score s = new Score(Integer.parseInt( score.getText()));
				kSession.insert(s);
                kSession.fireAllRules();
				show.setText(s.GetOutput());
				}
				catch (Exception e2) {
					// TODO: handle exception
					show.setText("输入不合法");
				}
				
				//dispose();
			}
		});
		this.setSize(350, 150);
		this.setTitle("专家系统");
	    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    this.setVisible(true);
		
	}
	
    public static final void main(String[] args) {
    	
    	DroolsTest dro = new DroolsTest();
    	/*
        try {
            // load up the knowledge base
	        

            // go !
            Message message = new Message();
            message.setMessage("Hello World");
            message.setStatus(Message.HELLO);
            
            kSession.insert(message);
            
            kSession.fireAllRules();
        } catch (Throwable t) {
            t.printStackTrace();
        }
        */
    }

    public static class Score {
    	public String output = null;
    	public int score;
        Score(int Score){
            score = Score;
        }
        
        public int getScore() {
            return score;
        }
        
        public void SetOutput(String s){
        	output = s;
        }
        
        public String GetOutput(){
        	return output;
        }
    }

}
