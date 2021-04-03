class TreeNode{
	/**
	 * @param {string} label Label of node
	 * @param {Map<TreeNode, number>} children nodes paired with the distance to the node
	 */
	constructor(label, children = new Map()){
		this.label = label;
		for (const child of Array.from(children.keys())){
			child.parent = this;
		}
		this.children = children;

		this.parent = null;
	}
}

/**
 * @param {Set<TreeNode>} nodes
 * @param {TreeNode} start
 * @param {TreeNode} end
 */
function dijkstra(nodes, start, end){
	const unvisited = new Set(nodes);
	const distances = new Map()
	distances.set(start, 0);

	while (unvisited.size > 0){
		const current = [...unvisited].reduce((furthest, node) => {
			if (furthest === null) return node;
			const fd = distances.has(furthest) ? distances.get(furthest) : Number.MIN_SAFE_INTEGER;
			const nd = distances.has(node) ? distances.get(node) : Number.MIN_SAFE_INTEGER;
			return nd > fd ? node : furthest;
		}, null);

		const neighborDistances = [...current.children]
		if (current.parent) neighborDistances.push([current.parent, [...current.parent.children].find(([child]) => child === current)[1]]);
		for (const [neighbor, distance] of neighborDistances){
			if (!unvisited.has(neighbor)) continue;
			distances.set(neighbor, Math.max(distances.get(current) + distance, distances.has(neighbor) ? distances.get(neighbor) : Number.MIN_SAFE_INTEGER));
		}

		unvisited.delete(current);
	}

	return distances.get(end);
}


/**
 * @param {Iterable<T>} iterable iterable to return pairs of
 *
 * @yields {[T, T]}
 */
function* pairsFrom(iterable){
	const array = Array.from(iterable);
	for (let i = 0; i < array.length - 1; i++){
		for (let j = i + 1; j < array.length; j++){
			yield [array[i], array[j]];
		}
	}
}


/**
 * @param {TreeNode} root
 *
 * @returns {number}
 */
function getLongestTreePath(root){
	const nodes = new Set([root]);

	const processing = Array.from(root.children.keys());
	while (processing.length){
		const current = processing.pop();
		nodes.add(current)
		processing.push(...Array.from(current.children.keys()));
	}

	let best = 0;
	for (const [start, end] of pairsFrom(nodes)){
		best = Math.max(best, dijkstra(nodes, start, end));
	}
	return best;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(getLongestTreePath(new TreeNode('a', new Map([
		[new TreeNode('b'), 3]
	]))), 3);

	assert.deepStrictEqual(getLongestTreePath(new TreeNode('a', new Map([
		[new TreeNode('b'), 3],
		[new TreeNode('c'), 5]
	]))), 8);

	assert.deepStrictEqual(getLongestTreePath(new TreeNode('a', new Map([
		[new TreeNode('b'), 3],
		[new TreeNode('c'), 5],
		[new TreeNode('d', new Map([
			[new TreeNode('e', new Map([
				[new TreeNode('g'), 1],
				[new TreeNode('h'), 1]
			])), 2],
			[new TreeNode('f'), 4]
		])), 8],
	]))), 17);
})();