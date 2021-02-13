class Node{
	/**
	 * @param {string | number} value
	 * @param {Node | null} left
	 * @param {Node | null} right
	 */
	constructor(value, left=null, right=null){
		this.value = value;
		this.left = left;
		this.right = right;
	}

	/**
	 * @returns {{
	 * 	value: string | number,
	 *  left: Node | null,
	 *  right: Node | null
	 * }}
	 */
	valueOf(){
		return JSON.stringify({
			value: this.value,
			left: this.left?.valueOf() || null,
			right: this.right?.valueOf() || null
		})
	}
}


/**
 * Invert the provided binary tree
 *
 * @param {Node | null} root
 *
 * @returns {Node | null}
 */
function invertBinaryTree(root){
	if (!root) return null;
	([root.left, root.right] = [invertBinaryTree(root.right), invertBinaryTree(root.left)]);
	return root;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(
		invertBinaryTree(new Node(1, new Node(2))),
		new Node(1, null, new Node(2))
	);

	assert.deepStrictEqual(
		invertBinaryTree(
			new Node('a',
				new Node('b',
					new Node('d', null, null),
					new Node('e', null, null)
				),
				new Node('c',
					new Node('f', null, null),
					null
				)
			)
		),
		new Node('a',
			new Node('c',
				null,
				new Node('f', null, null)
			),
			new Node('b',
				new Node('e', null, null),
				new Node('d', null, null)
			)
		)
	);
})();