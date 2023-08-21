# Untitled string in Schema for SigMF Meta Files Schema

```txt
#/properties/global/properties/core%3Alicense#/properties/global/properties/core:license
```

A URL for the license document under which the Recording is offered. (RFC 3986)

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../sigmf.schema.json "open original schema") |

## core:license Type

`string`

## core:license Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

## core:license Examples

```json
"https://creativecommons.org/licenses/by-sa/4.0/"
```
