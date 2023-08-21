# Untitled string in Schema for SigMF Meta Files Schema

```txt
#/properties/global/properties/core%3Adataset#/properties/global/properties/core:dataset
```

The full filename of the Dataset file this Metadata file describes.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../sigmf.schema.json "open original schema") |

## core:dataset Type

`string`

## core:dataset Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^\/\\:*?"<>|]+(\.[^\/\\:*?"<>|]+)*$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%5C%2F%5C%5C%3A*%3F%22%3C%3E%7C%5D%2B\(%5C.%5B%5E%5C%2F%5C%5C%3A*%3F%22%3C%3E%7C%5D%2B\)*%24 "try regular expression with regexr.com")
