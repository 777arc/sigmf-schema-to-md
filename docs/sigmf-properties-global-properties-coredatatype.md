# Untitled string in Schema for SigMF Meta Files Schema

```txt
#/properties/global/properties/core%3Adatatype#/properties/global/properties/core:datatype
```

The SigMF Dataset format of the stored samples in the Dataset file.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../out/sigmf.schema.json "open original schema") |

## core:datatype Type

`string`

## core:datatype Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(c|r)(f32|f64|i32|i16|u32|u16|i8|u8)(_le|_be)?$
```

[try pattern](https://regexr.com/?expression=%5E\(c%7Cr\)\(f32%7Cf64%7Ci32%7Ci16%7Cu32%7Cu16%7Ci8%7Cu8\)\(_le%7C_be\)%3F%24 "try regular expression with regexr.com")

## core:datatype Default Value

The default value is:

```json
"cf32_le"
```

## core:datatype Examples

```json
"ri16_le"
```
