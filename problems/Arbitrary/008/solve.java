public class solve{

	public static String capitalizeWords(String string){
		char[] chars = string.toCharArray();
		for (int i = 0; i < chars.length; i++){
			if (i == 0 || Character.isWhitespace(chars[i - 1])){
				chars[i] = Character.toUpperCase(chars[i]);
			}
		}

		String result = "";
		for (char c : chars){
			result += c;
		}
		return result;
	}

	public static void main(String[] args){
		try{
			assert false == true;
			System.out.println("Assertions are not enabled, exiting");
			System.exit(1);
		}catch(AssertionError e){}

		assert capitalizeWords("hello world").equals("Hello World");
		assert capitalizeWords("How are you doing, this...  lovely day?").equals("How Are You Doing, This...  Lovely Day?");
	}
}
