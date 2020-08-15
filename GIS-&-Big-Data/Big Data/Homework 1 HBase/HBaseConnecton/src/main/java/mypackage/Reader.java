package mypackage;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Iterator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;
import com.sun.tools.javac.util.List;

public class Reader {
	
	public static BufferedReader getReader(String filpath) throws FileNotFoundException {
		//String filpath = "E:\\\\BaiduNetdiskDownload\\\\BigData\\\\2014\\\\20140101.export.CSV";
		FileReader fr = new FileReader(filpath);
		BufferedReader bf = new BufferedReader(fr);
		
		return bf;
	}
	
	public static void main(String[] args) throws Exception {
		
		String path = "E:\\\\\\\\BaiduNetdiskDownload\\\\\\\\BigData\\\\\\\\2014\\\\";		//要遍历的路径
		File file = new File(path);		//获取其file对象
		File[] fs = file.listFiles();	//遍历path下的文件和目录，放在File数组中
		for(File f:fs){					//遍历File[]数组
			if(!f.isDirectory())		//若非目录(即文件)，则打印
				{
				System.out.println(f.getPath());
//				FileReader fr = new FileReader(f);
//				BufferedReader bf = new BufferedReader(fr);
//				String str;
//				// 按行读取字符串
//				while ((str = bf.readLine()) != null) {
//					String [] arr = str.split("\\t");
//					System.out.println(Arrays.toString(arr));
//					}
				}
		}
	}

	//	String filpath = "E:\\\\BaiduNetdiskDownload\\\\BigData\\\\2014\\\\20140101.export.CSV";
		
			
	

}
