# sm.ai

AI utility functions.

## Functions

### directPathAvailable {#directpathavailable}

``` { .lua .api-signature }
sm.ai.directPathAvailable( unit, position, range )
```

Check if the unit can reach the target position by moving straight.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](../Userdata/Unit.md) | The unit. |
| `position` | [Vec3](../Userdata/Vec3.md) | The target position. |
| `range` | number | The maximum allowed distance to target position. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the position is available directly. |

<a id="getaimposition"></a>
### getAimPosition(Character, Harvestable, number, number) {#getaimposition-character-harvestable-number-number}

``` { .lua .api-signature }
sm.ai.getAimPosition( self, target, range, width )
```

Returns true if the character can fire at the target harvestable within a given fire lane.

Also returns the aim position that allows the character to succeed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | [Character](../Userdata/Character.md) | The firing character. |
| `target` | [Harvestable](../Userdata/Harvestable.md) | The target harvestable. |
| `range` | number | The maximum firing distance. |
| `width` | number | The width of the fire lane. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean,[Vec3](../Userdata/Vec3.md) | The result. |

### getAimPosition(Character, Character, number, number, integer) {#getaimposition-character-character-number-number-integer}

``` { .lua .api-signature }
sm.ai.getAimPosition( self, target, range, width, attack )
```

Returns true if the character can fire at the target character within a given fire lane.

Also returns the aim position that allows the character to succeed.

Any obstacle shape that blocks the target, but can be destroyed by the projectile, will be targeted instead.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | [Character](../Userdata/Character.md) | The firing character. |
| `target` | [Character](../Userdata/Character.md) | The target character. |
| `range` | number | The maximum firing distance. |
| `width` | number | The width of the fire lane. |
| `attack` | integer | The attack level of the projectile. (Defaults to 5) |

**Returns:**

| Type | Description |
| --- | --- |
| boolean,[Vec3](../Userdata/Vec3.md) | The result. |

### getBreachablePosition {#getbreachableposition}

``` { .lua .api-signature }
sm.ai.getBreachablePosition( unit, position, range, attack )
```

Check if there's an attackable object between the unit and a position.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](../Userdata/Unit.md) | The unit. |
| `position` | [Vec3](../Userdata/Vec3.md) | The target position. |
| `range` | number | The distance. |
| `attack` | integer | The possible attack level from the breacher. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean,[Vec3](../Userdata/Vec3.md),[Shape](../Userdata/Shape.md) | Returns true if a breachable object is found, an attackable position, and an attackable shape. |
| boolean,[Vec3](../Userdata/Vec3.md),[Harvestable](../Userdata/Harvestable.md) | Returns true if a breachable object is found, an attackable position, and an attackable harvestable. |
| boolean,[Vec3](../Userdata/Vec3.md),[Lift](../Userdata/Lift.md) | Returns true if a breachable object is found, an attackable position, and an attackable lift. |
| boolean,[Vec3](../Userdata/Vec3.md) | Returns false if the object is unbreachable and an attackable position. |
| boolean | Returns true when nothing is found. |

### getClosestTree {#getclosesttree}

``` { .lua .api-signature }
sm.ai.getClosestTree( position, world? )
```

Find the closest harvestable of 'tree' type in a world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | The world position to search around. |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to search in. (Defaults to the world of the script that is calling the function) |

**Returns:**

| Type | Description |
| --- | --- |
| [Harvestable](../Userdata/Harvestable.md) | The closest tree harvestable. |

### getClosestVisibleCharacterType {#getclosestvisiblecharactertype}

``` { .lua .api-signature }
sm.ai.getClosestVisibleCharacterType( unit, uuid )
```

Returns the character of a given uuid type that is closest to the unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](../Userdata/Unit.md) | The unit. |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The character uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| [Character](../Userdata/Character.md) | The character. |

### getClosestVisibleCrop {#getclosestvisiblecrop}

``` { .lua .api-signature }
sm.ai.getClosestVisibleCrop( unit )
```

Returns the farming harvestable that is closest to the unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](../Userdata/Unit.md) | The unit. |

**Returns:**

| Type | Description |
| --- | --- |
| [Harvestable](../Userdata/Harvestable.md) | The harvestable. |

### getClosestVisiblePlayerCharacter {#getclosestvisibleplayercharacter}

``` { .lua .api-signature }
sm.ai.getClosestVisiblePlayerCharacter( unit )
```

Returns the character closest to the unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](../Userdata/Unit.md) | The unit. |

**Returns:**

| Type | Description |
| --- | --- |
| [Character](../Userdata/Character.md) | The character. |

### getClosestVisibleTeamOpponent {#getclosestvisibleteamopponent}

``` { .lua .api-signature }
sm.ai.getClosestVisibleTeamOpponent( unit, color )
```

Returns the character, with an opposing color, closest to the unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](../Userdata/Unit.md) | The unit. |
| `color` | [Color](../Userdata/Color.md) | The color. |

**Returns:**

| Type | Description |
| --- | --- |
| [Character](../Userdata/Character.md) | The character. |

### getRandomCreationPosition {#getrandomcreationposition}

``` { .lua .api-signature }
sm.ai.getRandomCreationPosition( body )
```

eturns a random position on a given body.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](../Userdata/Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The position. |

### isReachable {#isreachable}

``` { .lua .api-signature }
sm.ai.isReachable( unit, position )
```

Check if the unit can reach the target position by moving along a path.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](../Userdata/Unit.md) | The unit. |
| `position` | [Vec3](../Userdata/Vec3.md) | The target position. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the position is reachable. |
