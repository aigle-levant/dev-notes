---
tags: [react]
---
- **How are state updates applied?**: They're queued, processed and then re-rendered with the final result.
	- **Why is this done?**
		- Efficiency
		- Ensuring consistent and predictable state update order.
		- Batching updates
	- **How can this be rectified?**: Use stuff like ``setState(prev => prev + 1)``