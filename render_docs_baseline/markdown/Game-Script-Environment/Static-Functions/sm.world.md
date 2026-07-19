# sm.world

**Associated type:** [World](../Userdata/World.md)

The <strong>world</strong> api handles the creation and destruction of worlds.

A world contains the terrain and simulates the physics environment in which other game objects can exist.

## Constants

### ids {#ids}

Predefined special world ids

| Value |
| --- |
| anyWorld |
| noWorld |

### voxelFilter {#voxelfilter}

Filters are used to specify what materials a terrain modification sphere can destroy.

The filters are:

- <strong>material0</strong> &ndash; Allows destruction of material 0 in the voxel material set.
- <strong>material1</strong> &ndash; Allows destruction of material 1 in the voxel material set.
- <strong>material2</strong> &ndash; Allows destruction of material 2 in the voxel material set.
- <strong>material3</strong> &ndash; Allows destruction of material 3 in the voxel material set.
- <strong>material4</strong> &ndash; Allows destruction of material 4 in the voxel material set.
- <strong>material5</strong> &ndash; Allows destruction of material 5 in the voxel material set.
- <strong>material6</strong> &ndash; Allows destruction of material 6 in the voxel material set.
- <strong>material7</strong> &ndash; Allows destruction of material 7 in the voxel material set.
- <strong>all</strong> &ndash; Allows destruction of all materials in the voxel material set.

| Value | Description |
| --- | --- |
| none | 0 |
| material0 | 1 |
| material1 | 2 |
| material2 | 4 |
| material3 | 8 |
| material4 | 16 |
| material5 | 32 |
| material6 | 64 |
| material7 | 128 |
| all | 255 |

**Returns:**

| Type | Description |
| --- | --- |
| table | The filter type list. |

## Server + Client

### getCurrentWorld {#getcurrentworld}

``` { .lua .api-signature }
sm.world.getCurrentWorld(  )
```

Get the world that the scripted object is in.

**Returns:**

| Type | Description |
| --- | --- |
| [World](../Userdata/World.md) | The world |

### getDirtySpheres {#getdirtyspheres}

``` { .lua .api-signature }
sm.world.getDirtySpheres( position?, radius? )
```

Returns an array of tables representing spheres where something has changed in the world.

The optional position and radius parameters will construct a sphere, and use it as a filter to only show results that intersect that sphere.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The world position of the sphere. (Optional) |
| `radius` *(optional)* | number | The radius of the sphere. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of tables. { {center=[Vec3](../Userdata/Vec3.md), radius=number}, ..} |

## Server-only

### createWorld {#createworld}

``` { .lua .api-signature }
sm.world.createWorld( filename, classname, terrainParams?, seed? )
```

Creates a new world object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `filename` | string | The world script filename. |
| `classname` | string | The world script class name. |
| `terrainParams` *(optional)* | any | The world's terrain parameters. (Optional) |
| `seed` *(optional)* | integer | The world's seed. Defaults to 0 (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [World](../Userdata/World.md) | The created world object. |

### getLegacyCreativeWorld {#getlegacycreativeworld}

``` { .lua .api-signature }
sm.world.getLegacyCreativeWorld(  )
```

Gets a previously saved creative world

**Returns:**

| Type | Description |
| --- | --- |
| [World](../Userdata/World.md) | The world (id 0) if it exists in the database or nil |

### loadWorld {#loadworld}

``` { .lua .api-signature }
sm.world.loadWorld( world )
```

Loads a previously created world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | The world that should be loaded. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the world was loaded. |
