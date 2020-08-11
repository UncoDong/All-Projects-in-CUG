package com.sa.Soap;

import com.sa.message.EmailRequest;
import com.sa.message.SenderRequest;
import com.sa.message.SenderResponse;
import com.sa.webserver.SendEmail;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;

@Endpoint
public class SoapEndpoint {
    //发送邮件
    @PayloadRoot(namespace = "http://segmentfault.com/schemas", localPart = "SenderRequest")
    @ResponsePayload
    public SenderResponse getSender(@RequestPayload SenderRequest request) throws UnsupportedEncodingException {
        System.out.println("-----------SOAP-------------");

        //得到信息
        String url = request.getUrl();
        String title = request.getTitle();
        String payload = request.getPayload();
        url = URLDecoder.decode(url,"utf-8");
        title = URLDecoder.decode(title,"utf-8");
        payload = URLDecoder.decode(payload,"utf-8");
        System.out.println(url);
        System.out.println(title);
        System.out.println(payload);
        String satue = null;
        SenderResponse response = new SenderResponse();

        response.setStatue(SendEmail.sendEmail(url, title, "Soap:"+payload));
        System.out.println("-----------SOAP结束-------------");
        return response;

    }

    //判断邮件格式
    @PayloadRoot(namespace = "http://segmentfault.com/schemas", localPart = "EmailRequest")
    @ResponsePayload
    public SenderResponse getSender(@RequestPayload EmailRequest request) throws UnsupportedEncodingException {
        System.out.println("-----------SOAP-------------");

        //得到信息
        String url = request.getUrl();
        url = URLDecoder.decode(url,"utf-8");
        System.out.println(url);
        String satue = null;
        SenderResponse response = new SenderResponse();
        if(SendEmail.validateEmailAddress(url)==true)
            response.setStatue("emailY");
        else
            response.setStatue("emailN");
        System.out.println("-----------SOAP结束-------------");
        return response;

    }
}
