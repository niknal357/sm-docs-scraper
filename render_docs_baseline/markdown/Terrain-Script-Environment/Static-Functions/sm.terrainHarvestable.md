# sm.terrainHarvestable

**Associated type:** [Harvestable](../Userdata/Harvestable.md)

## Functions

### calculateInitialHash {#calculateinitialhash}

``` { .lua .api-signature }
sm.terrainHarvestable.calculateInitialHash( uuid, world, position, rotation )
```

Calculates the initial hash of a kinematic. The initial hash identifies the kinematic by its initial world position, uuid and world id.

This hash will be unsalted. Usually kinematics created from script rather than from cell loading have their hashes salted with random numbers.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The kinematic uuid. |
| `world` | [World](../Userdata/World.md) | The world the kinematic is in. |
| `position` | [Vec3](../Userdata/Vec3.md) | The initial position of the kinematic in world space. |
| `rotation` | [Quat](../Userdata/Quat.md) | The initial rotation of the kinematic. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The calculated unsalted initial hash. |
