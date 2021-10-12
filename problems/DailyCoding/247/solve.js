class Node{
	/**
	 * @param {number} value
	 * @param {Node | null} left
	 * @param {Node | null} right
	 */
	constructor(value, left=null, right=null){
		this.value = value;
		this.left = left;
		this.right = right;
	}
}

function height(root){
	return root === null ? 0 : Math.max(height(root.left), height(root.right)) + 1;
}

/**
 * Given a Binary Tree, return if it is height-balanced.
 *
 * A height-balanced tree is one in which the difference of height between the left and right subtrees is no more then 1
 *
 * @param {Node | null} root
 * @returns {boolean}
 */
function isBalanced(root){
	return root === null || Math.abs(height(root.left) - height(root.right)) <= 1;
}


(() => {
	const assert = require('assert');


	assert.deepStrictEqual(isBalanced(new Node(0, new Node(1, new Node(2)))), false);
	assert.deepStrictEqual(isBalanced(new Node(0, new Node(1))), true);
	assert.deepStrictEqual(isBalanced(new Node(0, new Node(1), new Node(2, new Node(3)))), true);
	assert.deepStrictEqual(isBalanced(new Node(0, new Node(1), new Node(2, new Node(3, new Node(4))))), false);
})();
