# Lift

**Associated namespace:** [sm.lift](../Static-Functions/sm.lift.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a <strong>lift</strong> in the game.

**Values:**

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a lift.

- <a id="level"></a>`level` [ **integer** ] <br>
    - `Get`: Returns the level of a lift.

- <a id="worldposition"></a>`worldPosition` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the world position of a lift.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Lift == Lift` | boolean | Checks if two instances of [Lift](Lift.md) refer to the same Lift. |

## Server + Client

### getId {#getid}

``` { .lua .api-signature }
lift:getId(  )
```

Returns the id of a lift.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `lift` | [Lift](Lift.md) | The lift. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The lift's id. |

### getLevel {#getlevel}

``` { .lua .api-signature }
lift:getLevel(  )
```

Returns the level of a lift.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `lift` | [Lift](Lift.md) | The lift. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The lift's level. |

### getWorldPosition {#getworldposition}

``` { .lua .api-signature }
lift:getWorldPosition(  )
```

Returns the world position of a lift.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `lift` | [Lift](Lift.md) | The lift. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The lift's world position. |

### hasBodies {#hasbodies}

``` { .lua .api-signature }
lift:hasBodies(  )
```

Returns whether there's a body on the lift.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `lift` | [Lift](Lift.md) | The lift. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the lift has a body. |

## Server-only

### destroy {#destroy}

``` { .lua .api-signature }
lift:destroy(  )
```

Destroys a lift.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `lift` | [Lift](Lift.md) | The lift. |
