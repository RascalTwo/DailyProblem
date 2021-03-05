public class solve{

	public static int getFixedPoint(int[] integers){
		for (int i = 0; i < integers.length; i++){
			if (integers[i] == i) return i;
		}
		return -1;
	}

	public static void main(String[] args){
		try{
			assert false == true;
			System.out.println("Assertions are not enabled, exiting");
			System.exit(1);
		}catch(AssertionError e){}


		assert fixedPointOf(new int[] {7, 8, 5, 2, 4, 9}) == 4;
		assert fixedPointOf(new int[] {7, 8, 5, 2, 8, 9}) == -1;
	}
}