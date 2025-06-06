---
tags: [react]
---
- A component can have different states [empty, typing, success, failure].
	- Each state has its own set of UI actions and other effects.
- Most websites using React track data entered in user-input. [Without this, UI is dum-dum].
- **Imperative programming**: Write exact instructions to manipulate UI depending on what just happened.
- **Declarative programming**: You declare components in UI and React figures out how to update UI based on state.
- **What hooks lets you give memory to components?**: `useState()`
- **What event listener is used to update state of a component?**: `onChange`
- **What are the 5 things to take care of while modelling UI as a function of state using declarative programming?** [how to make UI React-worthy?]
	- Identify every possible look your component could've based on interactions. [eg: typing, submitting, error, etc.]
	- For each state, ask yourself 'what triggers those states? what causes a state to transition into another state?' [eg: typing updates input field and is triggered by onChange, submit btn triggers onClick or onSubmit, etc.]
		- Event -> Logic -> State change -> Re-rendering component
	- Represent only the key states in memory using `useState()`
		- Determine if you need to remember this across renders. If yes, use `useState()`. If not, let it be a variable alone.
	- Don't store derived values. Also, keep state change minimal.
	- Now connect components and their event handlers together.

![[Pasted image 20250508132523.png]]

## Challenge 1

### Problem statement

Make it so that clicking on the picture _removes_ the `background--active` CSS class from the outer `<div>`, but _adds_ the `picture--active` class to the `<img>`. Clicking the background again should restore the original CSS classes.

Visually, you should expect that clicking on the picture removes the purple background and highlights the picture border. Clicking outside the picture highlights the background, but removes the picture border highlight.

### My Solution

```jsx
export default function Picture() {
  const [active, setActive] = useState("no");
  let backgroundClassName = "background";
  let pictureClassName = "picture";

  function handleClick(e) {
    if (e) {
      backgroundClassName -= " background--active";
      pictureClassName += " picture--active";
    }
    setActive(!active);
  }
  return (
    <div
      className=
      onClick={() => {
        handleClick(true);
      }}
    >
      <img
        className="picture"
        alt="Rainbow houses in Kampung Pelangi, Indonesia"
        src="https://i.imgur.com/5qwVYb1.jpeg"
        onClick={() => {
          handleClick(true);
        }}
      />
    </div>
  );
}
```

### Proposed solution

```jsx
export default function Picture() {
  const [active, setActive] = useState(false);
  let backgroundClassName = "background";
  let pictureClassName = "picture";

  if (active) {
    pictureClassName += " picture--active";
  } else {
    backgroundClassName += " background--active";
  }
  return (
    <div
      className={backgroundClassName}
      onClick={() => {
        setActive(false);
      }}
    >
      <img
        className={pictureClassName}
        alt="Rainbow houses in Kampung Pelangi, Indonesia"
        src="https://i.imgur.com/5qwVYb1.jpeg"
        onClick={(e) => {
          e.stopPropagation();
          setActive(true);
        }}
      />
    </div>
  );
}
```
## Challenge 2

### Problem statement

This form switches between two modes: in the editing mode, you see the inputs, and in the viewing mode, you only see the result. The button label changes between “Edit” and “Save” depending on the mode you’re in. When you change the inputs, the welcome message at the bottom updates in real time.

Your task is to reimplement it in React in the sandbox below. For your convenience, the markup was already converted to JSX, but you’ll need to make it show and hide the inputs like the original does.

Make sure that it updates the text at the bottom, too!

### Your solution

```jsx
import { useState } from "react";

export default function EditProfile() {
  const [editing, isEditing] = useState(false);
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");

  function handleClick() {
    if (editing) {
    }
    isEditing(!editing);
  }

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        isEditing(!editing);
      }}
    >
      <label>
        First name:{" "}
        {editing ? (
          <>
            <input
              value={firstName}
              onChange={(e) => {
                setFirstName(e.target.value);
              }}
            />
          </>
        ) : (
          <>
            <b>{firstName}</b>
          </>
        )}
      </label>
      <label>
        Last name:{" "}
        {editing ? (
          <input
            value={lastName}
            onChange={(e) => {
              setLastName(e.target.value);
            }}
          />
        ) : (
          <b>{lastName}</b>
        )}
      </label>
      <button
        type="submit"
        onClick={() => {
          handleClick;
        }}
      >
        Edit Profile
      </button>
      <p>
        {editing ? (
          <i>What is your name?</i>
        ) : (
          <i>
            Hello, {firstName} {lastName}!
          </i>
        )}
      </p>
    </form>
  );
}
```


