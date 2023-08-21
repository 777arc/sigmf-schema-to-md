# SigMF Specification

## Global

The `global` object consists of key/value pairs that provide information applicable to the entire Dataset.
It contains the information that is minimally necessary to open and parse the Dataset file, as well as general information about the Recording itself.

|Field         |Required|Type   |Default|Description                                                                                                                                                                                                                                                                                                                 |
|--------------|--------|-------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|author        |        |string |       |A text identifier for the author potentially including name, handle, email, and/or other ID like Amateur Call Sign.                                                                                                                                                                                                         |
|collection    |        |string |       |The base filename of a `collection` with which this Recording is associated.                                                                                                                                                                                                                                                |
|dataset       |        |string |       |The full filename of the Dataset file this Metadata file describes.                                                                                                                                                                                                                                                         |
|data_doi      |        |string |       |The registered DOI (ISO 26324) for a Recording's Dataset file.                                                                                                                                                                                                                                                              |
|datatype      |Required|string |cf32_le|The SigMF Dataset format of the stored samples in the Dataset file.                                                                                                                                                                                                                                                         |
|description   |        |string |       |A text description of the SigMF Recording.                                                                                                                                                                                                                                                                                  |
|hw            |        |string |       |A text description of the hardware used to make the Recording.                                                                                                                                                                                                                                                              |
|license       |        |string |       |A URL for the license document under which the Recording is offered. (RFC 3986)                                                                                                                                                                                                                                             |
|metadata_only |        |boolean|       |Indicates the Metadata file is intentionally distributed without the Dataset.                                                                                                                                                                                                                                               |
|meta_doi      |        |string |       |The registered DOI (ISO 26324) for a Recording's Metadata file.                                                                                                                                                                                                                                                             |
|num_channels  |        |integer|1      |Total number of interleaved channels in the Dataset file. If omitted, this defaults to one.                                                                                                                                                                                                                                 |
|offset        |        |integer|0      |The index number of the first sample in the Dataset. If not provided, this value defaults to zero. Typically used when a Recording is split over multiple files. All sample indices in SigMF are absolute, and so all other indices referenced in metadata for this recording SHOULD be greater than or equal to this value.|
|recorder      |        |string |       |The name of the software used to make this SigMF Recording.                                                                                                                                                                                                                                                                 |
|sample_rate   |        |number |       |The sample rate of the signal in samples per second.                                                                                                                                                                                                                                                                        |
|sha512        |        |string |       |The SHA512 hash of the Dataset file associated with the SigMF file.                                                                                                                                                                                                                                                         |
|trailing_bytes|        |integer|       |The number of bytes to ignore at the end of a Non-Conforming Dataset file.                                                                                                                                                                                                                                                  |
|version       |Required|string |1.0.0  |The SHA512 hash of the Dataset file associated with the SigMF file.                                                                                                                                                                                                                                                         |
|extensions    |        |array  |[]     |The `core:extensions` field in the Global Object is an array of extension objects that describe SigMF extensions. Extension Objects MUST contain the three key/value pairs defined below, and MUST NOT contain any other fields.                                                                                            |

### author

description: A text identifier for the author potentially including name, handle, email, and/or other ID like Amateur Call Sign.
examples: ['Bruce Wayne bruce@waynetech.com', 'Bruce (K3X)']
type: string

### collection

description: The base filename of a `collection` with which this Recording is associated.
type: string

### dataset

description: The full filename of the Dataset file this Metadata file describes.
type: string
pattern: ^[^\/\\:*?"<>|]+(\.[^\/\\:*?"<>|]+)*$

### data_doi

description: The registered DOI (ISO 26324) for a Recording's Dataset file.
type: string

### datatype

description: The SigMF Dataset format of the stored samples in the Dataset file.
examples: ['ri16_le']
default: cf32_le
pattern: ^(c|r)(f32|f64|i32|i16|u32|u16|i8|u8)(_le|_be)?$
type: string

### description

description: A text description of the SigMF Recording.
type: string

### hw

description: A text description of the hardware used to make the Recording.
type: string

### license

description: A URL for the license document under which the Recording is offered. (RFC 3986)
examples: ['https://creativecommons.org/licenses/by-sa/4.0/']
format: uri
type: string

### metadata_only

description: Indicates the Metadata file is intentionally distributed without the Dataset.
type: boolean

### meta_doi

description: The registered DOI (ISO 26324) for a Recording's Metadata file.
type: string

### num_channels

description: Total number of interleaved channels in the Dataset file. If omitted, this defaults to one.
default: 1
minimum: 1
maximum: 18446744073709551615
type: integer

### offset

description: The index number of the first sample in the Dataset. If not provided, this value defaults to zero. Typically used when a Recording is split over multiple files. All sample indices in SigMF are absolute, and so all other indices referenced in metadata for this recording SHOULD be greater than or equal to this value.
default: 0
minimum: 0
maximum: 18446744073709551615
type: integer

### recorder

description: The name of the software used to make this SigMF Recording.
type: string

### sample_rate

description: The sample rate of the signal in samples per second.
minimum: 0
maximum: 1.7976931348623157e+308
type: number

### sha512

description: The SHA512 hash of the Dataset file associated with the SigMF file.
type: string
pattern: ^[0-9a-fA-F]{128}$

### trailing_bytes

description: The number of bytes to ignore at the end of a Non-Conforming Dataset file.
type: integer
exclusiveMinimum: 0
maximum: 18446744073709551615

### version

description: The SHA512 hash of the Dataset file associated with the SigMF file.
default: 1.0.0
type: string
enum: ['1.0.0']

### extensions

description: The `core:extensions` field in the Global Object is an array of extension objects that describe SigMF extensions. Extension Objects MUST contain the three key/value pairs defined below, and MUST NOT contain any other fields.
type: array
default: []
additionalItems: False
items: {'$id': '#/properties/global/properties/core%3Aextensions/items', 'type': 'object', 'anyOf': [{'$id': '#/properties/global/properties/core%3Aextensions/items/anyOf/0', 'required': ['name', 'version', 'optional'], 'type': 'object', 'properties': {'name': {'$id': '#/properties/global/properties/core%3Aextensions/items/anyOf/0/properties/name', 'description': 'The name of the SigMF extension namespace.', 'type': 'string'}, 'version': {'$id': '#/properties/global/properties/core%3Aextensions/items/anyOf/0/properties/version', 'description': 'The version of the extension namespace specification used.', 'examples': ['1.0.0'], 'type': 'string'}, 'optional': {'$id': '#/properties/global/properties/core%3Aextensions/items/anyOf/0/properties/optional', 'description': 'If this field is `true`, the extension is REQUIRED to parse this Recording.', 'type': 'boolean'}}, 'additionalProperties': False}]}

## Captures

The `captures` value is an array of capture segment objects that describe the parameters of the signal capture. It MUST be sorted by the value of each capture segment's `core:sample_start` key, ascending.

|Field       |Required|Type   |Default|Description                                                                                |
|------------|--------|-------|-------|-------------------------------------------------------------------------------------------|
|datetime    |        |string |       |An ISO-8601 string indicating the timestamp of the sample index specified by sample_start. |
|frequency   |        |number |       |The center frequency of the signal in Hz.                                                  |
|global_index|        |integer|       |The index of the sample referenced by `sample_start` relative to an original sample stream.|
|header_bytes|        |integer|       |The number of bytes preceding a chunk of samples that are not sample data, used for NCDs.  |
|sample_start|Required|integer|0      |Index of first sample of this chunk.                                                       |

### datetime

description: An ISO-8601 string indicating the timestamp of the sample index specified by sample_start.
examples: ['1955-11-05T14:00:00.000Z']
pattern: ^([\+-]?\d{4}(?!\d{2}))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$
type: string

### frequency

description: The center frequency of the signal in Hz.
type: number
minimum: -1.7976931348623157e+308
maximum: 1.7976931348623157e+308

### global_index

description: The index of the sample referenced by `sample_start` relative to an original sample stream.
type: integer
minimum: 0
maximum: 18446744073709551615

### header_bytes

description: The number of bytes preceding a chunk of samples that are not sample data, used for NCDs.
type: integer
minimum: 0
maximum: 18446744073709551615

### sample_start

default: 0
description: Index of first sample of this chunk.
minimum: 0
maximum: 18446744073709551615
type: integer

## Annotations

The `annotations` value is an array of annotation segment objects that describe anything regarding the signal data not part of the Captures and Global objects. It MUST be sorted by the value of each Annotation Segment's `core:sample_start` key, ascending.

|Field          |Required|Type   |Default|Description                                                                      |
|---------------|--------|-------|-------|---------------------------------------------------------------------------------|
|comment        |        |string |       |A human-readable comment.                                                        |
|freq_lower_edge|        |number |       |The frequency (Hz) of the lower edge of the feature described by this annotation.|
|freq_upper_edge|        |number |       |The frequency (Hz) of the upper edge of the feature described by this annotation.|
|generator      |        |string |       |Human-readable name of the entity that created this annotation.                  |
|label          |        |string |       |A short form human/machine-readable label for the annotation.                    |
|sample_count   |Required|integer|       |The number of samples that this Segment applies to.                              |
|sample_start   |Required|integer|0      |The sample index at which this Segment takes effect.                             |
|uuid           |        |string |       |RFC-4122 unique identifier.                                                      |

### comment

default: 
description: A human-readable comment.
type: string

### freq_lower_edge

description: The frequency (Hz) of the lower edge of the feature described by this annotation.
type: number
minimum: -1.7976931348623157e+308
maximum: 1.7976931348623157e+308

### freq_upper_edge

description: The frequency (Hz) of the upper edge of the feature described by this annotation.
type: number
minimum: -1.7976931348623157e+308
maximum: 1.7976931348623157e+308

### generator

description: Human-readable name of the entity that created this annotation.
type: string

### label

description: A short form human/machine-readable label for the annotation.
type: string

### sample_count

description: The number of samples that this Segment applies to.
type: integer
minimum: 0
maximum: 18446744073709551615

### sample_start

default: 0
description: The sample index at which this Segment takes effect.
minimum: 0
maximum: 18446744073709551615
type: integer

### uuid

description: RFC-4122 unique identifier.
format: uuid
type: string

