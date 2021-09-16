# Get All Possible Animal Evolutions

<!-- INFO TABLE BEGIN -->

| Provider                                          | Solutions                                                                                                                                                                                                                                                                                                    |
| :-----------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Arbitrary](../../../docs/providers/Arbitrary.md) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Given methods to interact with an API that returns various animal information, given the name of an animal, return all the possible evolutions of that animal.

The API has been abstracted into methods described below, with the relevant information described:

- `get_species_id(name)`
  - Receives ID of the provided species
- `get_evolution_chain(species_id)`
  - Receives ID of an evolution chain
- `get_evolution_chain(evolution_chain_id)`
  - Receives root link of evolution chain, structure shown below:

```json
{
  "evolves_to": [/*Array of Link objects*/],
  "species": {
    "name": "",
    "id": 0
  }
}
```

## Examples

| Input       | Output                                                                                              |
| ----------- | --------------------------------------------------------------------------------------------------- |
| `'eevee'`   | `{'umbreon', 'sylveon', 'glaceon', 'espeon', 'leafeon', 'vaporeon', 'eevee', 'jolteon', 'flareon'}` |
| `'wurmple'` | `{'beautifly', 'wurmple', 'dustox', 'silcoon', 'cascoon'}`                                          |
| `'pichu'`   | `{'pichu', 'raichu', 'pikachu'}`                                                                    |
