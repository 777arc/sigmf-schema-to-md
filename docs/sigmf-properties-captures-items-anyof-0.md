# Untitled object in Schema for SigMF Meta Files Schema

```txt
#/properties/captures/items/anyOf/0#/properties/captures/items/anyOf/0
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../sigmf.schema.json "open original schema") |

## 0 Type

`object` ([Details](sigmf-properties-captures-items-anyof-0.md))

# 0 Properties

| Property                                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                 |
| :-------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [core:datetime](#coredatetime)          | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-captures-items-anyof-0-properties-coredatetime.md "#/properties/captures/items/anyOf/0/properties/core%3Adatetime#/properties/captures/items/anyOf/0/properties/core:datetime")             |
| [core:frequency](#corefrequency)        | `number`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-captures-items-anyof-0-properties-corefrequency.md "#/properties/captures/items/anyOf/0/properties/core%3Afrequency#/properties/captures/items/anyOf/0/properties/core:frequency")          |
| [core:global\_index](#coreglobal_index) | `integer` | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-captures-items-anyof-0-properties-coreglobal_index.md "#/properties/captures/items/anyOf/0/properties/core%3Aglobal_index#/properties/captures/items/anyOf/0/properties/core:global_index") |
| [core:header\_bytes](#coreheader_bytes) | `integer` | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-captures-items-anyof-0-properties-coreheader_bytes.md "#/properties/captures/items/anyOf/0/properties/core%3Aheader_bytes#/properties/captures/items/anyOf/0/properties/core:header_bytes") |
| [core:sample\_start](#coresample_start) | `integer` | Required | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-captures-items-anyof-0-properties-coresample_start.md "#/properties/captures/items/anyOf/0/properties/core%3Asample_start#/properties/captures/items/anyOf/0/properties/core:sample_start") |
| Additional Properties                   | Any       | Optional | can be null    |                                                                                                                                                                                                                                            |

## core:datetime

An ISO-8601 string indicating the timestamp of the sample index specified by sample\_start.

`core:datetime`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-captures-items-anyof-0-properties-coredatetime.md "#/properties/captures/items/anyOf/0/properties/core%3Adatetime#/properties/captures/items/anyOf/0/properties/core:datetime")

### core:datetime Type

`string`

### core:datetime Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([\+-]?\d{4}(?!\d{2}))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$
```

[try pattern](https://regexr.com/?expression=%5E\(%5B%5C%2B-%5D%3F%5Cd%7B4%7D\(%3F!%5Cd%7B2%7D%08\)\)\(\(-%3F\)\(\(0%5B1-9%5D%7C1%5B0-2%5D\)\(%5C3\(%5B12%5D%5Cd%7C0%5B1-9%5D%7C3%5B01%5D\)\)%3F%7CW\(%5B0-4%5D%5Cd%7C5%5B0-2%5D\)\(-%3F%5B1-7%5D\)%3F%7C\(00%5B1-9%5D%7C0%5B1-9%5D%5Cd%7C%5B12%5D%5Cd%7B2%7D%7C3\(%5B0-5%5D%5Cd%7C6%5B1-6%5D\)\)\)\(%5BT%5Cs%5D\(\(\(%5B01%5D%5Cd%7C2%5B0-3%5D\)\(\(%3A%3F\)%5B0-5%5D%5Cd\)%3F%7C24%5C%3A%3F00\)\(%5B%5C.%2C%5D%5Cd%2B\(%3F!%3A\)\)%3F\)%3F\(%5C17%5B0-5%5D%5Cd\(%5B%5C.%2C%5D%5Cd%2B\)%3F\)%3F\(%5BzZ%5D%7C\(%5B%5C%2B-%5D\)\(%5B01%5D%5Cd%7C2%5B0-3%5D\)%3A%3F\(%5B0-5%5D%5Cd\)%3F\)%3F\)%3F\)%3F%24 "try regular expression with regexr.com")

### core:datetime Examples

```json
"1955-11-05T14:00:00.000Z"
```

## core:frequency

The center frequency of the signal in Hz.

`core:frequency`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-captures-items-anyof-0-properties-corefrequency.md "#/properties/captures/items/anyOf/0/properties/core%3Afrequency#/properties/captures/items/anyOf/0/properties/core:frequency")

### core:frequency Type

`number`

### core:frequency Constraints

**maximum**: the value of this number must smaller than or equal to: `1.7976931348623157e+308`

**minimum**: the value of this number must greater than or equal to: `-1.7976931348623157e+308`

## core:global\_index

The index of the sample referenced by `sample_start` relative to an original sample stream.

`core:global_index`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-captures-items-anyof-0-properties-coreglobal_index.md "#/properties/captures/items/anyOf/0/properties/core%3Aglobal_index#/properties/captures/items/anyOf/0/properties/core:global_index")

### core:global\_index Type

`integer`

### core:global\_index Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum**: the value of this number must greater than or equal to: `0`

## core:header\_bytes

The number of bytes preceding a chunk of samples that are not sample data, used for NCDs.

`core:header_bytes`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-captures-items-anyof-0-properties-coreheader_bytes.md "#/properties/captures/items/anyOf/0/properties/core%3Aheader_bytes#/properties/captures/items/anyOf/0/properties/core:header_bytes")

### core:header\_bytes Type

`integer`

### core:header\_bytes Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum**: the value of this number must greater than or equal to: `0`

## core:sample\_start

Index of first sample of this chunk.

`core:sample_start`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-captures-items-anyof-0-properties-coresample_start.md "#/properties/captures/items/anyOf/0/properties/core%3Asample_start#/properties/captures/items/anyOf/0/properties/core:sample_start")

### core:sample\_start Type

`integer`

### core:sample\_start Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum**: the value of this number must greater than or equal to: `0`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
