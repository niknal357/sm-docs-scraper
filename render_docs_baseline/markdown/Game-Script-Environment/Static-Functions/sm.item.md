# sm.item

Allows checking for static infortmation about items.

## Constants

### trackingType {#trackingtype}

Item tracking filter types

| Value |
| --- |
| mainQuest |
| sideQuest |
| researchable |

**Returns:**

| Type | Description |
| --- | --- |
| table | The item tracking types list. |

## Server + Client

### getBuoyancyRating {#getbuoyancyrating}

``` { .lua .api-signature }
sm.item.getBuoyancyRating( uuid )
```

Returns the buoyancy rating of an item.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The item uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The buoyancy. |

### getCharacterShape {#getcharactershape}

``` { .lua .api-signature }
sm.item.getCharacterShape( uuid )
```

Return the data for the character [Shape](../Userdata/Shape.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The shape uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The character shape data. |

### getDensityRating {#getdensityrating}

``` { .lua .api-signature }
sm.item.getDensityRating( uuid )
```

Returns the density rating of an item.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The item uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The density. |

### getDurabilityRating {#getdurabilityrating}

``` { .lua .api-signature }
sm.item.getDurabilityRating( uuid )
```

Returns the durability rating of an item.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The item uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The durability. |

### getEdible {#getedible}

``` { .lua .api-signature }
sm.item.getEdible( uuid )
```

Return the data for the edible [Shape](../Userdata/Shape.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The shape uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The edible data. |

### getFeatureData {#getfeaturedata}

``` { .lua .api-signature }
sm.item.getFeatureData( uuid )
```

Returns the shapes feature data.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The item uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The feature data table |

### getFrictionRating {#getfrictionrating}

``` { .lua .api-signature }
sm.item.getFrictionRating( uuid )
```

Returns the friction rating of an item.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The item uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The friction. |

### getInteractablesUuidsOfType {#getinteractablesuuidsoftype}

``` { .lua .api-signature }
sm.item.getInteractablesUuidsOfType( interactableType )
```

Returns a table of all [interactable](../Userdata/Interactable.md) [uuids](../Userdata/Uuid.md) of a interactable type

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactableType` | string | The interactable type name |

**Returns:**

| Type | Description |
| --- | --- |
| table | table of interactable [uuids](../Userdata/Uuid.md) {[Uuid](../Userdata/Uuid.md), ..} |

### getMaterial {#getmaterial}

``` { .lua .api-signature }
sm.item.getMaterial( uuid )
```

Returns the material of a shape uuid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the shape. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The shape's material. |

### getMaterialId {#getmaterialid}

``` { .lua .api-signature }
sm.item.getMaterialId( uuid )
```

Returns the material id of a shape uuid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the shape. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The shape's material id. |

### getPlantable {#getplantable}

``` { .lua .api-signature }
sm.item.getPlantable( uuid )
```

Return the data for the plantable [Shape](../Userdata/Shape.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The shape uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The plantable data. |

### getPlantableUuids {#getplantableuuids}

``` { .lua .api-signature }
sm.item.getPlantableUuids(  )
```

Returns a table of all plantable [uuids](../Userdata/Uuid.md).

**Returns:**

| Type | Description |
| --- | --- |
| table | table of all plantable [uuids](../Userdata/Uuid.md) {[Uuid](../Userdata/Uuid.md), ..}. |

### getQualityLevel {#getqualitylevel}

``` { .lua .api-signature }
sm.item.getQualityLevel( uuid )
```

Return the quality level for the [Shape](../Userdata/Shape.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The shape uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The quality level. |

### getShapeDefaultColor {#getshapedefaultcolor}

``` { .lua .api-signature }
sm.item.getShapeDefaultColor( uuid )
```

Returns the default color of a shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The item uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](../Userdata/Color.md) | Color of the shape. |

### getShapeOffset {#getshapeoffset}

``` { .lua .api-signature }
sm.item.getShapeOffset( uuid )
```

Return the [Shape](../Userdata/Shape.md) offset

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The shape uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The offset vector. |

### getShapeRotation {#getshaperotation}

``` { .lua .api-signature }
sm.item.getShapeRotation( uuid, rotationIndex?, localNormal? )
```

Gets the shape local rotation given a shape rotation index and a surface normal in local space (unit axis vector).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The shape uuid. |
| `rotationIndex` *(optional)* | integer | The rotation index to get the rotation for. (Defaults to 0) |
| `localNormal` *(optional)* | [Vec3](../Userdata/Vec3.md) | The local space normal the is considered to be placed on. (Defaults to positive Z axis) |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The local shape rotation. |

### getShapeSize {#getshapesize}

``` { .lua .api-signature }
sm.item.getShapeSize( uuid )
```

Returns the block dimensions of an shape. Returns nil if the uuid is not an item.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The item uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | Size of the shape. |

### getStackSize {#getstacksize}

``` { .lua .api-signature }
sm.item.getStackSize( uuid )
```

Return the stack size for the item. Returns the default stack size of 1 if the item is not found or is a Tool.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The item uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The stack size. |

### isBlock {#isblock}

``` { .lua .api-signature }
sm.item.isBlock( uuid )
```

Check if the item is a block.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The item uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the item is a block. |

### isFlammable {#isflammable}

``` { .lua .api-signature }
sm.item.isFlammable( uuid )
```

Returns whether the item is flammable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The item uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if flammable. |

### isHarvestablePart {#isharvestablepart}

``` { .lua .api-signature }
sm.item.isHarvestablePart( uuid )
```

Return whether the [Shape](../Userdata/Shape.md) uuid belongs to a harvestable shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The shape uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if shape is a harvestable shape. |

### isJoint {#isjoint}

``` { .lua .api-signature }
sm.item.isJoint( uuid )
```

Check if the item is a [Joint](../Userdata/Joint.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The item uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the item is a joint. |

### isPart {#ispart}

``` { .lua .api-signature }
sm.item.isPart( uuid )
```

Check if the item is a part.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The item uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the item is a part. |

### isTool {#istool}

``` { .lua .api-signature }
sm.item.isTool( uuid )
```

Check if the item uuid belongs to a [Tool](../Userdata/Tool.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the item uuid belongs to a tool. |

## Client-only

### addTrackedItem {#addtrackeditem}

``` { .lua .api-signature }
sm.item.addTrackedItem( uuid, type )
```

Adds a shape uuid to be a tracked item.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the shape. |
| `type` | integer | The [sm.item.trackingType](#trackingtype). |

### removeTrackedItem {#removetrackeditem}

``` { .lua .api-signature }
sm.item.removeTrackedItem( uuid, type )
```

Removes a shape uuid from the tracked items.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the shape. |
| `type` | integer | The [sm.item.trackingType](#trackingtype). |
