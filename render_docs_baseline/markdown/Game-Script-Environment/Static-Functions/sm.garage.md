# sm.garage

**Associated type:** [Garage](../Userdata/Garage.md)

The <strong>Garage</strong> library contains various utility functions for handling the garage.

## Functions

### createGarage {#creategarage}

``` { .lua .api-signature }
sm.garage.createGarage( garageId, worldId, halfextents, position )
```

Creates a new garage.

The garage is a spawn area for creations defined by a bounding box. The garage can track blueprints and import them into the world.

The garage is identified by an user specified id.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `garageId` | int | The id of the garage to create |
| `worldId` | uint | The world the garage is in |
| `halfextents` | [Vec3](../Userdata/Vec3.md) | Half extents of the spawnbox inside the garage |
| `position` | [Vec3](../Userdata/Vec3.md) | Position of the spawn box inside the garage |

**Returns:**

| Type | Description |
| --- | --- |
| [Garage](../Userdata/Garage.md)		Garage					The Garage object |  |

### getGarage {#getgarage}

``` { .lua .api-signature }
sm.garage.getGarage( garageId )
```

Gets a already existing garage returns nil if it does not exist.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `garageId` | uint | The id of the garage to get |

**Returns:**

| Type | Description |
| --- | --- |
| [Garage](../Userdata/Garage.md)		Garage					The Garage object |  |
