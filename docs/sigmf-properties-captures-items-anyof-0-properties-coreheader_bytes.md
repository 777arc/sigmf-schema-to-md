# Untitled integer in Schema for SigMF Meta Files Schema

```txt
#/properties/captures/items/anyOf/0/properties/core%3Aheader_bytes#/properties/captures/items/anyOf/0/properties/core:header_bytes
```

The number of bytes preceding a chunk of samples that are not sample data, used for NCDs.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../out/sigmf.schema.json "open original schema") |

## core:header\_bytes Type

`integer`

## core:header\_bytes Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum**: the value of this number must greater than or equal to: `0`
