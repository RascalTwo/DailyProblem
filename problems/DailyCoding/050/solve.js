class Node{
	/**
	 * @param {string | number} value
	 * @param {Node | null} left
	 * @param {Node | null} right
	 */
	constructor(value, left = null, right = null){
		this.value = value;
		this.left = left;
		this.right = right;
	}
}

/**
 * Given a simple expression seralized as a binary tree, evaluate and return the final value.
 *
 * All interior nodes - nodes with children - are the operation symbols - and all leaf nodes - nodes without children - are the numeric values.
 *
 * @param {Node} node
 * @returns {number}
 */
function evaluateTree(node){
	if (typeof node.value === 'number') return node.value;

	return eval(`${evaluateTree(node.left)}${node.value}${evaluateTree(node.right)}`)
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(evaluateTree(new Node(5)), 5)
	// 5 = 5
	assert.deepStrictEqual(evaluateTree(new Node('*', new Node(5), new Node(5))), 25)
	// 5 * 5 = 25
	assert.deepStrictEqual(evaluateTree(new Node('*', new Node('+', new Node(5), new Node(4)), new Node('+', new Node(3), new Node(2)))), 45)
	// (3 + 2) * (4 + 5) = 45
})();