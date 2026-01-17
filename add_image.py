import re

with open('cse-platform/src/data/syllabus.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the hierarchical data model image
content = content.replace(
    '### Hierarchical model (tree)\n- Tree structure with single parent for each child\n- Simple and fast traversal, but weak at complex relationships',
    '### Hierarchical model (tree)\n- Tree structure with single parent for each child\n- Simple and fast traversal, but weak at complex relationships\n\n![Hierarchical Data Model](/images/unit1/hirerarchical%20data%20model.png)'
)

with open('cse-platform/src/data/syllabus.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Added hierarchical data model image')
