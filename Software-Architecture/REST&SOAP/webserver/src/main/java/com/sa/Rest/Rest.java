package com.sa.Rest;

import com.sa.webserver.SendEmail;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.net.URLDecoder;

@Controller
public class Rest {
    @RequestMapping("/test1")
    public String Test(){
        return "lalalala";
    }
    @RequestMapping("/index")
    public String VisIndex(){ return "index"; }
    //发送邮件
    @RequestMapping(value = "/send")
    public String GetInfoMation(@RequestParam(name = "url") String url,//邮箱地址
                                @RequestParam(name = "title") String title,//文件标题
                                @RequestParam(name = "payload") String payload)  {//输入内容
        System.out.println("-----------REST-------------");

        try{
            url = URLDecoder.decode(url,"utf-8");
            title = URLDecoder.decode(title,"utf-8");
            payload = URLDecoder.decode(payload,"utf-8");
            System.out.println(url);
            System.out.println(title);
            System.out.println(payload);
            System.out.println("-----------REST结束-------------");
            return SendEmail.sendEmail(url, title, "Rest:"+payload);
        }
        catch (Exception e){
            e.printStackTrace();
            return "wrong";
        }
    }
    //验证邮件格式
    @RequestMapping(value = "/email")
    public String PanEmail(@RequestParam(name = "url") String url)
    {
        if(SendEmail.validateEmailAddress(url)==true)
            return "emailY";
        else
            return "emailN";
    }

}
