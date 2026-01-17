#!/usr/bin/env python3

with open('cse-platform/src/data/syllabus.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Rule 1 image
old = '- The primary key of the table will be the key attribute of the entity set\\n\\n**Example**:'
new = '- The primary key of the table will be the key attribute of the entity set\\n\\n![ER to Table Conversion Rule 1](/images/unit2/er_to_table%20Conversion_rule1.png)\\n\\n**Example**:'

if old in content:
    content = content.replace(old, new, 1)
    with open('cse-platform/src/data/syllabus.ts', 'w', encoding='utf-8') as f:
        f.write(content)
    print('✅ Added Rule 1 image!')
else:
    print('✗ Pattern not found')
