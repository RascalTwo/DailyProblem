/**
 * Decode boolean flags from flags into an object with keys
 *
 * @param {int} flags
 * @param  {...string} keys
 *
 * @returns {{[key as string]: boolean}}
 */
function decode(flags, ...keys){
	const results = {};
	const bits = Math.max(keys.length, flags.toString(2).length);
	for (let i = 0; i < bits; i++){
		results[keys[i]] = Boolean(flags >> i & 1)
	}
	return results; //?
}


/**
 * Encode object of booleans into an integer
 *
 * @param {{[key as string]: bool}} map
 *
 * @returns {int}
 */
function encode(map){
	let flags = 0;
	for (const [i, value] of Object.values(map).entries()){
		flags |= Number(value) << i;
	}
	return flags;
}


(() => {
	const assert = require('assert');

	for (const [flags, keys, expectedMap] of [
		[0b0001, ['User', 'Mod', 'Admin', 'Owner'], {'User': true, 'Mod': false, 'Admin': false, 'Owner': false}],
		[0b101, ['A', 'B', 'C'], {'A': true, 'B': false, 'C': true}]
	]){
		const decoded = decode(flags, ...keys);
		assert.deepStrictEqual(decoded, expectedMap)
		assert.deepStrictEqual(encode(decoded), flags)
	}
})();