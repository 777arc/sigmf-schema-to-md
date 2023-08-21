import subprocess
cmd = "jsonschema2md -d . -o temp -x - -h false"
subprocess.call(cmd, shell=True)
print('done')

def read_in_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()

md_file = open('sigmf.md', 'w')
md_file.write(read_in_file('temp/sigmf.md'))
md_file.write(read_in_file('temp/sigmf-properties-global.md'))
md_file.write(read_in_file('temp/sigmf-properties-captures-items-anyof-0.md'))
md_file.write(read_in_file('temp/sigmf-properties-annotations-annotations-type-anyof-0.md'))
md_file.close()