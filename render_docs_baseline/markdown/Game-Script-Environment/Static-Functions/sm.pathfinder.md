# sm.pathfinder

Pathfinder

## Constants

### conditionProperty {#conditionproperty}

Condition link types

| Value |
| --- |
| height |
| target |
| none |

## Server-only

### constrainPointToNavMesh {#constrainpointtonavmesh}

``` { .lua .api-signature }
sm.pathfinder.constrainPointToNavMesh( world, point, abilities? )
```

Constrain a point to nav mesh. Returns original point if no nav mesh is found.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | The world to look in. |
| `point` | [Vec3](../Userdata/Vec3.md) | The point. |
| `abilities` *(optional)* | table | Table of actor abilities { canWalk=boolean, canSwim=boolean }. Defaults to all abilities. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The modified point. |

### getPath {#getpath}

``` { .lua .api-signature }
sm.pathfinder.getPath( character, destination, groundPos?, abilities?, costs? )
```

Find a path

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](../Userdata/Character.md) | The character to find path for |
| `destination` | [Vec3](../Userdata/Vec3.md) | The path destination |
| `groundPos` *(optional)* | boolean | If the destination is ground level (ignored if nav mesh is used) (Defaults to true) |
| `abilities` *(optional)* | table | Table of actor abilities { canWalk=boolean, canSwim=boolean }. Defaults to character abilities. |
| `costs` *(optional)* | table | Table of traverse area costs [1-10] { ground=number, water=number, chemicals=number, oil=number, lava=number }. Defaults to default costs. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The path as table of PathNodes |

### getRandomPoint {#getrandompoint}

``` { .lua .api-signature }
sm.pathfinder.getRandomPoint( world, point, radius, abilities? )
```

Fetches a random point from the navmesh polys in a set radius. The point can be outside the radius but no polys outside the radius will be selected.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | The world to look in. |
| `point` | [Vec3](../Userdata/Vec3.md) | The point. |
| `radius` | number | The radius to search in. |
| `abilities` *(optional)* | table | Table of actor abilities { canWalk=boolean, canSwim=boolean }. Defaults to all abilities. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The new random point. (returns original point in case of failure) |

### getSortedNodes {#getsortednodes}

``` { .lua .api-signature }
sm.pathfinder.getSortedNodes( worldPosition, minDist, maxDist )
```

Find all nearby path nodes

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `worldPosition` | [Vec3](../Userdata/Vec3.md) | The position to look in |
| `minDist` | number | Minimum distance around pos |
| `maxDist` | number | Maximum distance around pos |

**Returns:**

| Type | Description |
| --- | --- |
| table | Table of PathNodes sorted closest to farthest |

### getWorldPath {#getworldpath}

``` { .lua .api-signature }
sm.pathfinder.getWorldPath( world, start, destination, abilities?, costs? )
```

Find a path

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | The world to look in |
| `start` | [Vec3](../Userdata/Vec3.md) | The path start |
| `destination` | [Vec3](../Userdata/Vec3.md) | The path destination |
| `abilities` *(optional)* | table | Table of actor abilities { canWalk=boolean, canSwim=boolean }. Defaults to all abilities. |
| `costs` *(optional)* | table | Table of traverse area costs [1-10] { ground=number, water=number, chemicals=number, oil=number, lava=number }. Defaults to default costs. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The path as table of PathNodes |

### traversableRaycast {#traversableraycast}

``` { .lua .api-signature }
sm.pathfinder.traversableRaycast( world, start, destination, abilities? )
```

Looks at the surface of the navmesh from the start position toward the destination position to see if it is traversable.

If the distance isn't fully traversable, the out_fDistance is the traversable distance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | The world to look in. |
| `start` | [Vec3](../Userdata/Vec3.md) | The path start |
| `destination` | [Vec3](../Userdata/Vec3.md) | The path destination |
| `abilities` *(optional)* | table | Table of actor abilities { canWalk=boolean, canSwim=boolean }. Defaults to all abilities. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean,number | True if fully traversable, and a traversable distance when not fully traversable. (distance becomes FLT_MAX when fully traversable) |
