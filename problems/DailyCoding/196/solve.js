class Node{
	/**
	 * @param {number} value
	 * @param {Node | null} left
	 * @param {Node | null} right
	 */
	constructor(value, left = null, right = null){
		this.value = value;
		this.left = left;
		this.right = right
	}
}

/**
 * @param {Node} node
 * @returns {number}
 */
function sumTree(node){
	if (node === null) return 0;

	return node.value + sumTree(node.left) + sumTree(node.right);
}

function mostFrequentSubtreeSum(root){
	const sums = {}
	function sumTree(node){
		if (node === null) return 0;

		const sum = node.value + sumTree(node.left) + sumTree(node.right);
		if (!(sum in sums)) sums[sum] = 1
		else sums[sum] += 1

		return sum;
	}

	sumTree(root);
	return Number(Object.entries(sums).sort((a, b) => b[1] - a[1])[0][0]);
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(sumTree(new Node(5, new Node(2), new Node(-5))), 2);
	assert.deepStrictEqual(mostFrequentSubtreeSum(new Node(5, new Node(2), new Node(-5))), 2);
	assert.deepStrictEqual(sumTree(new Node(5, new Node(2, new Node(3)), new Node(-5, null, new Node(7)))), 12);
	assert.deepStrictEqual(mostFrequentSubtreeSum(new Node(0, new Node(2, new Node(3)), new Node(-5, null, new Node(7)))), 7);
})();
