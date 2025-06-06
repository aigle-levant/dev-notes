---
tags: [react]
---
- **What do pure functions do?**: Perform a calculation, nothing else.
- **What are the 2 characteristics of a pure function?**
	- It doesn't change any objects or variables before it [i.e. its existence].
	- Given the same inputs, it returns the same output.

This is a pure function.
```js
function double(n) {
	return (2*n);
}
```
- **How are they treated in React?**: Every component is a pure function.
	- **What does this mean?**: Given the same inputs, every component must always return the same JSX.

This is a pure component.

```jsx
function StudentTotal({ sOne, sTwo, sThree, sFour, sFive }) {
	return (
		<p>Total: {sOne+sTwo+sThree+sFour+sFive}</p>
	)
}

export default function App() {
	return (
		<StudentTotal sOne={23} sTwo={45} sThree={64} sFour={54} sFive={23}/>
	)
}
```
