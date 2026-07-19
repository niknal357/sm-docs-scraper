# sm.effect

**Associated type:** [Effect](../Userdata/Effect.md)

The <strong>effect</strong> api handles the creation and playing of audio and visual effects.

Effects can consist of multiple components each being of separate types and with unique offsets, rotations and delays.

For more information on how to setup effects please take a look in the Effects/Database/EffectSets folder in the game data.

## Constants

### axis {#axis}

Rotation axis removal types for hosted effects. Not combinable

| Value |
| --- |
| xaxis |
| yaxis |
| zaxis |
| all |
| none |

**Returns:**

| Type | Description |
| --- | --- |
| table | The rotation axis removal list. |

## Server + Client

### playEffect {#playeffect}

``` { .lua .api-signature }
sm.effect.playEffect(
    name,
    position?,
    velocity?,
    rotation?,
    scale?,
    parameters?,
    startTime?,
    world?
)
```

Plays an effect. If this function is called on the server it will play the effect on all clients.

> **Note:**
> If you start a looping effect using this function you will not be able to stop it.<br>Please use [createEffect](#createeffect) for looping effects.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name. |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The position. (Defaults to [0,0,0]) |
| `velocity` *(optional)* | [Vec3](../Userdata/Vec3.md) | The velocity. (Defaults to no velocity) |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation. (Defaults to no rotation) |
| `scale` *(optional)* | [Vec3](../Userdata/Vec3.md) | The scale. (Defaults to no scale, only applied to renderables) |
| `parameters` *(optional)* | table | The table containing the parameters for the effect. (Defaults to no parameters) |
| `startTime` *(optional)* | number | The initial time progression of the effect. Can be used to fast forward some effect parts. Can be used to delay effect part activation if negative. |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to play the effect in. (Defaults to [World](../Userdata/World.md) from script context) |

## Client-only

<a id="createeffect"></a>
### createEffect(string) {#createeffect-string}

``` { .lua .api-signature }
sm.effect.createEffect( name )
```

Creates an effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name. |

**Returns:**

| Type | Description |
| --- | --- |
| [Effect](../Userdata/Effect.md) | The created effect. |

### createEffect(string, Interactable, string?, integer?) {#createeffect-string-interactable-string-optional-integer-optional}

``` { .lua .api-signature }
sm.effect.createEffect( name, interactable, boneName?, axis? )
```

Creates an effect.

If you provide a host interactable to the effect then it will fetch position, velocity and orientation data from the interactable instead of relying on this information being fed to it.

This results in far more accurate positioning of effects that are supposed to stay attached to an object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name. |
| `interactable` | [Interactable](../Userdata/Interactable.md) | The interactable the effect is attached to. |
| `boneName` *(optional)* | string | Bone name to attach effect to. (Defaults to not attached to a bone) (Optional) |
| `axis` *(optional)* | integer | The axis of which the effect will ignore the hosts rotation around. (Defaults to [sm.effect.axis.none](#axis)) (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [Effect](../Userdata/Effect.md) | The created effect. |

### createEffect(string, Shape, string?, integer?) {#createeffect-string-shape-string-optional-integer-optional}

``` { .lua .api-signature }
sm.effect.createEffect( name, shape, boneName?, axis? )
```

Creates an effect.

If you provide a host shape to the effect then it will fetch position, velocity and orientation data from the shape instead of relying on this information being fed to it.

This results in far more accurate positioning of effects that are supposed to stay attached to an object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name. |
| `shape` | [Shape](../Userdata/Shape.md) | The shape the effect is attached to. |
| `boneName` *(optional)* | string | Bone name to attach effect to. (Defaults to not attached to a bone) (Optional) |
| `axis` *(optional)* | integer | The axis of which the effect will ignore the hosts rotation around. (Defaults to [sm.effect.axis.none](#axis)) (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [Effect](../Userdata/Effect.md) | The created effect. |

### createEffect(string, Harvestable, integer?) {#createeffect-string-harvestable-integer-optional}

``` { .lua .api-signature }
sm.effect.createEffect( name, harvestable, axis? )
```

Creates an effect.

If you provide a host harvestable to the effect then it will fetch position, velocity and orientation data from the harvestable instead of relying on this information being fed to it.

This results in far more accurate positioning of effects that are supposed to stay attached to an object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name. |
| `harvestable` | [Harvestable](../Userdata/Harvestable.md) | The harvestable the effect is attached to. |
| `axis` *(optional)* | integer | The axis of which the effect will ignore the hosts rotation around. (Defaults to [sm.effect.axis.none](#axis)) (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [Effect](../Userdata/Effect.md) | The created effect. |

### createEffect(string, Character, string?, integer?) {#createeffect-string-character-string-optional-integer-optional}

``` { .lua .api-signature }
sm.effect.createEffect( name, character, boneName?, axis? )
```

Creates an effect.

If you provide a host character to the effect then it will fetch position, velocity and orientation data from the character instead of relying on this information being fed to it.

This results in far more accurate positioning of effects that are supposed to stay attached to an object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name. |
| `character` | [Character](../Userdata/Character.md) | The character the effect is attached to. |
| `boneName` *(optional)* | string | Bone name to attach effect to. (Defaults to not attached to a bone) (Optional) |
| `axis` *(optional)* | integer | The axis of which the effect will ignore the hosts rotation around. (Defaults to [sm.effect.axis.none](#axis)) (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [Effect](../Userdata/Effect.md) | The created effect. |

### createEffect2D {#createeffect2d}

``` { .lua .api-signature }
sm.effect.createEffect2D( name )
```

Creates an 2d effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name of the effect. |

**Returns:**

| Type | Description |
| --- | --- |
| [Effect](../Userdata/Effect.md) | The created effect. |

### createEffectFirstPerson {#createeffectfirstperson}

``` { .lua .api-signature }
sm.effect.createEffectFirstPerson( name )
```

Creates an effect that is only visible in the first person scene.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name of the effect. |

**Returns:**

| Type | Description |
| --- | --- |
| [Effect](../Userdata/Effect.md) | The created effect. |

### createEffectSky {#createeffectsky}

``` { .lua .api-signature }
sm.effect.createEffectSky( name )
```

Creates an Sky effect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name of the effect. |

**Returns:**

| Type | Description |
| --- | --- |
| [Effect](../Userdata/Effect.md) | The created effect. |

### estimateSize {#estimatesize}

``` { .lua .api-signature }
sm.effect.estimateSize( name, parameters )
```

Estimates the radius of influence for an effect and instance parameters

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name of the effect. |
| `parameters` | table | Table of params |

**Returns:**

| Type | Description |
| --- | --- |
| number | The Range |

<a id="playhostedeffect"></a>
### playHostedEffect(string, Interactable, string?, table?, integer?, number?, Vec3?, Quat?, Vec3?) {#playhostedeffect-string-interactable-string-optional-table-optional-integer-optional-number-optional-vec3-optional-quat-optional-vec3-optional}

``` { .lua .api-signature }
sm.effect.playHostedEffect(
    name,
    interactable,
    boneName?,
    parameters?,
    axis?,
    startTime?,
    offsetPosition?,
    offsetRotation?,
    scale?
)
```

Plays an effect. It will fetch position, velocity and orientation data from the host interactable.

> **Note:**
> If you start a looping effect using this function you will not be able to stop it.<br>Please use [createEffect](#createeffect) for looping effects

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The effect name. |
| `interactable` | [Interactable](../Userdata/Interactable.md) | The interactable the effect is attached to. |
| `boneName` *(optional)* | string | The bone name. (Optional) |
| `parameters` *(optional)* | table | The table containing the parameters for the effect. (Optional) |
| `axis` *(optional)* | integer | The axis of which the effect will ignore the hosts rotation around. (Defaults to [sm.effect.axis.none](#axis)) (Optional) |
| `startTime` *(optional)* | number | The initial time progression of the effect. Can be used to fast forward some effect parts. Can be used to delay effect part activation if negative. |
| `offsetPosition` *(optional)* | [Vec3](../Userdata/Vec3.md) | The host object relative offset position. (Defaults to sm.vec3.zero()) |
| `offsetRotation` *(optional)* | [Quat](../Userdata/Quat.md) | The host object relative offset rotation. (Defaults to sm.quat.identity()) |
| `scale` *(optional)* | [Vec3](../Userdata/Vec3.md) | The scale, only applied to renderables. (Defaults to sm.vec3.one()) |

### playHostedEffect(string, Shape, string?, table?, integer?, number?, Vec3?, Quat?, Vec3?) {#playhostedeffect-string-shape-string-optional-table-optional-integer-optional-number-optional-vec3-optional-quat-optional-vec3-optional}

``` { .lua .api-signature }
sm.effect.playHostedEffect(
    name,
    shape,
    boneName?,
    parameters?,
    axis?,
    startTime?,
    offsetPosition?,
    offsetRotation?,
    scale?
)
```

Plays an effect. It will fetch position, velocity and orientation data from the host shape.

> **Note:**
> If you start a looping effect using this function you will not be able to stop it.<br>Please use [createEffect](#createeffect) for looping effects

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The effect name. |
| `shape` | [Shape](../Userdata/Shape.md) | The shape the effect is attached to. |
| `boneName` *(optional)* | string | The bone name. (Optional) |
| `parameters` *(optional)* | table | The table containing the parameters for the effect. (Optional) |
| `axis` *(optional)* | integer | The axis of which the effect will ignore the hosts rotation around. (Defaults to [sm.effect.axis.none](#axis)) (Optional) |
| `startTime` *(optional)* | number | The initial time progression of the effect. Can be used to fast forward some effect parts. Can be used to delay effect part activation if negative. |
| `offsetPosition` *(optional)* | [Vec3](../Userdata/Vec3.md) | The host object relative offset position. (Defaults to sm.vec3.zero()) |
| `offsetRotation` *(optional)* | [Quat](../Userdata/Quat.md) | The host object relative offset rotation. (Defaults to sm.quat.identity()) |
| `scale` *(optional)* | [Vec3](../Userdata/Vec3.md) | The scale, only applied to renderables. (Defaults to sm.vec3.one()) |

### playHostedEffect(string, Harvestable, string?, table?, integer?, number?, Vec3?, Quat?, Vec3?) {#playhostedeffect-string-harvestable-string-optional-table-optional-integer-optional-number-optional-vec3-optional-quat-optional-vec3-optional}

``` { .lua .api-signature }
sm.effect.playHostedEffect(
    name,
    harvestable,
    boneName?,
    parameters?,
    axis?,
    startTime?,
    offsetPosition?,
    offsetRotation?,
    scale?
)
```

Plays an effect. It will fetch position, velocity and orientation data from the host harvestable.

> **Note:**
> If you start a looping effect using this function you will not be able to stop it.<br>Please use [createEffect](#createeffect) for looping effects

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The effect name. |
| `harvestable` | [Harvestable](../Userdata/Harvestable.md) | The harvestable the effect is attached to. |
| `boneName` *(optional)* | string | The bone name. (Optional) |
| `parameters` *(optional)* | table | The table containing the parameters for the effect. (Optional) |
| `axis` *(optional)* | integer | The axis of which the effect will ignore the hosts rotation around. (Defaults to [sm.effect.axis.none](#axis)) (Optional) |
| `startTime` *(optional)* | number | The initial time progression of the effect. Can be used to fast forward some effect parts. Can be used to delay effect part activation if negative. |
| `offsetPosition` *(optional)* | [Vec3](../Userdata/Vec3.md) | The host object relative offset position. (Defaults to sm.vec3.zero()) |
| `offsetRotation` *(optional)* | [Quat](../Userdata/Quat.md) | The host object relative offset rotation. (Defaults to sm.quat.identity()) |
| `scale` *(optional)* | [Vec3](../Userdata/Vec3.md) | The scale, only applied to renderables. (Defaults to sm.vec3.one()) |

### playHostedEffect(string, Character, string?, table?, integer?, number?, Vec3?, Quat?, Vec3?) {#playhostedeffect-string-character-string-optional-table-optional-integer-optional-number-optional-vec3-optional-quat-optional-vec3-optional}

``` { .lua .api-signature }
sm.effect.playHostedEffect(
    name,
    character,
    boneName?,
    parameters?,
    axis?,
    startTime?,
    offsetPosition?,
    offsetRotation?,
    scale?
)
```

Plays an effect. It will fetch position, velocity and orientation data from the host character.

> **Note:**
> If you start a looping effect using this function you will not be able to stop it.<br>Please use [createEffect](#createeffect) for looping effects

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The effect name. |
| `character` | [Character](../Userdata/Character.md) | The character the effect is attached to. |
| `boneName` *(optional)* | string | The bone name. (Optional) |
| `parameters` *(optional)* | table | The table containing the parameters for the effect. (Optional) |
| `axis` *(optional)* | integer | The axis of which the effect will ignore the hosts rotation around. (Defaults to [sm.effect.axis.none](#axis)) (Optional) |
| `startTime` *(optional)* | number | The initial time progression of the effect. Can be used to fast forward some effect parts. Can be used to delay effect part activation if negative. |
| `offsetPosition` *(optional)* | [Vec3](../Userdata/Vec3.md) | The host object relative offset position. (Defaults to sm.vec3.zero()) |
| `offsetRotation` *(optional)* | [Quat](../Userdata/Quat.md) | The host object relative offset rotation. (Defaults to sm.quat.identity()) |
| `scale` *(optional)* | [Vec3](../Userdata/Vec3.md) | The scale, only applied to renderables. (Defaults to sm.vec3.one()) |
