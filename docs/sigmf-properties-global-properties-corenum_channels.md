# Untitled integer in Schema for SigMF Meta Files Schema

```txt
#/properties/global/properties/core%3Anum_channels#/properties/global/properties/core:num_channels
```

Total number of interleaved channels in the Dataset file. If omitted, this defaults to one.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../out/sigmf.schema.json "open original schema") |

## core:num\_channels Type

`integer`

## core:num\_channels Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum**: the value of this number must greater than or equal to: `1`

## core:num\_channels Default Value

The default value is:

```json
1
```
