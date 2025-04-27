---
tags:
  - react
  - event-handling
---
**How is it done?**: Declaring event handlers inside the component.

**onClick**: Event that happens on clicking [or touching] an element.

> Don't call the event handler, just pass it down.

```js
export default function ThemeButton() {
    // this is the event handler
    function handleClick() {
        console.log("And here I am.")
    }
    return (
        <button onClick={handleClick}>
            Click for a message.
        </button>
    )
}
```
