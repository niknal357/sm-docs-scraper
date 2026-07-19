# sm.construction

The <strong>Construction</strong> api is used for interacting with the shape construction system. 

## Constants

### constants {#constants}

Constants used by the construction system.

- <strong>subdivideRatio</strong> &ndash; The physical size of one block.
- <strong>subdivideRatio_2</strong> &ndash; The physical size of one block divided by two.
- <strong>subdivisions</strong> &ndash; One dividided by subdivideRatio.
- <strong>shapeSpacing</strong> &ndash; Bias value.

| Value | Description |
| --- | --- |
| subdivideRatio | 0.25 |
| subdivideRatio_2 | 0.125 |
| subdivisions | 4 |
| shapeSpacing | 0.004 |

**Returns:**

| Type | Description |
| --- | --- |
| table |  |

## Server + Client

<a id="validatelocalposition"></a>
### validateLocalPosition(Uuid, Vec3, Vec3, Shape) {#validatelocalposition-uuid-vec3-vec3-shape}

``` { .lua .api-signature }
sm.construction.validateLocalPosition( uuid, localPosition, localNormal, shape )
```

Validates if a shape can be built on another shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the shape to validate. |
| `localPosition` | [Vec3](../Userdata/Vec3.md) | The position local to the body. |
| `localNormal` | [Vec3](../Userdata/Vec3.md) | The normal of the surface to validate placement. |
| `shape` | [Shape](../Userdata/Shape.md) | The shape to build on. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if position is valid. |

### validateLocalPosition(Uuid, Vec3, Vec3, Joint) {#validatelocalposition-uuid-vec3-vec3-joint}

``` { .lua .api-signature }
sm.construction.validateLocalPosition( uuid, localPosition, localNormal, joint )
```

Validates if a shape can be built on another joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the shape to validate. |
| `localPosition` | [Vec3](../Userdata/Vec3.md) | The position local to the body. |
| `localNormal` | [Vec3](../Userdata/Vec3.md) | The normal of the surface to validate placement. |
| `joint` | [Joint](../Userdata/Joint.md) | The joint to build on. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if position is valid. |

### validateLocalPosition(Uuid, Vec3, Vec3) {#validatelocalposition-uuid-vec3-vec3}

``` { .lua .api-signature }
sm.construction.validateLocalPosition( uuid, localPosition, localNormal )
```

Validates if a shape can be built on terrain.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the shape to validate. |
| `localPosition` | [Vec3](../Userdata/Vec3.md) | The position local to the body. |
| `localNormal` | [Vec3](../Userdata/Vec3.md) | The normal of the surface to validate placement. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if position is valid. |

## Server-only

<a id="buildblock"></a>
### buildBlock(Uuid, Vec3, Shape) {#buildblock-uuid-vec3-shape}

``` { .lua .api-signature }
sm.construction.buildBlock( uuid, localPosition, shape )
```

Builds a block on a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the block to build. |
| `localPosition` | [Vec3](../Userdata/Vec3.md) | The position to build the block on. |
| `shape` | [Shape](../Userdata/Shape.md) | The shape to build on. |

### buildBlock(Uuid, Vec3, Joint) {#buildblock-uuid-vec3-joint}

``` { .lua .api-signature }
sm.construction.buildBlock( uuid, localPosition, joint )
```

Builds a block on a joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the block to build. |
| `localPosition` | [Vec3](../Userdata/Vec3.md) | The position to build the block on. |
| `joint` | [Joint](../Userdata/Joint.md) | The joint to build on. |

### buildBlock(Uuid, Vec3, Lift) {#buildblock-uuid-vec3-lift}

``` { .lua .api-signature }
sm.construction.buildBlock( uuid, localPosition, lift )
```

Builds a block a lift.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the block to build. |
| `localPosition` | [Vec3](../Userdata/Vec3.md) | The position to build the block on. |
| `lift` | [Lift](../Userdata/Lift.md) | The lift to build on. |

### buildBlock(Uuid, Vec3) {#buildblock-uuid-vec3}

``` { .lua .api-signature }
sm.construction.buildBlock( uuid, localPosition )
```

Builds a block on terrain.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the block to build. |
| `localPosition` | [Vec3](../Userdata/Vec3.md) | The position to build the block on. |
