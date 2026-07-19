# sm.lift

**Associated type:** [Lift](../Userdata/Lift.md)

## Server-only

### createNonPlayerLift {#createnonplayerlift}

``` { .lua .api-signature }
sm.lift.createNonPlayerLift( world, pos, body?, level?, rotation? )
```

Creates a non-player lift. A non-player lift is a lift that doesn't belong to any player. 

return	[Lift](../Userdata/Lift.md):						The created lift.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | World to place the lift in. |
| `pos` | [Vec3](../Userdata/Vec3.md) | Position to place the lift at. |
| `body` *(optional)* | [Body](../Userdata/Body.md) | Body to place on the lift (optional). |
| `level` *(optional)* | integer | Level to place the lift at. (Defaults to 0.) |
| `rotation` *(optional)* | integer | Rotation index to place the lift at. (Defaults to 0.) |

### createVirtualLift {#createvirtuallift}

``` { .lua .api-signature }
sm.lift.createVirtualLift( world, body )
```

Creates a virtual lift. A virtual lift is a lift that doesn't exist in the game world. But allows for a static body to be placed on it.

return	[Lift](../Userdata/Lift.md):					The created lift.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | World to place the lift in. |
| `body` | [Body](../Userdata/Body.md) | Body to place on the lift. |
