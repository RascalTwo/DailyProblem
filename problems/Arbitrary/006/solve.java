import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class solve{

	public static List<Integer> removeSortedDupes(List<Integer> integers){
		int i = 0;
		while(i < integers.size() - 1){
			if(integers.get(i) == integers.get(i + 1)){
				integers.remove(i);
			}
			else{
				i++;
			}
		}
		return integers;
	}

	public static void main(String[] args){
		try{
			assert false == true;
			System.out.println("Assertions are not enabled, exiting");
			System.exit(1);
		}catch(Exception e){}


		assert removeSortedDupes(new ArrayList<Integer>(Arrays.asList(1, 1, 2))).equals(new ArrayList<Integer>(Arrays.asList(1, 2)));
		assert removeSortedDupes(new ArrayList<Integer>(Arrays.asList(0, 0, 1, 1, 1, 2, 2, 3, 3, 4))).equals(new ArrayList<Integer>(Arrays.asList(0, 1, 2, 3, 4)));
		assert removeSortedDupes(new ArrayList<Integer>(Arrays.asList(4, 4, 5, 7, 7, 7, 7, 8, 9, 10, 10, 10))).equals(new ArrayList<Integer>(Arrays.asList(4, 5, 7, 8, 9, 10)));
	}
}
