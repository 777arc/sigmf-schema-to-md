## 0 Type

`object` ([Details](sigmf-properties-annotations-annotations-type-anyof-0.md))

# 0 Properties

| Property                                       | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                              |
| :--------------------------------------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [core:comment](#corecomment)                   | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-corecomment.md "#/properties/annotations/items/anyOf/0/properties/core%3Acomment#/properties/annotations/items/anyOf/0/properties/core:comment")                         |
| [core:freq\_lower\_edge](#corefreq_lower_edge) | `number`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-corefreq_lower_edge.md "#/properties/annotations/items/anyOf/0/properties/core%3Afreq_lower_edge#/properties/annotations/items/anyOf/0/properties/core:freq_lower_edge") |
| [core:freq\_upper\_edge](#corefreq_upper_edge) | `number`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-corefreq_upper_edge.md "#/properties/annotations/items/anyOf/0/properties/core%3Afreq_upper_edge#/properties/annotations/items/anyOf/0/properties/core:freq_upper_edge") |
| [core:generator](#coregenerator)               | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-coregenerator.md "#/properties/annotations/items/anyOf/0/properties/core%3Agenerator#/properties/annotations/items/anyOf/0/properties/core:generator")                   |
| [core:label](#corelabel)                       | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-corelabel.md "#/properties/annotations/items/anyOf/0/properties/core%3Alabel#/properties/annotations/items/anyOf/0/properties/core:label")                               |
| [core:sample\_count](#coresample_count)        | `integer` | Required | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-coresample_count.md "#/properties/annotations/items/anyOf/0/properties/core%3Asample_count#/properties/annotations/items/anyOf/0/properties/core:sample_count")          |
| [core:sample\_start](#coresample_start)        | `integer` | Required | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-coresample_start.md "#/properties/annotations/items/anyOf/0/properties/core%3Asample_start#/properties/annotations/items/anyOf/0/properties/core:sample_start")          |
| [core:uuid](#coreuuid)                         | `string`  | Optional | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-coreuuid.md "#/properties/annotations/items/anyOf/0/properties/core%3Auuid#/properties/annotations/items/anyOf/0/properties/core:uuid")                                  |
| Additional Properties                          | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                         |

## core:comment

A human-readable comment.

`core:comment`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-corecomment.md "#/properties/annotations/items/anyOf/0/properties/core%3Acomment#/properties/annotations/items/anyOf/0/properties/core:comment")

### core:comment Type

`string`

## core:freq\_lower\_edge

The frequency (Hz) of the lower edge of the feature described by this annotation.

`core:freq_lower_edge`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-corefreq_lower_edge.md "#/properties/annotations/items/anyOf/0/properties/core%3Afreq_lower_edge#/properties/annotations/items/anyOf/0/properties/core:freq_lower_edge")

### core:freq\_lower\_edge Type

`number`

### core:freq\_lower\_edge Constraints

**maximum**: the value of this number must smaller than or equal to: `1.7976931348623157e+308`

**minimum**: the value of this number must greater than or equal to: `-1.7976931348623157e+308`

## core:freq\_upper\_edge

The frequency (Hz) of the upper edge of the feature described by this annotation.

`core:freq_upper_edge`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-corefreq_upper_edge.md "#/properties/annotations/items/anyOf/0/properties/core%3Afreq_upper_edge#/properties/annotations/items/anyOf/0/properties/core:freq_upper_edge")

### core:freq\_upper\_edge Type

`number`

### core:freq\_upper\_edge Constraints

**maximum**: the value of this number must smaller than or equal to: `1.7976931348623157e+308`

**minimum**: the value of this number must greater than or equal to: `-1.7976931348623157e+308`

## core:generator

Human-readable name of the entity that created this annotation.

`core:generator`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-coregenerator.md "#/properties/annotations/items/anyOf/0/properties/core%3Agenerator#/properties/annotations/items/anyOf/0/properties/core:generator")

### core:generator Type

`string`

## core:label

A short form human/machine-readable label for the annotation.

`core:label`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-corelabel.md "#/properties/annotations/items/anyOf/0/properties/core%3Alabel#/properties/annotations/items/anyOf/0/properties/core:label")

### core:label Type

`string`

## core:sample\_count

The number of samples that this Segment applies to.

`core:sample_count`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-coresample_count.md "#/properties/annotations/items/anyOf/0/properties/core%3Asample_count#/properties/annotations/items/anyOf/0/properties/core:sample_count")

### core:sample\_count Type

`integer`

### core:sample\_count Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum**: the value of this number must greater than or equal to: `0`

## core:sample\_start

The sample index at which this Segment takes effect.

`core:sample_start`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-coresample_start.md "#/properties/annotations/items/anyOf/0/properties/core%3Asample_start#/properties/annotations/items/anyOf/0/properties/core:sample_start")

### core:sample\_start Type

`integer`

### core:sample\_start Constraints

**maximum**: the value of this number must smaller than or equal to: `18446744073709552000`

**minimum**: the value of this number must greater than or equal to: `0`

## core:uuid

RFC-4122 unique identifier.

`core:uuid`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-annotations-annotations-type-anyof-0-properties-coreuuid.md "#/properties/annotations/items/anyOf/0/properties/core%3Auuid#/properties/annotations/items/anyOf/0/properties/core:uuid")

### core:uuid Type

`string`

### core:uuid Constraints

**UUID**: the string must be a UUID, according to [RFC 4122](https://tools.ietf.org/html/rfc4122 "check the specification")

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
