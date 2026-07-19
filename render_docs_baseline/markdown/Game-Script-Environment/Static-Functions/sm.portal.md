# sm.portal

**Associated type:** [Portal](../Userdata/Portal.md)

A <strong>portal</strong> moves objects inside a box to another box in another place.

## Server + Client

### findBestPortalToWorld {#findbestportaltoworld}

``` { .lua .api-signature }
sm.portal.findBestPortalToWorld( playerWorld, targetWorld, fromPosition )
```

Finds the portal position that has the best path to the given world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `playerWorld` | integer | The player's current world id. |
| `targetWorld` | integer | The world id we wanna get a path towards. |
| `fromPosition` | [Vec3](../Userdata/Vec3.md) | The position we wanna get a path from. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md), [Portal](../Userdata/Portal.md) | The position of the portal, and the portal with the shortest path to the given world. |

## Server-only

### addWorldPortalHook {#addworldportalhook}

``` { .lua .api-signature }
sm.portal.addWorldPortalHook( world, name, portal )
```

Adds a hook that a new world can find to hook up the other side of a portal.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | The target world. |
| `name` | string | The portal name. |
| `portal` | [Portal](../Userdata/Portal.md) | The portal. |

### createPortal {#createportal}

``` { .lua .api-signature }
sm.portal.createPortal( dimensions )
```

Creates a new portal.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `dimensions` | [Vec3](../Userdata/Vec3.md) | The dimensions of the portal box. |

**Returns:**

| Type | Description |
| --- | --- |
| [Portal](../Userdata/Portal.md) | The created portal. |

### destroy {#destroy}

``` { .lua .api-signature }
sm.portal.destroy( portal )
```

Destroys a portal.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `portal` | [Portal](../Userdata/Portal.md) | The portal to be destroyed. |

### popWorldPortalHook {#popworldportalhook}

``` { .lua .api-signature }
sm.portal.popWorldPortalHook( name, world? )
```

Finds and pops world hook for this world if present.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The portal name. |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to look in (Optional, defaults to world from script context) |

**Returns:**

| Type | Description |
| --- | --- |
| [Portal](../Userdata/Portal.md) | The portal. Nil if nothing was found. |

### transferBToB {#transferbtob}

``` { .lua .api-signature }
sm.portal.transferBToB( fromPortal, toPortal, filter? )
```

Transfers objects inside one B opening to the B opening of another portal.

Can be used to make elevators with several floors.

Portal sizes and opening A must match (world, position and rotation).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `fromPortal` | [Portal](../Userdata/Portal.md) | The portal to transfer from. |
| `toPortal` | [Portal](../Userdata/Portal.md) | The portal to transfer to. |
| `filter` *(optional)* | integer | A [sm.physics.filter](sm.physics.md#filter) mask selecting which contents to transfer. Only [dynamicBody](sm.physics.md#filter), [staticBody](sm.physics.md#filter) and [character](sm.physics.md#filter) are meaningful. Defaults to transferring bodies and characters. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if successful, false on failure. |
