import subprocess
cmd = "jsonschema2md -d . -o temp -x - -h false"
subprocess.call(cmd, shell=True)
print('done')

def read_in_file(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
        content = remove_defined_in(content)
        content = remove_defined_in_header(content)
        content = replace_table_2ndline(content)
        return content

def remove_defined_in(content):
    while True:
        indx_start = content.find('[Schema for SigMF Meta Files]')
        if indx_start == -1:
            break
        indx_end = content.find(')', indx_start + 1)
        if (indx_end - indx_start) < 300:
            content = content[:indx_start] + content[indx_end+1:]
            
            # Check if the next char is a | and remove the remainder of the line if it is
            if content[indx_start:indx_start+100].lstrip()[0] == '|':
                new_stop_indx = content[indx_start:indx_start+100].find('|')
                content = content[:indx_start] + content[indx_start + new_stop_indx + 1:]
        else:
            print('error')
            exit()
    return content

def remove_defined_in_header(content):
    while True:
        indx_start = content.find('| Defined by')
        if indx_start == -1:
            break
        indx_end = content.find('|', indx_start + 1)
        if (indx_end - indx_start) < 300:
            content = content[:indx_start+1] + content[indx_end+1:]
        else:
            print('error')
            exit()
    return content

def replace_table_2ndline(content):
    indx_start = content.find('| :---')
    indx_end = content.find('\n', indx_start)
    #content = content[:indx_start] + content[indx_end:]
    content = content[:indx_start] + content[indx_end+1:]
    return content

def replace_table_2ndline(content):
    new_2ndline = '| :--- | :--- | :--- | :---: |\n'
    i = 0
    while i < len(content):
        indx_start = content.find('| :---', i)
        if indx_start == -1:
            break
        indx_end = content.find('\n', indx_start + 1)
        if (indx_end - indx_start) < 500:
            content = content[:indx_start] + new_2ndline + content[indx_end+1:]
            i = indx_start + len(new_2ndline)
        else:
            print('error')
            exit()
    return content

md_file = open('sigmf.md', 'w')
md_file.write(read_in_file('temp/sigmf.md'))
md_file.write(read_in_file('temp/sigmf-properties-global.md'))
md_file.write(read_in_file('temp/sigmf-properties-captures-items-anyof-0.md'))
md_file.write(read_in_file('temp/sigmf-properties-annotations-annotations-type-anyof-0.md'))
md_file.close()