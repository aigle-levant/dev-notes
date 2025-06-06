
# Navbar

## Dark

### Screenshot

![alt text](image.png)

### Procedure

#### Let's start with the header

```tsx
<header className="fixed top-4 left-1/2 z-50 w-[90%] max-w-4xl -translate-x-1/2 rounded-full bg-zinc-950 px-2 py-1 dark:bg-zinc-950">
    <div className="relative flex items-center justify-center">
        {/* ... */}
    </div>
</header>
```

- It is fixed at the top and has the highest z-index of all components in that page, so that clipping doesn't occur.
- Background is dark and text is light. In dark mode, it's reversed.
- Navbar takes upto 90% of width of the page.
- The container has rounded edges with enough padding.
- The navbar sits at the center of the area provided for it by using `translate` rule.

- The `div` inside it lets items be stacked row-wise at center.
- It is `relative` just so that the children can be `absolute`.

#### Let's see the children...

```tsx
{/* theme switch */}
<div className="absolute left-4">
    <button className="text-sm text-zinc-950 dark:text-zinc-50">Theme</button>
</div>
```

- This component has `absolute` and `left-4` just so that it can be push to the left part of the parent.
- Within it is a button that can change theme upon tap / click.

```tsx
{/* Logo - center */}
<div>
    <a href="/" className="text-lg text-zinc-950 dark:text-zinc-50">Voile</a>
</div>
```

- This is just a link with styling that showcases the logo of this page. It contains the link to homepage.

```tsx
{/* Hamburger - right */}
<div className="absolute right-4">
    <button
        onClick={() => setMenuOpen(!menuOpen)}
        className="text-zinc-900 focus:outline-none dark:text-zinc-100"
    >
        <svg
            className="h-6 w-6"
            fill="none"
            stroke="currentColor"
            strokeWidth={2}
            viewBox="0 0 24 24"
        >
            {menuOpen ? (
                <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="M6 18L18 6M6 6l12 12"
                />
            ) : (
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M4 6h16M4 12h16M4 18h16"
                />
              )}
        </svg>
    </button>
</div>
```

- The hamburger has `absolute right-4` to position it on the right side of the parent.
- It contains a button, which has the icon [svg] of a hamburger menu. This button, upon tapping / clicking, will trigger the state function `setMenuOpen()`, which sets `menuOpen` state variable to `true`.

#### And finally, the hamburger menu contents

```tsx
{menuOpen && (
    <div className="absolute top-20 left-1/2 z-40 w-[90%] max-w-4xl -translate-x-1/2 rounded-xl bg-white p-4 shadow-lg dark:bg-zinc-950">
        <ul className="space-y-3 text-center text-base text-zinc-900 dark:text-zinc-100">
            <li>
                <a href="/about" className="block hover:underline">About</a>
            </li>
            <li>
              <a href="/history" className="block hover:underline">History</a>
            </li>
            <li>
              <a href="/contact" className="block hover:underline">Contact</a>
            </li>
        </ul>
    </div>
)}
```

- If `menuOpen` is `true`, this will be shown.
- The `div` has `absolute top-20` in order to be just below the navbar, leaving some gap between navbar and contents.
- `rounded-xl` would make the edges slightly rounded [only slightly].
- To help the contents stay in the same centered position as the navbar, `z-40 w-[90%] max-w-4xl -translate-x-1/2` is used.
- `space-y-3` simply means ``margin-top: 0.75rem;``
- While `text-base` means ``font-size: 1rem; line-height: 1.5rem;``.
- Upon hovering, the links will be underlined, thanks to `hover:underline`.
