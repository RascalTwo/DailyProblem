class TreeNode {
	val: number
	left: TreeNode | null
	right: TreeNode | null
	constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
		this.val = (val === undefined ? 0 : val)
		this.left = (left === undefined ? null : left)
		this.right = (right === undefined ? null : right)
	}
	rangeSumBST(low: number, high: number): number {
		return (this.val >= low && this.val <= high ? this.val : 0) +
			(this.left?.rangeSumBST(low, high) ?? 0) +
			(this.right?.rangeSumBST(low, high) ?? 0)
	}
}


const rangeSumBST = (root: TreeNode, low: number, high: number): number => {
	return (root.val >= low && root.val <= high ? root.val : 0) +
		(root.left ? rangeSumBST(root.left, low, high) : 0) +
		(root.right ? rangeSumBST(root.right, low, high) : 0);
};


(() => {
	const assert = require('assert');

	for (const { root, low, high, expected } of [{
		root: new TreeNode(10, new TreeNode(5, new TreeNode(3), new TreeNode(7)), new TreeNode(15, undefined, new TreeNode(18))),
		low: 7, high: 15, expected: 32
	}, {
		root: new TreeNode(10, new TreeNode(5, new TreeNode(3, new TreeNode(1)), new TreeNode(7, new TreeNode(6))), new TreeNode(15, new TreeNode(13), new TreeNode(18))),
		low: 6, high: 10, expected: 23
	}]) {
		assert.deepStrictEqual(rangeSumBST(root, low, high), expected);
		assert.deepStrictEqual(root.rangeSumBST(low, high), expected);
	}
})();
