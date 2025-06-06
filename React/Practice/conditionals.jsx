import React from 'react';

function Button({ value, handleClick }) {
    return (
        <button style={{backgroundColor:value}} onClick={handleClick}>Click me</button>
    )
}

export default function Box() {
    const [backgroundColor, setBackgroundColor] = React.useState("brown");

    function handleClick(e) {
        if (backgroundColor) {
            setBackgroundColor("white");
            console.log("BG has changed.")
        } else {
            setBackgroundColor("brown")
            console.log("BG isn't changed.")
        }
    }

    return (
        <>
            <Button value={backgroundColor} handleClick={handleClick} />
        </>
    )
}