#!/usr/bin/env python3
"""
Script to properly reorganize the syllabus.ts file according to requirements:
1. Unit 2 Data Models: Replace sections 4 & 5 in technicalDepth with Physical Data Model and Table Conversion rules
2. Remove duplicate content from practical section
3. Ensure all content is professionally organized
"""

import re

# Read the current file
with open('cse-platform/src/data/syllabus.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Replace sections 4 and 5 in Unit 2 Data Models technicalDepth
old_sections_4_5 = r'''## 3\) Object-Oriented Data Model
Objects objects combine data \+ relationships in a single structure; useful for complex data like multimedia\.

\!\[Object-Oriented Data Model\]\(/images/unit2/object%20oriented%20data%20model\.png\)

## 4\) Integrity Constraints \(must always hold\)
- \*\*Domain constraint\*\*: values must come from an allowed domain \(Age between 0–120\)
- \*\*Entity integrity\*\*: primary key cannot be NULL
- \*\*Referential integrity\*\*: foreign key must match a referenced primary key \(or be NULL if allowed\)

## 5\) Data Manipulation Operations \(DML\)
- \*\*SELECT\*\* \(read\)
- \*\*INSERT\*\* \(add new rows\)
- \*\*UPDATE\*\* \(modify rows\)
- \*\*DELETE\*\* \(remove rows\)'''

new_sections_4_5 = '''## 3) Object-Oriented Data Model
Objects combine data + relationships in a single structure; useful for complex data like multimedia.

![Object-Oriented Data Model](/images/unit2/object%20oriented%20data%20model.png)

## 4) Physical Data Model

The physical data model represents how data will be implemented in a specific DBMS. It includes storage details, indexes, and optimization strategies.

### ER Diagram (Unit 1, Slide 52)

![ER Model Representation](/images/unit1/er%20model.png)

The ER diagram shows entities, attributes, and relationships in a visual format that is easy to understand and communicate with stakeholders.

### ER Model Explanation

The Entity-Relationship model provides:
- **Entities**: Real-world objects (rectangles)
- **Attributes**: Properties of entities (ovals)
- **Relationships**: Associations between entities (diamonds)
- **Cardinality**: One-to-One, One-to-Many, Many-to-Many
- **Participation**: Total (double line) or Partial (single line)

### Representation Diagrams (Unit 1, Slide 53)

Different notation styles exist for ER diagrams:
- Chen notation (original)
- Crow's Foot notation (popular in industry)
- UML notation (used in software engineering)

## 5) Converting ER Diagrams to Tables

Following rules are used for converting an ER diagram into relational tables:

### Rule-01: Strong Entity Set With Only Simple Attributes

**Rule**: A strong entity set with only simple attributes will require only one table in the relational model.
- Attributes of the table will be the attributes of the entity set
- The primary key of the table will be the key attribute of the entity set

**Example**:
```
Entity: Student (StudentID, Name, Email, Major)
↓
Table: Student
StudentID (PK) | Name | Email | Major
```

### Rule-02: Strong Entity Set With Composite Attributes

**Rule**: A strong entity set with any number of composite attributes will require only one table.
- While conversion, simple attributes of the composite attributes are taken into account, not the composite attribute itself

**Example**:
```
Entity: Employee (EmpID, Name, Address{Street, City, Zip})
↓
Table: Employee
EmpID (PK) | Name | Street | City | Zip
```

### Rule-03: Strong Entity Set With Multi-Valued Attributes

**Rule**: A strong entity set with any number of multi-valued attributes will require two tables.
- One table will contain all the simple attributes with the primary key
- Other table will contain the primary key and all the multi-valued attributes

**Example**:
```
Entity: Employee (EmpID, Name, {PhoneNumbers})
↓
Table 1: Employee
EmpID (PK) | Name

Table 2: EmployeePhones
EmpID (FK) | PhoneNumber
PRIMARY KEY (EmpID, PhoneNumber)
```

### Rule-04: Translating Relationship Set into a Table

**Rule**: A relationship set will require one table in the relational model.

**Attributes of the table are**:
- Primary key attributes of the participating entity sets
- Its own descriptive attributes if any
- Set of non-descriptive attributes will be the primary key

**Note**: If we consider the overall ER diagram, three tables will be required:
- One table for entity set "Employee"
- One table for entity set "Department"
- One table for relationship set "Works_in"

### Rule-05: Binary Relationships With Cardinality Ratios

Four cases are possible:

**Case-01: Binary Relationship With Cardinality Ratio m:n**

Here, three tables will be required:
```
A (a1, a2)
R (a1, b1)  -- Junction table
B (b1, b2)
```

**Case-02: Binary Relationship With Cardinality Ratio 1:n**

Here, two tables will be required:
```
A (a1, a2)
BR (a1, b1, b2)  -- Combined table for B and R
```
Note: Combined table is drawn for entity set B and relationship set R.

**Case-03: Binary Relationship With Cardinality Ratio m:1**

Here, two tables will be required:
```
AR (a1, a2, b1)  -- Combined table for A and R
B (b1, b2)
```
Note: Combined table is drawn for entity set A and relationship set R.

**Case-04: Binary Relationship With Cardinality Ratio 1:1**

Here, two tables will be required. Either combine 'R' with 'A' or 'B':

Way-01:
```
AR (a1, a2, b1)
B (b1, b2)
```

Way-02:
```
A (a1, a2)
BR (a1, b1, b2)
```

### Rule-06: Binary Relationship With Cardinality and Participation Constraints

**Cardinality constraints**: Implemented as discussed in Rule-05

**Total participation constraint**: Foreign key acquires NOT NULL constraint (i.e., foreign key cannot be null)

**Case-01: Cardinality Constraint and Total Participation From One Side**

Because cardinality ratio = 1:n, we combine entity set B and relationship set R:
```
A (a1, a2)
BR (a1 NOT NULL, b1, b2)
```
Because of total participation, foreign key a1 has acquired NOT NULL constraint.

**Case-02: Cardinality Constraint and Total Participation From Both Sides**

If there is a key constraint from both sides with total participation, then that binary relationship is represented using only a single table:
```
ARB (a1, a2, b1, b2)
```

### Rule-07: Binary Relationship With Weak Entity Set

**Rule**: Weak entity set always appears in association with identifying relationship with total participation constraint.

Here, two tables will be required:
```
A (a1, a2)
BR (a1, b1, b2)
```
Where B is the weak entity and A is the strong (owner) entity.'''

# Apply replacement
content = re.sub(old_sections_4_5, new_sections_4_5, content, flags=re.DOTALL)

# Write the updated content
with open('cse-platform/src/data/syllabus.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Successfully reorganized Unit 2 Data Models - sections 4 & 5 replaced")
print("✅ Backup created at: cse-platform/src/data/syllabus.ts.backup")
