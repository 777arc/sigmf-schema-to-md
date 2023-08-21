# Untitled string in Schema for SigMF Meta Files Schema

```txt
#/properties/global/properties/core%3Asha512#/properties/global/properties/core:sha512
```

The SHA512 hash of the Dataset file associated with the SigMF file.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../sigmf.schema.json "open original schema") |

## core:sha512 Type

`string`

## core:sha512 Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9a-fA-F]{128}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9a-fA-F%5D%7B128%7D%24 "try regular expression with regexr.com")
