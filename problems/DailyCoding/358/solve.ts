class Incrementor{
	values: Record<string, number>
	constructor(){
		this.values = {}
	}

	plus(key: string){
		if (!(key in this.values)) this.values[key] = 0;
		this.values[key]++;
	}

	minus(key: string){
		if (!(key in this.values)) return
		this.values[key]--;
		if (!this.values[key]) delete this.values[key];
	}

	getMax(){
		return Object.entries(this.values).reduce(([maxKey, maxValue], [key, value]) => value > maxValue ? [key, value] : [maxKey, maxValue])[0];
	}

	getMin(){
		return Object.entries(this.values).reduce(([minKey, minValue], [key, value]) => value < minValue ? [key, value] : [minKey, minValue])[0];
	}
}

(() => {
	const assert = require('assert');

	const instance = new Incrementor();

	instance.plus('b');
	assert.deepStrictEqual(instance.getMax(), 'b');

	instance.plus('a');
	instance.plus('a');
	assert.deepStrictEqual(instance.getMax(), 'a');
	assert.deepStrictEqual(instance.getMin(), 'b');

	instance.minus('a');
	instance.minus('a');
	assert.deepStrictEqual(instance.getMax(), 'b');
})();
