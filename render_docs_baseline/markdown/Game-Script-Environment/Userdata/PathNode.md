# PathNode

**Associated namespace:** [sm.pathNode](../Static-Functions/sm.pathNode.md)

**Usage:** Server Only

**Serializable:** Yes

A userdata object representing a PathNode in the game.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`PathNode == PathNode` | boolean | Checks if two instances of [PathNode](PathNode.md) refer to the same PathNode. |

## Server-only

### connect {#connect}

``` { .lua .api-signature }
pathNode:connect( to )
```

Create a PathNode connection

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `from` | [PathNode](PathNode.md) | PathNode to create connection from |
| `to` | [PathNode](PathNode.md) | PathNode to create connection to |

### destroy {#destroy}

``` { .lua .api-signature }
pathNode:destroy(  )
```

Destroys a path node.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `node` | [PathNode](PathNode.md) | The path node to be destroyed. |

### getPosition {#getposition}

``` { .lua .api-signature }
pathNode:getPosition(  )
```

Get the world position of a path node

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `node` | [PathNode](PathNode.md) | The path node |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | World position |
