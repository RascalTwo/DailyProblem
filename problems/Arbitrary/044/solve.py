import sys

import requests

from typing import Any, Dict, Set



class API:
	@staticmethod
	def get_species_id(name: str) -> int:
		response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
		if not response.ok:
			print('Invalid Request:', response)
			sys.exit(1)
		return int(response.json()['species']['url'].split('/')[-2])


	@staticmethod
	def get_evolution_chain_id(species_id: int) -> int:
		response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{species_id}')
		if not response.ok:
			print('Invalid Request:', response)
			sys.exit(1)
		return int(response.json()['evolution_chain']['url'].split('/')[-2])


	@staticmethod
	def get_evolution_chain(evolution_chain_id: int) -> Dict[str, Any]:
		response = requests.get(f'https://pokeapi.co/api/v2/evolution-chain/{evolution_chain_id}')
		if not response.ok:
			print('Invalid Request:', response)
			sys.exit(1)
		return response.json()['chain']


def solve(name: str) -> Set[str]:
	species_id = API.get_species_id(name)
	evolution_chain_id = API.get_evolution_chain_id(species_id)
	chain = API.get_evolution_chain(evolution_chain_id)

	names: Set[str] = set()

	links = [chain]
	while links:
		link = links.pop()
		names.add(link['species']['name'])
		links += link['evolves_to']
	return names


def test_solve():
	assert solve('eevee') == {'umbreon', 'sylveon', 'glaceon', 'espeon', 'leafeon', 'vaporeon', 'eevee', 'jolteon', 'flareon'}
	assert solve('wurmple') == {'beautifly', 'wurmple', 'dustox', 'silcoon', 'cascoon'}
	assert solve('pichu') == {'pichu', 'raichu', 'pikachu'}
