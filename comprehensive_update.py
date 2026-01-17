#!/usr/bin/env python3
"""
Comprehensive script to update the DBMS educational website according to requirements.
Handles all Unit 2, 3, and 4 updates while maintaining file structure.
"""

import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def remove_master_references(content):
    """Remove all references to master.txt, master list, Master Notes but preserve structure"""
    
    # Replace inline references
    content = content.replace('![ER Symbols (Master Notes)]', '![ER Symbols]')
    content = content.replace('### Advantages (from master.txt)', '### Advantages of ER Model')
    content = content.replace('### Disadvantages (from master.txt)', '### Disadvantages of ER Model')
    content = content.replace('### How to draw ER diagram (master.txt checklist)', '### How to draw ER diagram')
    content = content.replace('From master.txt:', 'Objects')
    content = content.replace('From the master notes:', 'The')
    content = content.replace('from the master notes:', '')
    content = content.replace('## Relational algebra operations (master list)', '## Relational algebra operations')
    content = content.replace('### 2NF (master definition)', '### 2NF')
    content = content.replace('### 3NF (master definitions)', '### 3NF')
    content = content.replace('### Dependency preservation (master)', '### Dependency preservation')
    content = content.replace('Master example:', 'Example:')
    content = content.replace('## Worked example (2NF) — based on master.txt', '## Worked example (2NF)')
    content = content.replace('## Worked example (3NF) — based on master.txt', '## Worked example (3NF)')
    content = content.replace('(as in master examples)', '')
    content = content.replace('(like the master 2NF/3NF worked problems)', '')
    content = content.replace('### Step 3: Convert to 2NF (master decomposition)', '### Step 3: Convert to 2NF')
    content = content.replace('### Step 3: Convert to 3NF (master decomposition)', '### Step 3: Convert to 3NF')
    content = content.replace('(the same technique used in the master.txt 2NF/3NF examples)', '')
    content = content.replace('From master.txt, the pipeline is:', 'The pipeline is:')
    content = content.replace('From master.txt (disk storage section): large', 'Large')
    content = content.replace('From master.txt:', '')
    content = content.replace('          concept: "From the master notes:', '          concept: "Query languages are categorized into two types:')
    
    return content

def replace_dollar_with_rupee(content):
    """Replace $ with ₹ in transaction processing examples"""
    # Only in Unit 4 context, be specific about transaction examples
    content = content.replace('Imagine transferring $500 from your savings', 'Imagine transferring ₹500 from your savings')
    content = content.replace('You\'d lose $500!', 'You\'d lose ₹500!')
    content = content.replace('deduct $500 from savings', 'deduct ₹500 from savings')
    content = content.replace('add $500 to checking', 'add ₹500 to checking')
    content = content.replace('Balance - 500', 'Balance - 500')  # Keep the code as is
    content = content.replace('Balance + 500', 'Balance + 500')  # Keep the code as is
    
    return content

def main():
    filepath = '/Users/vivek/Desktop/Code/DBMS/cse-platform/src/data/syllabus.ts'
    
    print("Reading file...")
    content = read_file(filepath)
    
    print("Step 1: Removing master.txt references...")
    content = remove_master_references(content)
    
    print("Step 2: Replacing $ with ₹ in transaction examples...")
    content = replace_dollar_with_rupee(content)
    
    print("Writing updated file...")
    write_file(filepath, content)
    
    print("✓ Done! Basic cleanup completed.")
    print("\nNote: The following manual updates still need to be done:")
    print("- Unit 2: Add Physical Data Model content and diagrams")
    print("- Unit 2: Add Table Conversion rules from PPT")
    print("- Unit 2: Update Relational Query Language with new examples")
    print("- Unit 3: Add Keys Concept section at the start")
    print("- Unit 3: Add Constraints section from W3Schools")
    print("- Unit 4: Add content from Slides 18-20 after Conflict Serializability")
    print("- Unit 4: Add View Serializability Example from Slide 27")

if __name__ == '__main__':
    main()
