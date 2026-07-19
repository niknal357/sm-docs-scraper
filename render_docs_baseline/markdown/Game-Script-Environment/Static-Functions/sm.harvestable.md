# sm.harvestable

**Associated type:** [Harvestable](../Userdata/Harvestable.md)

Harvestable creation

## Server + Client

### create {#create}

``` { .lua .api-signature }
sm.harvestable.create( uuid, position, rotation?, slopeNormal? )
```

> **Deprecated:**
> Use createHarvestable instead
>

Create a new harvestable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the harvestable. |
| `position` | [Vec3](../Userdata/Vec3.md) | The harvestable's world position. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The harvestable's world rotation, optional uses identity rotation if nil. |
| `slopeNormal` *(optional)* | [Vec3](../Userdata/Vec3.md) | The harvestable's slope normal. For "skew" and "rotate" slope settings, optional uses z axis if nil. |

**Returns:**

| Type | Description |
| --- | --- |
| [Harvestable](../Userdata/Harvestable.md) | The created harvestable. |

### getAllHarvestables {#getallharvestables}

``` { .lua .api-signature }
sm.harvestable.getAllHarvestables( world? )
```

Returns a table with all the harvestables in the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` *(optional)* | [World](../Userdata/World.md) | The world, will default to the script's world. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of all harvestables. {[Harvestable](../Userdata/Harvestable.md), ..} |

### getKinematicByInitialHash {#getkinematicbyinitialhash}

``` { .lua .api-signature }
sm.harvestable.getKinematicByInitialHash( initialHash )
```

Gets a kinematic matching the provided initial hash if it exists.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `initialHash` | number | The initial hash to search for. |

**Returns:**

| Type | Description |
| --- | --- |
| [Harvestable](../Userdata/Harvestable.md)					The kinematic if it exists. |  |

## Server-only

### createHarvestable {#createharvestable}

``` { .lua .api-signature }
sm.harvestable.createHarvestable(
    uuid,
    position,
    rotation?,
    slopeNormal?,
    world?
)
```

Create a new harvestable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the harvestable. |
| `position` | [Vec3](../Userdata/Vec3.md) | The harvestable's world position. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The harvestable's world rotation, optional uses identity rotation if nil. |
| `slopeNormal` *(optional)* | [Vec3](../Userdata/Vec3.md) | The harvestable's slope normal. For "skew" and "rotate" slope settings, optional uses z axis if nil. |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to create the harvestable in. Defaults to the world of the script. |

**Returns:**

| Type | Description |
| --- | --- |
| [Harvestable](../Userdata/Harvestable.md) | The created harvestable. |
