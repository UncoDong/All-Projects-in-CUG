package mypackage;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.util.Arrays;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.Admin;
import org.apache.hadoop.hbase.client.Connection;
import org.apache.hadoop.hbase.client.ConnectionFactory;
import org.apache.hadoop.hbase.client.Get;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.client.Table;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.log4j.BasicConfigurator;

import com.opencsv.CSVReader;



public class connect {
	public static Configuration configuration;
	public static Connection connection;
	public static Admin admin;
	
	public static void init() {

		// TODO Auto-generated method stub
		configuration = HBaseConfiguration.create();
		configuration.set("hbase.zookeeper.quorum", "182.92.100.19");
		try {
			connection = ConnectionFactory.createConnection(configuration);
			admin = connection.getAdmin();
		}
		catch (IOException e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}
	
	public static void close()
	{
		try {
			if(admin != null) {
				admin.close();
			}
			if(null != connection) {
				connection.close();
			}
		}
			catch (IOException e) {
				// TODO: handle exception
				e.printStackTrace();
			}
	}
	
	/*创建表格*/
	/**
	 *    
	 * @param myTableName   表名
	 * @param colFamily     列组的名字们
	 * @throws IOException
	 */
	public static void createTable(String myTableName, String[] colFamily) throws IOException{
		TableName tableName = TableName.valueOf(myTableName);
		// 如果存在这张表
		if(admin.tableExists(tableName))
		{
			System.out.println("存在这张表");
		}else {
			// 建立表格
			HTableDescriptor hTableDescriptor = new HTableDescriptor(tableName);
			// 建立列族
			for(String str:colFamily) {
				HColumnDescriptor hColumnDescriptor = new HColumnDescriptor(str);
				// 在表格中添加列族
				hTableDescriptor.addFamily(hColumnDescriptor);
			}
			admin.createTable(hTableDescriptor);
		}
	}
	
	/*添加数据*/
	/**
	 * 
	 * @param tableName   表名
	 * @param rowKey	   行键名
	 * @param colFamily   列族
	 * @param col         列组内的列名
	 * @param val         要写入的数据
	 * @throws IOException
	 */
	public static void insertData(String tableName, String rowKey,
			String colFamily, String col, String val)throws IOException
	{
		Table table = connection.getTable(TableName.valueOf(tableName));
		Put put = new Put(Bytes.toBytes(rowKey));
		
		put.addColumn(Bytes.toBytes(colFamily),  Bytes.toBytes(col),Bytes.toBytes(val));
		table.put(put);
		table.close();
	}
	
	/*浏览数据*/
	/**
	 * 
	 * @param tableName   表名
	 * @param rowKey      行键值
	 * @param colFamily   列族名
	 * @param col         列组名下的列名
	 * @throws IOException
	 */
	public static void getData(String tableName, String rowKey, 
			String colFamily, String col)throws IOException{
		Table table = connection.getTable(TableName.valueOf(tableName));
		Get get = new Get(Bytes.toBytes(rowKey));
		get.addColumn(Bytes.toBytes(colFamily), Bytes.toBytes(col));
		// 获取的结果result是结果集，还需要格式化输出
		Result result = table.get(get);
        byte[] resByte = result.getValue(Bytes.toBytes(colFamily), Bytes.toBytes(col));
        System.out.println("准备输出");
        System.out.println(new String(resByte));
//		/System.out.println(new String(result.getValue(colFamily.getBytes(colFamily).col==null?null:col.getBytes())));
		table.close();
	}
	
	/**
	 *   用来创建GDELT表的
	 * @throws Exception
	 */
	public static void createGDELT() throws Exception
	{

//	    EVENTID AND DATE ATTRIBUTES，  全局唯一表示号码
//	    ACTOR ATTRIBUTES，			   参与者的CAMEO码
//	    EVENT ACTION ATTRIBUTES，        事件行为和重要性评估
//	    EVENT GEOGRAPHY，			  地理位置信息
//	    DATA MANAGEMENT FIELDS       数据库管理记录

		createTable("GDELT",new String[]{"EVENTID AND DATE ATTRIBUTES","ACTOR ATTRIBUTES",
				"EVENT ACTION ATTRIBUTES","EVENT GEOGRAPHY","DATA MANAGEMENT FIELDS"});
	}
	
	static private String[] EVENT_AND_DATE_ATTRIBUTES = {"GlobalEventID","Day","MonthYear","Year","FractionDate"};
	static private String[] ACTOR_ATTRIBUTESS = {"Actor1Code","Actor1Name","Actor1CountryCode","Actor1KnownGroupCode","Actor1EthnicCode","Actor1Religion1Code","Actor1Religion2Code","Actor1Type1Code","Actor1Type2Code","Actor1Type3Code",
			"Actor2Code","Actor2Name","Actor2CountryCode","Actor2KnownGroupCode","Actor2EthnicCode","Actor2Religion1Code","Actor2Religion2Code","Actor2Type1Code","Actor2Type2Code","Actor2Type3Code"};
	static private String[] EVENT_ACTION_ATTRIBUTES = {"IsRootEvent","EventCode","EventBaseCode","EventRootCode","QuadClass","GoldsteinScale","NumMentions","NumSources","NumArticles","AvgTone"};
	static private String[] EVENT_GEOGRAPHY = {"Actor1Geo_Type"," Actor1Geo_Fullname","Actor1Geo_CountryCode","Actor1Geo_ADM1Code","Actor1Geo_Lat","Actor1Geo_Long","Actor1Geo_FeatureID",
			"Actor2Geo_Type"," Actor2Geo_Fullname","Actor2Geo_CountryCode","Actor2Geo_ADM1Code","Actor2Geo_Lat","Actor2Geo_Long","Actor2Geo_FeatureID",
			"ActionGeo_Type ","ActionGeo_Fullname","ActionGeo_CountryCode","ActionGeo_ADM1Code","ActionGeo_Lat","ActionGeo_Long","ActionGeo_FeatureID"};
	static private String[] DATA_MANAGEMENT_FIELDS = {"DATEADDED","SOURCEURL"};
	
	public static void insertEachCsv(String filpath, String fliname) throws Exception{
		BufferedReader bf =  Reader.getReader(filpath);
		String str = null;
		int index = 0;
		while ((str = bf.readLine()) != null) {
			String [] arr = str.split("\\t");
			// EVENT AND DATE ATTRIBUTES 事件标识码
			for(int i = 0; i < 5; i++)
			{
				
				insertData("GDELT",arr[0],"EVENTID AND DATE ATTRIBUTES",EVENT_AND_DATE_ATTRIBUTES[i],arr[i]);
				//System.out.print(EVENT_AND_DATE_ATTRIBUTES[i]+arr[i]);
			}
			// ACTOR ATTRIBUTES 参与者CAMEO码
			for(int i = 5; i < 25; i++)
			{
				insertData("GDELT",arr[0],"ACTOR ATTRIBUTES",ACTOR_ATTRIBUTESS[i-5],arr[i]);
				//System.out.print(ACTOR_ATTRIBUTESS[i-5]+arr[i]);
			}
			// EVENT ACTION ATTRIBUTES 参与者CAMEO码
			for(int i = 25; i < 35; i++)
			{
				insertData("GDELT",arr[0],"EVENT ACTION ATTRIBUTES",EVENT_ACTION_ATTRIBUTES[i-25],arr[i]);
				//System.out.print(EVENT_ACTION_ATTRIBUTES[i-25]+arr[i]);	
			}
			// EVENT GEOGRAPHY 地理位置信息
			for(int i = 35; i < 56; i++)
			{
				insertData("GDELT",arr[0],"EVENT GEOGRAPHY",EVENT_GEOGRAPHY[i-35],arr[i]);
				//System.out.print(EVENT_GEOGRAPHY[i-35]+arr[i]);	
			}
			// DATA MANAGEMENT FIELDS 事件记录
			for(int i = 56; i < 58; i++)
			{
				insertData("GDELT",arr[0],"DATA MANAGEMENT FIELDS",DATA_MANAGEMENT_FIELDS[i-56],arr[i]);
				//System.out.print(DATA_MANAGEMENT_FIELDS[i-56]+arr[i]);	
			}
			//index+=1;
			//System.out.println(arr[0]+" 第"+index+"行");
		}
	}
	
	
	public static void main(String[] args) {
		BasicConfigurator.configure(); //自动快速地使用缺省Log4j环境。
		try {
			// 初始化链接
			init();		
			// 查询
			getData("GDELT", "281750002", "EVENT GEOGRAPHY", "ActionGeo_FeatureID");
			// 遍历插入数据
//			String path = "E:\\BaiduNetdiskDownload\\BigData\\2014\\";
//			File file = new File(path);		//获取其file对象
//			File[] fs = file.listFiles();	//遍历path下的文件和目录，放在File数组中
//			for(File f:fs){					//遍历File[]数组
//				if(!f.isDirectory())		//若非目录(即文件)，则打印
//					{
//					System.out.println(f);
//					insertEachCsv(f.getPath(),"");
//					System.out.println(f);
//					System.out.println("插入完毕");
//					}
//			}
			
			
////		System.out.println("建表");
//		createTable("student",new String[]{"score","message"});
////		System.out.println("插入");
//		insertData("student","zhangsan","score","English","69");
//		insertData("student","zhangsan","score","Math","69");
//		insertData("student","zhangsan","score","Computer","69");
//		System.out.println("查询");
//		getData("student", "zhangsan", "score", "English");
//		System.out.println("初始化完成");
//		getData("test", "001", "cf1", "name");
////		close();
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}

