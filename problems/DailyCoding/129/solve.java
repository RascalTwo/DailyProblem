public class solve{

	public static double squareRoot(int n){
		return Math.sqrt(n);
	}

	public static void main(String[] args){
		try{
			assert false == true;
			System.out.println("Assertions are not enabled, exiting");
			System.exit(1);
		}catch(AssertionError e){}


		assert squareRoot(9) == 3;
	}
}
