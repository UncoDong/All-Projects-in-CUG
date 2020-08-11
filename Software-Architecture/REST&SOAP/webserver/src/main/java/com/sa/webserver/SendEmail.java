package com.sa.webserver;

import com.aliyuncs.DefaultAcsClient;
import com.aliyuncs.IAcsClient;
import com.aliyuncs.dm.model.v20151123.SingleSendMailRequest;
import com.aliyuncs.dm.model.v20151123.SingleSendMailResponse;
import com.aliyuncs.exceptions.ClientException;
import com.aliyuncs.exceptions.ServerException;
import com.aliyuncs.profile.DefaultProfile;
import com.aliyuncs.profile.IClientProfile;

import java.io.PrintWriter;
import java.io.StringWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SendEmail {
    //判断是否有效
    static public boolean 	validateEmailAddress(String _url)
    {
        String regex = "^\\w+([-+.]\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(_url);
        return  matcher.matches();  // matches返回false
    }

    public static String sendEmail(String _url,String _title,String _payload) {
        StringBuffer RecvAdress = new StringBuffer();
        String[] strarray=_url.split(",");
        List<String> anslist = new ArrayList<>();
        for (int i = 0; i < strarray.length; i++)
        {
            if(validateEmailAddress(strarray[i])==true)
                anslist.add(strarray[i]);
        }

        if(anslist.size()==0)return "wrong";
        else
        {
            _url = "";
            for(String each:anslist)
            {
                RecvAdress.append(each);
                RecvAdress.append(",");
            }
            RecvAdress.delete(RecvAdress.length()-1, RecvAdress.length());
            _url = RecvAdress.toString();
        }


        // 如果是除杭州region外的其它region（如新加坡、澳洲Region），需要将下面的"cn-hangzhou"替换为"ap-southeast-1"、或"ap-southeast-2"。
        IClientProfile profile = DefaultProfile.getProfile("cn-hangzhou ", "你的号", "你的tkoen");
        IAcsClient client = new DefaultAcsClient(profile);
        SingleSendMailRequest request = new SingleSendMailRequest();
        try {
            //request.setVersion("2017-06-22");// 如果是除杭州region外的其它region（如新加坡region）,必须指定为2017-06-22
            request.setAccountName("dan@uncledong.xyz");
            request.setFromAlias("DAN");
            request.setAddressType(1);
            request.setTagName("TestMessage");
            request.setReplyToAddress(true);
            request.setToAddress(_url);
            //可以给多个收件人发送邮件，收件人之间用逗号分开，批量发信建议使用BatchSendMailRequest方式
            //request.setToAddress("邮箱1,邮箱2");
            request.setSubject(_title);
            request.setHtmlBody(_payload);
            //如果调用成功，正常返回httpResponse；如果调用失败则抛出异常，需要在异常中捕获错误异常码；错误异常码请参考对应的API文档;
            SingleSendMailResponse httpResponse = client.getAcsResponse(request);

            System.out.println(httpResponse);
        } catch (ServerException e) {
            //捕获错误异常码

            System.out.println("ErrCode : " + e.getErrCode());
            e.printStackTrace();
//            final Writer result = new StringWriter();
//            final PrintWriter print = new PrintWriter(result);
//            e.printStackTrace(print);

            //return result.toString();
            return "wrong";

        } catch (ClientException e) {
            e.printStackTrace();
//            final Writer result = new StringWriter();
//            final PrintWriter print = new PrintWriter(result);
//            e.printStackTrace(print);
            //return result.toString();
            return "wrong";

        }
        //return "向"+_url+"发送"+_payload+"成功！";
        return "yes";

    }
}
