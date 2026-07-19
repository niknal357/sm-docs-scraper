# sm.particle

The <strong>particle</strong> api allows you to create particle effects at a position.

If you require more control or complexity, please see the [effect](sm.effect.md) api.

## Client-only

### createParticle {#createparticle}

``` { .lua .api-signature }
sm.particle.createParticle( particle, position, rotation?, color? )
```

Create a particle effect at a given position and rotation.

> **Note:**
> If you start a looping particle effect through this method then the only way to get rid of it is by reloading the save.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `particle` | string | The particle name. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation. (Defaults to no rotation) |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The blend color. (Defaults to white) |
