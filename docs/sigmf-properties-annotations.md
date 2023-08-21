# Untitled array in Schema for SigMF Meta Files Schema

```txt
#/properties/annotations#/properties/annotations
```

The `annotations` value is an array of annotation segment objects that describe anything regarding the signal data not part of the Captures and Global objects. It MUST be sorted by the value of each Annotation Segment's `core:sample_start` key, ascending.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [sigmf.schema.json\*](../out/sigmf.schema.json "open original schema") |

## annotations Type

`object[]` ([Details](sigmf-properties-annotations-items.md))

## annotations Default Value

The default value is:

```json
[]
```
