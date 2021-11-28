class PriceTracker{
	private prices: Record<number, number>;
	constructor(){
		this.prices = {}
	}

	get length(){
		return Object.keys(this.prices).length;
	}

	get min(){
		return this.length ? Math.min(...Object.values(this.prices)) : -Number.MAX_SAFE_INTEGER;
	}

	get max(){
		return this.length ? Math.max(...Object.values(this.prices)) : Number.MAX_SAFE_INTEGER;
	}

	get average(){
		return this.length ? Object.values(this.prices).reduce((sum, value) => sum + value) / this.length : 0;
	}

	add(timestamp: number, price: number){
		this.prices[timestamp] = price;
	}

	update(timestamp: number, price: number){
		this.add(timestamp, price);
	}

	remove(timestamp: number){
		if (timestamp in this.prices) delete this.prices[timestamp];
	}
}


(() => {
	const assert = require('assert');

	const tracker = new PriceTracker();
	const assertMinMaxAverage = (min: number, max: number, average: number) => {
		assert.deepStrictEqual(tracker.min, min);
		assert.deepStrictEqual(tracker.max, max);
		assert.deepStrictEqual(tracker.average, average);
	}

	assertMinMaxAverage(-Number.MAX_SAFE_INTEGER, Number.MAX_SAFE_INTEGER, 0)
	tracker.add(0, 0)
	assertMinMaxAverage(0, 0, 0)
	tracker.add(1, 1)
	assertMinMaxAverage(0, 1, 0.5)
	tracker.add(2, 2)
	assertMinMaxAverage(0, 2, 1)
	tracker.add(3, -1)
	assertMinMaxAverage(-1, 2, 0.5)
	tracker.add(4, 5)
	assertMinMaxAverage(-1, 5, 1.4)
	tracker.remove(3)
	assertMinMaxAverage(0, 5, 2)
	tracker.update(4, 4)
	assertMinMaxAverage(0, 4, 1.75)
})();
