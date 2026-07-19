# Garage

**Associated namespace:** [sm.garage](../Static-Functions/sm.garage.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing an <strong>Garage</strong> in the game.

**Values:**

- <a id="id"></a>`id` [ **int** ] <br>
    - `Get`: returns the id of the garage

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Garage == Garage` | boolean | Checks if two instances of [Garage](Garage.md) refer to the same Garage. |

## Server + Client

### creationFits {#creationfits}

``` { .lua .api-signature }
garage:creationFits(  )
```

Checks if the tracked creation fits into the garage returns nil if no creation is tracked.

**Returns:**

| Type | Description |
| --- | --- |
| bool				true if the creation fits otherwise false. |  |

### getBlueprintBounds {#getblueprintbounds}

``` { .lua .api-signature }
garage:getBlueprintBounds(  )
```

Returns the bounds of the body of the actively tracked blueprint in the garage. Returns nil if there is no actively tracked blueprint.

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of { min, max } |

### getGarageBounds {#getgaragebounds}

``` { .lua .api-signature }
garage:getGarageBounds(  )
```

Returns the bounds of the garage staging area.

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of { min, max } |

### getPlacement {#getplacement}

``` { .lua .api-signature }
garage:getPlacement(  )
```

Imports a actively tracked blueprint using the garage returns nil if the blueprint is not initialized yet.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | position	The world position of the tracked blueprint. |

### getPosition {#getposition}

``` { .lua .api-signature }
garage:getPosition(  )
```

Returns the position of the garage.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | position |

### getTrackedBlueprint {#gettrackedblueprint}

``` { .lua .api-signature }
garage:getTrackedBlueprint(  )
```

Gets the tracked creation Name and JsonTable from the garage.

**Returns:**

| Type | Description |
| --- | --- |
| string					Name |  |
| table					jsonData |  |

### getTrackingRevision {#gettrackingrevision}

``` { .lua .api-signature }
garage:getTrackingRevision(  )
```

Returns the tracking revision counter, incremented each time the tracked blueprint changes.

**Returns:**

| Type | Description |
| --- | --- |
| int | revision |

### hasActiveTracking {#hasactivetracking}

``` { .lua .api-signature }
garage:hasActiveTracking(  )
```

Checks if the garage has an actively tracked blueprint.

**Returns:**

| Type | Description |
| --- | --- |
| bool				true if there is an actively tracked blueprint, false otherwise. |  |

### importBlueprint {#importblueprint}

``` { .lua .api-signature }
garage:importBlueprint(  )
```

Imports a actively tracked blueprint using the garage

### untrackBlueprint {#untrackblueprint}

``` { .lua .api-signature }
garage:untrackBlueprint(  )
```

Untrack a blueprint from a garage and synchronizes it to all other clients.

## Client-only

### trackBlueprint {#trackblueprint}

``` { .lua .api-signature }
garage:trackBlueprint( blueprint )
```

Tracks a blueprint from a garage and synchronizes it to all other clients.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `blueprint` | string | path			The path of the blueprint |
