class Node{
	/**
	 * @param {number} value
	 * @param {Node|null} left
	 * @param {Node|null} right
	 */
	constructor(value, left = null, right = null){
		this.value = value;
		this.left = left;
		this.right = right;
	}
}


/**
 * @param {Node|undefined} node
 * @returns {number}
 */
function sumTree(node){
	return !node ? 0 : node.value + sumTree(node.left) + sumTree(node.right);
}


(() => {
	const assert = require('assert');


	assert.deepStrictEqual(sumTree(new Node(1,
		new Node(2, new Node(3)),
		new Node(4, null, new Node(5))
	)), 15);

	assert.deepStrictEqual(sumTree(new Node(1,
		new Node(2, new Node(3)),
		new Node(4, null, new Node(-5))
	)), 5);
})();