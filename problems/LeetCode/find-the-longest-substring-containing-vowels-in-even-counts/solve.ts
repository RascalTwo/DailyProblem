function solveBrute(string: string) {
  let best = '';
  for (let start = 0; start < string.length; start++) {
    for (let end = string.length; end >= start + 1; end--) {
      const substring = string.slice(start, end);
      const counts = substring
        .split(/([aeiou])/g)
        .reduce((counts, char) => (!(char in counts) ? counts : { ...counts, [char]: counts[char] + 1 }), {
          a: 0,
          e: 0,
          i: 0,
          o: 0,
          u: 0,
        } as Record<string, number>);
      if (Object.values(counts).some(count => count % 2 !== 0)) continue;
      if (substring.length > best.length) best = substring;
    }
  }
  return best;
}


function solvePrefixHashed(string: string){
  const indexes: Record<string, number> = {};
  const vowels = { a: 0b00001, e: 0b00010, i: 0b00100, o: 0b01000, u: 0b10000 }
  let evenOdd = 0b00000;
  indexes[evenOdd] = -1

  let best = 0;
  for (const [i, char] of [...string].entries()){
    if (char in vowels) evenOdd ^= vowels[char as keyof typeof vowels];

    if (evenOdd in indexes) best = Math.max(best, i - indexes[evenOdd])
    else indexes[evenOdd] = i;

  }
  return best
}

(() => {
  const assert = require('assert');

  assert.deepStrictEqual(solveBrute('eleetminicoworoep'), 'leetminicowor');
  assert.deepStrictEqual(solveBrute('leetcodeisgreat'), 'leetc');
  assert.deepStrictEqual(solveBrute('bcbcbc'), 'bcbcbc');

  assert.deepStrictEqual(solvePrefixHashed('eleetminicoworoep'), 13);
  assert.deepStrictEqual(solvePrefixHashed('leetcodeisgreat'), 5);
  assert.deepStrictEqual(solvePrefixHashed('bcbcbc'), 6);
  assert.deepStrictEqual(solvePrefixHashed('ixzhsdka'), 6)
})();
