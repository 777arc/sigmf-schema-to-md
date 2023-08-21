# Untitled integer in Schema for SigMF Meta Files Schema

```txt
#/properties/global/properties/core%3Atrailing_bytes#/properties/global/properties/core:trailing_bytes
```

The number of bytes to ignore at the end of a Non-Conforming Dataset file.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../out/sigmf.schema.json "open original schema") |

## core:trailing\_bytes Type

`integer`

## core:trailing\_bytes Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum (exclusive)**: the value of this number must be greater than: `0`
