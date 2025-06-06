---
tags: [react]
---
---
tags:
  - react
  - lists
---
**map()**: Execute a function [be it named or anonymous, mostly anonymous] for each item in a list.

```js
// list of 3 players from project zomboid
const players = [
    { name: 'Jean Antonique', isBitten: false, id: 1 },
    { name: 'Yves Montagne', isBitten: true, id: 2 },
    { name: 'Lola Luche', isBitten: false, id: 3 }
];

// don't have to pass players as arg if its global
export default function PlayerList() {
    /*
    pass each list item with styling
    basically a simpler for-loop without for-loop
    nonsense
    */
    const final = players.map(player =>
        <li key={player.id}
        style={{
            // if isBitten, color is red
            // if not, color is green
            color: player.isBitten ? 'red' : 'green'
        }}>
            Name: {player.name}
        </li>
    );
    return ( <ul>{final}</ul> );
}
```
![](https://i.imgur.com/lJseZ6F.png)
