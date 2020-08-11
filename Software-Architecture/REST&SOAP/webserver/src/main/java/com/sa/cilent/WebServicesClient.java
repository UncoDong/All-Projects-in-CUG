package com.sa.cilent;

import com.sa.message.EmailRequest;
import com.sa.message.SenderRequest;
import com.sa.message.SenderResponse;
import org.springframework.http.*;

import org.springframework.web.client.RestTemplate;

import org.springframework.ws.client.core.WebServiceTemplate;
import org.springframework.oxm.jaxb.Jaxb2Marshaller;
import sun.net.www.http.HttpClient;

import java.io.*;
import java.net.*;
import java.time.Instant;

/**
 * Web Service 客户端（Spring 实现）
 */
public class WebServicesClient {
   static String url = "1758322248@qq.com,123";
   static String title = "来自发送测试的标题";
   static String payload = "发送测试的文本内容";




    public static void SoapTest() throws UnsupportedEncodingException {
        url =  URLEncoder.encode(url,"utf-8");
        title = URLEncoder.encode(title,"utf-8");
        payload = URLEncoder.encode(payload,"utf-8");

        RestTemplate restTemplate =  new RestTemplate();

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.TEXT_XML);

        String xmlString =
                "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:sch=\"http://segmentfault.com/schemas\">" +
                        "<soapenv:Header/>" +
                        "<soapenv:Body>" +
                        "<sch:SenderRequest>" +
                        "<sch:url>"+url+"</sch:url>" +
                        "<sch:title>"+title+"</sch:title>" +
                        "<sch:payload>"+payload+"</sch:payload>" +
                        "</sch:SenderRequest>" +
                        "</soapenv:Body>" +
                        "</soapenv:Envelope>";

        HttpEntity<String> formEntity = new HttpEntity<>(xmlString,headers);
        ResponseEntity<String> responseEntity = restTemplate.postForEntity("http://localhost:8080/test/ws/my", formEntity, String.class);

        System.out.println( responseEntity.getBody());
    }
    public static void SoapTest2() throws Exception{
//        url = URLEncoder.encode(url,"utf-8");
//        title = URLEncoder.encode(title,"utf-8");
//        payload = URLEncoder.encode(payload,"utf-8");

        String input = "http://49.234.124.119:8080/test/ws/my";
        System.out.println(input);
        //创建HTTP连接对象
        URL obj = new URL(input);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        //添加HTTP请求头
        con.setRequestProperty("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) ...");
        con.setRequestProperty("Accept-Language", "en-US,en;q=0.5");
        con.setRequestProperty("Content-Type", "text/xml");
        //设置POST请求方法
        con.setRequestMethod("POST");
        con.setDoOutput(true);
        DataOutputStream wr = new DataOutputStream(con.getOutputStream());
        String xmlString =
                "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:sch=\"http://segmentfault.com/schemas\">" +
                        "<soapenv:Header/>" +
                        "<soapenv:Body>" +
                        "<sch:SenderRequest>" +
                        "<sch:url>"+url+"</sch:url>" +
                        "<sch:title>"+title+"</sch:title>" +
                        "<sch:payload>"+payload+"</sch:payload>" +
                        "</sch:SenderRequest>" +
                        "</soapenv:Body>" +
                        "</soapenv:Envelope>";
        wr.writeBytes(xmlString);
        wr.flush();
        wr.close();
        //读取服务端返回的数据

        int responseCode = con.getResponseCode();
        String responseBody = readResponseBody(con.getInputStream());
        responseBody = URLDecoder.decode(responseBody,"utf-8");
        System.out.println(responseBody);
    }

    public static void SoapTest3() throws Exception {
        url = URLEncoder.encode(url,"utf-8");
        title = URLEncoder.encode(title,"utf-8");
        payload = URLEncoder.encode(payload,"utf-8");
        String urlStr = "http://49.234.124.119:8080/test/ws/my";

        URL url = new URL(urlStr);
        URLConnection con = url.openConnection();
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
        BufferedReader br = new BufferedReader(new InputStreamReader(con
                .getInputStream()));
        String line = "";
        for (line = br.readLine(); line != null; line = br.readLine()) {
            System.out.println(line);
        }
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
    public static void RestRequest() throws Exception {

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
    }

    public static void SoapRequest() throws UnsupportedEncodingException {
        url = URLEncoder.encode(url,"utf-8");
        title = URLEncoder.encode(title,"utf-8");
        payload = URLEncoder.encode(payload,"utf-8");
        WebServiceTemplate webServiceTemplate = new WebServiceTemplate();
        //新建转换
        Jaxb2Marshaller jaxb2Marshaller = new Jaxb2Marshaller();
        jaxb2Marshaller.setClassesToBeBound(SenderRequest.class, SenderResponse.class);
        //设置转换
        webServiceTemplate.setMarshaller(jaxb2Marshaller);
        webServiceTemplate.setUnmarshaller(jaxb2Marshaller);
        //构造 SOAP 请求
        SenderRequest request = new SenderRequest();

        request.setUrl(url);
        request.setTitle(title);
        request.setPayload(payload);
        //收到回复
        SenderResponse response = (SenderResponse) webServiceTemplate.marshalSendAndReceive(
                "http://49.234.124.119:8080/test/ws/my", request);
        //输出回复结果
        System.out.println(response.getStatue());
    }

    public static void URLRequest() throws UnsupportedEncodingException {
        url = URLEncoder.encode(url,"utf-8");
        WebServiceTemplate webServiceTemplate = new WebServiceTemplate();
        //新建转换
        Jaxb2Marshaller jaxb2Marshaller = new Jaxb2Marshaller();
        jaxb2Marshaller.setClassesToBeBound(EmailRequest.class, SenderResponse.class);
        //设置转换
        webServiceTemplate.setMarshaller(jaxb2Marshaller);
        webServiceTemplate.setUnmarshaller(jaxb2Marshaller);
        //构造 SOAP 请求
        EmailRequest request = new EmailRequest();

        request.setUrl(url);
        //收到回复
        SenderResponse response = (SenderResponse) webServiceTemplate.marshalSendAndReceive(
                "http://49.234.124.119:8080/test/ws/my", request);
        //输出回复结果
        System.out.println(response.getStatue());
    }

    //传入参数
    public void SetParameter(String url, String title, String payload){
        this.url = url;
        this.title = title;
        this.payload = payload;

    }

    //只传入URL
    public void SetUrl(String url){
        this.url = url;

    }


    public static void main(String[] args) {
        try {
            SoapTest3();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
