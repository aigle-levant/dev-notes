- **How should we update objects in React?**: Create a new object [or make a copy of an existing object] and set the state to use that one instead.
- **How do we replace the value of a state variable?**: Trigger a re-render using the function.
- **If objects are immutable, how are values changed in them?**: The state of the object changes, but not the object itself.
- **Why should we treat objects as immutable, even though they are mutable?**: Even though the values are changed, React won't notice those changes.
	- **What does React keep track of?**: Previous state.
	- **What kind of comparison is done by React when comparing new and old objects?**: Shallow comparison [checks if object itself is new, not its values].
	- **What happens when we simply change the values of an object without replacing the original object?**: React will treat it as the old object.
	- **How to rectify this mistake?**: Create a new object with new values.

```jsx
import React from 'react';
import './App.css';

function Order() {
  const [order, setOrder] = React.useState({
    drink: null,
    food: null
  });
  return (
    <div onClick={() => {
      order.drink = "Java coffee",
      order.food = "Pork Adobo"
    }}>
      Drink: {order.drink}
      Food: {order.food}
    </div>
  )
}
export default Order;
```

This part shouldn't be modified directly, React won't recognise it as a new object at all.
```jsx
<div onClick={() => {
      order.drink = "Java coffee",
      order.food = "Pork Adobo"
}}>
```

- **How to trigger a re-render for an object?**: Create a new object and pass it to the state setting function.

```jsx
import React from 'react';

function Order() {
  const [order, setOrder] = React.useState({
    drink: null,
    food: null
  });
// display stuff only if values for order.drink &
// order.food exist, else return 'Nothing'
  return (
    <div onClick={() => {
      setOrder({
        drink: "Java coffee",
        food: "Pork Adobo"
      })
    }}>
      {order.drink && order.food ? (
        <>
          <p>Drink: {order.drink}</p>
          <p>Food: {order.food}</p>
        </>
      ): (<p>Nothing</p>)}
    </div>
  )
}
export default Order;
```
- **What is a local mutation?**: Modifying a freshly-created object [which no other code has referenced to yet].

```jsx
function setOrderItems() {
	const order = {
		drink: "Jigarthanda",
		food: "Kotthu Parotta"
	}
	order.food = "Set Dosa";
	return order;
}
```
- **What if I want to include existing data as a part of the new object?**: Use object spread syntax.

```jsx
export default function Form() {
  const [person, setPerson] = useState({
    firstName: 'Barbara',
    lastName: 'Hepworth',
    email: 'bhepworth@sculpture.com'
  });

  function handleChange(e) {
    setPerson({
      ...person,
      [e.target.name]: e.target.value
    });
  }

  return (
    <>
      <label>
        First name:
        <input
          name="firstName"
          value={person.firstName}
          onChange={handleChange}
        />
      </label>
      <label>
        Last name:
        <input
          name="lastName"
          value={person.lastName}
          onChange={handleChange}
        />
      </label>
      <label>
        Email:
        <input
          name="email"
          value={person.email}
          onChange={handleChange}
        />
      </label>
      <p>
        {person.firstName}{' '}
        {person.lastName}{' '}
        ({person.email})
      </p>
    </>
  );
}
```

## Example 1 - Custom email address

```jsx
import React from 'react';

export default function Form() {
// object created here with predefined values
  const [email, setEmail] = React.useState({
    username: "anon",
    mailserver: "yandex"
  });

  function handleInput(e) {
// we use the state function to change values
// to keep all changing functions in one place, we use
// e.target.name: e.target.value after object spread syntax
    setEmail({
      ...email,
      [e.target.name]: [e.target.value]
  })}

  return (
// value is set accordingly
// onChange modifies email.[value] at <p> when input is
// entered
    <>
      <form className='form'>
        <label for="username">Username:</label>
        <input className='input' type="text" name="username" value={email.username} onChange={handleInput}/>
        <label for="mailserver">Which mail server do you use?</label>
        <input className='input' type="text" name="mailserver" value={email.mailserver} onChange={handleInput}/>
      </form>
      <p>Here's your email address : {email.username}@{email.mailserver}.com</p>
    </>
  )
}
```
## Example 2 - Add books without and with Immer

### Without Immer

```jsx
import React from 'react';

export default function ReadingList() {
  // initial state
  const [books, addBooks] = React.useState({
    user : {
      name: "Anon",
      books: ["Crime and Punishment", "Posthumous Memories of Bras Cubas"]
    }
  })

  // add books
  function handleClick() {
    // setting new state for object
    addBooks(prev => ({
      // spread syntax for previous state's object
      ...prev,
      user: {
        // spread syntax for name
        ...prev.user,
        // spread syntax for previous state's user object
        // book values
        books: [...prev.user.books, "Wuthering Heights"]
      }
    }))
  }

  return (
    // use state for current state
    <div>
      <h2>{books.user.name}'s books:</h2>
      <ul>
        {books.user.books.map((bookName, index) => (
          <li key={index}>{bookName}</li>
        ))}
      </ul>
      <button onClick={handleClick}>Add a book</button>
    </div>
  )
}
```

### With Immer

```jsx
import React from "react";
import { useImmer } from "use-immer";

export default function ReadingList() {
  // initial state
  const [books, addBooks] = useImmer({
    user : {
      name: "Anon",
      books: ["Crime and Punishment", "Posthumous Memories of Bras Cubas"]
    }
  })

  // add books
  function handleClick() {
    addBooks(draft => {
      draft.user.books.push("Wuthering Heights");
    })
  }

  return (
    // use state for current state
    <div>
      <h2>{books.user.name}'s books:</h2>
      <ul>
        {books.user.books.map((bookName, index) => (
          <li key={index}>{bookName}</li>
        ))}
      </ul>
      <button onClick={handleClick}>Add a book</button>
    </div>
  )
}
```
