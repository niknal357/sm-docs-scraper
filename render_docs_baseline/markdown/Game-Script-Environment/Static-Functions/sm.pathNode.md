# sm.pathNode

**Associated type:** [PathNode](../Userdata/PathNode.md)

Path node creation

## Server-only

### createPathNode {#createpathnode}

``` { .lua .api-signature }
sm.pathNode.createPathNode( worldPosition, radius, temporary? )
```

Create a PathNode

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `worldPosition` | [Vec3](../Userdata/Vec3.md) | The node's world position |
| `radius` | number | The node's radius |
| `temporary` *(optional)* | boolean | Temporary nodes are not saved and relies on lua garbage collection for removal (defaults to false). |

**Returns:**

| Type | Description |
| --- | --- |
| [PathNode](../Userdata/PathNode.md) | The path node |
