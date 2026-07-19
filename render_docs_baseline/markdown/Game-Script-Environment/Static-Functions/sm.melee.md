# sm.melee

Information about melee attacks are located in `/Data/Melee/attacks.json`.

## Functions

### getMeleeAttackHits {#getmeleeattackhits}

``` { .lua .api-signature }
sm.melee.getMeleeAttackHits( uuid, origin, directionRange, source )
```

Performs melee attack check and returns a table of raycast results.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the melee attack. |
| `origin` | [Vec3](../Userdata/Vec3.md) | The source position of the attack. |
| `directionRange` | [Vec3](../Userdata/Vec3.md) | The direction and reach of the attack. |
| `source` | [Unit](../Userdata/Unit.md) | The unit that is the source of the attack. |

**Returns:**

| Type | Description |
| --- | --- |
| table | RaycastResult		A table containing [RaycastResult](../Userdata/RaycastResult.md) data. |

<a id="meleeattack"></a>
### meleeAttack(string, integer, Vec3, Vec3, Player, integer?, number?, table) {#meleeattack-string-integer-vec3-vec3-player-integer-optional-number-optional-table}

``` { .lua .api-signature }
sm.melee.meleeAttack(
    name,
    damage,
    origin,
    directionRange,
    source,
    delay?,
    power?,
    ignoreCharacters
)
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Perform a melee attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name of the melee attack. |
| `damage` | integer | The damage the attack will inflict. |
| `origin` | [Vec3](../Userdata/Vec3.md) | The source position of the attack. |
| `directionRange` | [Vec3](../Userdata/Vec3.md) | The direction and reach of the attack. |
| `source` | [Player](../Userdata/Player.md) | The player that is the source of the attack. |
| `delay` *(optional)* | integer | The number of ticks before performing the attack. (Defaults to 0) |
| `power` *(optional)* | number | The strength of the knockback power. (Defaults to 5000) |
| `ignoreCharacters` | table | A table of characters to ignore in the attack. (optional) |

### meleeAttack(string, integer, Vec3, Vec3, Unit, integer?, number?, table) {#meleeattack-string-integer-vec3-vec3-unit-integer-optional-number-optional-table}

``` { .lua .api-signature }
sm.melee.meleeAttack(
    name,
    damage,
    origin,
    directionRange,
    source,
    delay?,
    power?,
    ignoreCharacters
)
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Perform a melee attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name of the melee attack. |
| `damage` | integer | The damage the attack will inflict. |
| `origin` | [Vec3](../Userdata/Vec3.md) | The source position of the attack. |
| `directionRange` | [Vec3](../Userdata/Vec3.md) | The direction and reach of the attack. |
| `source` | [Unit](../Userdata/Unit.md) | The unit that is the source of the attack. |
| `delay` *(optional)* | integer | The number of ticks before performing the attack. (Defaults to 0) |
| `power` *(optional)* | number | The strength of the knockback power. (Defaults to 5000) |
| `ignoreCharacters` | table | A table of characters to ignore in the attack. (optional) |

### meleeAttack(Uuid, integer, Vec3, Vec3, Player, integer?, number?, table) {#meleeattack-uuid-integer-vec3-vec3-player-integer-optional-number-optional-table}

``` { .lua .api-signature }
sm.melee.meleeAttack(
    uuid,
    damage,
    origin,
    directionRange,
    source,
    delay?,
    power?,
    ignoreCharacters
)
```

Perform a melee attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the melee attack. |
| `damage` | integer | The damage the attack will inflict. |
| `origin` | [Vec3](../Userdata/Vec3.md) | The source position of the attack. |
| `directionRange` | [Vec3](../Userdata/Vec3.md) | The direction and reach of the attack. |
| `source` | [Player](../Userdata/Player.md) | The player that is the source of the attack. |
| `delay` *(optional)* | integer | The number of ticks before performing the attack. (Defaults to 0) |
| `power` *(optional)* | number | The strength of the knockback power. (Defaults to 5000) |
| `ignoreCharacters` | table | A table of characters to ignore in the attack. (optional) |

### meleeAttack(Uuid, integer, Vec3, Vec3, Unit, integer?, number?, table) {#meleeattack-uuid-integer-vec3-vec3-unit-integer-optional-number-optional-table}

``` { .lua .api-signature }
sm.melee.meleeAttack(
    uuid,
    damage,
    origin,
    directionRange,
    source,
    delay?,
    power?,
    ignoreCharacters
)
```

Perform a melee attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the melee attack. |
| `damage` | integer | The damage the attack will inflict. |
| `origin` | [Vec3](../Userdata/Vec3.md) | The source position of the attack. |
| `directionRange` | [Vec3](../Userdata/Vec3.md) | The direction and reach of the attack. |
| `source` | [Unit](../Userdata/Unit.md) | The unit that is the source of the attack. |
| `delay` *(optional)* | integer | The number of ticks before performing the attack. (Defaults to 0) |
| `power` *(optional)* | number | The strength of the knockback power. (Defaults to 5000) |
| `ignoreCharacters` | table | A table of characters to ignore in the attack. (optional) |
