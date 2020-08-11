package com.sa.Soap;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.ws.wsdl.wsdl11.DefaultWsdl11Definition;
import org.springframework.ws.wsdl.wsdl11.Wsdl11Definition;
import org.springframework.xml.xsd.SimpleXsdSchema;
import org.springframework.xml.xsd.XsdSchema;

@Configuration
public class SoapConfiguration {
    /**
     *     设置访问路径：@Bean("my")，案例：http://localhost:8080/test/ws/my.wsdl
     * 其中，wsdl是MessageDispatcherServlet中规定的结尾
     * @param userXsdSchema @Autowired自动装配下方的userXsdSchema
     * @return Wsdl11Definition对象
     */
    @Bean("my")
    @Autowired
    public Wsdl11Definition userWsdl11Definition(XsdSchema userXsdSchema){
        DefaultWsdl11Definition defaultWsdl11Definition = new DefaultWsdl11Definition();
        defaultWsdl11Definition.setPortTypeName("SenderServicePort");
        //设置访问路径：@Bean("my")，案例：http://localhost:8080/test/ws/my.wsdl
        defaultWsdl11Definition.setLocationUri("/ws");
        //user.xsd中的targetNamespace属性
        defaultWsdl11Definition.setTargetNamespace("http://segmentfault.com/schemas");
        defaultWsdl11Definition.setSchema(userXsdSchema);

        return defaultWsdl11Definition;
    }

    /**
     * 注册email.xsd（Schema文件）对应的java对象
     */
    @Bean
    public XsdSchema userXsdSchema(){
        return new SimpleXsdSchema(new ClassPathResource("email.xsd"));
    }
}
