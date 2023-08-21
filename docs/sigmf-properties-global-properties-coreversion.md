# Untitled string in Schema for SigMF Meta Files Schema

```txt
#/properties/global/properties/core%3Aversion#/properties/global/properties/core:version
```

The SHA512 hash of the Dataset file associated with the SigMF file.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../sigmf.schema.json "open original schema") |

## core:version Type

`string`

## core:version Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"1.0.0"` |             |

## core:version Default Value

The default value is:

```json
"1.0.0"
```
