# Effect

**Associated namespace:** [sm.effect](../Static-Functions/sm.effect.md)

**Usage:** Client Only

**Serializable:** No

A userdata object representing an <strong>effect</strong>.

**Values:**

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of an effect.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Effect == Effect` | boolean | Checks if two instances of [Effect](Effect.md) refer to the same Effect. |

## Server + Client

### destroy {#destroy}

``` { .lua .api-signature }
effect:destroy(  )
```

Stops and destroys the effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

### getId {#getid}

``` { .lua .api-signature }
effect:getId(  )
```

Returns the id of an effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The effect's id. |

## Client-only

### bindEventCallback {#bindeventcallback}

``` { .lua .api-signature }
effect:bindEventCallback( methodName, params?, reference? )
```

> **Deprecated:**
> use [Effect.bindEventClientCallback](#bindeventclientcallback) instead.
>

Bind a lua callback to be triggered by the effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `methodName` | string | The name of the callback method being bound. Example: MyClass.methodName( self, event, params ) |
| `params` *(optional)* | any | Parameter object passed to the callback. (Optional) |
| `reference` *(optional)* | table | Table to receive the callback. (Optional) |

### bindEventClientCallback {#bindeventclientcallback}

``` { .lua .api-signature }
effect:bindEventClientCallback( params?, reference? )
```

Bind a lua client callback script reference to be used by the effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `params` *(optional)* | any | Parameter object passed to the callback. (Optional) |
| `reference` *(optional)* | table | Table to receive the callback. (Optional) |

### bindEventServerCallback {#bindeventservercallback}

``` { .lua .api-signature }
effect:bindEventServerCallback( params?, reference? )
```

Bind a lua server callback script reference to be used by the effect. Host only.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `params` *(optional)* | any | Parameter object passed to the callback. (Optional) |
| `reference` *(optional)* | table | Table to receive the callback. (Optional) |

### clearClientEventCallback {#clearclienteventcallback}

``` { .lua .api-signature }
effect:clearClientEventCallback(  )
```

Clear the effect lua client callback script reference.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

### clearEventCallbacks {#cleareventcallbacks}

``` { .lua .api-signature }
effect:clearEventCallbacks(  )
```

> **Deprecated:**
> use [Effect.clearClientEventCallback](#clearclienteventcallback) together with [Effect.bindEventClientCallback](#bindeventclientcallback) instead.
>

Clear all lua effect callbacks.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

### clearServerEventCallback {#clearservereventcallback}

``` { .lua .api-signature }
effect:clearServerEventCallback(  )
```

Clear the effect lua server callback script reference.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

### detach {#detach}

``` { .lua .api-signature }
effect:detach(  )
```

Detaches the effect from its host object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

### getCameraData {#getcameradata}

``` { .lua .api-signature }
effect:getCameraData(  )
```

Get a table of camera effect data.

Returns nil if the effect is not a camera effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The settings. { hasBlendIn = boolean, hasBlendOut = boolean, active = boolean, cameraPosition = [Vec3](Vec3.md), cameraRotation = [Quat](Quat.md), cameraFov = number } |

### getWorldPosition {#getworldposition}

``` { .lua .api-signature }
effect:getWorldPosition(  )
```

Gets the current world position

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md)								The world position. |  |

### hasActiveCamera {#hasactivecamera}

``` { .lua .api-signature }
effect:hasActiveCamera(  )
```

Check if the effect has an active camera effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Is active. |

### hasHost {#hashost}

``` { .lua .api-signature }
effect:hasHost(  )
```

Returns whether the effect has a host.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the effect is hosted. |

### isBreakSustaining {#isbreaksustaining}

``` { .lua .api-signature }
effect:isBreakSustaining(  )
```

Returns whether the effect is break sustained.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether effect is break sustained. |

### isDone {#isdone}

``` { .lua .api-signature }
effect:isDone(  )
```

Returns whether the effect is done, meaning that all effect instances have finished.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether effect is done. |

### isPlaying {#isplaying}

``` { .lua .api-signature }
effect:isPlaying(  )
```

Returns whether the effect is currently playing.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether effect is playing. |

### setAutoPlay {#setautoplay}

``` { .lua .api-signature }
effect:setAutoPlay( autoplay, autoPlayOnce?, resetPlayOnce? )
```

Sets an effect to start playing and repeating automatically.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `autoplay` | boolean | Autoplay enabled. |
| `autoPlayOnce` *(optional)* | boolean | If set the effect will not loop when autoplaying. (Defaults to false) (Optional) |
| `resetPlayOnce` *(optional)* | boolean | Will reset the autoPlayOnce condition, allowing the effect to play again if it already has since earlier. (Defaults to false) (Optional) |

### setDetachOnHostDestroy {#setdetachonhostdestroy}

``` { .lua .api-signature }
effect:setDetachOnHostDestroy( detach )
```

Detaches the effect from its host object when the host disappears.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `detach` | boolean | If the effect should automatically detach from the host or not. |

<a id="sethost"></a>
### setHost(Interactable, string?) {#sethost-interactable-string-optional}

``` { .lua .api-signature }
effect:setHost( Interactable, boneName? )
```

Sets a [Interactable](Interactable.md) as host for an effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `Interactable` | [Interactable](Interactable.md) | The Interactable the effect is attached to. |
| `boneName` *(optional)* | string | The bone name to attach effect to. (Defaults to not attached to a bone) (Optional) |

### setHost(Shape, string?) {#sethost-shape-string-optional}

``` { .lua .api-signature }
effect:setHost( shape, boneName? )
```

Sets a [Shape](Shape.md) as host for an effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `shape` | [Shape](Shape.md) | The shape the effect is attached to. |
| `boneName` *(optional)* | string | The bone name to attach effect to. (Defaults to not attached to a bone) (Optional) |

### setHost(Character, string?) {#sethost-character-string-optional}

``` { .lua .api-signature }
effect:setHost( Character, boneName? )
```

Sets a [Character](Character.md) as host for an effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `Character` | [Character](Character.md) | The Character the effect is attached to. |
| `boneName` *(optional)* | string | The bone name to attach effect to. (Defaults to not attached to a bone) (Optional) |

### setHost(Harvestable, string?) {#sethost-harvestable-string-optional}

``` { .lua .api-signature }
effect:setHost( pHarvestable, boneName? )
```

Sets a [Harvestable](Harvestable.md) as host for an effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `pHarvestable` | [Harvestable](Harvestable.md) | The pHarvestable the effect is attached to. |
| `boneName` *(optional)* | string | The bone name to attach effect to. (Defaults to not attached to a bone) (Optional) |

### setHostAxisIgnore {#sethostaxisignore}

``` { .lua .api-signature }
effect:setHostAxisIgnore( axis )
```

Sets a rotation axis which hosted effects will ignore.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `axis` | integer | The rotation axis. |

### setOffsetPosition {#setoffsetposition}

``` { .lua .api-signature }
effect:setOffsetPosition( offsetPosition )
```

Offsets the position of the effect relatively to the host.

> **Note:**
> Does not work if the effect was created without a host.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `offsetPosition` | [Vec3](Vec3.md) | The relative offset position. |

### setOffsetRotation {#setoffsetrotation}

``` { .lua .api-signature }
effect:setOffsetRotation( offsetRotation )
```

Offsets the orientation of the effect relatively to the host.

> **Note:**
> Does not work if the effect was created without a host.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `offsetRotation` | [Quat](Quat.md) | The relative offset rotation. |

### setParameter {#setparameter}

``` { .lua .api-signature }
effect:setParameter( name, value )
```

Sets a named parameter value on the effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `name` | string | The name. |
| `value` | any | The effect parameter value. |

### setPosition {#setposition}

``` { .lua .api-signature }
effect:setPosition( position )
```

Sets the position of an effect.

> **Note:**
> Does not work if the effect has a host.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `position` | [Vec3](Vec3.md) | The position. |

### setRotation {#setrotation}

``` { .lua .api-signature }
effect:setRotation( rotation )
```

Sets the orientation of an effect using a quaternion.

> **Note:**
> Does not work if the effect has a host.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `rotation` | [Quat](Quat.md) | The rotation. |

### setScale {#setscale}

``` { .lua .api-signature }
effect:setScale( scale )
```

Sets the scale of an effect.

> **Note:**
> Only applies to effect renderables.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `scale` | [Vec3](Vec3.md) | The scale. |

### setStartStopDistance {#setstartstopdistance}

``` { .lua .api-signature }
effect:setStartStopDistance( startDistance, stopDistance )
```

Sets an effect to stop and restart depending on distance to the player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `startDistance` | number | The distance when effect will start |
| `stopDistance` | number | The distance when effect will stop |

### setTimeOfDay {#settimeofday}

``` { .lua .api-signature }
effect:setTimeOfDay( enabled, start, end, inversed )
```

Sets an effect to be active during specific period of the day / night cycle.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `enabled` | boolean | Time of day enabled. |
| `start` | number | Start normalized time of day. |
| `end` | number | End normalized time of day. |
| `inversed` | boolean | If true, period between start-end becomes inactive time. |

### setVelocity {#setvelocity}

``` { .lua .api-signature }
effect:setVelocity( velocity )
```

Sets the velocity of an effect. The effect will move along at the set velocity until it receives a new position.

> **Note:**
> Does not work if the effect has a host.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `velocity` | [Vec3](Vec3.md) | The velocity. |

### setWorld {#setworld}

``` { .lua .api-signature }
effect:setWorld( world )
```

Sets the world for an effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `world` | [World](World.md) | The world. Defaults to world from script context. (optional) |

### setWorldAny {#setworldany}

``` { .lua .api-signature }
effect:setWorldAny(  )
```

Sets the effect's world to UWorldId_Any, used to play global sounds through the dialog manager.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

### start {#start}

``` { .lua .api-signature }
effect:start( startTime? )
```

Starts playing an effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
| `startTime` *(optional)* | number | The start time of the effect. Only applies to audio and cinematic effects. (Defaults to 0) |

### stop {#stop}

``` { .lua .api-signature }
effect:stop(  )
```

Stops playing an effect

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

### stopBreakSustain {#stopbreaksustain}

``` { .lua .api-signature }
effect:stopBreakSustain(  )
```

Stops playing an effect, letting sound finish before destroying the effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |

### stopImmediate {#stopimmediate}

``` { .lua .api-signature }
effect:stopImmediate(  )
```

Immediately stop playing an effect, sound effects ended immediately.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `effect` | [Effect](Effect.md) | The effect. |
