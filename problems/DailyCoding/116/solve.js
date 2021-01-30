class Node{
	#_left;
	#_right;

	constructor(value, left=false, right=false){
		this.value = value;
		this.#_left = left;
		this.#_right = right;
	}

	get left(){
		if (this.#_left === false){
			this.#_left = Math.random() < 0.5 ? new Node(this.value - 1) : null;
		}
		return this.#_left;
	}

	set left(value){
		this.#_left = value;
	}

	get right(){
		if (this.#_right === false){
			this.#_right = Math.random() < 0.5 ? new Node(this.value + 1) : null;
		}
		return this.#_right;
	}

	set right(value){
		this.#_right = value;
	}

	toString(){
		return `value=${this.value} left=(${this.left}) right=(${this.right})`;
	}

	inspect = this.toString
}


function generate(){
	return new Node(0);
}


(() => {
	const assert = require('assert');

	const tree = generate();
	assert.notDeepStrictEqual(tree.left, false);
	assert.notDeepStrictEqual(tree.right, false);

	for (let i = 0; i < 10; i++){
		try{
			assert.deepStrictEqual(generate().toString().length > 32, true);
			break;
		}
		catch(_){}
	}
})();