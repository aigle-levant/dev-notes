---
tags: [react]
---
- **What is it?**: Converting React components -> DOM elements
- **Why do we do that?**: To display them in a browser.
- **Steps in requesting and serving UI**:
	- Triggering a render.
	- Rendering components.
	- Committing to the DOM.
- **Why is a render triggered?**
	- A component is facing its first [initial] render. [eg: if I'm rendering my webpage for the first time]
	- State of component [or ancestor] has been updated. [eg: if I change the semester from 4th to 5th]
- **How is a render triggered?**: By calling `createRoot()` with the root element and then calling `root.render()`.

```jsx
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

const root = createRoot(document.getElementById('root'));
root.render(<App />);
```

- **How to trigger renders after updating state?**: Update the component's state using `set()`.
- **What component is called upon initial render?**: Root component
- **What component is called upon subsequent renders?**: Function component whose change of state is triggering the render.
	- If the component returns some other component, it will be rendered next.
	- Continues until there are no more nested components.
- **How does React modify the DOM for initial render?**: `appendChild()` is used to put all the DOM nodes properly on screen.
- **How does React modify the DOM for re-renders?**: Only the necessary operations are done to update it.
- **What is the usage of ``<StrictMode>``?**: Lets you find common bugs early in development.
	- Components will re-render a second time and re-run effects again -> Impure rendering, missing Effect cleanup.
	- Callbacks refs will be run again -> Finds bugs caused by missing ref cleanup.
	- Depreciated APIs will be found out.
