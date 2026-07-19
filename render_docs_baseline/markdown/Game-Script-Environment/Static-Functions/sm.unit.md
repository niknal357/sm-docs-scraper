# sm.unit

**Associated type:** [Unit](../Userdata/Unit.md)

Unit creation and management

## Server-only

### createUnit {#createunit}

``` { .lua .api-signature }
sm.unit.createUnit( uuid, feetPos, yaw?, data?, pitch?, visible? )
```

Creates a new unit of type from an [Uuid](../Userdata/Uuid.md)

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The character type uuid. |
| `feetPos` | [Vec3](../Userdata/Vec3.md) | The feet position in world where unit should spawn. |
| `yaw` *(optional)* | number | The initial yaw. Defaults to 0 (Optional) |
| `data` *(optional)* | any | The param data. (Optional) |
| `pitch` *(optional)* | number | The initial pitch. Defaults to 0 (Optional) |
| `visible` *(optional)* | boolean | Whether the unit is visible on spawn. Defaults to true. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [Unit](../Userdata/Unit.md) | The created unit. |

### forceDestroy {#forcedestroy}

``` { .lua .api-signature }
sm.unit.forceDestroy( unit )
```

Destroys a unit.

If the unit does not exist at the moment, it is removed from the save file. This will stop it from loading back into the game.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](../Userdata/Unit.md) | The unit. |

### getAllUnits {#getallunits}

``` { .lua .api-signature }
sm.unit.getAllUnits( world? )
```

Returns a table with all the units in the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to get units from. Defaults to the world of the script (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of all units. {[Unit](../Userdata/Unit.md), ..} |

### getUnitsInRange {#getunitsinrange}

``` { .lua .api-signature }
sm.unit.getUnitsInRange( world, position, range, heightModifier? )
```

Returns a table with units within a given range.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | The world to check in. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position to check from. |
| `range` | number | The range to check. |
| `heightModifier` *(optional)* | number | A value to modify the height of the range check. Defaults to 1. Higher values makes enemy elevation difference deemed as greater distance. |
