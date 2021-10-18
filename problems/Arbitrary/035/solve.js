class Node{
	constructor(value, left, right){
		this.value = value;
		this.left = left;
		this.right = right;
	}
}

const sumTree = node => node ? (sumTree(node.left) + node.value + sumTree(node.right)) : 0;

function solve(root){
	if (!root.left || !root.right) return false;

	return sumTree(root.left) === sumTree(root.right)
}

(() => {
	const assert = require('assert');

	const root = new Node(0,
		new Node(-7, new Node(-3, new Node(4), new Node(5)), new Node(10, new Node(2), new Node(11))),
		new Node(-13, new Node(1, null, new Node(9)), new Node(8, new Node(-12), new Node(14)))
	)

	assert.deepStrictEqual(solve(root), false);
	assert.deepStrictEqual(solve(root.right), true);
	assert.deepStrictEqual(solve(new Node(1, new Node(2, new Node(3)))), false);
})()