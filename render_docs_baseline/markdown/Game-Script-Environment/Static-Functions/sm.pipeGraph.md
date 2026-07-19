# sm.pipeGraph

Pipe utility functions.

## Constants

### direction {#direction}

Pipe direction types

| Value |
| --- |
| any |
| incoming |
| outgoing |

**Returns:**

| Type | Description |
| --- | --- |
| table | The pipe directions type list. |

## Server + Client

### getContainerShapeToCollectTo {#getcontainershapetocollectto}

``` { .lua .api-signature }
sm.pipeGraph.getContainerShapeToCollectTo( requester, items, quantities )
```

Returns a chest which allows for collection of specified items of the specified quantities.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The shape connected to the pipe graph who requests the information. |
| `items` | table | The uuids of items to check. |
| `quantities` | table | The number of items of each uuid. Needs to match the number of uuids.	 |

**Returns:**

| Type | Description |
| --- | --- |
| [Shape](../Userdata/Shape.md) | container		The shape of the container which was the first one that allows the collection. |

### getContainerShapeToSpendFrom {#getcontainershapetospendfrom}

``` { .lua .api-signature }
sm.pipeGraph.getContainerShapeToSpendFrom( requester, item, quantities )
```

Returns a chest which allows for spending of specific item with a given quantity.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The shape connected to the pipe graph who requests the information. |
| `item` | [Uuid](../Userdata/Uuid.md) | The uuid of the target item. |
| `quantities` | number | The target spending amount. |

**Returns:**

| Type | Description |
| --- | --- |
| [Shape](../Userdata/Shape.md) | container		The shape of the container which was the first one that allows spending. |

### getInputContainers {#getinputcontainers}

``` { .lua .api-signature }
sm.pipeGraph.getInputContainers( requester )
```

Returns a table of all connected input containers sorted by closest first. If the asking shape doesn't have input and output directions it returns all connected containers.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The shape connected to the pipe graph who's connected chests you want. |

**Returns:**

| Type | Description |
| --- | --- |
| table | containers		A table of connected container shapes sorted by closest first. |

### getMatchingPipedContainers {#getmatchingpipedcontainers}

``` { .lua .api-signature }
sm.pipeGraph.getMatchingPipedContainers( originInteractable )
```

Returns the containers of all chests connected to the given shape through the pipe connections. Will only return containers from shapes of the same type as the original.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `originInteractable` | [Interactable](../Userdata/Interactable.md) | The interactable where the search will start from. |

**Returns:**

| Type | Description |
| --- | --- |
| table | containers				The container of the originInteractable as well as those of the same type connected through pipes. |

### getOutputContainers {#getoutputcontainers}

``` { .lua .api-signature }
sm.pipeGraph.getOutputContainers( requester )
```

Returns a table of all connected output containers sorted by closest first. If the asking shape doesn't have input and output directions it returns all connected containers.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The shape connected to the pipe graph who's connected chests you want. |

**Returns:**

| Type | Description |
| --- | --- |
| table | containers		A table of connected container shapes sorted by closest first. |

## Server-only

### getInteractableConditionTicks {#getinteractableconditionticks}

``` { .lua .api-signature }
sm.pipeGraph.getInteractableConditionTicks( requester )
```

Returns the remaining of special condition, nil if no data is available.

return integer:	remainingTicks	The remaining ticks of the special condition.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The requesting shape. |

### removeAutomatedTask {#removeautomatedtask}

``` { .lua .api-signature }
sm.pipeGraph.removeAutomatedTask( requester, item )
```

Removes all stored automated tasks capable of producing the specified item from a producing shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The requesting shape. |
| `item` | [Uuid](../Userdata/Uuid.md) | The production to stop. |

### removeAutomatedTasks {#removeautomatedtasks}

``` { .lua .api-signature }
sm.pipeGraph.removeAutomatedTasks( requester )
```

Removes any stored automated tasks for the requesting shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The requesting shape. |

### setAutomatedTask {#setautomatedtask}

``` { .lua .api-signature }
sm.pipeGraph.setAutomatedTask( requester, recipe, parallel? )
```

Sets an automated task to be performed by the pipe graph when the body is unloaded.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The shape which requests the automated process. |
| `recipe` | table | A table with information on the recipe. Uses the crafter recipe format. Can have "craftTime", "quantity", "itemId", "externalContainers"(containers targeted outside pipe graph for consumption, example: refinery), "selfOutputContainer"(if the shape has it's own collection container), "ingredientList", "randomCraftList" random weighted crafts (see prospector), "specialCrafting" used to target specific container slots with custom information (see ore crusher). |
| `parallel` *(optional)* | boolean | Whether the craft tasks should be carried out in parallel or not, off by default. A parallel task will be carried out independently of other automated tasks on this shape. (Optional) |

### setInteractableCondition {#setinteractablecondition}

``` { .lua .api-signature }
sm.pipeGraph.setInteractableCondition( requester, condition )
```

Sets special conditions for allowing an interactable to craft.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The requesting shape. |
| `condition` | table | Values for special conditions to allow crafting. Uses "uuid", "tickFrequency", "remainingTicks"(optional), "consumptionCount", "onlyExternal". See Prospector.lua for example. |

### setParallelLimit {#setparallellimit}

``` { .lua .api-signature }
sm.pipeGraph.setParallelLimit( requester, amount )
```

Sets the maximum amount of parallel crafts, 65535 if not set.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The requesting shape. |
| `amount` | integer | The number of parallel crafts allowed to be done at once. |

## Client-only

### getContainerPath {#getcontainerpath}

``` { .lua .api-signature }
sm.pipeGraph.getContainerPath( requester, target, direction? )
```

Returns a table of shapes on the path between the requesting shape and target container shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The requesting shape. |
| `target` | [Shape](../Userdata/Shape.md) | The target container shape. |
| `direction` *(optional)* | integer | The direction to fetch in. Defaults to [sm.pipeGraph.direction.any](#direction) (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | shapes			The shapes on the path between requesting shape to target. Requester not included in table. |

### releaseLightingOverride {#releaselightingoverride}

``` { .lua .api-signature }
sm.pipeGraph.releaseLightingOverride( requester )
```

Releases any glow and UV overrides made by the shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The requesting shape. |

### requestLightingOverride {#requestlightingoverride}

``` { .lua .api-signature }
sm.pipeGraph.requestLightingOverride( requester, target, uvIndex, glow )
```

Requests a glow and UV override for pipes between requesting shape and target container.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `requester` | [Shape](../Userdata/Shape.md) | The requesting shape. |
| `target` | [Shape](../Userdata/Shape.md) | The target container shape. |
| `uvIndex` | integer | The uv frame index for the affected pipes. Ranges 0 to 3. |
| `glow` | number | The glow multiplier of the pipes. |
