- **What is it?**: Detecting errors in code without running it at all.
- **What is static type checking?**: Determining whether something's an error or not based on type of operands.
- **What does TS check before execution?**: Types of values of variables and others.
- **What is a superset?**: Language that includes all features of another language + new features [e.g.: C and C++, JS and TS].

```ts
let me = "Anon";
me = 99;
console.log(me);
// Type 'number' is not assignable to type 'string'.ts(2322)
```
- **What are the types used in TS?**: string, number, bigint, boolean, undefined, null, symbol
- **How can we set the type of a variable?**: ``let varName: dType = true;``.
- **What is a union type?**: A variable that can be assigned more than one type. 
	- ``let age: string | number;``

- **What is a primitive type?**: A type whose value is contained within a variable.
- **What is a reference type?**: A type whose value's memory location is referenced by the variable.

- **How can you define the type of elements in an array?**: ``const arr: dType[] = [elements];``.
- **How do you make an array that can contain any type?**: ``const arr: any[] = [elements];``.
- **How do you make an array that can contain more than one type?**: ``const arr: (string|boolean|number)[] = [elements];``

- **What is a tuple?**: Array with fixed size and types.
	- ``const student: [string, number, boolean] = ["Anon",67, true];``
- **How can you declare and use objects in TS?**: They must be declared with their types explicitly.

```ts
let song: {
	name: string;
	artist: string;
	isListened: boolean;
}

songOne = {
	name: "The Nights",
	artist: "Avicii",
	isListened: true,
};
```
- **What is an interface?**: A template for declaring multiple similar objects.

```ts
interface Song {
	name: string;
	artist: string;
	isListened: boolean;
}

let songOne: Song = {
	name: "The Nights",
	artist: "Avicii",
	isListened: true,
};

let songTwo: Song = {
	name: "My Blood",
	artist: "Twenty One Pilots",
	isListened: true,
}
```
- **How do you declare functions in Interfaces?**

```ts
interface Song {
	setListeningTo(name: string): string;
} let saySong: Song = {
	setListeningTo: function (name: string) {
		return `Currently listening to ${name}`;
	}
}
console.log(saySong.setListeningTo('Panic - 2011 Remaster'));
```
