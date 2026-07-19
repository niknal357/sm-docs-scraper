# Joint

**Associated namespace:** [sm.joint](../Static-Functions/sm.joint.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a <strong>joint</strong> in the game.

**Values:**

- <a id="angle"></a>`angle` [ **number** ] <br>
    - `Get`: Returns the angle of a bearing.

- <a id="angularvelocity"></a>`angularVelocity` [ **number** ] <br>
    - `Get`: Returns the angular velocity of a bearing.

        The angular velocity can be set using [setMotorVelocity](#setmotorvelocity) or [setTargetAngle](#settargetangle).

- <a id="appliedimpulse"></a>`appliedImpulse` [ **number** ] <br>
    - `Get`: Returns the applied impulse of a bearing.

        The applied impulse can be set using [setMotorVelocity](#setmotorvelocity) or [setTargetAngle](#settargetangle).

- <a id="color"></a>`color` [ **[Color](Color.md)** ] <br>
    - `Get`: Returns the color of a joint.
    - `Set`: (Server-Only) Sets the color of a joint.

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a joint.

- <a id="length"></a>`length` [ **number** ] <br>
    - `Get`: Returns the current length of a piston. The length is measured in blocks.

- <a id="localposition"></a>`localPosition` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the local position of a joint.

- <a id="localrotation"></a>`localRotation` [ **[Quat](Quat.md)** ] <br>
    - `Get`: Returns the local rotation of a joint.

- <a id="reversed"></a>`reversed` [ **boolean** ] <br>
    - `Get`: Returns whether a bearing has been reversed using the <em>Connect Tool</em>. A reversed bearing rotates counterclockwise.

- <a id="shapea"></a>`shapeA` [ **[Shape](Shape.md)** ] <br>
    - `Get`: Returns the [Shape](Shape.md) a joint is attached to. This shape does always exist.

- <a id="shapeb"></a>`shapeB` [ **[Shape](Shape.md)** ] <br>
    - `Get`: Returns the [Shape](Shape.md) that is attached to a joint on another [Body](Body.md). This method returns nil if there is no shape attached to the joint.

- <a id="shapeuuid"></a>`shapeUuid` [ **[Uuid](Uuid.md)** ] <br>
    - `Get`: Returns the uuid string unique to a joint type.

- <a id="type"></a>`type` [ **string** ] <br>
    - `Get`: Returns the joint type of a joint.

- <a id="uuid"></a>`uuid` [ **[Uuid](Uuid.md)** ] <br>
    - `Get`: Returns the uuid string unique to a joint type.

- <a id="worldposition"></a>`worldPosition` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the world position of a joint.

- <a id="xaxis"></a>`xAxis` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the local x-axis vector of a joint.

- <a id="yaxis"></a>`yAxis` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the local y-axis vector of a joint.

- <a id="zaxis"></a>`zAxis` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the local z-axis vector of a joint.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Joint == Joint` | boolean | Checks if two instances of [Joint](Joint.md) refer to the same Joint. |

## Server + Client

### getAngle {#getangle}

``` { .lua .api-signature }
joint:getAngle(  )
```

Returns the angle of a bearing.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `bearing` | [Joint](Joint.md) | The bearing. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The bearing's angle. The angle ranges between `-math.pi` and `+math.pi`. |

### getAngularVelocity {#getangularvelocity}

``` { .lua .api-signature }
joint:getAngularVelocity(  )
```

Returns the angular velocity of a bearing.

The angular velocity can be set using [setMotorVelocity](#setmotorvelocity) or [setTargetAngle](#settargetangle).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `bearing` | [Joint](Joint.md) | The bearing. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The bearing's angular velocity. |

### getAngularVelocityVector {#getangularvelocityvector}

``` { .lua .api-signature }
joint:getAngularVelocityVector(  )
```

Returns the angular velocity of a generic joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The joint's angular velocities. |

### getAppliedImpulse {#getappliedimpulse}

``` { .lua .api-signature }
joint:getAppliedImpulse(  )
```

Returns the applied impulse of a bearing.

The applied impulse can be set using [setMotorVelocity](#setmotorvelocity) or [setTargetAngle](#settargetangle).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `bearing` | [Joint](Joint.md) | The bearing. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The bearing's applied impulse. |

### getBearingEnabled {#getbearingenabled}

``` { .lua .api-signature }
joint:getBearingEnabled(  )
```

Returns whether a joint has a bearing enabled.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the joint has a bearing enabled. Springs return whether their bearing is enabled, bearings always return true, pistons always return false. |

### getBoundingBox {#getboundingbox}

``` { .lua .api-signature }
joint:getBoundingBox(  )
```

Returns the bounding box of a joint &ndash; the dimensions that a joint occupies when building.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The size of the joint's bounding box. |

### getColor {#getcolor}

``` { .lua .api-signature }
joint:getColor(  )
```

Returns the color of a joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](Color.md) | The joint's color. |

### getId {#getid}

``` { .lua .api-signature }
joint:getId(  )
```

Returns the id of a joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The joint's id. |

### getLength {#getlength}

``` { .lua .api-signature }
joint:getLength(  )
```

Returns the current length of a piston. The length is measured in blocks.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `piston` | [Joint](Joint.md) | The piston. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The piston's current length in blocks. |

### getLocalPosition {#getlocalposition}

``` { .lua .api-signature }
joint:getLocalPosition(  )
```

Returns the local position of a joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The joint's local position. |

### getLocalRotation {#getlocalrotation}

``` { .lua .api-signature }
joint:getLocalRotation(  )
```

Returns the local rotation of a joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The joint's local rotation. |

### getMultiShapeJoints {#getmultishapejoints}

``` { .lua .api-signature }
joint:getMultiShapeJoints(  )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | A Join that is part of a multishape |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of joints contained in the multishape (returns nil if joint wasn't a multishape) |

### getMultiShapeShapes {#getmultishapeshapes}

``` { .lua .api-signature }
joint:getMultiShapeShapes(  )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | A joint that is part of a multishape |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of shapes contained in the multishape (returns nil if joint wasn't a multishape) |

### getShapeA {#getshapea}

``` { .lua .api-signature }
joint:getShapeA(  )
```

Returns the [Shape](Shape.md) a joint is attached to. This shape does always exist.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Shape](Shape.md) | The joint's first shape. |

### getShapeB {#getshapeb}

``` { .lua .api-signature }
joint:getShapeB(  )
```

Returns the [Shape](Shape.md) that is attached to a joint on another [Body](Body.md). This method returns nil if there is no shape attached to the joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Shape](Shape.md) | The joint's second shape. |

### getShapeUuid {#getshapeuuid}

``` { .lua .api-signature }
joint:getShapeUuid(  )
```

Returns the uuid string unique to a joint type.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](Uuid.md) | The joint's uuid. |

### getSticky {#getsticky}

``` { .lua .api-signature }
joint:getSticky(  )
```

Returns the sticky directions of the joint for positive xyz and negative xyz.

A value of 1 means that the direction is sticky and a value of 0 means that the direction is not sticky.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md),[Vec3](Vec3.md) | The negative xyz sticky and the positive xyz sticky. |

### getType {#gettype}

``` { .lua .api-signature }
joint:getType(  )
```

Returns the joint type of a joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| string | One of the joint's type found in (sm.joint.types). |

### getWorldPosition {#getworldposition}

``` { .lua .api-signature }
joint:getWorldPosition(  )
```

Returns the world position of a joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The joint's world position. |

### getWorldRotation {#getworldrotation}

``` { .lua .api-signature }
joint:getWorldRotation(  )
```

Returns the world rotation of a joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The joint's world rotation. |

### getXAxis {#getxaxis}

``` { .lua .api-signature }
joint:getXAxis(  )
```

Returns the local x-axis vector of a joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The joint's x-axis. |

### getYAxis {#getyaxis}

``` { .lua .api-signature }
joint:getYAxis(  )
```

Returns the local y-axis vector of a joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The joint's y-axis. |

### getZAxis {#getzaxis}

``` { .lua .api-signature }
joint:getZAxis(  )
```

Returns the local z-axis vector of a joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The joint's z-axis. |

### isReversed {#isreversed}

``` { .lua .api-signature }
joint:isReversed(  )
```

Returns whether a bearing has been reversed using the <em>Connect Tool</em>. A reversed bearing rotates counterclockwise.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `bearing` | [Joint](Joint.md) | The bearing. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the bearing is reversed (rotating counterclockwise). |

### setMotorVelocity {#setmotorvelocity}

``` { .lua .api-signature }
joint:setMotorVelocity( targetVelocity, maxImpulse )
```

Sets the motor velocity for a bearing. The bearing will try to maintain the target velocity with the given amount of impulse/strength.

In Scrap Mechanic, the Gas Engine increases both velocity and impulse with every gear. The Electric Engine increases velocity, but maintains the same impulse for every gear, making it sturdier.

This method cancels the effects of [setTargetAngle](#settargetangle).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `bearing` | [Joint](Joint.md) | The bearing. |
| `targetVelocity` | number | The target velocity. |
| `maxImpulse` | number | The max impulse. |

### setTargetAngle {#settargetangle}

``` { .lua .api-signature }
joint:setTargetAngle( targetAngle, targetVelocity, maxImpulse )
```

Sets the target angle for a bearing. The bearing will try to reach the target angle with the target velocity and the given amount of impulse/strength.

The target angle is set to range between `-math.pi` and `+math.pi`. The bearing will always try to rotate in the direction closest to the target angle.

This method cancels the effects of [setMotorVelocity](#setmotorvelocity).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `bearing` | [Joint](Joint.md) | The bearing. |
| `targetAngle` | number | The target angle. |
| `targetVelocity` | number | The target velocity. |
| `maxImpulse` | number | The max impulse. |

## Server-only

### createBlock {#createblock}

``` { .lua .api-signature }
joint:createBlock( uuid, size, position, forceCreate? )
```

Create a block on joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The parent joint. |
| `uuid` | [Uuid](Uuid.md) | The uuid of the shape. |
| `size` | [Vec3](Vec3.md) | The shape's size. |
| `position` | [Vec3](Vec3.md) | The shape's local position. |
| `forceCreate` *(optional)* | boolean | Set true to force create the shape. (Defaults to true) |

### createPart {#createpart}

``` { .lua .api-signature }
joint:createPart( uuid, position, zAxis, xAxis, forceCreate? )
```

Create a part on joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The parent joint. |
| `uuid` | [Uuid](Uuid.md) | The uuid of the shape. |
| `position` | [Vec3](Vec3.md) | The shape's local position. |
| `zAxis` | [Vec3](Vec3.md) | The shape's local z direction. |
| `xAxis` | [Vec3](Vec3.md) | The shape's local x direction. |
| `forceCreate` *(optional)* | boolean | Set true to force create the shape. (Defaults to true) |

### setColor {#setcolor}

``` { .lua .api-signature }
joint:setColor( color )
```

Sets the color of a joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `joint` | [Joint](Joint.md) | The joint. |
| `color` | [Color](Color.md) | The new color. |

### setTargetLength {#settargetlength}

``` { .lua .api-signature }
joint:setTargetLength( targetLength, targetVelocity, maxImpulse? )
```

Sets the target length for a piston. The piston will try to reach the target length with the target velocity and the given amount of impulse/strength.

The target length is measured in blocks.

This method cancels the effects of [setMotorVelocity](#setmotorvelocity).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `bearing` | [Joint](Joint.md) | The bearing. |
| `targetLength` | number | The target length. |
| `targetVelocity` | number | The target velocity. |
| `maxImpulse` *(optional)* | number | The max impulse. (Defaults to impulse used in game) |
