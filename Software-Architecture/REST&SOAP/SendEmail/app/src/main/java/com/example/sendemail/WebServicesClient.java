package com.example.sendemail;


import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLDecoder;
import java.net.URLEncoder;
/**
 * Web Service 客户端（Spring 实现）
 */
public class WebServicesClient {
   static String url = "1758322248@qq.com";
   static String title = "来自发送测试的标题";
   static String payload = "发送测试的文本内容";

    public static String SoapRequest() throws Exception {
        url = URLEncoder.encode(url,"utf-8");
        title = URLEncoder.encode(title,"utf-8");
        payload = URLEncoder.encode(payload,"utf-8");
        String urlStr = "http://49.234.124.119:8080/test/ws/my";

        URL _url = new URL(urlStr);
        URLConnection con = _url.openConnection();
        con.setDoOutput(true);
        con.setRequestProperty("Pragma", "no-cache");
        con.setRequestProperty("Cache-Control", "no-cache");
        con.setRequestProperty("Content-Type", "text/xml");

        OutputStreamWriter out = new OutputStreamWriter(con
                .getOutputStream());
        String xmlInfo = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:sch=\"http://segmentfault.com/schemas\">" +
                "<soapenv:Header/>" +
                "<soapenv:Body>" +
                "<sch:SenderRequest>" +
                "<sch:url>" + url + "</sch:url>" +
                "<sch:title>" + title + "</sch:title>" +
                "<sch:payload>" + payload + "</sch:payload>" +
                "</sch:SenderRequest>" +
                "</soapenv:Body>" +
                "</soapenv:Envelope>";
        System.out.println("urlStr=" + urlStr);
        System.out.println("xmlInfo=" + xmlInfo);
        out.write(new String(xmlInfo.getBytes("ISO-8859-1")));
        out.flush();
        out.close();
        StringBuffer returnmessage = new StringBuffer();

        BufferedReader br = new BufferedReader(new InputStreamReader(con
                .getInputStream()));
        String line = "";
        for (line = br.readLine(); line != null; line = br.readLine()) {
            System.out.println(line);
            returnmessage.append(line);
        }
        return returnmessage.toString();
    }

    //验证邮件
    public static String EmailRequest() throws Exception {
        url = URLEncoder.encode(url,"utf-8");
        String urlStr = "http://49.234.124.119:8080/test/ws/my";

        URL _url = new URL(urlStr);
        URLConnection con = _url.openConnection();
        con.setDoOutput(true);
        con.setRequestProperty("Pragma", "no-cache");
        con.setRequestProperty("Cache-Control", "no-cache");
        con.setRequestProperty("Content-Type", "text/xml");

        OutputStreamWriter out = new OutputStreamWriter(con
                .getOutputStream());
        String xmlInfo = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:sch=\"http://segmentfault.com/schemas\">" +
                "<soapenv:Header/>" +
                "<soapenv:Body>" +
                "<sch:EmailRequest>" +
                "<sch:url>" + url + "</sch:url>" +
                "</sch:EmailRequest>" +
                "</soapenv:Body>" +
                "</soapenv:Envelope>";
        System.out.println("urlStr=" + urlStr);
        System.out.println("xmlInfo=" + xmlInfo);
        out.write(new String(xmlInfo.getBytes("ISO-8859-1")));
        out.flush();
        out.close();
        StringBuffer returnmessage = new StringBuffer();

        BufferedReader br = new BufferedReader(new InputStreamReader(con
                .getInputStream()));
        String line = "";
        for (line = br.readLine(); line != null; line = br.readLine()) {
            System.out.println(line);
            returnmessage.append(line);
        }
        return returnmessage.toString();
    }


    // 读取输入流中的数据
    static private String readResponseBody(InputStream inputStream) throws IOException {

        BufferedReader in = new BufferedReader(
                new InputStreamReader(inputStream));
        String inputLine;
        StringBuffer response = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        return response.toString();
    }

    //Rest消息发送
    public static String RestRequest() throws Exception {

        url = URLEncoder.encode(url,"utf-8");
        title = URLEncoder.encode(title,"utf-8");
        payload = URLEncoder.encode(payload,"utf-8");

        String input = "http://49.234.124.119:8080/send?url="+url+"&title="+title+"&payload="+payload;
        System.out.println(input);
        //创建HTTP连接对象
        URL obj = new URL(input);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        //添加HTTP请求头
        con.setRequestProperty("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) ...");
        con.setRequestProperty("Accept-Language", "en-US,en;q=0.5");
        //设置GET请求方法
        con.setRequestMethod("GET");
        //读取服务端返回的数据
        int responseCode = con.getResponseCode();
        String responseBody = readResponseBody(con.getInputStream());
        responseBody = URLDecoder.decode(responseBody,"utf-8");
        System.out.println(responseBody);
        return responseBody;
    }

    //只传入URL
    public void SetUrl(String url){
        this.url = url;

    }

    public void SetParameter(String url, String title, String payload){
        this.url = url;
        this.title = title;
        this.payload = payload;

    }


    public static void main(String[] args) {
        try {
            //SoapRequest();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
