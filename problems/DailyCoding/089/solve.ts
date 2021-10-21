class TreeNode{
	public value: number | string;
	public left: TreeNode | null;
	public right: TreeNode | null;

	constructor(value: number | string, left: TreeNode | null=null, right: TreeNode | null=null){
		this.value = value;
		this.left = left;
		this.right = right;
	}

	get valid(): boolean{
		if (this.left && this.left.value > this.value) return false;
		if (this.right && this.right.value < this.value) return false;
		return (this.left?.valid && this.right?.valid) ?? true;
	}
}

const isValidBST = (root: TreeNode | null): boolean => {
	if (!root) return true;
	if (root.left && root.left.value > root.value) return false;
	if (root.right && root.right.value < root.value) return false;
	return isValidBST(root.left) && isValidBST(root.right);
}

(() => {
	const assert = require('assert');

	const CASES: [TreeNode, boolean][] = [
		// No children
		[new TreeNode(0), true],
		// Left less
		[new TreeNode(0, new TreeNode(-1)), true],
		// Left equal
		[new TreeNode(0, new TreeNode(0)), true],
		// Left greater
		[new TreeNode(0, new TreeNode(1)), false],
		// Right greater
		[new TreeNode(0, null, new TreeNode(1)), true],
		// Right equal
		[new TreeNode(0, null, new TreeNode(0)), true],
		// Right less
		[new TreeNode(0, null, new TreeNode(-1)), false],
		// Nested lefts less
		[new TreeNode(0, new TreeNode(-1, new TreeNode(-2))), true],
		// Nested lefts greater
		[new TreeNode(0, new TreeNode(-1, new TreeNode(1))), false],
		[
			new TreeNode(8,
				new TreeNode(3, new TreeNode(1), new TreeNode(6, new TreeNode(4, null, new TreeNode(7)))),
				new TreeNode(10, null, new TreeNode(14, new TreeNode(13)))
			),
			true
		]
	]
	for (const [root, expected] of CASES){
		assert.deepStrictEqual(isValidBST(root), expected);
		assert.deepStrictEqual(root.valid, expected);
	}
})();
