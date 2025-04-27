---
tags:
  - react
  - react-props
---
**What are they?**: Info. that you can pass to a JSX tag.
- Parent component -> Child component
## Reading props inside a child components.
**Prerequisite**: Define the props' names as arguments of a component.

```js
// this part can be changeable
// promotes modularity
function Profile({ player }) {
    return (
        <div>
            <h1>Welcome back,</h1>
            <img src="alt" alt={player.name}/>
            <p>{player.name} from {player.place}</p>
            <p>Profession: {player.job}</p>
        </div>
    );
}

export default function Player() {
    const playerInfo = {
        name: "Jean Antonique",
        profession: "Ranger",
        place: "Rosewood, KY"
    }
    return (
        <Profile player={playerInfo}/>;
    )
}
```

> Using parenthesis in arguments is called **destructuring**. It's akin to this :

```js
function Profile (player){
    let name = player.name;
    let job = player.job;
    // ...
}
```
```