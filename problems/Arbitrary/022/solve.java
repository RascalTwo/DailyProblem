public class solve {

	public static String defang(String uri){
		return uri.replaceAll(".", "[.]");
	}

	public static String refang(String uri){
		return uri.replaceAll("[.]", ".");
	}

	public static void main(String[] args){
		try{
			assert false == true;
			System.out.println("Assertions are not enabled, exiting");
			System.exit(1);
		}catch(AssertionError e){}


		assert defang("192.168.1.1").equals("192[.]168[.]1[.]1");
		assert refang("192[.]168[.]1[.]1").equals("192.168.1.1");

		assert defang("http://www.google.com/").equals("http://www[.]google[.]com/");
		assert refang("http://www[.]google[.]com/").equals("http://www.google.com/");
	}
}
