# Untitled array in Schema for SigMF Meta Files Schema

```txt
#/properties/global/properties/core%3Aextensions#/properties/global/properties/core:extensions
```

The `core:extensions` field in the Global Object is an array of extension objects that describe SigMF extensions. Extension Objects MUST contain the three key/value pairs defined below, and MUST NOT contain any other fields.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../out/sigmf.schema.json "open original schema") |

## core:extensions Type

`object[]` ([Details](sigmf-properties-global-properties-coreextensions-items.md))

## core:extensions Default Value

The default value is:

```json
[]
```
