class Node{
	constructor(value, left = null, right = null){
		this.value = value;
		this.left = left;
		this.right = right;
	}
}

const isUnival = root => {
	const leaves = [root.left, root.right].filter(Boolean);
	if (!leaves.length) return true;

	return leaves.every(leaf => leaf.value === root.value) && leaves.every(isUnival);
}

/**
 * Returns the number of unival trees within this binary tree.
 *
 * A unival tree is a tree in which all nodes contain the same value
 * @param {Node} root
 */
function countUnival(root){
	return root ? isUnival(root) + countUnival(root.left) + countUnival(root.right) : 0;
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(countUnival(
		new Node(0,
			new Node(1),
			new Node(0,
				new Node(1,
					new Node(1),
					new Node(1)
				),
				new Node(0)
			)
		)
	), 5);

	assert.deepStrictEqual(countUnival(
		new Node(0,
			new Node(0),
			new Node(0)
		)
	), 3);

	assert.deepStrictEqual(countUnival(
		new Node(0,
			new Node(1),
			new Node(0)
		)
	), 2);

	assert.deepStrictEqual(countUnival(
		new Node(0,
			new Node(0,
				new Node(0)
			),
			new Node(0)
		)
	), 4);

	assert.deepStrictEqual(countUnival(
		new Node(0,
			new Node(1,
				new Node(0)
			),
			new Node(0)
		)
	), 2);

	assert.deepStrictEqual(countUnival(
		new Node(0,
			new Node(0,
				new Node(1)
			)
		)
	), 1);
})();