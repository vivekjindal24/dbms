import re

with open('cse-platform/src/data/syllabus.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Rule 1
content = content.replace(
    '### Rule-01: Strong Entity Set With Only Simple Attributes\n\n**Rule**: A strong entity set with only simple attributes will require only one table in the relational model.\n- Attributes of the table will be the attributes of the entity set\n- The primary key of the table will be the key attribute of the entity set\n\n**Example**:',
    '### Rule-01: Strong Entity Set With Only Simple Attributes\n\n**Rule**: A strong entity set with only simple attributes will require only one table in the relational model.\n- Attributes of the table will be the attributes of the entity set\n- The primary key of the table will be the key attribute of the entity set\n\n![ER to Table Conversion Rule 1](/images/unit2/er_to_table%20Conversion_rule1.png)\n\n**Example**:'
)

# Rule 2
content = content.replace(
    '### Rule-02: Strong Entity Set With Composite Attributes\n\n**Rule**: A strong entity set with any number of composite attributes will require only one table.\n- While conversion, simple attributes of the composite attributes are taken into account, not the composite attribute itself\n\n**Example**:',
    '### Rule-02: Strong Entity Set With Composite Attributes\n\n**Rule**: A strong entity set with any number of composite attributes will require only one table.\n- While conversion, simple attributes of the composite attributes are taken into account, not the composite attribute itself\n\n![ER to Table Conversion Rule 2](/images/unit2/er_to_table_conversion_rule2.png)\n\n**Example**:'
)

# Rule 3
content = content.replace(
    '### Rule-03: Strong Entity Set With Multi-Valued Attributes\n\n**Rule**: A strong entity set with any number of multi-valued attributes will require two tables.\n- One table will contain all the simple attributes with the primary key\n- Other table will contain the primary key and all the multi-valued attributes\n\n**Example**:',
    '### Rule-03: Strong Entity Set With Multi-Valued Attributes\n\n**Rule**: A strong entity set with any number of multi-valued attributes will require two tables.\n- One table will contain all the simple attributes with the primary key\n- Other table will contain the primary key and all the multi-valued attributes\n\n![ER to Table Conversion Rule 3](/images/unit2/er-to-table-conversion-rule3.png)\n\n**Example**:'
)

# Rule 4
content = content.replace(
    '### Rule-04: Translating Relationship Set into a Table\n\n**Rule**: A relationship set will require one table in the relational model.\n\n**Attributes of the table are**:\n- Primary key attributes of the participating entity sets\n- Its own descriptive attributes if any\n- Set of non-descriptive attributes will be the primary key\n\n**Note**:',
    '### Rule-04: Translating Relationship Set into a Table\n\n**Rule**: A relationship set will require one table in the relational model.\n\n**Attributes of the table are**:\n- Primary key attributes of the participating entity sets\n- Its own descriptive attributes if any\n- Set of non-descriptive attributes will be the primary key\n\n![ER to Table Conversion Rule 4](/images/unit2/er-to-table-conversion-rule4.png)\n\n**Note**:'
)

# Rule 5 Cases
content = content.replace(
    '**Case-01: Binary Relationship With Cardinality Ratio m:n**\n\nHere, three tables will be required:',
    '**Case-01: Binary Relationship With Cardinality Ratio m:n**\n\n![ER to Table Conversion Rule 5 Case 1](/images/unit2/er-to-table-conversion-rule5-case1.png)\n\nHere, three tables will be required:'
)

content = content.replace(
    '**Case-02: Binary Relationship With Cardinality Ratio 1:n**\n\nHere, two tables will be required:',
    '**Case-02: Binary Relationship With Cardinality Ratio 1:n**\n\n![ER to Table Conversion Rule 5 Case 2](/images/unit2/er-to-table-conversion-rule5-case2.png)\n\nHere, two tables will be required:'
)

content = content.replace(
    '**Case-03: Binary Relationship With Cardinality Ratio m:1**\n\nHere, two tables will be required:',
    '**Case-03: Binary Relationship With Cardinality Ratio m:1**\n\n![ER to Table Conversion Rule 5 Case 3](/images/unit2/er-to-table-conversion-rule5-case3.png)\n\nHere, two tables will be required:'
)

content = content.replace(
    '**Case-04: Binary Relationship With Cardinality Ratio 1:1**\n\nHere, two tables will be required. Either combine',
    '**Case-04: Binary Relationship With Cardinality Ratio 1:1**\n\n![ER to Table Conversion Rule 5 Case 4](/images/unit2/er-to-table-conversion-rule5-case4.png)\n\nHere, two tables will be required. Either combine'
)

# Rule 6 Cases
content = content.replace(
    '**Case-01: Cardinality Constraint and Total Participation From One Side**\n\nBecause cardinality ratio = 1:n',
    '**Case-01: Cardinality Constraint and Total Participation From One Side**\n\n![ER to Table Conversion Rule 6 Case 1](/images/unit2/er-to-table-conversion-rule6-case1.png)\n\nBecause cardinality ratio = 1:n'
)

content = content.replace(
    '**Case-02: Cardinality Constraint and Total Participation From Both Sides**\n\nIf there is a key constraint from both sides',
    '**Case-02: Cardinality Constraint and Total Participation From Both Sides**\n\n![ER to Table Conversion Rule 6 Case 2](/images/unit2/er-to-table-conversion-rule6-case2.png)\n\nIf there is a key constraint from both sides'
)

# Rule 7
content = content.replace(
    '### Rule-07: Binary Relationship With Weak Entity Set\n\n**Rule**: Weak entity set always appears in association with identifying relationship with total participation constraint.\n\nHere, two tables will be required:',
    '### Rule-07: Binary Relationship With Weak Entity Set\n\n**Rule**: Weak entity set always appears in association with identifying relationship with total participation constraint.\n\n![ER to Table Conversion Rule 7](/images/unit2/er-to-table-conversion-rule7.png)\n\nHere, two tables will be required:'
)

with open('cse-platform/src/data/syllabus.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Added all 11 rule images successfully!')
