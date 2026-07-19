# sm.areaTrigger

**Associated type:** [AreaTrigger](../Userdata/AreaTrigger.md)

An <strong>area trigger</strong> is an invisible collider in the world that can trigger events when objects move in or out of it. This allows the script to, for instance, detect when a character enters a door, or count the number of shapes there are in a room.

Example usage:

```lua
	function MyClass.server_onCreate( self )
		local size = sm.vec3.new( 1, 1, 1 )
		local position = self.shape:getWorldPosition()

		self.myArea = sm.areaTrigger.createBox( size, position )
		self.myArea:bindOnEnter( "onEnter" )
	end

	function MyClass.onEnter( self, trigger, results )
		for i, object in ipairs( results ) do
			print( object, "just entered" )
		end
	end
```

Example with a filter:

```lua
	function MyClass.server_onCreate( self )
		local size = sm.vec3.new( 10, 10, 5 )
		local position = sm.vec3.new( 50, 40, 30 )

		-- Only detect characters
		local filter = sm.areaTrigger.filter.character

		self.myArea = sm.areaTrigger.createBox( size, position, filter )
		self.myArea:bindOnStay( "onStay" )
	end

	-- Callback receives a list of characters
	function MyClass.onStay( self, trigger, results )
		if #results > 0 then
			print( "Intruder alert!" )
		end
	end
```

## Constants

### areaTriggerProxyType {#areatriggerproxytype}

Defines special area trigger features:

- <strong>default</strong> &ndash; Nothing special.
- <strong>water</strong> &ndash; Buoyancy applied to colliding objects.
- <strong>interactable</strong> &ndash; Can be interacted with if implementing bindCanInteract, bindOnInteract, bindCanErase and bindOnDestroy.
- <strong>ladder</strong> &ndash; Attach colliding players to the trigger.
- <strong>melee</strong> &ndash; Can react to melee attack callbacks if implementing bindOnMelee.

| Value | Description |
| --- | --- |
| default | 0 |
| water | 1 |
| interactable | 2 |
| ladder | 3 |

**Returns:**

| Type | Description |
| --- | --- |
| table | The area trigger proxy type list. |

### filter {#filter}

Filters are used to specify what object types an area trigger is able to detect. If an area trigger is created with a filter, it will <strong>only</strong> react to objects of that type. Filters can be combined by adding them.

The filters are:

- <strong>dynamicBody</strong> &ndash; Detects [bodies](../Userdata/Body.md) that are free to move around in the world.
- <strong>staticBody</strong> &ndash; Detects [bodies](../Userdata/Body.md) that are built on the ground or on the lift.
- <strong>character</strong> &ndash; Detects [characters](../Userdata/Character.md) such as players.
- <strong>areatrigger</strong> &ndash; Detects [areatriggers](../Userdata/AreaTrigger.md) such as water areas.
- <strong>harvestable</strong> &ndash; Detects [harvestables](../Userdata/Harvestable.md) such as planted objects.
- <strong>lift</strong> &ndash; Detects [lifts](../Userdata/Lift.md).
- <strong>voxelTerrain</strong> &ndash; Detects destructible terrain.
- <strong>all</strong> &ndash; Detects all of the object types above. (Default)

| Value | Description |
| --- | --- |
| dynamicBody | 1 |
| staticBody | 2 |
| character | 4 |
| areatrigger | 8 |
| harvestable | 512 |
| lift | 1024 |
| voxelTerrain | 32768 |
| all | 34319 |

**Returns:**

| Type | Description |
| --- | --- |
| table | The filter type list. |

### liquidType {#liquidtype}

Defines the liquid type of an area trigger.

Only has an effect on area triggers with the <strong>water</strong> proxy type; setting it on any other proxy type has no effect.

Currently only <strong>lava</strong> has special behavior.

- <strong>water</strong> &ndash; Water. The default. No special behavior beyond the water proxy buoyancy.
- <strong>chemical</strong> &ndash; Chemical. No special behavior beyond the water proxy buoyancy.
- <strong>oil</strong> &ndash; Oil. No special behavior beyond the water proxy buoyancy.
- <strong>lava</strong> &ndash; Lava. Occasionally destroys submerged shapes. Requires [AreaTrigger](../Userdata/AreaTrigger.md): setIncludeShapesInContent.

**Returns:**

| Type | Description |
| --- | --- |
| table | The liquid type list. |

## Functions

<a id="createattachedbox"></a>
### createAttachedBox(Character, Vec3, Vec3?, Quat?, integer?, table?, integer?, string?) {#createattachedbox-character-vec3-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional-string-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedBox(
    character,
    dimension,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?,
    boneName?
)
```

Creates an area trigger box with a given size that stays attached to an [character](sm.character.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](../Userdata/Character.md) | The host character. |
| `dimension` | [Vec3](../Userdata/Vec3.md) | The size of the box |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |
| `boneName` *(optional)* | string | The bone name of the character to attach the area trigger to. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createAttachedBox(Harvestable, Vec3, Vec3?, Quat?, integer?, table?, integer?) {#createattachedbox-harvestable-vec3-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedBox(
    harvestable,
    dimension,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?
)
```

Creates an area trigger box with a given size that stays attached to an [harvestable](sm.harvestable.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](../Userdata/Harvestable.md) | The host harvestable. |
| `dimension` | [Vec3](../Userdata/Vec3.md) | The size of the box |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createAttachedBox(Shape, Vec3, Vec3?, Quat?, integer?, table?, integer?, string?) {#createattachedbox-shape-vec3-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional-string-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedBox(
    shape,
    dimension,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?,
    boneName?
)
```

Creates an area trigger box with a given size that stays attached to an [shape](sm.shape.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](../Userdata/Shape.md) | The host shape |
| `dimension` | [Vec3](../Userdata/Vec3.md) | The size of the box |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |
| `boneName` *(optional)* | string | The bone name of the shape to attach the area trigger to. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createAttachedBox(Interactable, Vec3, Vec3?, Quat?, integer?, table?, integer?, string?) {#createattachedbox-interactable-vec3-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional-string-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedBox(
    interactable,
    dimension,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?,
    boneName?
)
```

Creates an area trigger box with a given size that stays attached to an [interactable](sm.interactable.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](../Userdata/Interactable.md) | The host interactable |
| `dimension` | [Vec3](../Userdata/Vec3.md) | The size of the box |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |
| `boneName` *(optional)* | string | The bone name of the interactable to attach the area trigger to. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

<a id="createattachedcylinder"></a>
### createAttachedCylinder(Character, number, number, Vec3?, Quat?, integer?, table?, integer?, string?) {#createattachedcylinder-character-number-number-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional-string-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedCylinder(
    character,
    radius,
    halfLength,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?,
    boneName?
)
```

Creates an area trigger cylinder with a given size that stays attached to a [character](sm.character.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](../Userdata/Character.md) | The host character. |
| `radius` | number | The radius of the cylinder. |
| `halfLength` | number | The lengthwise extent of the cylinder (i.e. half the length of the cylinder). |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |
| `boneName` *(optional)* | string | The bone name of the character to attach the area trigger to. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createAttachedCylinder(Harvestable, number, number, Vec3?, Quat?, integer?, table?, integer?) {#createattachedcylinder-harvestable-number-number-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedCylinder(
    harvestable,
    radius,
    halfLength,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?
)
```

Creates an area trigger cylinder with a given size that stays attached to an [harvestable](sm.harvestable.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](../Userdata/Harvestable.md) | The host harvestable. |
| `radius` | number | The radius of the cylinder. |
| `halfLength` | number | The lengthwise extent of the cylinder (i.e. half the length of the cylinder). |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createAttachedCylinder(Shape, number, number, Vec3?, Quat?, integer?, table?, integer?, string?) {#createattachedcylinder-shape-number-number-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional-string-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedCylinder(
    shape,
    radius,
    halfLength,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?,
    boneName?
)
```

Creates an area trigger cylinder with a given size that stays attached to an [shape](sm.shape.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](../Userdata/Shape.md) | The host shape |
| `radius` | number | The radius of the cylinder. |
| `halfLength` | number | The lengthwise extent of the cylinder (i.e. half the length of the cylinder). |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |
| `boneName` *(optional)* | string | The bone name of the shape to attach the area trigger to. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createAttachedCylinder(Interactable, number, number, Vec3?, Quat?, integer?, table?, integer?, string?) {#createattachedcylinder-interactable-number-number-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional-string-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedCylinder(
    interactable,
    radius,
    halfLength,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?,
    boneName?
)
```

Creates an area trigger cylinder with a given size that stays attached to an [interactable](sm.interactable.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](../Userdata/Interactable.md) | The host interactable |
| `radius` | number | The radius of the cylinder. |
| `halfLength` | number | The lengthwise extent of the cylinder (i.e. half the length of the cylinder). |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |
| `boneName` *(optional)* | string | The bone name of the interactable to attach the area trigger to. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

<a id="createattachedhull"></a>
### createAttachedHull(Character, string, Vec3?, Quat?, integer?, table?, integer?, string?) {#createattachedhull-character-string-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional-string-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedHull(
    character,
    hull,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?,
    boneName?
)
```

Creates an area trigger hull with a given size that stays attached to a [character](sm.character.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](../Userdata/Character.md) | The host character. |
| `hull` | string | The path to the hull file. |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |
| `boneName` *(optional)* | string | The bone name of the character to attach the area trigger to. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createAttachedHull(Harvestable, string, Vec3?, Quat?, integer?, table?, integer?) {#createattachedhull-harvestable-string-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedHull(
    harvestable,
    hull,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?
)
```

Creates an area trigger hull with a given size that stays attached to an [harvestable](sm.harvestable.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](../Userdata/Harvestable.md) | The host harvestable. |
| `hull` | string | The path to the hull file. |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createAttachedHull(Shape, string, Vec3?, Quat?, integer?, table?, integer?, string?) {#createattachedhull-shape-string-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional-string-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedHull(
    shape,
    hull,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?,
    boneName?
)
```

Creates an area trigger hull with a given size that stays attached to an [shape](sm.shape.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](../Userdata/Shape.md) | The host shape |
| `hull` | string | The path to the hull file. |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |
| `boneName` *(optional)* | string | The bone name of the shape to attach the area trigger to. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createAttachedHull(Interactable, string, Vec3?, Quat?, integer?, table?, integer?, string?) {#createattachedhull-interactable-string-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional-string-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedHull(
    interactable,
    hull,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?,
    boneName?
)
```

Creates an area trigger hull with a given size that stays attached to an [interactable](sm.interactable.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](../Userdata/Interactable.md) | The host interactable |
| `hull` | string | The path to the hull file. |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |
| `boneName` *(optional)* | string | The bone name of the interactable to attach the area trigger to. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

<a id="createattachedsphere"></a>
### createAttachedSphere(Character, number, Vec3?, Quat?, integer?, table?, integer?, string?) {#createattachedsphere-character-number-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional-string-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedSphere(
    character,
    radius,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?,
    boneName?
)
```

Creates an area trigger sphere with a given size that stays attached to a [character](sm.character.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](../Userdata/Character.md) | The host character. |
| `radius` | number | The radius of the sphere. |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |
| `boneName` *(optional)* | string | The bone name of the character to attach the area trigger to. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createAttachedSphere(Harvestable, number, Vec3?, Quat?, integer?, table?, integer?) {#createattachedsphere-harvestable-number-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedSphere(
    harvestable,
    radius,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?
)
```

Creates an area trigger sphere with a given size that stays attached to an [harvestable](sm.harvestable.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](../Userdata/Harvestable.md) | The host harvestable. |
| `radius` | number | The radius of the sphere. |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createAttachedSphere(Shape, number, Vec3?, Quat?, integer?, table?, integer?, string?) {#createattachedsphere-shape-number-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional-string-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedSphere(
    shape,
    radius,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?,
    boneName?
)
```

Creates an area trigger sphere with a given size that stays attached to an [shape](sm.shape.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](../Userdata/Shape.md) | The host shape |
| `radius` | number | The radius of the sphere. |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |
| `boneName` *(optional)* | string | The bone name of the shape to attach the area trigger to. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createAttachedSphere(Interactable, number, Vec3?, Quat?, integer?, table?, integer?, string?) {#createattachedsphere-interactable-number-vec3-optional-quat-optional-integer-optional-table-optional-integer-optional-string-optional}

``` { .lua .api-signature }
sm.areaTrigger.createAttachedSphere(
    interactable,
    radius,
    position?,
    rotation?,
    filter?,
    userdata?,
    areaTriggerProxyType?,
    boneName?
)
```

Creates an area trigger sphere with a given size that stays attached to an [interactable](sm.interactable.md)

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](../Userdata/Interactable.md) | The host interactable |
| `radius` | number | The radius of the sphere. |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position offset (Defaults to [sm.vec3.zero](sm.vec3.md#zero)) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation offset (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |
| `boneName` *(optional)* | string | The bone name of the interactable to attach the area trigger to. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createBox {#createbox}

``` { .lua .api-signature }
sm.areaTrigger.createBox(
    dimension,
    position,
    rotation?,
    filter?,
    userdata?,
    world?,
    areaTriggerProxyType?
)
```

Creates a new box area trigger at a given position with a given size.

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `dimension` | [Vec3](../Userdata/Vec3.md) | The dimensions of the box. |
| `position` | [Vec3](../Userdata/Vec3.md) | The world position. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The world rotation. (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to create the area trigger in. (optional) |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createBoxWater {#createboxwater}

``` { .lua .api-signature }
sm.areaTrigger.createBoxWater(
    dimension,
    position,
    rotation?,
    filter?,
    userdata?
)
```

> **Deprecated:**
> use [sm.areaTrigger.createBox](#createbox) with [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype) instead.
>

Creates a new box area trigger that represent water ie. certain objects cant be placed in it.

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `dimension` | [Vec3](../Userdata/Vec3.md) | The dimensions of the box. |
| `position` | [Vec3](../Userdata/Vec3.md) | The world position. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The world rotation. (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createCylinder {#createcylinder}

``` { .lua .api-signature }
sm.areaTrigger.createCylinder(
    radius,
    halfLength,
    position,
    rotation?,
    filter?,
    userdata?,
    world?,
    areaTriggerProxyType?
)
```

Creates a new cylinder area trigger at a given position with a given size.

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `radius` | number | The radius of the cylinder. |
| `halfLength` | number | The lengthwise extent of the cylinder (i.e. half the length of the cylinder). |
| `position` | [Vec3](../Userdata/Vec3.md) | The world position. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The world rotation. (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to create the area trigger in. (optional) |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createHull {#createhull}

``` { .lua .api-signature }
sm.areaTrigger.createHull(
    hull,
    position,
    rotation?,
    filter?,
    userdata?,
    world?,
    areaTriggerProxyType?
)
```

Creates a new hull area trigger at a given position with a given size.

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `hull` | string | The path to the hull file. |
| `position` | [Vec3](../Userdata/Vec3.md) | The world position. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The world rotation. (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to create the area trigger in. (optional) |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |

### createSphere {#createsphere}

``` { .lua .api-signature }
sm.areaTrigger.createSphere(
    radius,
    position,
    rotation?,
    filter?,
    userdata?,
    world?,
    areaTriggerProxyType?
)
```

Creates a new sphere area trigger at a given position with a given size.

If a filter is specified, the trigger area will only be able to detects objects of that certain type. See [sm.areaTrigger.filter](#filter) for more information about filters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `radius` | number | The radius of the sphere. |
| `position` | [Vec3](../Userdata/Vec3.md) | The world position. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The world rotation. (Defaults to [sm.quat.identity](sm.quat.md#identity)) |
| `filter` *(optional)* | integer | The object types the area trigger may detect. (See [sm.areaTrigger.filter](#filter)). (Defaults to sm.areaTrigger.filter.all) |
| `userdata` *(optional)* | table | An optional table of user data |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to create the area trigger in. (optional) |
| `areaTriggerProxyType` *(optional)* | integer | The proxy type of the area trigger. (See [sm.areaTrigger.areaTriggerProxyType](#areatriggerproxytype)) (Defaults to sm.areaTrigger.areaTriggerProxyType.default) |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](../Userdata/AreaTrigger.md) | The created area trigger. |
