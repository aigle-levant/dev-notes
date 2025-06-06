---
tags: [react]
---
**What are they?**: JS functions that return markup.
**Function**: Serve as pieces of the UI.
- Has its own logic and appearance.
**Written using**: JavaScript XML [JSX].

> Use [Transform tools](https://transform.tools/html-to-jsx) to convert HTML to JSX.

```js
// assume everything we need is imported
function Nav() {
  return (
    <>
      <nav className="nav-bar">
        // nav links
      </nav>
    </>
  )
}

export default function App() {
  return (
    <div>
      <Nav />
    </div>
  )
}
```

## Attributes
**className** : Specifies CSS class.
**style**: Inline CSS

## Displaying data
Data can be pulled from a variable and displayed.
```js
export default function Profile (
  const userData = {
    name: 'Anon',
    username: '@' + 'anonnumo',
    lastSeenMonth: 'May',
    lastSeenYear: '2024'
  }
  return (
    <>
      <h1>{userData.name}</h1>
      <p>{userData.username}</p>
      <p>{userData.lastSeenMonth}, {userData.lastSeenYear}</p>
    </>
  )
)
```