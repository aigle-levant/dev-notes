---
tags: [react]
---
- **Declarative programming**: Focus on what the program should achieve, rather than how it should achieve it.
- **Imperative programming**: Each step is explicitly stated in order to achieve a desired outcome.
- **How to implement an UI declaratively?**
	- Identify the components' visual states.
	- What triggers those states?
	- Represent each state in memory using `useState`.
	- Remove any non-essential state variables.
	- Connect the event handlers to set the state.
- Each state may have its own mock-up for testing [like empty, typing, submitting, etc.]
	- Each mock-up has its own `status` value.

```jsx
export default function Form({ status='empty' }) {
	if (status==='success') {
		return <p>Yay!</p>
	}
	return (
		<>
			<p>You gotta loicense for that, mate?</p>
			<form>
				<textarea />
				<button>Submit</button>
			</form>
		</>
	)
}
```

- If a component has a lotta visual states, show them all in one page [storybooks or living styleguides].
- **What are the 2 kinds of inputs triggering responses?**
	- Human inputs [clicking buttons, typing in field, etc.]
	- Computer inputs [network response, image loading, server down, etc.]

```jsx
const [isEmpty, setIsEmpty] = useState(true);
const [isTyping, setIsTyping] = useState(false);
const [isSubmitting, setIsSubmitting] = useState(false);
const [isSuccess, setIsSuccess] = useState(false);
const [isError, setIsError] = useState(false);
```
- **What's the goal of having a better UI?**: To prevent cases where state in memory isn't related to the UI components you want your user to see [eg: don't show error message and disable input at the same time].