# Untitled integer in Schema for SigMF Meta Files Schema

```txt
#/properties/captures/items/anyOf/0/properties/core%3Aglobal_index#/properties/captures/items/anyOf/0/properties/core:global_index
```

The index of the sample referenced by `sample_start` relative to an original sample stream.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../sigmf.schema.json "open original schema") |

## core:global\_index Type

`integer`

## core:global\_index Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum**: the value of this number must greater than or equal to: `0`
