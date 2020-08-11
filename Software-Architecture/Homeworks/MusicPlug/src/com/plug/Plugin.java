package com.plug;

import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;

public class Plugin {
		private String name;
	    private String jar;
	    private String className;
	    
	    
	    public String getName() {
	        return name;
	    }
	    public void setName(String name) {
	        this.name = name;
	    }
	    public String getJar() {
	        return jar;
	    }
	    public void setJar(String jar) {
	        this.jar = jar;
	    }
	    public String getClassName() {
	        return className;
	    }
	    public void setClassName(String className) {
	        this.className = className;
	    }
	    
		public IPlayerPlugin getInstance() throws Exception {
			//得到jar包的文件路径
	        URL[] urls = new URL[1];
	        urls[0] = new URL("file:"+jar);
	        //动态加载jar包
	        ClassLoader loader = new URLClassLoader(urls);
	        // 插件实例化对象，插件都是实现PluginService接口
	        Class<?> clazz = loader.loadClass(className);
	        //返回插件类型
	        IPlayerPlugin instance = (IPlayerPlugin)clazz.newInstance();
	 
	        return instance;
	    }
}
