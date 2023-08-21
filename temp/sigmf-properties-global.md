## global Type

`object` ([Details](sigmf-properties-global.md))

# global Properties

| Property                                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                       |
| :------------------------------------------ | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [core:author](#coreauthor)                  | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreauthor.md "#/properties/global/properties/core%3Aauthor#/properties/global/properties/core:author")                         |
| [core:collection](#corecollection)          | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-corecollection.md "#/properties/global/properties/core%3Acollection#/properties/global/properties/core:collection")             |
| [core:dataset](#coredataset)                | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coredataset.md "#/properties/global/properties/core%3Adataset#/properties/global/properties/core:dataset")                      |
| [core:data\_doi](#coredata_doi)             | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coredata_doi.md "#/properties/global/properties/core%3Adata_doi#/properties/global/properties/core:data_doi")                   |
| [core:datatype](#coredatatype)              | `string`  | Required | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coredatatype.md "#/properties/global/properties/core%3Adatatype#/properties/global/properties/core:datatype")                   |
| [core:description](#coredescription)        | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coredescription.md "#/properties/global/properties/core%3Adescription#/properties/global/properties/core:description")          |
| [core:hw](#corehw)                          | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-corehw.md "#/properties/global/properties/core%3Ahw#/properties/global/properties/core:hw")                                     |
| [core:license](#corelicense)                | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-corelicense.md "#/properties/global/properties/core%3Alicense#/properties/global/properties/core:license")                      |
| [core:metadata\_only](#coremetadata_only)   | `boolean` | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coremetadata_only.md "#/properties/global/properties/core%3Ametadata_only#/properties/global/properties/core:metadata_only")    |
| [core:meta\_doi](#coremeta_doi)             | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coremeta_doi.md "#/properties/global/properties/core%3Ameta_doi#/properties/global/properties/core:meta_doi")                   |
| [core:num\_channels](#corenum_channels)     | `integer` | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-corenum_channels.md "#/properties/global/properties/core%3Anum_channels#/properties/global/properties/core:num_channels")       |
| [core:offset](#coreoffset)                  | `integer` | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreoffset.md "#/properties/global/properties/core%3Aoffset#/properties/global/properties/core:offset")                         |
| [core:recorder](#corerecorder)              | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-corerecorder.md "#/properties/global/properties/core%3Arecorder#/properties/global/properties/core:recorder")                   |
| [core:sample\_rate](#coresample_rate)       | `number`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coresample_rate.md "#/properties/global/properties/core%3Asample_rate#/properties/global/properties/core:sample_rate")          |
| [core:sha512](#coresha512)                  | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coresha512.md "#/properties/global/properties/core%3Asha512#/properties/global/properties/core:sha512")                         |
| [core:trailing\_bytes](#coretrailing_bytes) | `integer` | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coretrailing_bytes.md "#/properties/global/properties/core%3Atrailing_bytes#/properties/global/properties/core:trailing_bytes") |
| [core:version](#coreversion)                | `string`  | Required | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreversion.md "#/properties/global/properties/core%3Aversion#/properties/global/properties/core:version")                      |
| [core:extensions](#coreextensions)          | `array`   | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreextensions.md "#/properties/global/properties/core%3Aextensions#/properties/global/properties/core:extensions")             |
| Additional Properties                       | Any       | Optional | can be null    |                                                                                                                                                                                                  |

## core:author

A text identifier for the author potentially including name, handle, email, and/or other ID like Amateur Call Sign.

`core:author`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreauthor.md "#/properties/global/properties/core%3Aauthor#/properties/global/properties/core:author")

### core:author Type

`string`

### core:author Examples

```json
"Bruce Wayne bruce@waynetech.com"
```

```json
"Bruce (K3X)"
```

## core:collection

The base filename of a `collection` with which this Recording is associated.

`core:collection`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-corecollection.md "#/properties/global/properties/core%3Acollection#/properties/global/properties/core:collection")

### core:collection Type

`string`

## core:dataset

The full filename of the Dataset file this Metadata file describes.

`core:dataset`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coredataset.md "#/properties/global/properties/core%3Adataset#/properties/global/properties/core:dataset")

### core:dataset Type

`string`

### core:dataset Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^\/\\:*?"<>|]+(\.[^\/\\:*?"<>|]+)*$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%5C%2F%5C%5C%3A*%3F%22%3C%3E%7C%5D%2B\(%5C.%5B%5E%5C%2F%5C%5C%3A*%3F%22%3C%3E%7C%5D%2B\)*%24 "try regular expression with regexr.com")

## core:data\_doi

The registered DOI (ISO 26324) for a Recording's Dataset file.

`core:data_doi`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coredata_doi.md "#/properties/global/properties/core%3Adata_doi#/properties/global/properties/core:data_doi")

### core:data\_doi Type

`string`

## core:datatype

The SigMF Dataset format of the stored samples in the Dataset file.

`core:datatype`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coredatatype.md "#/properties/global/properties/core%3Adatatype#/properties/global/properties/core:datatype")

### core:datatype Type

`string`

### core:datatype Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^(c|r)(f32|f64|i32|i16|u32|u16|i8|u8)(_le|_be)?$
```

[try pattern](https://regexr.com/?expression=%5E\(c%7Cr\)\(f32%7Cf64%7Ci32%7Ci16%7Cu32%7Cu16%7Ci8%7Cu8\)\(_le%7C_be\)%3F%24 "try regular expression with regexr.com")

### core:datatype Default Value

The default value is:

```json
"cf32_le"
```

### core:datatype Examples

```json
"ri16_le"
```

## core:description

A text description of the SigMF Recording.

`core:description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coredescription.md "#/properties/global/properties/core%3Adescription#/properties/global/properties/core:description")

### core:description Type

`string`

## core:hw

A text description of the hardware used to make the Recording.

`core:hw`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-corehw.md "#/properties/global/properties/core%3Ahw#/properties/global/properties/core:hw")

### core:hw Type

`string`

## core:license

A URL for the license document under which the Recording is offered. (RFC 3986)

`core:license`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-corelicense.md "#/properties/global/properties/core%3Alicense#/properties/global/properties/core:license")

### core:license Type

`string`

### core:license Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc3986 "check the specification")

### core:license Examples

```json
"https://creativecommons.org/licenses/by-sa/4.0/"
```

## core:metadata\_only

Indicates the Metadata file is intentionally distributed without the Dataset.

`core:metadata_only`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coremetadata_only.md "#/properties/global/properties/core%3Ametadata_only#/properties/global/properties/core:metadata_only")

### core:metadata\_only Type

`boolean`

## core:meta\_doi

The registered DOI (ISO 26324) for a Recording's Metadata file.

`core:meta_doi`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coremeta_doi.md "#/properties/global/properties/core%3Ameta_doi#/properties/global/properties/core:meta_doi")

### core:meta\_doi Type

`string`

## core:num\_channels

Total number of interleaved channels in the Dataset file. If omitted, this defaults to one.

`core:num_channels`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-corenum_channels.md "#/properties/global/properties/core%3Anum_channels#/properties/global/properties/core:num_channels")

### core:num\_channels Type

`integer`

### core:num\_channels Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum**: the value of this number must greater than or equal to: `1`

### core:num\_channels Default Value

The default value is:

```json
1
```

## core:offset

The index number of the first sample in the Dataset. If not provided, this value defaults to zero. Typically used when a Recording is split over multiple files. All sample indices in SigMF are absolute, and so all other indices referenced in metadata for this recording SHOULD be greater than or equal to this value.

`core:offset`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreoffset.md "#/properties/global/properties/core%3Aoffset#/properties/global/properties/core:offset")

### core:offset Type

`integer`

### core:offset Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum**: the value of this number must greater than or equal to: `0`

## core:recorder

The name of the software used to make this SigMF Recording.

`core:recorder`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-corerecorder.md "#/properties/global/properties/core%3Arecorder#/properties/global/properties/core:recorder")

### core:recorder Type

`string`

## core:sample\_rate

The sample rate of the signal in samples per second.

`core:sample_rate`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coresample_rate.md "#/properties/global/properties/core%3Asample_rate#/properties/global/properties/core:sample_rate")

### core:sample\_rate Type

`number`

### core:sample\_rate Constraints

**maximum**: the value of this number must smaller than or equal to: `1.7976931348623157e+308`

**minimum**: the value of this number must greater than or equal to: `0`

## core:sha512

The SHA512 hash of the Dataset file associated with the SigMF file.

`core:sha512`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coresha512.md "#/properties/global/properties/core%3Asha512#/properties/global/properties/core:sha512")

### core:sha512 Type

`string`

### core:sha512 Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[0-9a-fA-F]{128}$
```

[try pattern](https://regexr.com/?expression=%5E%5B0-9a-fA-F%5D%7B128%7D%24 "try regular expression with regexr.com")

## core:trailing\_bytes

The number of bytes to ignore at the end of a Non-Conforming Dataset file.

`core:trailing_bytes`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coretrailing_bytes.md "#/properties/global/properties/core%3Atrailing_bytes#/properties/global/properties/core:trailing_bytes")

### core:trailing\_bytes Type

`integer`

### core:trailing\_bytes Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum (exclusive)**: the value of this number must be greater than: `0`

## core:version

The SHA512 hash of the Dataset file associated with the SigMF file.

`core:version`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreversion.md "#/properties/global/properties/core%3Aversion#/properties/global/properties/core:version")

### core:version Type

`string`

### core:version Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"1.0.0"` |             |

### core:version Default Value

The default value is:

```json
"1.0.0"
```

## core:extensions

The `core:extensions` field in the Global Object is an array of extension objects that describe SigMF extensions. Extension Objects MUST contain the three key/value pairs defined below, and MUST NOT contain any other fields.

`core:extensions`

*   is optional

*   Type: `object[]` ([Details](sigmf-properties-global-properties-coreextensions-items.md))

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreextensions.md "#/properties/global/properties/core%3Aextensions#/properties/global/properties/core:extensions")

### core:extensions Type

`object[]` ([Details](sigmf-properties-global-properties-coreextensions-items.md))

### core:extensions Default Value

The default value is:

```json
[]
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
