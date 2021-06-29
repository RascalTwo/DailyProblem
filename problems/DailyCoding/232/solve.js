class Trie{
	/**
	 * @param {string} char
	 */
	constructor(){
		this.value = 0;
		/** @type {{ [key: string]: Trie }} */
		this.children = {};
		this.isWord = false;
	}
}

class PrefixMapSum{
	constructor(){
		this.root = new Trie();
	}

	/**
	 * @param {string} key
	 * @param {number} value
	 */
	insert(key, value){
		const traversed = [];
		let current = this.root;
		while (key){
			traversed.push(current);
			if (!(key[0] in current.children)){
				current.children[key[0]] = new Trie();
			}
			current = current.children[key[0]];
			key = key.slice(1);
		}

		if (current.isWord) value = -current.value + value;
		current.isWord = true;

		for (const trie of [...traversed, current]){
			trie.value += value;
		}
	}

	/**
	 * @param {string} prefix
	 */
	sum(prefix){
		let current = this.root;
		while (current && prefix){
			current = current.children?.[prefix[0]];
			prefix = prefix.slice(1);
		}

		return current ? current.value : 0;
	}
}

(() => {
	const assert = require('assert');

	const mapsum = new PrefixMapSum()
	mapsum.insert('columnar', 3)
	assert.deepStrictEqual(mapsum.sum('col'), 3);

	mapsum.insert('column', 2)
	assert.deepStrictEqual(mapsum.sum('col'), 5);

	mapsum.insert('columnar', 0)
	assert.deepStrictEqual(mapsum.sum('col'), 2);

	mapsum.insert('column', 0)
	assert.deepStrictEqual(mapsum.sum('col'), 0);

	mapsum.insert('columnar', 10)
	assert.deepStrictEqual(mapsum.sum('col'), 10);

	assert.deepStrictEqual(mapsum.sum('abc'), 0);
})();