# sm.shape

**Associated type:** [Shape](../Userdata/Shape.md)

A <strong>shape</strong> is any block, part or basic material that can be built by a player. Shapes are always connected to a [body](sm.body.md), which is a collection of shapes.

For more information about creating your own scripted shapes, see [ShapeClass](../Classes/ShapeClass.md).

## Constants

### destructionType {#destructiontype}

Shape destruction types. Using these will handle the destruction as if it was caused by the specified type.

| Value |
| --- |
| None |
| Melee |
| Projectile |
| Explosion |

**Returns:**

| Type | Description |
| --- | --- |
| table | The destruction type list. |

### material {#material}

Shape physics materials

| Value |
| --- |
| None |
| Default |
| Grass |
| Dirt |
| Sand |
| Gravel |
| Rock |
| Wood |
| Plastic |
| Metal |
| Glass |
| Fence |
| Fabric |
| Cardboard |
| Foliage |
| Tape |
| Water |
| WaterSubmerged |
| RagdollHuman |
| Mechanical |
| Fruit |
| RagdollAnimal |
| Electronics |
| Sticky |
| Ice |
| Bubblewrap |
| Scrapmetal |
| Rewardlocker |
| Chili |
| VoxelBlueRock |
| VoxelPurpleRock |
| VoxelRedRock |
| VoxelBlueMineral |
| VoxelPurpleMineral |
| VoxelRedMineral |

**Returns:**

| Type | Description |
| --- | --- |
| table | The physics material types list. |

## Server + Client

### getIsHarvest {#getisharvest}

``` { .lua .api-signature }
sm.shape.getIsHarvest( uuid )
```

Return whether the shape uuid belongs to a harvest shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The shape uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the shape is harvestable. |

### getIsStackable {#getisstackable}

``` { .lua .api-signature }
sm.shape.getIsStackable( uuid )
```

Return whether the shape uuid belongs to a stackable shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The shape uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the shape is stackable. |

### getShapeDescription {#getshapedescription}

``` { .lua .api-signature }
sm.shape.getShapeDescription( uuid )
```

Returns the block/part description for the given uuid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The shape description. |

### getShapeIcon {#getshapeicon}

``` { .lua .api-signature }
sm.shape.getShapeIcon(  )
```

> **Deprecated:**
> Deprecated function. Kept for compability with old scripts.
>

Does nothing.

### getShapeTitle {#getshapetitle}

``` { .lua .api-signature }
sm.shape.getShapeTitle( uuid )
```

Returns the block/part name for the given uuid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The shape title. |

### getShapeTypeColor {#getshapetypecolor}

``` { .lua .api-signature }
sm.shape.getShapeTypeColor( uuid )
```

Returns the color of the uuid's shape type

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](../Userdata/Color.md) | The color of the shape type. |

### getShapeUpperCaseTitle {#getshapeuppercasetitle}

``` { .lua .api-signature }
sm.shape.getShapeUpperCaseTitle( uuid )
```

Returns the block/part name for the given uuid in uppercase as given in the inventory description translations. Defaults to the shape title if an upper case version does not exist.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The shape title in upper case. |

### shapesInSphere {#shapesinsphere}

``` { .lua .api-signature }
sm.shape.shapesInSphere( center, radius )
```

Returns a table of all shapes colliding with a given sphere.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `center` | [Vec3](../Userdata/Vec3.md) | The center position of the sphere. |
| `radius` | number | The radius of the sphere. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of found shapes. {[Shape](../Userdata/Shape.md), ..} |

### uuidExists {#uuidexists}

``` { .lua .api-signature }
sm.shape.uuidExists( uuid )
```

Return whether the shape uuid exists

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The shape uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | exists. |

## Server-only

### createBlock {#createblock}

``` { .lua .api-signature }
sm.shape.createBlock( uuid, size, position, rotation?, dynamic?, forceSpawn? )
```

Create a new block

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the shape. |
| `size` | [Vec3](../Userdata/Vec3.md) | The size of the block. |
| `position` | [Vec3](../Userdata/Vec3.md) | The shape's world position. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The shape's world rotation. Defaults to no rotation (Optional) |
| `dynamic` *(optional)* | boolean | Set true if the shape is dynamic or false if the shape is static. Defaults to true (Optional) |
| `forceSpawn` *(optional)* | boolean | Set true to force spawn the shape even if it will cause collision. Defaults to true (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [Shape](../Userdata/Shape.md)							The created block |  |

### createPart {#createpart}

``` { .lua .api-signature }
sm.shape.createPart( uuid, position, rotation, dynamic?, forceSpawn?, world? )
```

Create a new part

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the shape. |
| `position` | [Vec3](../Userdata/Vec3.md) | The shape's world position. |
| `rotation` | [Quat](../Userdata/Quat.md) | The shape's world rotation. Defaults to no rotation (Optional) |
| `dynamic` *(optional)* | boolean | Set true if the shape is dynamic or false if the shape is static. Defaults to true (Optional) |
| `forceSpawn` *(optional)* | boolean | Set true to force spawn the shape even if it will cause collision. Defaults to true (Optional) |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to create the part in. Uses the script's world by default. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [Shape](../Userdata/Shape.md)							The created part |  |

### createWedge {#createwedge}

``` { .lua .api-signature }
sm.shape.createWedge( uuid, size, position, rotation?, dynamic?, forceSpawn? )
```

Creates a wedge. The wedge is oriented with one 

cathetus along the Y-axis and the other along the Z-axis, forming a right angle. 

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the shape. |
| `size` | [Vec3](../Userdata/Vec3.md) | The size of the wedge. |
| `position` | [Vec3](../Userdata/Vec3.md) | The shape's world position. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The shape's world rotation. Defaults to no rotation (Optional) |
| `dynamic` *(optional)* | boolean | Set true if the shape is dynamic or false if the shape is static. Defaults to true (Optional) |
| `forceSpawn` *(optional)* | boolean | Set true to force spawn the shape even if it will cause collision. Defaults to true (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [Shape](../Userdata/Shape.md)							The created wedge |  |
