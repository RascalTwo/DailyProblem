import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class solve{

	public static Map<Character, List<Integer>> getCharacterIndexes(String string){
		Map<Character, List<Integer>> indexes = new HashMap<Character, List<Integer>>();
		for (int i = 0; i < string.length(); i++){
			char curr = string.charAt(i);
			if (!indexes.containsKey(curr)) indexes.put(curr, new ArrayList<Integer>());
			indexes.get(curr).add(i);
		}
		return indexes;
	}

	public static void main(String[] args){
		try{
			assert false == true;
			System.out.println("Assertions are not enabled, exiting");
			System.exit(1);
		}catch(AssertionError e){}


		assert getCharacterIndexes("abc  cba").equals(Map.of(
			'a', Arrays.asList(0, 7),
			'b', Arrays.asList(1, 6),
			'c', Arrays.asList(2, 5),
			' ', Arrays.asList(3, 4)
		));

		assert getCharacterIndexes("hello, world!").equals(Map.of(
			'h', Arrays.asList(0),
			'e', Arrays.asList(1),
			'l', Arrays.asList(2, 3, 10),
			'o', Arrays.asList(4, 8),
			',', Arrays.asList(5),
			' ', Arrays.asList(6),
			'w', Arrays.asList(7),
			'r', Arrays.asList(9),
			'd', Arrays.asList(11),
			'!', Arrays.asList(12)
		));
	}
}
