import re
lines = [] 
with open('tmpl.html') as template: 
    lines = template.readlines() 

heading_pattern = re.compile(r'(#{1,6}).*(</h[1-6])')
end_p_pattern = re.compile(r'</p>')
p_pattern = re.compile(r'<p>(.*)$')
p_flag = False # if the line is in between paragraph tags 
#line = lines[6]
#print(line) 
#match = re.search(heading_pattern, line)
#print(match.groups())
#print(re.sub(heading_pattern, f"{match.group(1)} {match.group(2)}", line)) 
empty_lines = []

for line in lines: 
    if re.search(end_p_pattern, line): 
        p_flag = False
    if p_flag: 
        line = '\n'
    match = re.search(heading_pattern, line)
    if match:
        print(re.sub(heading_pattern, f"{match.group(1)} {match.group(2)}", line)) 
        line = re.sub(heading_pattern, f"{match.group(1)} {match.group(2)}", line)
    match = re.search(p_pattern, line) 
    if match: 
        line = re.sub(p_pattern, "<p>", line)
        p_flag = True   
    empty_lines.append(line) 

print(empty_lines) 
with open('empty.html', 'w') as empty: 
    empty.writelines(empty_lines) 
