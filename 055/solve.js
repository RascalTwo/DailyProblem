class URLShortener{
	static pool = '0123456789abcdefghijklmnopqrstuvwxyz';
	constructor(){
		this.urls = [];
		this.shorts = [];
	}

	static generateShort(){
		return Array(6).fill(null)
			.map(() => this.pool[Math.floor(Math.random() * this.pool.length)])
			.map(char => Math.random() < 0.5 ? char.toLowerCase() : char.toUpperCase())
			.join('')
	}

	shorten(url){
		const urlIndex = this.urls.indexOf(url);
		if (urlIndex !== -1) return this.shorts[urlIndex];

		const short = URLShortener.generateShort();
		this.urls.push(url);
		this.shorts.push(short);

		return short;
	}

	restore(short){
		const shortIndex = this.shorts.indexOf(short);
		if (shortIndex === -1) return null;

		return this.urls[shortIndex];
	}
}

(() => {
	const assert = require('assert');

	const instance = new URLShortener();

	for (const [url, shortened] of ['abc', 'def', 'ghi'].map(url => [url, instance.shorten(url)])){
		assert.deepStrictEqual(instance.restore(shortened), url);
		assert.deepStrictEqual(instance.shorten(url), shortened);
	}
	assert.deepStrictEqual(instance.restore('nonexistant'), null);

})();