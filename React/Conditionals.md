---
tags:
  - react
  - conditionals
---
Some components can be render based on a [[State|state]] or [[Props|props]].
- **Usage**: Displaying different UI elements like user login, account info, etc.

```js
const user = {
  // user info.
}

// this comes under react state management
function AppStatus() {
  const [status, setStatus] = useState('loading');
  // default status is loading
  // depending on value inputted, it'll change status and will affect userProfile() as well.
}

function userProfile({user}) {
  // switch case to explain the different statuses
  let message;
  switch (status) {
    case 'loading':
      message = "Loading your content..."
    case 'error':
      message = "Something went wrong. Please try again."
    case 'success':
      message = `Welcome back, {user.name}!"`
  }
  // now to return the user profile
  return (
    <div>
      <h1>Status: {status}</h1>
      <p>{message}</p>
    </div>
  )
}
```

## Practice one

**Create a React component that toggles the background color of a button between "brown" and "white" each time it is clicked.**

### Requirements:

1. Use React state to manage the background color.
2. The initial background color should be `"brown"`.
3. Clicking the button should:
    - Change the background color to `"white"` if it is `"brown"`.
    - Change it back to `"brown"` if it is `"white"`.
4. Display the current background color on the button using inline styles.
5. Log a message to the console indicating whether the background color has changed.

### Solution

```jsx
import React from 'react';

function Button({ value, handleClick }) {
    return (
        <button style={{backgroundColor:value}} onClick={handleClick}>Click me</button>
    )
}

export default function Box() {
    const [backgroundColor, setBackgroundColor] = React.useState("brown");

    function handleClick(e) {
        if (backgroundColor) {
            setBackgroundColor("white");
            console.log("BG has changed.")
        } else {
            setBackgroundColor("brown")
        }
    }

    return (
        <>
            <Button value={backgroundColor} handleClick={handleClick} />
        </>
    )
}
```
