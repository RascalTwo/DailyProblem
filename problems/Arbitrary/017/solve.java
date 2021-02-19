public class solve {

	public static boolean isPrime(int number){
		for (int i = 2; i < (number / 2) + 1; i++){
			if (number % i == 0) return false;
		}
		return number > 1;
	}

	public static int countPrimes(int[] integers){
		int primes = 0;
		for (int num : integers){
			primes += isPrime(num) ? 1 : 0;
		}
		return primes;
	}

	public static void main(String[] args){
		try{
			assert false == true;
			System.out.println("Assertions are not enabled, exiting");
			System.exit(1);
		}catch(AssertionError e){}


		assert countPrimes(new int[] {1, 2, 3}) == 2;
		assert countPrimes(new int[] {17}) == 1;
		assert countPrimes(new int[] {4, 6, 8, 10}) == 0;
		assert countPrimes(new int[] {4, 4, 4, 13, 4, 4, 4}) == 1;
		assert countPrimes(new int[] {4, 8, 6, 2, 75, 98, 35, 14, 43, 48}) == 2;
	}
}
