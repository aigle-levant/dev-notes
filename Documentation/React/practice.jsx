import React from "react";

function Square({ value, onSquareClick }) {
  return (
    <button className="square" onClick={onSquareClick}>
      {value}
    </button>
  );
}

function Board(xIsNext, squaredArray, handleGame) {
  const [squares, setSquares] = React.useState(Array(9).fill(null));
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
    status = `{Winner: ${winner}}`;
  } else {
    status = `{Next: ${xTurn ? "X" : "O"}}`;
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
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}

export default function Game() {
  const [xTurn, xIsNext] = React.useState(true);
  const [history, goBack] = React.useState(Array(9).fill(null));
  const currentArray = history[history.length - 1];

  function handleGame(squaredArray) {
    goBack([[...history, squaredArray]]);
    xIsNext(!xTurn);
  }

  return (
    <div className="game">
      <div className="game-board">
        <Board xIsNext={xIsNext} squares={squaredArray} onPlay={handleGame} />
      </div>
      <div className="game-info"></div>
    </div>
  );
}
