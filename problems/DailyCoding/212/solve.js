/**
 * @param {string} address
 * @returns {number}
 */
function cellAddressToInteger(address){
	let result = 0;
	for (const char of address){
		result = result * 26 + (char.charCodeAt(0) - 'A'.codePointAt(0)) + 1
	}
	return result;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(cellAddressToInteger('A'), 1);
	assert.deepStrictEqual(cellAddressToInteger('F'), 6);
	assert.deepStrictEqual(cellAddressToInteger('Z'), 26);
	assert.deepStrictEqual(cellAddressToInteger('AA'), 27);
	assert.deepStrictEqual(cellAddressToInteger('AB'), 28);
	assert.deepStrictEqual(cellAddressToInteger('AD'), 30);
	assert.deepStrictEqual(cellAddressToInteger('AZ'), 52);
	assert.deepStrictEqual(cellAddressToInteger('BA'), 53);
	assert.deepStrictEqual(cellAddressToInteger('BZ'), 78);
	assert.deepStrictEqual(cellAddressToInteger('CA'), 79);
	assert.deepStrictEqual(cellAddressToInteger('YZ'), 676);
	assert.deepStrictEqual(cellAddressToInteger('ZA'), 677);
	assert.deepStrictEqual(cellAddressToInteger('ZZ'), 702);
	assert.deepStrictEqual(cellAddressToInteger('AAA'), 703);
	assert.deepStrictEqual(cellAddressToInteger('AAB'), 704);
	assert.deepStrictEqual(cellAddressToInteger('ALL'), 1000);
})();


/**
 * @param {number} number
 * @returns {string}
 */
function integerToCellAddress(number){
	let address = '';
	while (number){
		remaining = (number - 1) % 26;
		number = Math.floor((number - 1) / 26);
		address = String.fromCharCode('A'.charCodeAt(0) + remaining) + address;
	}
	return address
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(integerToCellAddress(1), 'A');
	assert.deepStrictEqual(integerToCellAddress(6), 'F');
	assert.deepStrictEqual(integerToCellAddress(26), 'Z');
	assert.deepStrictEqual(integerToCellAddress(27), 'AA');
	assert.deepStrictEqual(integerToCellAddress(28), 'AB');
	assert.deepStrictEqual(integerToCellAddress(30), 'AD');
	assert.deepStrictEqual(integerToCellAddress(52), 'AZ');
	assert.deepStrictEqual(integerToCellAddress(53), 'BA');
	assert.deepStrictEqual(integerToCellAddress(61), 'BI');
	assert.deepStrictEqual(integerToCellAddress(78), 'BZ');
	assert.deepStrictEqual(integerToCellAddress(79), 'CA');
	assert.deepStrictEqual(integerToCellAddress(676), 'YZ');
	assert.deepStrictEqual(integerToCellAddress(677), 'ZA');
	assert.deepStrictEqual(integerToCellAddress(702), 'ZZ');
	assert.deepStrictEqual(integerToCellAddress(703), 'AAA');
	assert.deepStrictEqual(integerToCellAddress(704), 'AAB');
	assert.deepStrictEqual(integerToCellAddress(1000), 'ALL');
})();