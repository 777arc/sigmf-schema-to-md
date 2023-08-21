# Schema for SigMF Meta Files Schema

```txt
https://github.com/sigmf/SigMF/spec/1.0.0/schema-meta
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [sigmf.schema.json](../sigmf.schema.json "open original schema") |

## Schema for SigMF Meta Files Type

`object` ([Schema for SigMF Meta Files](sigmf.md))

## Schema for SigMF Meta Files Default Value

The default value is:

```json
[
  "global",
  "captures",
  "annotations"
]
```

# Schema for SigMF Meta Files Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                        |
| :-------------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------- |
| [global](#global)           | `object` | Required | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global.md "#/properties/global#/properties/global")                |
| [captures](#captures)       | `array`  | Required | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-captures.md "#/properties/captures#/properties/captures")          |
| [annotations](#annotations) | `array`  | Required | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-annotations.md "#/properties/annotations#/properties/annotations") |

## global

The `global` object consists of key/value pairs that provide information applicable to the entire Dataset. It contains the information that is minimally necessary to open and parse the Dataset file, as well as general information about the Recording itself.

`global`

*   is required

*   Type: `object` ([Details](sigmf-properties-global.md))

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global.md "#/properties/global#/properties/global")

### global Type

`object` ([Details](sigmf-properties-global.md))

## captures

The `captures` value is an array of capture segment objects that describe the parameters of the signal capture. It MUST be sorted by the value of each capture segment's `core:sample_start` key, ascending.

`captures`

*   is required

*   Type: `object[]` ([Details](sigmf-properties-captures-items.md))

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-captures.md "#/properties/captures#/properties/captures")

### captures Type

`object[]` ([Details](sigmf-properties-captures-items.md))

### captures Default Value

The default value is:

```json
[]
```

## annotations

The `annotations` value is an array of annotation segment objects that describe anything regarding the signal data not part of the Captures and Global objects. It MUST be sorted by the value of each Annotation Segment's `core:sample_start` key, ascending.

`annotations`

*   is required

*   Type: `object[]` ([Details](sigmf-properties-annotations-items.md))

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-annotations.md "#/properties/annotations#/properties/annotations")

### annotations Type

`object[]` ([Details](sigmf-properties-annotations-items.md))

### annotations Default Value

The default value is:

```json
[]
```
