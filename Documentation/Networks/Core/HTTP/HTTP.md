---
tags: [networks]
---
- **Full form**: HyperText Transfer Protocol
- **Responsible for**: Communication between web servers and clients.
- **How is HTTP stateless?**: Every request is completely independent.
	- Has no memory about previous actions [unlike React components].
	- **How can we make it stateful?**: Introducing addons like LocalStorage, cookies, sessions, etc.

## Methods
### Request
- **What is it?**: A communication sent from a client to a server.
	- **Client**: Web browser
- **Why is it used?**: To ask or modify resources.

### Types of methods
- **GET**: Retrieve data from a server.
- **POST**: Adding or submitting data to a server.
- **PUT**: Modify existing data in the server.
- **DELETE**: Delete data from the server.

> Every time you visit a webpage, you make a GET request to the server via HTTP.

### Header fields
- **Header**
	- Has a method [GET, POST, etc.], path or url, and the protocol.
	- Types
		- General headers
			- Request URL -> URL of resource we're requesting.
			- Request method -> Type of request method
			- Status code
			- Remote address -> IP address of the remote computer
			- Referrer policy 
		- Response headers
			- Server -> Is hidden to prevent hackers
			- Set-cookie -> Used by server to send cookies to client
			- Content-type -> Type of content served
			- Content-length -> Length of content in octets
			- Date
		- Request headers
			- Cookies -> Used by client to send a previously-sent cookie back to server
			- Accept-xxx -> Encodings and languages
			- Content-type -> Type of content sent
			- Content-length
			- Authorization -> Since HTTP is stateless, tokens are sent from here to validate users
			- User-agent -> Software used by user
			- Referrer -> Referring site
- **Body**: Data being served from the server.


### HTTP/2
- Under-the-hood changes - No need to go and modify status codes, requests, etc. on your own.
- **Reduces**: Latency, by enabling full request & response multiplexing.
	- **Multi-plexing**: Sending multiple streams of info. over a communications link at the same time
- Takes lesser steps than HTTP/1.1
## References

[[Status codes]], [[HTTPS]]

[HTTP Crash Course & Exploration | Traversy Media](https://www.youtube.com/watch?v=iYM2zFP3Zn0)