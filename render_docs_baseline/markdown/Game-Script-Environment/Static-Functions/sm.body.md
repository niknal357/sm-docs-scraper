# sm.body

**Associated type:** [Body](../Userdata/Body.md)

A <strong>body</strong> is a collection of [shapes](../Userdata/Shape.md) that are built together. Bodies can be connected to other bodies using [joints](../Userdata/Joint.md) such as the bearing.

## Server + Client

### getAllBodies {#getallbodies}

``` { .lua .api-signature }
sm.body.getAllBodies( world? )
```

Returns a table with all the bodies in the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` *(optional)* | [World](../Userdata/World.md) | The world, will default to the script's world. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of all bodies. {[Body](../Userdata/Body.md), ...} |

### getCreationsFromBodies {#getcreationsfrombodies}

``` { .lua .api-signature }
sm.body.getCreationsFromBodies( bodies )
```

Returns a table of tables, which is an array of tables containing bodies grouped by creation.

A creation includes all bodies connected by [joints](../Userdata/Joint.md), etc.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `bodies` | table | The bodies to find all creation bodies from. {[Body](../Userdata/Body.md), ...} |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table array containing tables of all the bodies, grouped by creation. { {[Body](../Userdata/Body.md), ...}, ... } |

### getLift {#getlift}

``` { .lua .api-signature }
sm.body.getLift( body )
```

Get the lift a body is on.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](../Userdata/Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| [Lift](../Userdata/Lift.md) | The lift the body is on, or nil if the body is not on a lift. |

## Server-only

### createBody {#createbody}

``` { .lua .api-signature }
sm.body.createBody( position, rotation?, isDynamic? )
```

Create a new body

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | The body's world position. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The body's world rotation. (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `isDynamic` *(optional)* | boolean | Set true if the body is dynamic or false if the body is static. (Defaults to true) |

**Returns:**

| Type | Description |
| --- | --- |
| [Body](../Userdata/Body.md) | The created body |
