# sm.interactable

**Associated type:** [Interactable](../Userdata/Interactable.md)

## Constants

### actions {#actions}

Actions are used to specify what inputs types an [Interactable](../Userdata/Interactable.md) is able to detect.

**Returns:**

| Type | Description |
| --- | --- |
| table | The filter type list. |

### connectionType {#connectiontype}

<h3>Logic</h3>

The interactable sends or reads a boolean signal to signal it's current state. ([isActive](../Userdata/Interactable.md#isactive)) to signal its output.

In: The interactable reads a boolean ([isActive](../Userdata/Interactable.md#isactive)) from its parent as input.

<h3>Power</h3>

Out: The controller uses a float ([getPower](../Userdata/Interactable.md#getpower)) to signal strength output (steering only).

In: The controller reads a float ([getPower](../Userdata/Interactable.md#getpower)) from its parent as input for strength.

| Value | Description |
| --- | --- |
| none | 0 |
| logic | 1 |
| power | 2 |
| bearing | 4 |
| seated | 8 |
| piston | 16 |
| gasoline | 256 |
| electricity | 512 |
| water | 1024 |
| ammo | 2048 |
| chemical | 4096 |

**Returns:**

| Type | Description |
| --- | --- |
| table | The connection type list. |

### steering {#steering}

Flags to be used with the steering component.

**Returns:**

| Type | Description |
| --- | --- |
| table | The flag list. |

### types {#types}

| Value |
| --- |
| "electricEngine" |
| "gasEngine" |
| "steering" |
| "seat" |
| "controller" |
| "button" |
| "lever" |
| "sensor" |
| "thruster" |
| "radio" |
| "horn" |
| "tone" |
| "logic" |
| "timer" |
| "particlePreview" |
| "spring" |
| "pointLight" |
| "spotLight" |
| "chest" |
| "scripted" |
| "piston" |
| "simpleInteractive" |

**Returns:**

| Type | Description |
| --- | --- |
| table | The type list. |
