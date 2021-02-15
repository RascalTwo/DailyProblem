public class solve{

	public static class Node<V>{
		public V value;
		public Node<V> left;
		public Node<V> right;

		public Node(V value, Node<V> left, Node<V> right){
			this.value = value;
			this.left = left;
			this.right = right;
		}
		public Node(V value, Node<V> left){
			this(value, left, null);
		}
		public Node(V value){
			this(value, null, null);
		}

		@Override
		public boolean equals(Object obj) {
			if (!(obj instanceof Node)) return false;
			Node<V> other = (Node<V>) obj;
			return this.value.equals(other.value)
				&& (this.left == null || this.left.equals(other.left))
				&& (this.right == null || this.right.equals(other.right));
		}

		@Override
		public String toString() {
			return String.format("value=%d left=(%s) right=(%s)", this.value, this.left, this.right);
		}
	}

	public static <V> Node<V> invertBinaryTree(Node<V> root){
		if (root == null) return null;
		Node<V> newleft = invertBinaryTree(root.right);
		Node<V> newRight = invertBinaryTree(root.left);
		root.left = newleft;
		root.right = newRight;
		return root;
	}

	public static void main(String[] args){
		try{
			assert false == true;
			System.out.println("Assertions are not enabled, exiting");
			System.exit(1);
		}catch(Exception e){}

		assert invertBinaryTree(
			new Node<Integer>(1, new Node<Integer>(2))
		).equals(
			new Node<Integer>(1, null, new Node<Integer>(2))
		);

		assert invertBinaryTree(
			new Node<Character>('a',
				new Node<Character>('b',
					new Node<Character>('d', null, null),
					new Node<Character>('e', null, null)
				),
				new Node<Character>('c',
					new Node<Character>('f', null, null),
					null
				)
			)
		).equals(new Node<Character>('a',
			new Node<Character>('c',
				null,
				new Node<Character>('f', null, null)
			),
			new Node<Character>('b',
				new Node<Character>('e', null, null),
				new Node<Character>('d', null, null)
			)
		));
	}
}
