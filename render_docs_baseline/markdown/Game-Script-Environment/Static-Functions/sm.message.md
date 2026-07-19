# sm.message

## Server-only

### send {#send}

``` { .lua .api-signature }
sm.message.send( messageKey, data? )
```

Sends a message to all script instances registered for the given key. Can only be called from server!

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `messageKey` | string | The message key. |
| `data` *(optional)* | any | Optional data to send with the message. |

### subscribe {#subscribe}

``` { .lua .api-signature }
sm.message.subscribe( messageKey, callbackName )
```

Subscribes the calling script instance to receive messages for a given key. Can only be called from server!

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `messageKey` | string | The message key to subscribe to. |
| `callbackName` | string | The name of the callback function to invoke. |
