- **What would you do if you need the state of 2 components to change together?**: Set that state on the parent component and pass it down to the child components via props.
- **What is lifting state up?**: Sharing state between components using a common parent component.

Instead of setting state in the child component...

```jsx
// parent
export function App() {
  return (
    <div className='App'>
      <h1>Look at these cards!</h1>
      <Card
        name="Anonymous Another"
        power="Hacker"
      />
      <Card
        name="Anonymous Asexual"
        power="100% Productive"
      />
    </div>
  );
}

// child
export function Card({ name, power }) {
  const [isActive, setIsActive] = React.useState(false);
  return (
    <div className="card">
      <hr/>
      <p>Name: {name}</p>
      {isActive ? (
        <p>Power: {power}</p>
      ) : (
        <button onClick={() => setIsActive(true)}>Reveal my power</button>
      )}
      <hr/>
    </div>
  )
}
```

We could set them in the parent component instead.

```jsx
// parent
export function App() {
  const [active, setIsActive] = React.useState(0);
  return (
    <div className='App'>
      <h1>Look at these cards!</h1>
      <Card
        name="Anonymous Another"
        power="Hacker"
        isActive={active===0}
        reveal={() => setIsActive(0)}
      />
      <Card
        name="Anonymous Asexual"
        power="100% Productive"
        isActive={active===1}
        reveal={() => setIsActive(1)}
      />
    </div>
  );
}

// child
export function Card({ name, power, isActive, reveal }) {
  return (
    <div className="card">
      <hr/>
      <p>Name: {name}</p>
      {isActive ? (
        <p>Power: {power}</p>
      ) : (
        <button onClick={reveal}>Reveal my power</button>
      )}
      <hr/>
    </div>
  )
}
```
- **What do you mean by single source of truth in terms of React?**: For each piece of state, there's a specific component holding that piece of information.