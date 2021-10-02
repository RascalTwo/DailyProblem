/**
 * @param {object} obj
 * @returns {object}
 */
function flatten(obj, prefix=''){
	const result = {}
	for (const [key, value] of Object.entries(obj)){
		const prefixKey = prefix + key
		if (typeof value === 'object'){
			Object.assign(result, flatten(value, prefixKey + '.'))
		}
		else{
			result[prefixKey] = value;
		}
	}

	return result
}

/**
 * @param {object} obj
 * @returns {object}
 */
function unflatten(obj){
	const result = {}
	for (const [key, value] of Object.entries(obj)){
		const paths = key.split('.');
		let current = result;
		for (const key of paths.slice(0, -1)){
			if (!(key in current)) current[key] = {};
			current = current[key];
		}
		current[paths.slice(-1)[0]] = value;
	}

	return result
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(flatten({
		key: 3,
		foo: {
				a: 5,
				bar: {
						baz: 8
				}
		}
	}), {
		key: 3,
		'foo.a': 5,
		'foo.bar.baz': 8
	});
	assert.deepStrictEqual(flatten({
		key: 3,
		arr: ['a', 'b', 'c']
	}), {
		key: 3,
		'arr.0': 'a',
		'arr.1': 'b',
		'arr.2': 'c'
	});
	assert.deepStrictEqual(unflatten({
		key: 3,
		'foo.a': 5,
		'foo.bar.baz': [8, 9]
	}), {
		key: 3,
		foo: {
				a: 5,
				bar: {
						baz: [8, 9]
				}
		}
	});
})();
