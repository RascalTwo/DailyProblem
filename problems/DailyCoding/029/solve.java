public class solve{

	public static String decode(String encoded){
		String result = "";

		String multiplier = "";
		for (int i = 0; i < encoded.length(); i++){
			char curr = encoded.charAt(i);
			if (curr >= '0' && curr <= '9'){
				multiplier += curr;
			}
			else{
				result += String.valueOf(curr).repeat(Integer.parseInt(multiplier));
				multiplier = "";
			}
		}

		return result;
	}

	public static String encode(String string){
		if (string.length() == 0) return "";

		String result = "";
		String duplicates = String.valueOf(string.charAt(0));
		for (int i = 1; i < string.length(); i++){
			char curr = string.charAt(i);
			if (duplicates.contains(curr + "")){
				duplicates += curr;
			}
			else{
				result += String.valueOf(duplicates.length()) + duplicates.charAt(0);
				duplicates = String.valueOf(curr);
			}
		}
		result += String.valueOf(duplicates.length()) + duplicates.charAt(0);
		return result;
	}

	public static void main(String[] args){
		try{
			assert false == true;
			System.out.println("Assertions are not enabled, exiting");
			System.exit(1);
		}catch(AssertionError e){}


		assert encode("").equals("");
		assert decode("").equals("");

		assert encode("A").equals("1A");
		assert decode("1A").equals("A");

		assert encode("AAA").equals("3A");
		assert decode("3A").equals("AAA");

		assert encode("AAAABBBCCDAA").equals("4A3B2C1D2A");
		assert decode("4A3B2C1D2A").equals("AAAABBBCCDAA");

		assert encode("BAAAAAAAAAAAAAAAB").equals("1B15A1B");
		assert decode("1B15A1B").equals("BAAAAAAAAAAAAAAAB");
	}
}
