package com.sa.cilent;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CilentUI extends JFrame {
    // 定义组件
    //构件
    static JPanel jp1, jp2, jp3,jp4,jp5;
    //标签
    static JLabel url_label, title_label, payload_label;
    //发送按钮
    static JButton restsend,soapsend,testurl;
    //输入框
    static JTextField url_input, title_input;
    //创建文本域
    static JTextArea payload_text;

    static void init() {
        //新建构件
        jp1 = new JPanel();
        jp2 = new JPanel();
        jp3 = new JPanel();
        jp4 = new JPanel();
        jp5 = new JPanel();

        //标签
        url_label = new JLabel("地址");
        title_label = new JLabel("桌面端标题");
        payload_label = new JLabel("   桌面端正文");

        //按钮
        restsend = new JButton("Rest发送");
        soapsend = new JButton("Soap发送");
        testurl = new JButton("测试地址");

        //输入框
        url_input = new JTextField(15);
        url_input.setText("1758322248@qq.com");
        title_input = new JTextField(15);
        title_input.setText("来自桌面的标题");

        //文本域
        payload_text = new JTextArea(15,40);
        payload_text.setText("来自桌面的文件内容");
        payload_text.setLineWrap(true);

        //放邮箱输入
        jp1.add(url_label);
        jp1.add(url_input);
        //放标题输入
        jp2.add(title_label);
        jp2.add(title_input);
        //放入文本框
        jp3.add(payload_label);
        jp4.add(payload_text);
        //放入按钮
        jp5.add(restsend);
        jp5.add(soapsend);
        jp5.add(testurl);

        restsend.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String url = url_input.getText();
                String title = title_input.getText();
                String payload = payload_text.getText();
                try {

                    WebServicesClient s = new WebServicesClient();
                    s.SetParameter(url,title,payload);
                    s.RestRequest();
                } catch (Exception ex) {
                    ex.printStackTrace();
                }
            }
        });

        soapsend.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String url = url_input.getText();
                String title = title_input.getText();
                String payload = payload_text.getText();
                try {

                    WebServicesClient s = new WebServicesClient();
                    s.SetParameter(url,title,payload);
                    s.SoapRequest();
                } catch (Exception ex) {
                    ex.printStackTrace();
                }
            }
        });

        testurl.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String url = url_input.getText();

                try {

                    WebServicesClient s = new WebServicesClient();
                    s.SetUrl(url);
                    s.URLRequest();
                } catch (Exception ex) {
                    ex.printStackTrace();
                }
            }
        });

    }


    public CilentUI() {
        //布局策略
        this.setLayout(new GridLayout(5, 1));
        init();
        this.add(jp1);
        this.add(jp2);
        //this.add(payload_text);
        this.add(jp3);
        this.add(jp4);
        this.add(jp5);
        this.setSize(300, 250);
        this.setTitle("登录");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setVisible(true);
    }

    public static void main(String[] args) {
         CilentUI s = new CilentUI();

    }
}
