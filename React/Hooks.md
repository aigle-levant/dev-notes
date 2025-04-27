---
tags:
  - react
  - react-hooks
---
**What are they?**: Functions starting with `use` keyword.
**Where can they be called?**: On top of components or hooks.
- **What if I want to use them in a conditional?**: Put the conditional inside a child component.
- **Why can't I use them just like that?**: If the condition changes between state renders, the hook may or may not be called. It should be in one camp, not be a cat on the wall.

```js
// this is not allowed
if (condition) {
    const [backgroundColor, setBackgroundColor] = useState('beige');
}

// this is also not allowed
for (let i=0; i<5; i++) {
    const [backgroundColor, setBackgroundColor] = useState('beige');
}
```

```js
export default function App() {
    // hook is on top
    // remember, the 2nd option is a FUNCTION
    const [backgroundColor, setBackgroundColor] = useState('beige');
    
    return (
        // upon click, call the event handler that
        // changes the state of bg of the button
        <div style={{backgroundColor}}>
            <button onClick={() => setBackgroundColor('lightblue')}>
                Change me.
            </button>
        </div>
    )
}
```
