# sm.joint

**Associated type:** [Joint](../Userdata/Joint.md)

A <strong>joint</strong> is a part that can be built by a player that is used to connect [bodies](../Userdata/Body.md). There are multiple scriptable joint types:

- The <strong>bearing</strong> allows two bodies to revolve freely around each other. (See [Interactable.getBearings](../Userdata/Interactable.md#getbearings))
- The <strong>piston</strong> extends and contracts to change the distance between two bodies. (See [Interactable.getPistons](../Userdata/Interactable.md#getpistons))

## Constants

### types {#types}

| Value | Description |
| --- | --- |
| "bearing" | A bearing part. |
| "spring" | A spring part. |
| "piston" | A piston part. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The type list. |
