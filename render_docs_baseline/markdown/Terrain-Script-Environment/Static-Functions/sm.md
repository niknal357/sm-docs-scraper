# sm

The <strong>sm</strong> namespace contain all API features related to Scrap Mechanic.

## Constants

### isHost {#ishost}

Returns whether the game is currently running on the hosting player's computer.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the game is running on the host. |

### types {#types}

Lua types

| Value |
| --- |
| nil |
| boolean |
| number |
| string |
| function |
| userdata |
| thread |
| table |
| uuid |
| vec3 |
| quat |
| color |
| raycastResult |
| loadCellHandle |
| effect |
| shape |
| body |
| interactable |
| container |
| harvestable |
| network |
| world |
| unit |
| storage |
| player |
| character |
| joint |
| aiState |
| quest |
| areaTrigger |
| portal |
| pathNode |
| lift |
| scriptableObject |
| builderGuide |
| cullSphereGroup |
| voxelTerrain |
| jsonGui |
| jsonWidget |
| clientScriptableObject |

**Returns:**

| Type | Description |
| --- | --- |
| table | The lua types list. |

### version {#version}

Returns the current version of the game as a string.

**Returns:**

| Type | Description |
| --- | --- |
| string | The current version of the game. |

## Functions

### exists {#exists}

``` { .lua .api-signature }
sm.exists( object )
```

Returns whether an object exists in the game. This is useful for checking whether a reference to an object is valid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `object` | any | The object instance. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the object exists. |

### isServerMode {#isservermode}

``` { .lua .api-signature }
sm.isServerMode(  )
```

Returns whether the script is currently running in server mode. Otherwise, it is running in client mode. Server mode only occurs when [sm.isHost](#ishost) is true.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the script is running in server mode. |
