#!/usr/bin/env python3

with open('cse-platform/src/data/syllabus.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Define all image additions
additions = [
    # Unit 4 - View Serializability Example (already mentioned in context)
    (
        'View serializability example with 3-step verification',
        'View serializability example with 3-step verification\n\n![View Serializability Example](/images/unit4/View%20Serializability%20Example.png)'
    ),
    # Unit 4 - Testing conflict serializability
    (
        'conflict serializability testing algorithm (5 steps)',
        'conflict serializability testing algorithm (5 steps)\n\n![Testing Conflict Serializability](/images/unit4/Testing%20conflict%20serializability%20of%20a%20schedule.png)'
    ),
    # Unit 4 - Example of schedule not conflict serializable
    (
        'When precedence graph contains a cycle, schedule is not conflict serializable',
        'When precedence graph contains a cycle, schedule is not conflict serializable\n\n![Example of Non-Conflict Serializable Schedule](/images/unit4/Example-of-a-schedule-that-is-not-conflict-serializable.png)'
    ),
    # Unit 2 - ER Model Diagram (large comprehensive diagram)
    (
        'The ER diagram shows entities, attributes, and relationships in a visual format that is easy to understand and communicate with stakeholders.',
        'The ER diagram shows entities, attributes, and relationships in a visual format that is easy to understand and communicate with stakeholders.\n\n![Comprehensive ER Model Diagram](/images/unit2/er%20model%20diagram.png)'
    ),
    # Unit 2 - Cartesian Product example
    (
        '**Result of borrower × loan**:\\n\\nThe customer-name column contains all customers',
        '**Result of borrower × loan**:\n\n![Cartesian Product Result](/images/unit2/cartesian_product.png)\n\nThe customer-name column contains all customers'
    ),
    # Unit 2 - Result expression
    (
        '**Result**: We get only those tuples of borrower × loan that pertain to customers who have a loan at the Perryridge branch.',
        '**Result**: We get only those tuples of borrower × loan that pertain to customers who have a loan at the Perryridge branch.\n\n![Query Result](/images/unit2/result-of-this-expression.png)'
    ),
    # Unit 2 - ER Diagram Representation
    (
        '### ER Notation Styles\\n\\nDifferent notation styles exist for ER diagrams:',
        '### ER Notation Styles\n\n![ER Diagram Representation Styles](/images/unit2/ER_Diagram_reperentation.png)\n\nDifferent notation styles exist for ER diagrams:'
    ),
    # Unit 2 - Banking Enterprise ER diagram
    (
        'ER model is the standard conceptual model and converts easily to tables.',
        'ER model is the standard conceptual model and converts easily to tables.\n\n![Banking Enterprise ER Diagram](/images/unit2/E-R%20diagram%20for%20the%20Banking%20Enterprise.png)'
    ),
    # Unit 1 - Advantages of DBMS
    (
        '## Advantages of DBMS\\n\\n- **Data independence**',
        '## Advantages of DBMS\n\n![Advantages of DBMS](/images/unit1/Advantages%20of%20DBMS.png)\n\n- **Data independence**'
    ),
    # Unit 1 - Drawbacks of file systems
    (
        '## Drawbacks of File Systems\\n\\n- **Data redundancy and inconsistency**',
        '## Drawbacks of File Systems\n\n![Drawbacks of File Systems](/images/unit1/Drawbacks%20of%20using%20file%20systems%20to%20store%20data.png)\n\n- **Data redundancy and inconsistency**'
    ),
    # Unit 1 - Levels of abstraction
    (
        '- **View level**: application programs hide details',
        '![Levels of Data Abstraction](/images/unit1/levels%20of%20abstraction.png)\n\n- **View level**: application programs hide details'
    ),
    # Unit 1 - Three level schema architecture
    (
        'The architecture ensures **data independence**',
        '![Three Level Schema Architecture](/images/unit1/Three%20level%20schema%20architecture%20of%20database.png)\n\nThe architecture ensures **data independence**'
    ),
    # Unit 3 - Query processing
    (
        '## Query Processing Overview\\n\\nQuery processing involves',
        '## Query Processing Overview\n\n![Query Processing Steps](/images/unit3/query%20processing.png)\n\nQuery processing involves'
    ),
]

count = 0
not_found = []

# Apply all additions
for old, new in additions:
    if old in content:
        content = content.replace(old, new, 1)  # Replace only first occurrence
        count += 1
        print(f'✓ Added image {count}')
    else:
        not_found.append(old[:60])
        print(f'✗ NOT FOUND: {old[:60]}...')

# Write back
with open('cse-platform/src/data/syllabus.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n✅ Successfully added {count} images out of {len(additions)} attempted!')
if not_found:
    print(f'\n⚠️  Could not find {len(not_found)} patterns - may need manual adjustment')
