---
tags: [react]
---
## Make the Square and Board component where props for numerical values are passed to each square individually

```jsx
import React from 'react';

function Square({ value }) {
    return (
    // button className is square, not btn
        <button className='square'>{value}</button>
    )
}

export default function Board() {
    return (
        <>
            <div className='board-row'>
                <Square value='1'/>
                <Square value='2'/>
                <Square value='3'/>
            </div>
            <div className='board-row'>
                <Square value='4'/>
                <Square value='5'/>
                <Square value='6'/>
            </div>
            <div className='board-row'>
                <Square value='7'/>
                <Square value='8'/>
                <Square value='9'/>
            </div>
        </>
    )
}
```

## Ensure that upon clicking a Square component, it marks it with a 'X'

```jsx
import React from 'react';

function Square() {
// WHERE THE HELL IS CONST?!
    [value, changeValue] = React.useState(null);
    function handleClick() {
        changeValue('X')
    }
    // no need of anonymous function at this moment
    // add value [state variable] for btn
    return (<button className='square' onClick={() => {handleClick()}}></button>)
}

export default function Board() {
    return (
        <>
            <div className='board-row'>
                <Square/>
                <Square/>
                <Square/>
            </div>
            <div className='board-row'>
                <Square/>
                <Square/>
                <Square/>
            </div>
            <div className='board-row'>
                <Square/>
                <Square/>
                <Square/>
            </div>
        </>
    )
}
```

Corrected part

```jsx
function Square() {
    const [value, changeValue] = React.useState(null);
    function handleClick() {
        changeValue("X");
    }
    return (
        <button className="square" onClick={handleClick}>{value}</button>
    );
}
```

## Refactor the previous code so that Square's state is lifted into the parent component, Board

```jsx
import React from "react";

function Square({ value }) {
  return <button className="square">{value}</button>;
}

export default function Board() {
// EXP: We need an empty set of squares
// Array(9).fill(null) -> Creates an array with 9 elements
// and fills them with null value
  const [squares, setSquares] = React.useState(Array(9).fill(null));
  return (
    <>
      <div className="board-row">
        <Square squares={[0]} />
        <Square squares={[1]} />
        <Square squares={[2]} />
      </div>
      <div className="board-row">
        <Square squares={[3]} />
        <Square squares={[4]} />
        <Square squares={[5]} />
      </div>
      <div className="board-row">
        <Square squares={[6]} />
        <Square squares={[7]} />
        <Square squares={[8]} />
      </div>
    </>
  );
}
```

## Ensure that upon clicking, the square will mark X

```jsx
import React from "react";
// EXP : onSquareClick is the props we pass from Board to Square
function Square({ value, onSquareClick }) {
  return (
    <button className="square" onClick={onSquareClick}>
      {value}
    </button>
  );
}

export default function Board() {
  const [squares, setSquares] = React.useState(Array(9).fill(null));
//   this funct handles click events
  function handleClick(i) {
    // Array.slice() -> create a copy of Array
    const squaredArray = squares.slice();
    // i is the part of array we click
    squaredArray[i] = "X";
    // now we call state management function
    // to deal with event
    setSquares(squaredArray);
  }
  return (
    // value={squares[i]} -> Array value will change with handleClick()
    // onSquareClick is the 2nd prop for Square
    // onSquareClick will call event handler for that value in array
    <>
      <div className="board-row">
        <Square
          value={squares[0]}
          onSquareClick={() => {
            handleClick(0);
          }}
        />
        <Square
          value={squares[1]}
          onSquareClick={() => {
            handleClick(1);
          }}
        />
        <Square
          value={squares[2]}
          onSquareClick={() => {
            handleClick(2);
          }}
        />
      </div>
      <div className="board-row">
        <Square
          value={squares[3]}
          onSquareClick={() => {
            handleClick(3);
          }}
        />
        <Square
          value={squares[4]}
          onSquareClick={() => {
            handleClick(4);
          }}
        />
        <Square
          value={squares[5]}
          onSquareClick={() => {
            handleClick(5);
          }}
        />
      </div>
      <div className="board-row">
        <Square
          value={squares[6]}
          onSquareClick={() => {
            handleClick(6);
          }}
        />
        <Square
          value={squares[7]}
          onSquareClick={() => {
            handleClick(7);
          }}
        />
        <Square
          value={squares[8]}
          onSquareClick={() => {
            handleClick(8);
          }}
        />
      </div>
    </>
  );
}
```

## Ensure that Xs and Os can be marked accordingly.

```jsx
import React from "react";

function Square({ value, onSquareClick }) {
  return (
    <button className="square" onClick={onSquareClick}>
      {value}
    </button>
  );
}

export default function Board() {
  const [squares, setSquares] = React.useState(Array(9).fill(null));
// xTurn -> is true if its X turn, otherwise false
// xIsNext -> will set xTurn to false at even turns
  const [xTurn, xIsNext] = React.useState(true);

  function handleClick(i) {
    const squaredArray = squares.slice();
    // will print X at first, then O
    if (xTurn) {
        squaredArray[i] = "X";
    } else {
        squaredArray[i] = "O";
    }
    
    setSquares(squaredArray);
    // sets xTurn false at even turns
    xIsNext(!xTurn);
  }
  return (
    <>
      <div className="board-row">
        <Square
          value={squares[0]}
          onSquareClick={() => {
            handleClick(0);
          }}
        />
        <Square
          value={squares[1]}
          onSquareClick={() => {
            handleClick(1);
          }}
        />
        <Square
          value={squares[2]}
          onSquareClick={() => {
            handleClick(2);
          }}
        />
      </div>
      <div className="board-row">
        <Square
          value={squares[3]}
          onSquareClick={() => {
            handleClick(3);
          }}
        />
        <Square
          value={squares[4]}
          onSquareClick={() => {
            handleClick(4);
          }}
        />
        <Square
          value={squares[5]}
          onSquareClick={() => {
            handleClick(5);
          }}
        />
      </div>
      <div className="board-row">
        <Square
          value={squares[6]}
          onSquareClick={() => {
            handleClick(6);
          }}
        />
        <Square
          value={squares[7]}
          onSquareClick={() => {
            handleClick(7);
          }}
        />
        <Square
          value={squares[8]}
          onSquareClick={() => {
            handleClick(8);
          }}
        />
      </div>
    </>
  );
}
```

## Once a square has been marked, it shall not be overwritten again

```jsx
import React from "react";

function Square({ value, onSquareClick }) {
  return (
    <button className="square" onClick={onSquareClick}>
      {value}
    </button>
  );
}

export default function Board() {
  const [squares, setSquares] = React.useState(Array(9).fill(null));
// xTurn -> is true if its X turn, otherwise false
// xIsNext -> will set xTurn to false at even turns
  const [xTurn, xIsNext] = React.useState(true);

  function handleClick(i) {
    // if square already filled, do nothing
    if (squares[i]) return;
    const squaredArray = squares.slice();
    if (xTurn) {
        squaredArray[i] = "X";
    } else {
        squaredArray[i] = "O";
    }
    
    setSquares(squaredArray);
    xIsNext(!xTurn);
  }
  return (
    <>
      <div className="board-row">
        <Square
          value={squares[0]}
          onSquareClick={() => {
            handleClick(0);
          }}
        />
        <Square
          value={squares[1]}
          onSquareClick={() => {
            handleClick(1);
          }}
        />
        <Square
          value={squares[2]}
          onSquareClick={() => {
            handleClick(2);
          }}
        />
      </div>
      <div className="board-row">
        <Square
          value={squares[3]}
          onSquareClick={() => {
            handleClick(3);
          }}
        />
        <Square
          value={squares[4]}
          onSquareClick={() => {
            handleClick(4);
          }}
        />
        <Square
          value={squares[5]}
          onSquareClick={() => {
            handleClick(5);
          }}
        />
      </div>
      <div className="board-row">
        <Square
          value={squares[6]}
          onSquareClick={() => {
            handleClick(6);
          }}
        />
        <Square
          value={squares[7]}
          onSquareClick={() => {
            handleClick(7);
          }}
        />
        <Square
          value={squares[8]}
          onSquareClick={() => {
            handleClick(8);
          }}
        />
      </div>
    </>
  );
}
```

## Declare a winner using a helper function provided

Helper function :

```jsx
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
```

```jsx
import React from "react";

function Square({ value, onSquareClick }) {
  return (
    <button className="square" onClick={onSquareClick}>
      {value}
    </button>
  );
}

export default function Board() {
  const [squares, setSquares] = React.useState(Array(9).fill(null));
// xTurn -> is true if its X turn, otherwise false
// xIsNext -> will set xTurn to false at even turns
  const [xTurn, xIsNext] = React.useState(true);

  function handleClick(i) {
    if (squares[i] || calculateWinner(squares)) return;
    const squaredArray = squares.slice();
    if (xTurn) {
        squaredArray[i] = "X";
    } else {
        squaredArray[i] = "O";
    }
    
    setSquares(squaredArray);
    xIsNext(!xTurn);
  }
  const winner = calculateWinner(squares);
  let status;
  if (winner) {
    status = `{Winner: ${winner}}`
  } else {
    status = `{Next: ${xTurn ? 'X' : 'O'}}`
  }
  return (
    <>
        <p>Status: {status}</p>
      <div className="board-row">
        <Square
          value={squares[0]}
          onSquareClick={() => {
            handleClick(0);
          }}
        />
        <Square
          value={squares[1]}
          onSquareClick={() => {
            handleClick(1);
          }}
        />
        <Square
          value={squares[2]}
          onSquareClick={() => {
            handleClick(2);
          }}
        />
      </div>
      <div className="board-row">
        <Square
          value={squares[3]}
          onSquareClick={() => {
            handleClick(3);
          }}
        />
        <Square
          value={squares[4]}
          onSquareClick={() => {
            handleClick(4);
          }}
        />
        <Square
          value={squares[5]}
          onSquareClick={() => {
            handleClick(5);
          }}
        />
      </div>
      <div className="board-row">
        <Square
          value={squares[6]}
          onSquareClick={() => {
            handleClick(6);
          }}
        />
        <Square
          value={squares[7]}
          onSquareClick={() => {
            handleClick(7);
          }}
        />
        <Square
          value={squares[8]}
          onSquareClick={() => {
            handleClick(8);
          }}
        />
      </div>
    </>
  );
}

function calculateWinner(squares) {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ];
    for (let i = 0; i < lines.length; i++) {
      const [a, b, c] = lines[i];
      if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
        return squares[a];
      }
    }
    return null;
}
```

## Store the past moves in another array

