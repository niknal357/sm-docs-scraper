# AiState

**Usage:** Server Only

**Serializable:** No

A userdata object representing an <strong>AI state</strong> belonging to a [Unit](Unit.md).

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`AiState == AiState` | boolean | Checks if two instances of [AiState](AiState.md) are refer to the same AiState. |

## Server-only

### getFacingDirection {#getfacingdirection}

``` { .lua .api-signature }
aiState:getFacingDirection(  )
```

Returns the state's facing direction.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `state` | [AiState](AiState.md) | The state. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The direction. |

### getMovementDirection {#getmovementdirection}

``` { .lua .api-signature }
aiState:getMovementDirection(  )
```

Returns the state's movement direction.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `state` | [AiState](AiState.md) | The state. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The direction. |

### getMovementType {#getmovementtype}

``` { .lua .api-signature }
aiState:getMovementType(  )
```

Returns a string describing the state's movement type.

Movement type can be "stand", "walk", "sprint" or "crouch".

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `state` | [AiState](AiState.md) | The state. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The movement type. |

### getWantsCrouch {#getwantscrouch}

``` { .lua .api-signature }
aiState:getWantsCrouch(  )
```

Check if the state wants to crouch.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `state` | [AiState](AiState.md) | The state. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true when the state wants to crouch. |

### getWantsJump {#getwantsjump}

``` { .lua .api-signature }
aiState:getWantsJump(  )
```

Check if the state wants to jump.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `state` | [AiState](AiState.md) | The state. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true when the state wants to jump. |

### isDone {#isdone}

``` { .lua .api-signature }
aiState:isDone(  )
```

Checks if the AI state is done.

Returns true when the state is done, and a string describing the state's current situation.

Can be used to determine if another state is allowed to be started.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `state` | [AiState](AiState.md) | The state. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean, string | Returns true when done, and a string description. |

### onFixedUpdate {#onfixedupdate}

``` { .lua .api-signature }
aiState:onFixedUpdate( deltaTime )
```

Updates the state by adding delta time progression.

Should be called once every game tick while the state is active.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `state` | [AiState](AiState.md) | The state. |
| `deltaTime` | number | The delta time. |

### onUnitUpdate {#onunitupdate}

``` { .lua .api-signature }
aiState:onUnitUpdate( deltaTime )
```

Updates the state by adding delta time progression.

Should be called once every unit update, by the unit that owns the state, while the state is active.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `state` | [AiState](AiState.md) | The AI state. |
| `deltaTime` | number | The delta time. |

### start {#start}

``` { .lua .api-signature }
aiState:start(  )
```

Starts the state.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `state` | [AiState](AiState.md) | The state. |

### stop {#stop}

``` { .lua .api-signature }
aiState:stop(  )
```

Stops the state.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `state` | [AiState](AiState.md) | The state. |
