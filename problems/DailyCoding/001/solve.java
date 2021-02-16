public class solve{

	public static boolean anyEqual(int[] numbers, int goal){
		for (int i = 0; i < numbers.length; i++){
			for (int j = i+1; j < numbers.length; j++){
				if (numbers[i] + numbers[j] == goal) return true;
			}
		}

		return false;
	}

	public static void main(String[] args){
		try{
			assert false == true;
			System.out.println("Assertions are not enabled, exiting");
			System.exit(1);
		}catch(AssertionError e){}


		assert anyEqual(new int[] {1, 2}, 3) == true;
		assert anyEqual(new int[] {1}, 3) == false;
		assert anyEqual(new int[] {1, 4, 9, 6}, 10) == true;
		assert anyEqual(new int[] {10, 15, 3, 7}, 17) == true;
		assert anyEqual(new int[] {7, 3, 15, 10}, 17) == true;
		assert anyEqual(new int[] {9, 4, 3, 6}, 39) == false;
		assert anyEqual(new int[] {1, 7, 4, 8, 6, 7}, 12) == true;
	}
}
