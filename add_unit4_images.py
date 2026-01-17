#!/usr/bin/env python3

with open('cse-platform/src/data/syllabus.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Define all image additions with correct text from file
additions = [
    # Unit 4 - View Serializability Example
    (
        '#### View Serializability Example (Detailed)\\n\\nConsider schedule **S**',
        '#### View Serializability Example (Detailed)\n\n![View Serializability Example](/images/unit4/View%20Serializability%20Example.png)\n\nConsider schedule **S**'
    ),
    # Unit 4 - Testing conflict serializability - need to find the exact text
    (
        'Testing serializability: construct precedence graph from read/write conflicts',
        'Testing serializability: construct precedence graph from read/write conflicts\n\n![Testing Conflict Serializability](/images/unit4/Testing%20conflict%20serializability%20of%20a%20schedule.png)'
    ),
    # Unit 4 - Non-conflict serializable example - need to search for cycle text
    (
        'precedence graph: no cycle = serializable',
        'precedence graph: no cycle = serializable\n\n![Example of Non-Conflict Serializable Schedule](/images/unit4/Example-of-a-schedule-that-is-not-conflict-serializable.png)'
    ),
]

count = 0

# Apply all additions
for old, new in additions:
    if old in content:
        content = content.replace(old, new, 1)
        count += 1
        print(f'✓ Added Unit 4 image {count}')
    else:
        print(f'✗ NOT FOUND: {old[:80]}...')

# Write back
with open('cse-platform/src/data/syllabus.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n✅ Added {count} Unit 4 images!')
