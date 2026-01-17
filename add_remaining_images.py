#!/usr/bin/env python3

with open('cse-platform/src/data/syllabus.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Define replacements - these match the actual escaped newlines in the TypeScript file
replacements = [
    # Rule 2  
    (
        '- While conversion, simple attributes of the composite attributes are taken into account, not the composite attribute itself\\n\\n**Example**:',
        '- While conversion, simple attributes of the composite attributes are taken into account, not the composite attribute itself\\n\\n![ER to Table Conversion Rule 2](/images/unit2/er_to_table_conversion_rule2.png)\\n\\n**Example**:'
    ),
    # Rule 3
    (
        '- Other table will contain the primary key and all the multi-valued attributes\\n\\n**Example**:',
        '- Other table will contain the primary key and all the multi-valued attributes\\n\\n![ER to Table Conversion Rule 3](/images/unit2/er-to-table-conversion-rule3.png)\\n\\n**Example**:'
    ),
    # Rule 4
    (
        '- Set of non-descriptive attributes will be the primary key\\n\\n**Note**:',
        '- Set of non-descriptive attributes will be the primary key\\n\\n![ER to Table Conversion Rule 4](/images/unit2/er-to-table-conversion-rule4.png)\\n\\n**Note**:'
    ),
    # Rule 5 Case 1
    (
        '**Case-01: Binary Relationship With Cardinality Ratio m:n**\\n\\nHere, three tables will be required:',
        '**Case-01: Binary Relationship With Cardinality Ratio m:n**\\n\\n![ER to Table Conversion Rule 5 Case 1](/images/unit2/er-to-table-conversion-rule5-case1.png)\\n\\nHere, three tables will be required:'
    ),
    # Rule 5 Case 2
    (
        '**Case-02: Binary Relationship With Cardinality Ratio 1:n**\\n\\nHere, two tables will be required:',
        '**Case-02: Binary Relationship With Cardinality Ratio 1:n**\\n\\n![ER to Table Conversion Rule 5 Case 2](/images/unit2/er-to-table-conversion-rule5-case2.png)\\n\\nHere, two tables will be required:'
    ),
    # Rule 5 Case 3
    (
        '**Case-03: Binary Relationship With Cardinality Ratio m:1**\\n\\nHere, two tables will be required:',
        '**Case-03: Binary Relationship With Cardinality Ratio m:1**\\n\\n![ER to Table Conversion Rule 5 Case 3](/images/unit2/er-to-table-conversion-rule5-case3.png)\\n\\nHere, two tables will be required:'
    ),
    # Rule 5 Case 4
    (
        "**Case-04: Binary Relationship With Cardinality Ratio 1:1**\\n\\nHere, two tables will be required. Either combine 'R' with 'A' or 'B':",
        "**Case-04: Binary Relationship With Cardinality Ratio 1:1**\\n\\n![ER to Table Conversion Rule 5 Case 4](/images/unit2/er-to-table-conversion-rule5-case4.png)\\n\\nHere, two tables will be required. Either combine 'R' with 'A' or 'B':"
    ),
    # Rule 6 Case 1
    (
        '**Case-01: Cardinality Constraint and Total Participation From One Side**\\n\\nBecause cardinality ratio = 1:n',
        '**Case-01: Cardinality Constraint and Total Participation From One Side**\\n\\n![ER to Table Conversion Rule 6 Case 1](/images/unit2/er-to-table-conversion-rule6-case1.png)\\n\\nBecause cardinality ratio = 1:n'
    ),
    # Rule 6 Case 2
    (
        '**Case-02: Cardinality Constraint and Total Participation From Both Sides**\\n\\nIf there is a key constraint from both sides with total participation',
        '**Case-02: Cardinality Constraint and Total Participation From Both Sides**\\n\\n![ER to Table Conversion Rule 6 Case 2](/images/unit2/er-to-table-conversion-rule6-case2.png)\\n\\nIf there is a key constraint from both sides with total participation'
    ),
    # Rule 7
    (
        '**Rule**: Weak entity set always appears in association with identifying relationship with total participation constraint.\\n\\nHere, two tables will be required:',
        '**Rule**: Weak entity set always appears in association with identifying relationship with total participation constraint.\\n\\n![ER to Table Conversion Rule 7](/images/unit2/er-to-table-conversion-rule7.png)\\n\\nHere, two tables will be required:'
    )
]

count = 0
# Apply all replacements
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f'✓ Added image {count}')
    else:
        print(f'✗ NOT FOUND: {old[:60]}...')

# Write back
with open('cse-platform/src/data/syllabus.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n✅ Successfully added {count} images out of 10 attempted!')
