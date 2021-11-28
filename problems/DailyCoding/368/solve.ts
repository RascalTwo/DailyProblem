class KVS {
	private data: Map<number, number>;
	constructor() {
		this.data = new Map<number, number>();
	}

	update(key: number, value: number) {
		this.data.set(key, value);
	}

	maxKey(value: number) {
		return Math.max(...Array.from(this.data.entries())
			.filter(([_, lvalue]) => value === lvalue)
			.map(([key]) => key)
		);
	}
}


(() => {
	const assert = require('assert');

	const kv = new KVS();
	kv.update(1, 1)
	kv.update(2, 1)
	assert.deepStrictEqual(kv.maxKey(1), 2);
})();
