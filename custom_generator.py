import json
from py_markdown_table.markdown_table import markdown_table

sigmf_schema = open('sigmf.schema.json')
data = json.load(sigmf_schema)
sigmf_schema.close()

def gen_table(d):
    table = []
    for key, value in d["properties"].items():
        newdict = {"Field": key.replace('core:','')}
        newdict["Required"] = "Required" if key in d["required"] else ""
        newdict["Type"] = value.get("type", "MISSING")
        newdict["Default"] = str(value.get("default", ""))
        newdict["Description"] = str(value.get("description", ""))
        table.append(newdict)
    return markdown_table(table).set_params(quote=False, row_sep = 'markdown', padding_weight='right').get_markdown()

markdown = ''
markdown += data["properties"]["global"]["description"].replace('. ','.\n') + '\n\n'
markdown += gen_table(data["properties"]["global"]) + '\n\n'
markdown += data["properties"]["captures"]["description"] + '\n\n'
markdown += gen_table(data["properties"]["captures"]["items"]["anyOf"][0]) + '\n\n'
markdown += data["properties"]["annotations"]["description"] + '\n\n'
markdown += gen_table(data["properties"]["annotations"]["items"]["anyOf"][0]) + '\n\n'

sigmf_markdown = open('sigmf.md', 'w')
sigmf_markdown.write(markdown)
sigmf_markdown.close()