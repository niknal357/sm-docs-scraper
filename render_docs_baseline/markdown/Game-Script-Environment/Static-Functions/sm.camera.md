# sm.camera

The <strong>camera</strong> library contains methods related to the [localPlayer](sm.localPlayer.md)'s camera view.

In first-person view the camera is located inside the player's head, whereas in third-person view it floats behind them.

This library can only be used on the client.

## Constants

### state {#state}

Camera states are used to specify how the camera will view the world. The default state is meant for normal gameplay and the scripted states are meant to be used in cutscenes or interactables.

The states are:

- <strong>default</strong> &ndash; The camera is controlled by the player.
- <strong>cutsceneFP</strong> &ndash; Scripted first-person camera; position, rotation, and FOV are set by script.
- <strong>cutsceneTP</strong> &ndash; Scripted third-person camera; position, rotation, and FOV are set by script.
- <strong>forcedTP</strong> &ndash; Forces a third-person view regardless of the player's zoom step. Used during tumbling.
- <strong>gyroSeatFP</strong> &ndash; First-person camera whose direction is driven by the gyro seat's rotation.
- <strong>gyroSeatTP</strong> &ndash; Third-person camera for the gyro seat.
- <strong>scriptedTP</strong> &ndash; Third-person camera with position, rotation, and FOV fully overridden by script. Used for interactable cutscenes.
- <strong>seatLockedCamera</strong> &ndash; The camera direction and position are locked to the seat's local space. The view is first-person unless a pullback is set, which produces a third-person view.

| Value | Description |
| --- | --- |
| default | 1 |
| cutsceneFP | 2 |
| cutsceneTP | 3 |
| forcedTP | 4 |
| gyroSeatFP | 5 |
| gyroSeatTP | 6 |
| scriptedTP | 7 |
| seatLockedCamera | 8 |

**Returns:**

| Type | Description |
| --- | --- |
| table |  |

## Client-only

### cameraSphereCast {#cameraspherecast}

``` { .lua .api-signature }
sm.camera.cameraSphereCast( radius, start, direction )
```

Performs a distance convex sweep with the shape of a sphere, from a position with a given direction.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `radius` | number | The radius of the cast sphere |
| `start` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `direction` | [Vec3](../Userdata/Vec3.md) | The cast direction and range. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The fraction of the distance reached until collision. |

### getCameraPullback {#getcamerapullback}

``` { .lua .api-signature }
sm.camera.getCameraPullback(  )
```

Returns the camera's zoom step.

**Returns:**

| Type | Description |
| --- | --- |
| number | step		How far away the camera is from the player while standing |
| number | seatedStep	How far away the camera is from the player while seated |

### getCameraState {#getcamerastate}

``` { .lua .api-signature }
sm.camera.getCameraState(  )
```

Gets the camera's control state.

**Returns:**

| Type | Description |
| --- | --- |
| integer | state	How the camera is moved. (See [sm.camera.state](#state)) |

### getDefaultFov {#getdefaultfov}

``` { .lua .api-signature }
sm.camera.getDefaultFov(  )
```

Returns the camera's default field of view angle.

**Returns:**

| Type | Description |
| --- | --- |
| number | The field of view. |

### getDefaultPosition {#getdefaultposition}

``` { .lua .api-signature }
sm.camera.getDefaultPosition(  )
```

Returns the world position where the camera should be by default.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The camera's world position. |

### getDefaultRotation {#getdefaultrotation}

``` { .lua .api-signature }
sm.camera.getDefaultRotation(  )
```

Returns the world rotation where the camera should be by default.

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The camera's default world rotation. |

### getDirection {#getdirection}

``` { .lua .api-signature }
sm.camera.getDirection(  )
```

Returns the direction the camera is aiming.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The direction of the camera's aim. |

### getFov {#getfov}

``` { .lua .api-signature }
sm.camera.getFov(  )
```

Returns the camera's field of view angle.

**Returns:**

| Type | Description |
| --- | --- |
| number | The field of view. |

### getPosition {#getposition}

``` { .lua .api-signature }
sm.camera.getPosition(  )
```

Returns the world position of the camera.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The camera's world position. |

### getRight {#getright}

``` { .lua .api-signature }
sm.camera.getRight(  )
```

Returns the right-vector perpendicular to the camera's aim.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The right-vector of the camera's aim. |

### getRotation {#getrotation}

``` { .lua .api-signature }
sm.camera.getRotation(  )
```

Returns the world rotation of the camera.

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The camera's world rotation. |

### getUp {#getup}

``` { .lua .api-signature }
sm.camera.getUp(  )
```

Returns the up-vector perpendicular to the camera's aim.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The up-vector of the camera's aim. |

### setCameraPullback {#setcamerapullback}

``` { .lua .api-signature }
sm.camera.setCameraPullback( step, seatedStep )
```

Sets the camera's zoom step.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `step` | integer | How far away the camera is from the player while standing |
| `seatedStep` | integer | How far away the camera is from the player while seated |

### setCameraState {#setcamerastate}

``` { .lua .api-signature }
sm.camera.setCameraState( state )
```

Sets the camera's control state.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `state` | integer | How the camera is moved. (See [sm.camera.state](#state)) |

### setDirection {#setdirection}

``` { .lua .api-signature }
sm.camera.setDirection( direction )
```

Sets the direction the camera is aiming.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `direction` | [Vec3](../Userdata/Vec3.md) | The direction of the camera's aim. |

### setFov {#setfov}

``` { .lua .api-signature }
sm.camera.setFov( FOV )
```

Sets the camera's field of view angle.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `FOV` | number | The field of view. |

### setPosition {#setposition}

``` { .lua .api-signature }
sm.camera.setPosition( position )
```

Sets the world position of the camera.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | The camera's world position. |

### setRotation {#setrotation}

``` { .lua .api-signature }
sm.camera.setRotation( rotation )
```

Sets the rotation of the camera.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `rotation` | [Quat](../Userdata/Quat.md) | The rotation of the camera. |

### setSeatLockedCameraPullback {#setseatlockedcamerapullback}

``` { .lua .api-signature }
sm.camera.setSeatLockedCameraPullback( pullback )
```

Sets the camera pullback distance for the seatLockedCamera camera state.

When greater than zero the camera is pulled back from the seat origin along the camera direction.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `pullback` | number | The pullback distance. |

### setSeatLockedCameraUpOffset {#setseatlockedcameraupoffset}

``` { .lua .api-signature }
sm.camera.setSeatLockedCameraUpOffset( upOffset )
```

Sets the camera up offset for the seatLockedCamera camera state.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `upOffset` | number | The up offset in local space. |

### setSeatLockedLocalDirection {#setseatlockedlocaldirection}

``` { .lua .api-signature }
sm.camera.setSeatLockedLocalDirection( localDirection )
```

Sets the local direction for the camera when using the seatLockedCamera camera state.

The direction is in the seat's local space and will be transformed by the interpolated seat rotation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `localDirection` | [Vec3](../Userdata/Vec3.md) | The local direction to face. |

### setSeatLockedLocalUp {#setseatlockedlocalup}

``` { .lua .api-signature }
sm.camera.setSeatLockedLocalUp( localUp )
```

Sets the local up vector for the camera when using the seatLockedCamera camera state.

The up vector is in the seat's local space.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `localUp` | [Vec3](../Userdata/Vec3.md) | The local up direction. |

### setShake {#setshake}

``` { .lua .api-signature }
sm.camera.setShake( strength )
```

Sets the camera's level of camera shake.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `strength` | number | The camera shake strength. |

### setUnseatDirection {#setunseatdirection}

``` { .lua .api-signature }
sm.camera.setUnseatDirection( worldDirection? )
```

Sets the world-space direction for the local player character to face when the player unseats. Cleared automatically when used or when entering a seat.

Passing nil clears any previously set unseat direction.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `worldDirection` *(optional)* | [Vec3](../Userdata/Vec3.md) | The world-space direction to face on unseat. (optional) |
