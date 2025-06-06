- **When should you group related states?**: When you always update 2 or more state variables at the same time. They must be merged into a single variable.
- **What should be avoided, mainly?**: Contradicting and redundant states, duplication, deeply-nested states.
- **How can a state be redundant?**: If you can calculate info. from a component's props or existing state variables, it *doesn't* need a new state variable.
- **What's the end goal?**: Making state easy to update without introducing bugs. Modularity, in general.

> "Make your state as simple as it can be—but no simpler."

## Grouping states

This could be grouped together.
```jsx
function PlayerStatus() {
    const [isInjured, setIsInjured] = React.useState(false);
    const [health, setHealth] = React.useState(100);
}
```

```jsx
function PlayerStatus() {
    const [health, checkHealth] = React.useState(
        { isInjured: false, health: 100 }
    );
}
```

## Contradictions

- **What is wrong with this component?**
	- 2 state variables where a single one could do.
	- If `setIsSent` and `setIsSending` aren't called together, both become `true` at the same time and message never gets sent.

```jsx
import { useState } from 'react';

// this part has contradictions
export default function FeedbackForm() {
  const [text, setText] = useState('');
  const [isSending, setIsSending] = useState(false);
  const [isSent, setIsSent] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setIsSending(true);
    await sendMessage(text);
    setIsSending(false);
    setIsSent(true);
  }

  if (isSent) {
    return <h1>Thanks for feedback!</h1>
  }

  return (
    <form onSubmit={handleSubmit}>
      <p>How was your stay at The Prancing Pony?</p>
      <textarea
        disabled={isSending}
        value={text}
        onChange={e => setText(e.target.value)}
      />
      <br />
      <button
        disabled={isSending}
        type="submit"
      >
        Send
      </button>
      {isSending && <p>Sending...</p>}
    </form>
  );
}

// Pretend to send a message.
function sendMessage(text) {
  return new Promise(resolve => {
    setTimeout(resolve, 2000);
  });
}
```

- **How can it be fixed?**

```jsx
import { useState } from 'react';

export default function FeedbackForm() {
  const [text, setText] = useState('');
  const [status, setStatus] = useState('typing');

  async function handleSubmit(e) {
    e.preventDefault();
    setStatus('sending');
    await sendMessage(text);
    setStatus('sent');
  }
  let isSending = status === 'sending'
  let isSent = status === 'sent'

  if (isSent) {
    return <h1>Thanks for feedback!</h1>
  }

  return (
    <form onSubmit={handleSubmit}>
      <p>How was your stay at The Prancing Pony?</p>
      <textarea
        disabled={isSending}
        value={text}
        onChange={e => setText(e.target.value)}
      />
      <br />
      <button
        disabled={isSending}
        type="submit"
      >
        Send
      </button>
      {isSending && <p>Sending...</p>}
    </form>
  );
}

// Pretend to send a message.
function sendMessage(text) {
  return new Promise(resolve => {
    setTimeout(resolve, 2000);
  });
}
```

## Redundancies

- **Fix any redundancies in this form.**

```jsx
import { useState } from 'react';

export default function Form() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [fullName, setFullName] = useState('');

  function handleFirstNameChange(e) {
    setFirstName(e.target.value);
    setFullName(e.target.value + ' ' + lastName);
  }

  function handleLastNameChange(e) {
    setLastName(e.target.value);
    setFullName(firstName + ' ' + e.target.value);
  }

  return (
    <>
      <h2>Let’s check you in</h2>
      <label>
        First name:{' '}
        <input
          value={firstName}
          onChange={handleFirstNameChange}
        />
      </label>
      <label>
        Last name:{' '}
        <input
          value={lastName}
          onChange={handleLastNameChange}
        />
      </label>
      <p>
        Your ticket will be issued to: <b>{fullName}</b>
      </p>
    </>
  );
}
```

```jsx
import { useState } from 'react';

export default function Form() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
// removed fullName state variable
  function handleFirstNameChange(e) {
    setFirstName(e.target.value);
    // removed mentions of setFullName()
  }

  function handleLastNameChange(e) {
    setLastName(e.target.value);
    // removed mentions of setFullName()
  }
// added function to set full name from the state variables
  function setFullName(firstName, lastName) {
    return (firstName + ' ' + lastName);
  }

  return (
    <>
      <h2>Let’s check you in</h2>
      <label>
        First name:{' '}
        <input
          value={firstName}
          onChange={handleFirstNameChange}
        />
      </label>
      <label>
        Last name:{' '}
        <input
          value={lastName}
          onChange={handleLastNameChange}
        />
      </label>
      <p>
        Your ticket will be issued to: <b>{setFullName(firstName, lastName)}</b>
      </p>
    </>
  );
}
```

## Duplication

- **What's wrong with the below component?**
	- Value of `seletedItem` = Item in the `items` list.
		- Info. about item is duplicated in 2 different places.
		- `items = [{ id: 0, title: 'pretzels'}, ...]`
		- `selectedItem = {id: 0, title: 'pretzels'}`
		- `selectedItem` will still point to the old reference despite being edited.
	- If 'choose' is clicked, then the item is edited, the bottom label doesn't update at all.

```jsx
import { useState } from 'react';

const initialItems = [
  { title: 'pretzels', id: 0 },
  { title: 'crispy seaweed', id: 1 },
  { title: 'granola bar', id: 2 },
];

export default function Menu() {
  const [items, setItems] = useState(initialItems);
//   why does this exist?
  const [selectedItem, setSelectedItem] = useState(
    items[0]
  );

  function handleItemChange(id, e) {
    setItems(items.map(item => {
    // item id in list is the same as the shit we pass as
    // input
      if (item.id === id) {
        return {
          ...item,
          title: e.target.value,
        };
      } else {
        return item;
      }
    }));
  }

  return (
    <>
      <h2>What's your travel snack?</h2> 
      <ul>
        {items.map((item, index) => (
          <li key={item.id}>
            <input
              value={item.title}
              onChange={e => {
                handleItemChange(item.id, e)
              }}
            />
            {' '}
            <button onClick={() => {
              setSelectedItem(item);
            }}>Choose</button>
          </li>
        ))}
      </ul>
      <p>You picked {selectedItem.title}.</p>
    </>
  );
}
```

```jsx
import { useState } from 'react';

const initialItems = [
  { title: 'pretzels', id: 0 },
  { title: 'crispy seaweed', id: 1 },
  { title: 'granola bar', id: 2 },
];

export default function Menu() {
  const [items, setItems] = useState(initialItems);
  // changed selectedItem for selectedId
  const [selectedId, setId] = useState(0);

  // let selectedItem be a constant within scope.
  // set selectedItem based on selectedId matching
  // item's id
  const selectedItem = items.find(item =>
    item.id === selectedId
  )
  function handleItemChange(id, e) {
    setItems(items.map(item => {
      if (item.id === id) {
        return {
          ...item,
          title: e.target.value,
        };
      } else {
        return item;
      }
    }));
  }

  return (
    <>
      <h2>What's your travel snack?</h2> 
      <ul>
        {items.map((item, index) => (
          <li key={item.id}>
            <input
              value={item.title}
              onChange={e => {
                handleItemChange(item.id, e)
              }}
            />
            {' '}
            <button onClick={() => {
              setSelectedItem(item);
            }}>Choose</button>
          </li>
        ))}
      </ul>
      <p>You picked {selectedItem.title}.</p>
    </>
  );
}
```
