[_metadata_:generated]: - "true"

# Create the base - Dungeon crawler #1

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55f74a7433feba03680000c5`](https://www.codewars.com/kata/55f74a7433feba03680000c5) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

<h1>Create the base - Dungeon crawler #1</h1>
<p>
Welcome to the Dungeon crawler series! You and your friends had a great idea to create this awesome text based dungeon crawler for a school project. Since you're a programmer pro now you have been given the task of creating the logic and graphics (since this is just a text based game). First off you have to create the base of the game, Introduction, initilizing variables all the important basic stuff!
</p>

<h2>Task</h2>
<p>
Your task is to create all the base classes we will be using the four classes ```Game```, ```Player```, ```Monster``` and ```Map```.
</p>

<h2>Input</h2>
<p>
  <h4>Game</h4>
    <strong>Parameters</strong>
    <ul>
      <li>
        <p><strong>name</strong> - The name parameter will be used to pass into the ```Player``` class which will then be stored in the property name ```player```.
        </p>
      </li>
      <li>
        <p><strong>level</strong> - The level parameter will be used to determin the difficulty of the game you must store this in a property called ```level```. This should have a default value of 0. WARNING: You may also get given a string of a number if so parse it, but if you are given anything other than a valid int then default to 0         
        </p>
      </li>
    </ul>
  <strong>Properties</strong>
    <ul>
      <li>
        <p><strong>player</strong> - This should be a new Player class with the name used as the parameter.
        </p>
      </li>
      <li>
        <p><strong>level</strong> - This should store the level passed into the constructor.
        </p>
      </li>
      <li>
        <p><strong>floors</strong> - This should be an empty array for now.
        </p>
      </li>
    </ul>
  <br>
  <h4>Player</h4>
  <strong>Parameters</strong>
    <ul>
      <li>
        <p><strong>name</strong> - The name parameter will be used to pass into the ```Player``` class which will then be stored in the property name ```player```. This should have a default value of 'Player' if a name is null,  empty or not a string.
        </p>
      </li>
    </ul>
  <strong>Properties</strong>
    <ul>
      <li>
        <p><strong>name</strong> - The name property must be initilized with the name parameter but if the name is null or empty then you must use 'Player'        
        </p>
      </li>
      <li>
        <p><strong>health</strong> - The health property must have a default value of ```100.00```        
        </p>
      </li>
      <li>
        <p><strong>position</strong> - The position must have a default value of an object which looks similar to this: ```{x:0, y:0}```      
        </p>
      </li>
      <li>
        <p><strong>damage</strong> - The damage must have a default value of ```10.00```        
        </p>
      </li>
      <li>
        <p><strong>luck</strong> - The luck must have a default value of ```1.00```        
        </p>
      </li>
    </ul>
  <h4>Monster</h4>
  <strong>Parameters</strong>
    <ul>
      <li>
        <p><strong>level</strong> - The level parameter will be used to determin the difficulty of the game you must store this in a property called ```level```.          
        </p>
      </li>
    </ul>
  <strong>Properties</strong>
    <ul>
      <li>
        <p><strong>level</strong> - This should store the level passed into the constructor.
        </p>
      </li> 
    </ul>
  <h4>Map</h4>
  <strong>Parameters</strong>
    <ul>
      <li>
        <p><strong>level</strong> - The level parameter will be used to determin the difficulty of the game you must store this in a property called ```level```.          
        </p>
      </li>
    </ul>
  <strong>Properties</strong>
    <ul>
      <li>
        <p><strong>level</strong> - This should store the level passed into the constructor.
        </p>
      </li> 
    </ul>
</p>
