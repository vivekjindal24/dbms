#!/usr/bin/env python3

with open('cse-platform/src/data/syllabus.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Add view serializability image
old = '#### View Serializability Example (Detailed)\\n\\nConsider schedule **S** with three transactions T1, T2, and T3:'
new = '#### View Serializability Example (Detailed)\\n\\n![View Serializability Example](/images/unit4/View%20Serializability%20Example.png)\\n\\nConsider schedule **S** with three transactions T1, T2, and T3:'

if old in content:
    content = content.replace(old, new, 1)
    with open('cse-platform/src/data/syllabus.ts', 'w', encoding='utf-8') as f:
        f.write(content)
    print('✅ Added View Serializability image successfully!')
else:
    print('✗ Pattern not found in file')
