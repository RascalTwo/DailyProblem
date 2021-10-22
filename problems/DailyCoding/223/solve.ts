class TreeNode{
	value: number;
	left: TreeNode | null;
	right: TreeNode | null;

	constructor(value: number, left: TreeNode | null = null, right: TreeNode | null = null){
		this.value = value;
		this.left = left;
		this.right = right;
	}
}


function solve(root: TreeNode): number[]{
	const values = [];
	const stack = [];

	let current = root;
	while(current || stack.length){
		while(current){
			stack.push(current);
			current = current.left;
		}
		current = stack.pop();
		values.push(current.value);
		current = current.right;
	}

	return values;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(solve(new TreeNode(1, new TreeNode(2, new TreeNode(4), new TreeNode(5)), new TreeNode(3))), [4, 2, 5, 1, 3]);
	assert.deepStrictEqual(solve(new TreeNode(1, new TreeNode(2, new TreeNode(3), new TreeNode(4)), new TreeNode(5, new TreeNode(6), new TreeNode(7)))), [3, 2, 4, 1, 6, 5, 7]);
})();
