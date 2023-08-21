# Untitled integer in Schema for SigMF Meta Files Schema

```txt
#/properties/annotations/items/anyOf/0/properties/core%3Asample_count#/properties/annotations/items/anyOf/0/properties/core:sample_count
```

The number of samples that this Segment applies to.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../sigmf.schema.json "open original schema") |

## core:sample\_count Type

`integer`

## core:sample\_count Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum**: the value of this number must greater than or equal to: `0`
