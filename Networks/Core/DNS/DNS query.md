---
tags:
  - dns
---
**Path**: DNS client -> DNS server
- Refer [[Domain Name System|DNS]]
- **DNS client :** Your device
- **DNS server :** Server that has info. about domain names and their respective IP addresses.
**When is it done?**: Typing a domain in browser's search-bar.
**What is being asked?**: IP address of a particular domain.

### Types
#### Recursive DNS query

>Do, or die.

- DNS client asks all the available DNS serversr.
- **Outcome**: Get IP address or error
- **Used in** : Consumer devices.
#### Iterative DNS query

> I don't know, ask someone else.

- DNS client asks one DNS server at a time, waits between answers.
- **Outcome**: Get IP address or error after a while
- **Used in**: DNS root servers.