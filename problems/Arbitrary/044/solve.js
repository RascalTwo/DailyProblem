const fetch = require('node-fetch');

/**
 * @param {fetch.Response} response
 * @returns {object}
 */
async function handleResponse(response) {
  if (response.ok) return response.json();

  console.error('Invalid request:', response);
  process.exit(1);
}

const API = {
  getSpeciesID: name =>
    fetch(`https://pokeapi.co/api/v2/pokemon/${name}`)
      .then(handleResponse)
      .then(({ species: { url } }) => url.split('/').slice(-2)[0]),
  getEvolutionChainID: speciesID =>
    fetch(`https://pokeapi.co/api/v2/pokemon-species/${speciesID}`)
      .then(handleResponse)
      .then(({ evolution_chain: { url } }) => url.split('/').slice(-2)[0]),
  getEvolutionChain: evolutionChainID =>
    fetch(`https://pokeapi.co/api/v2/evolution-chain/${evolutionChainID}`)
      .then(handleResponse)
      .then(({ chain }) => chain),
};

/**
 * @param {string} name
 * @returns {string[]}
 */
async function getPokemonEvolutions(name) {
  const speciesID = await API.getSpeciesID(name);
  const evolutionChainID = await API.getEvolutionChainID(speciesID);
  const evolutionChain = await API.getEvolutionChain(evolutionChainID);

  const names = new Set();

  const links = [evolutionChain];
  while (links.length) {
    const link = links.pop();
    names.add(link.species.name);
    links.push(...link.evolves_to);
  }

  return names;
}

(async () => {
  const assert = require('assert');

  assert.deepStrictEqual(
    await getPokemonEvolutions('eevee'),
    new Set(['umbreon', 'sylveon', 'glaceon', 'espeon', 'leafeon', 'vaporeon', 'eevee', 'jolteon', 'flareon']),
  );
  assert.deepStrictEqual(
    await getPokemonEvolutions('wurmple'),
    new Set(['beautifly', 'wurmple', 'dustox', 'silcoon', 'cascoon']),
  );
  assert.deepStrictEqual(
		await getPokemonEvolutions('pichu'),
		new Set(['pichu', 'raichu', 'pikachu'])
	);
})();
