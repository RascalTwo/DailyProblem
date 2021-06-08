
/**
 * @param {number[]} prices
 * @returns {number}
 */
function bestPriceToBuy(prices){
	let bestBuy = 0;
	let bestPriceToBuy = 0;

	for (let i = 0; i < prices.length; i++){
		const buy = prices[i];
		const profit = Math.max(...prices.slice(i)) - buy;
		if (profit > bestPriceToBuy){
			bestBuy = buy
			bestPriceToBuy = profit
		}
	}

	return bestBuy
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(bestPriceToBuy([9, 11, 8, 5, 7, 10]), 5);
})();
