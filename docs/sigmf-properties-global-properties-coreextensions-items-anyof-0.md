# Untitled object in Schema for SigMF Meta Files Schema

```txt
#/properties/global/properties/core%3Aextensions/items/anyOf/0#/properties/global/properties/core:extensions/items/anyOf/0
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [sigmf.schema.json\*](../out/sigmf.schema.json "open original schema") |

## 0 Type

`object` ([Details](sigmf-properties-global-properties-coreextensions-items-anyof-0.md))

# 0 Properties

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                 |
| :-------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)         | `string`  | Required | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreextensions-items-anyof-0-properties-name.md "#/properties/global/properties/core%3Aextensions/items/anyOf/0/properties/name#/properties/global/properties/core:extensions/items/anyOf/0/properties/name")             |
| [version](#version)   | `string`  | Required | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreextensions-items-anyof-0-properties-version.md "#/properties/global/properties/core%3Aextensions/items/anyOf/0/properties/version#/properties/global/properties/core:extensions/items/anyOf/0/properties/version")    |
| [optional](#optional) | `boolean` | Required | cannot be null | [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreextensions-items-anyof-0-properties-optional.md "#/properties/global/properties/core%3Aextensions/items/anyOf/0/properties/optional#/properties/global/properties/core:extensions/items/anyOf/0/properties/optional") |

## name

The name of the SigMF extension namespace.

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreextensions-items-anyof-0-properties-name.md "#/properties/global/properties/core%3Aextensions/items/anyOf/0/properties/name#/properties/global/properties/core:extensions/items/anyOf/0/properties/name")

### name Type

`string`

## version

The version of the extension namespace specification used.

`version`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreextensions-items-anyof-0-properties-version.md "#/properties/global/properties/core%3Aextensions/items/anyOf/0/properties/version#/properties/global/properties/core:extensions/items/anyOf/0/properties/version")

### version Type

`string`

### version Examples

```json
"1.0.0"
```

## optional

If this field is `true`, the extension is REQUIRED to parse this Recording.

`optional`

*   is required

*   Type: `boolean`

*   cannot be null

*   defined in: [Schema for SigMF Meta Files](sigmf-properties-global-properties-coreextensions-items-anyof-0-properties-optional.md "#/properties/global/properties/core%3Aextensions/items/anyOf/0/properties/optional#/properties/global/properties/core:extensions/items/anyOf/0/properties/optional")

### optional Type

`boolean`
