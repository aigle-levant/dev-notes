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