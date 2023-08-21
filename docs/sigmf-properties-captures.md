# Untitled array in Schema for SigMF Meta Files Schema

```txt
#/properties/captures#/properties/captures
```

The `captures` value is an array of capture segment objects that describe the parameters of the signal capture. It MUST be sorted by the value of each capture segment's `core:sample_start` key, ascending.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../sigmf.schema.json "open original schema") |

## captures Type

`object[]` ([Details](sigmf-properties-captures-items.md))

## captures Default Value

The default value is:

```json
[]
```
