---
tags: [react]
---
## [[Components]]

- What are components?
	- Components are the parts of the user interface created using JSX.
- What is the usage of components?
	- To make an UI.
- What are components written using?
	- JavaScript XML [JSX].

**Write a component for a navigation bar.**

```jsx
function NavBar() {
  return (
    <nav>
      <div className='nav-logo'>
        <p>Logos</p>
      </div>
      <div className='nav-links'>
        <li><a href='#'>About</a></li>
        <li><a href='#'>Contact Us</a></li>
      </div>
    </nav>
  )
}

export default function App() {
  return (<NavBar/>)
}
```

## [[Conditionals]]

- Why are conditionals used in React?
	- To iterate through a list, for state management, etc.

**Write a conditional for displaying different messages in a box for user login states.**

```jsx

export default function Message() {
  // initial = started
  const [initial, result] = React.useState('started');
  const refs = React.useRef(null);
  switch (initial) {
    case 'success':
      refs.current.innerText = 'success';
      break;
    case 'failure':
      refs.current.innerText = 'failure';
      break;
  }
  return (
    <div className='message-box'>
      <p ref={refs}>Text</p>
      <button onClick={() => result('started')}>Click me</button>
    </div>
  )
}
```

## [[Rendering Lists]]

- What function is used to execute a function for each item in a list?

**Write a component that executes the following action for a set of students.**

- **If the student's grades are above 40, mark them with green.**
- **If the student's grades are 40 and below, mark them with red.**
**<!-- Calculate the CGPA on your own and check based on that. -->**

```jsx
function StudentDetails({ name, marks }) {
  return (
    <div
    style={{ backgroundColor: marks>=40 ? 'green' : 'red'}}>
      <p>Name: {name}</p>
      <p>Grade: {marks}</p>
    </div>
  )
}

export default function App() {
  return (
    <>
      <StudentDetails name="Niharika Amarnath" marks={45}/>
      <StudentDetails name="Silvio Fernandes" marks={67}/>
      <StudentDetails name="Manikandan Das" marks={24}/>
    </>
  );
}
```

## [[Props]]
- What are props?
	- Data passed to a JSX tag.
- From whom to whom are props passed down?
	- Parent component to child component
- **How can one read props inside a  child component?**
	- By referencing them in the parent component.
- **What is destructuring?**
	- Defining a common name for future usage as props.

```js
function Student({ student }) {
    return (
        <div>
            <img src={student.image} alt={student.name}/>
            <p>Name: {student.name}</p>
            <p>Course: {student.course}</p>
            <p>Department: {student.dept}</p>
        </div>
    );
}

export default function Profile() {
    return (
    <Student image="img" name="Anon" course="CSE" dept="ML"/>
  );
}
```
**How would Profile() be implemented to show the student details?**

## [[Hooks]]
- What are hooks?
	- They are functions called for state change and that which start with `use` keyword.
- Where should one call hooks?
	- Right after defining a component.

How can one call a conditional with a hook?

```jsx

```

How can one call a loop with a hook?

```jsx

```

## [[Event handling]]

- How are events handled in React?

Write a component to handle clicking a button to make its colour go from white to black.

