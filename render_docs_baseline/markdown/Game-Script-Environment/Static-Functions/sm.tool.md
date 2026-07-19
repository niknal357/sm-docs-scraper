# sm.tool

**Associated type:** [Tool](../Userdata/Tool.md)

A <strong>tool</strong> is a scripted tool a player holds in their hand. The tool object is focused on handling animations for first and third person view.

For more information about creating your own scripted tools, see [ToolClass](../Classes/ToolClass.md).

## Constants

### interactState {#interactstate}

The interact state describe what kind of interaction is made. This is used to check whether a mouse button or key was just made pressed, held, etc.

The states are:

- <strong>null</strong> &ndash; No keypress was made.
- <strong>start</strong> &ndash; The key was just pressed.
- <strong>hold</strong> &ndash; The key is held down.
- <strong>stop</strong> &ndash; The key was just released.

| Value | Description |
| --- | --- |
| null | 0 |
| start | 1 |
| hold | 2 |
| stop | 3 |

**Returns:**

| Type | Description |
| --- | --- |
| table | The interact state list. |

## Server + Client

### checkLiftCollision {#checkliftcollision}

``` { .lua .api-signature }
sm.tool.checkLiftCollision( creation, position, rotation )
```

Used to check collisions between the lift and the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `creation` | table | A table of all the bodies belonging to the creation placed on the lift. |
| `position` | [Vec3](../Userdata/Vec3.md) | The lift position. |
| `rotation` | integer | The rotation of the creation on the lift. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean, integer					True if the lift collides with the world; The lift level. |  |

### checkLiftCollisionAtLevel {#checkliftcollisionatlevel}

``` { .lua .api-signature }
sm.tool.checkLiftCollisionAtLevel(
    creation,
    position,
    rotation,
    level,
    timeStamp
)
```

Checks whether a specific lift level is valid (no collision) for a creation at the given position and rotation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `creation` | table | A table of all the bodies belonging to the creation placed on the lift. |
| `position` | [Vec3](../Userdata/Vec3.md) | The lift position. |
| `rotation` | integer | The rotation of the creation on the lift. |
| `level` | integer | The specific lift level to test. |
| `timeStamp` | integer | The timestamp of when the body set was initialized |

**Returns:**

| Type | Description |
| --- | --- |
| boolean								True if the level is valid (no collision). |  |

### findPaintToolPaletteColumnIndex {#findpainttoolpalettecolumnindex}

``` { .lua .api-signature }
sm.tool.findPaintToolPaletteColumnIndex(  )
```

Find index of column of shades that best matches given color.

**Returns:**

| Type | Description |
| --- | --- |
| integer | Palette column index. |

### getLiftMaxLevel {#getliftmaxlevel}

``` { .lua .api-signature }
sm.tool.getLiftMaxLevel(  )
```

Returns the maximum number of lift levels.

**Returns:**

| Type | Description |
| --- | --- |
| integer								The maximum lift level count. |  |

### uuidExists {#uuidexists}

``` { .lua .api-signature }
sm.tool.uuidExists( uuid )
```

Return whether the tool uuid exists

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The shape uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | exists. |

## Client-only

### forceTool {#forcetool}

``` { .lua .api-signature }
sm.tool.forceTool( tool )
```

Force equip a tool for the local player. Pass nil to unforce an already forced tool.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](../Userdata/Tool.md) | The tool. |

### preloadRenderables {#preloadrenderables}

``` { .lua .api-signature }
sm.tool.preloadRenderables( renderables )
```

Pre-loads renderable data to be used by the tool. This eliminates excessive loading during run time.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `renderables` | table | The table of renderables names. {string, ..} |
