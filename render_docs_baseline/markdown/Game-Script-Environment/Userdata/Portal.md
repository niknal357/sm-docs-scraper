# Portal

**Associated namespace:** [sm.portal](../Static-Functions/sm.portal.md)

**Usage:** Server And Client

**Serializable:** Yes

**Values:**

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a portal.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Portal == Portal` | boolean | Checks if two instances of [Portal](Portal.md) refer to the same Portal. |

## Server + Client

### getId {#getid}

``` { .lua .api-signature }
portal:getId(  )
```

Returns the id of a portal.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The portal's id. |

## Server-only

### getContentsA {#getcontentsa}

``` { .lua .api-signature }
portal:getContentsA(  )
```

Gets the contents of opening A

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of contents of type [Character](Character.md) and [Body](Body.md). |

### getContentsB {#getcontentsb}

``` { .lua .api-signature }
portal:getContentsB(  )
```

Gets the contents of opening B

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of contents of type [Character](Character.md) and [Body](Body.md). |

### getPositionA {#getpositiona}

``` { .lua .api-signature }
portal:getPositionA(  )
```

Returns the position of portal opening A.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The portal opening A position. |

### getPositionB {#getpositionb}

``` { .lua .api-signature }
portal:getPositionB(  )
```

Returns the position of portal opening B.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The portal opening B position. |

### getRotationA {#getrotationa}

``` { .lua .api-signature }
portal:getRotationA(  )
```

Returns the rotation of portal opening A.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The portal opening A rotation. |

### getRotationB {#getrotationb}

``` { .lua .api-signature }
portal:getRotationB(  )
```

Returns the rotation of portal opening B.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The portal opening B rotation. |

### getWorldA {#getworlda}

``` { .lua .api-signature }
portal:getWorldA(  )
```

Returns the world of a portal opening A.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |

**Returns:**

| Type | Description |
| --- | --- |
| [World](World.md) | The portal opening A world. |

### getWorldB {#getworldb}

``` { .lua .api-signature }
portal:getWorldB(  )
```

Returns the world of a portal opening B.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |

**Returns:**

| Type | Description |
| --- | --- |
| [World](World.md) | The portal opening B world. |

### hasOpeningA {#hasopeninga}

``` { .lua .api-signature }
portal:hasOpeningA(  )
```

Checks if the portal has opening A.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if opening A exists, false if not. |

### hasOpeningB {#hasopeningb}

``` { .lua .api-signature }
portal:hasOpeningB(  )
```

Checks if the portal has opening B.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if opening B exists, false if not. |

### setAMarkerOffset {#setamarkeroffset}

``` { .lua .api-signature }
portal:setAMarkerOffset( offset )
```

Sets the offset of the world marker of portal A

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |
| `offset` | [Vec3](Vec3.md) | The offset of the world marker in world space. |

### setAToBMarkerAllowed {#setatobmarkerallowed}

``` { .lua .api-signature }
portal:setAToBMarkerAllowed( allowed )
```

Set if transfer from A to B is allowed, used for marker placements

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal to edit |
| `allowed` | boolean | Whether the portal is allowed to show A to B connection |

### setBMarkerOffset {#setbmarkeroffset}

``` { .lua .api-signature }
portal:setBMarkerOffset( offset )
```

Sets the offset of the world marker of portal B

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |
| `offset` | [Vec3](Vec3.md) | The offset of the world marker in world space. |

### setBToAMarkerAllowed {#setbtoamarkerallowed}

``` { .lua .api-signature }
portal:setBToAMarkerAllowed( allowed )
```

Set if transfer from B to A is allowed, used for marker placements

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal to edit |
| `allowed` | boolean | Whether the portal is allowed to show A to B connection |

### setOpeningA {#setopeninga}

``` { .lua .api-signature }
portal:setOpeningA( position, rotation, world? )
```

Sets the position of portal opening A.

The world will be the same as the object that calls this function.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |
| `position` | [Vec3](Vec3.md) | The portal opening A position. |
| `rotation` | [Quat](Quat.md) | The portal opening A rotation. |
| `world` *(optional)* | [World](World.md) | The world to look in (Optional, defaults to world from script context) |

### setOpeningB {#setopeningb}

``` { .lua .api-signature }
portal:setOpeningB( position, rotation, world? )
```

Sets the position B of portal opening B.

The world will be the same as the object that calls this function.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |
| `position` | [Vec3](Vec3.md) | The portal opening B position. |
| `rotation` | [Quat](Quat.md) | The portal opening B rotation. |
| `world` *(optional)* | [World](World.md) | The world to look in (Optional, defaults to world from script context) |

### transferAToB {#transferatob}

``` { .lua .api-signature }
portal:transferAToB( filter? )
```

Transfers objects inside A opening to B opening

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |
| `filter` *(optional)* | integer | A [sm.physics.filter](../Static-Functions/sm.physics.md#filter) mask selecting which contents to transfer. Only [dynamicBody](../Static-Functions/sm.physics.md#filter), [staticBody](../Static-Functions/sm.physics.md#filter) and [character](../Static-Functions/sm.physics.md#filter) are meaningful. Defaults to transferring bodies and characters. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if successful, false on failure. |

### transferBToA {#transferbtoa}

``` { .lua .api-signature }
portal:transferBToA( filter? )
```

Transfers objects inside B opening to A opening

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](Portal.md) | The portal. |
| `filter` *(optional)* | integer | A [sm.physics.filter](../Static-Functions/sm.physics.md#filter) mask selecting which contents to transfer. Only [dynamicBody](../Static-Functions/sm.physics.md#filter), [staticBody](../Static-Functions/sm.physics.md#filter) and [character](../Static-Functions/sm.physics.md#filter) are meaningful. Defaults to transferring bodies and characters. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | true if successful, false on failure. |
