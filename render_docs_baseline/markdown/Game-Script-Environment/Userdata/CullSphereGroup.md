# CullSphereGroup

**Associated namespace:** [sm.cullSphereGroup](../Static-Functions/sm.cullSphereGroup.md)

**Usage:** Server And Client

**Serializable:** No

A userdata object representing a <strong>cull sphere group</strong>.

**Values:**

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a sphere group.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`CullSphereGroup == CullSphereGroup` | boolean | Checks if two instances of [CullSphereGroup](CullSphereGroup.md) refer to the same CullSphereGroup. |

## Functions

### addSphere {#addsphere}

``` { .lua .api-signature }
cullSphereGroup:addSphere( id, position, radius )
```

Adds a sphere to the sphere group, duplicate ids are ignored.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `sphereGroup` | [CullSphereGroup](CullSphereGroup.md) | The sphere group. |
| `id` | integer | Sphere id. |
| `position` | [Vec3](Vec3.md) | Sphere position. |
| `radius` | number | Sphere radius. |

### getDelta {#getdelta}

``` { .lua .api-signature }
cullSphereGroup:getDelta( position, innerRadius, outerRadius )
```

Queries the change in overlapping spheres since the last call to getDelta.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `sphereGroup` | [CullSphereGroup](CullSphereGroup.md) | The sphere group. |
| `position` | [Vec3](Vec3.md) | Position to query sphere. |
| `innerRadius` | number | Radius for inner sphere. |
| `outerRadius` | number | Radius for outer sphere. |

**Returns:**

| Type | Description |
| --- | --- |
| table, table | Arrays of removed, added ids {integer, ...}. |

### getOverlaps {#getoverlaps}

``` { .lua .api-signature }
cullSphereGroup:getOverlaps( position, radius )
```

Query for overlapping spheres.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `sphereGroup` | [CullSphereGroup](CullSphereGroup.md) | The sphere group. |
| `position` | [Vec3](Vec3.md) | Position to query sphere. |
| `radius` | number | Radius for query sphere. |

### leave {#leave}

``` { .lua .api-signature }
cullSphereGroup:leave(  )
```

Query all currently active spheres and leave them.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `sphereGroup` | [CullSphereGroup](CullSphereGroup.md) | The sphere group. |

**Returns:**

| Type | Description |
| --- | --- |
| table | An array of previously active ids {integer, ...}. |

### removeSphere {#removesphere}

``` { .lua .api-signature }
cullSphereGroup:removeSphere( id )
```

Removes a sphere from the sphere group.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `sphereGroup` | [CullSphereGroup](CullSphereGroup.md) | The sphere group. |
| `id` | integer | Sphere id. |
