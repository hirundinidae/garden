import re
lines = [] 
with open('tmpl.html') as template: 
    lines = template.readlines() 

pattern = re.compile(r'(#{1,6}).*(</h[1-6])')
line = lines[6]
print(line) 
match = re.search(pattern, line)
print(match.groups())
print(re.sub(pattern, f"{match.group(1)} {match.group(2)}", line)) 

