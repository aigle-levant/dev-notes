---
tags:
  - dns
---
**Other name**: Zone files
They are a set of instructions stored in authoritative DNS servers.
**Content**:
- Info. about IP address associated with domain
- How to handle requests for the domain.
- TTL
	- **TTL** indicates how often the DNS server will refresh that particular record.
**Format**: Text files written in DNS syntax
- **DNS syntax** is a string of characters telling DNS server what to do.

### Common types of DNS records

**A record / Address record** : Holds the IPv4 IP address of a domain

**AAAA record** : Holds the IPv6 IP address of a domain

**CNAME record / Canonical Name record** : Directs an alias domain [sub-domain] to the A or AAAA record of a canonical domain [main domain].
- If github.com is a canonical domain, github.com/marketplace is an alias domain.
- **Benefit**: If main domain's IP address changes, only the A / AAAA record will have to be updated.
- **What is being aliased?**: A single hostname.

**MX records**: Directs emails to the domain mail server.
- **Protocol used**: SMTP
- **Creates**: Individual email accounts linked to the domain [like user@example.com].
- Points to hostnames.
- **Priority number**: Lower the number, higher the priority. ``10 mail1.example.com`` will be used before ``20 mail2.example.com``.
- **Requires**: Hostname having A or AAAA record

**TXT record**: Stores textual info. related to domains or subdomains.
- **Purpose**: Email spam prevention, domain verification.

**NS record / Nameserver record**: Indicates which DNS server contains the actual DNS records for that domain [which phonebook to look into for that domain? which server to ask for the IP address?]
- **Points to**: DNS servers
- **When to change**: If switching DNS providers.

## Refer
[[https://www.cloudflare.com/en-gb/learning/dns/dns-records/|What is a DNS record? | Cloudflare]]
[[https://www.ibm.com/think/topics/dns-records|What are DNS records? | IBM]]