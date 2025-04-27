- **What is the library used by React to communicate with browsers?**: React-DOM
- **What's the usage of fragments ``<> </>``?**: To group elements together without a wrapper node.

## Props
**How can we ensure each square has an unique number?**: We use props [argument on Square component] to pass the value to each square individually. Then in the board, we update the props of the component.

```js
// value is the props being passed to each
// square component
function Square({ value }) {
  return <button className="square">{value}</button>;
}

export default function Board() {
    // its like passing args to a function
    // we pass value for the Square's props
  return (
    <>
      <div className="board-row">
        <Square value="1" />
        <Square value="2" />
        <Square value="3" />
      </div>
    </>
  );
}
```
## Event handling
**How do we handle events in a component?**: We define a function to handle it, then we introduce attributes [like onClick, etc.] to the component.
```js
function Square({ value }) {
// event handler
  function handleClick() {
    alert("You clicked me!");
  }
  return (
    // onClick -> event listener for clicking actions
    // it redirects to handleClick() for handling event
    <button className="square" onClick={handleClick}>
      {value}
    </button>
  );
}
```

## State management

- **What do components use to remember things?**: State
- **What hook lets a component have memory?**: `useState`.
- **What are the 2 parts of `useState`?**
	- State variable : Something you want the component to remember.
	- Function that can change the state variable.

```js
function Card() {
    /*
    background is the state variable
    changeBackground is the function to change the
    state variable
    'blue' is the current value of state variable
    */
	const [background, changeBackground] = useState('blue');

    return (
        // upon clicking, changeBackground() will be called
        // to change the state of background-color to yellow
        <>
            <button onClick={() => changeBackground('yellow')} style={{ backgroundColor: background }}>
                Click me
            </button>
        </>
    )
}
```

- **How should `style` be defined in a component when we use state variables?**: It should be defined in this format -> ``style={{ propertyName: stateVariable }}``
- **How can we set the value of a square to X upon click?**: We can setup a useState function to hold a value of `null`, then upon click, call the event handler that changes the state to 'X' from `null`.

```js
function Square() {
// value is the state variable, holds null rn
// setValue() is used to change value
  const [value, setValue] = react.useState(null);

// event handler that calls setValue() to
// change value
  function handleClick() {
    setValue("X");
  }
// upon click, handleClick() is called
// value [state variable] is the value of this
// component
  return (
    <button className="square" onClick={handleClick}>
      {value}
    </button>
  );
}
```
**How do we know the state of every Square component in the board?**: We store the game state in the Board component and pass a prop to Square for telling what it should display [like we passed a no. for each Square].

```js
// we go back to our props version
function Square({ value }) {
  return (
    <button className="square">{value}</button>
  );
}

export default function Board() {
/*
state variable is an array of 9 elements

Array(n).fill(null) -> Creates an array
with n number of elements and sets their
values to null.
*/
  const [squares, setSquares] = react.useState(Array(9).fill(null));
  return (
    // value is the props passed down to child
    // its value is squares[n]
    <>
      <div className="board-row">
        <Square value={squares[0]}/>
        <Square value={squares[1]}/>
        <Square value={squares[2]}/>
      </div>
    </>
)}
```

- **How do we have 2 child components communicate with each other?**: We declare the shared state [between the components] in their parent component.
- **How do we collect data from multiple children?**: Let the parent component pass state back to children via props.
- **How is event handling done when an event occurs in child and parent handles the state changes?**: A function is passed down from parent to child as props, which child will call upon event.

## Immutability

## Finale

## History

## 