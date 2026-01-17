#!/usr/bin/env python3
"""
Script to update syllabus.ts with all required changes for the educational website.
"""

import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def remove_master_references(content):
    """Remove all references to master.txt, master list, Master Notes"""
    # Replace Master Notes
    content = content.replace('(Master Notes)', '')
    content = content.replace('Master Notes', '')
    
    # Replace "from master.txt"
    content = re.sub(r'\(from master\.txt\)', '', content)
    content = re.sub(r'from master\.txt:', '', content)
    content = re.sub(r'From master\.txt:', '', content)
    content = re.sub(r'From the master notes,', 'The', content)
    content = re.sub(r'from the master notes:', '', content)
    
    # Replace "master list"
    content = re.sub(r'\(master list\)', '', content)
    content = re.sub(r'master list', '', content)
    
    # Replace "master.txt checklist"
    content = re.sub(r'\(master\.txt checklist\)', '', content)
    
    # Replace "based on master.txt"
    content = re.sub(r'— based on master\.txt', '', content)
    content = re.sub(r'based on master\.txt', '', content)
    
    # Replace "(master)" standalone
    content = re.sub(r'\(master\)', '', content)
    
    # Replace "master definition" and "master definitions"
    content = re.sub(r'\(master definition\)', '', content)
    content = re.sub(r'\(master definitions\)', '', content)
    
    # Replace "master decomposition"
    content = re.sub(r'\(master decomposition\)', '', content)
    
    # Replace "(as in master examples)"
    content = re.sub(r'\(as in master examples\)', '', content)
    
    # Replace "(like the master 2NF/3NF worked problems)"
    content = re.sub(r'\(like the master 2NF/3NF worked problems\)', '', content)
    
    # Replace "Master example:"
    content = re.sub(r'Master example:', 'Example:', content)
    
    # Clean up extra spaces
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r' \.', '.', content)
    content = re.sub(r' ,', ',', content)
    
    return content

def main():
    filepath = '/Users/vivek/Desktop/Code/DBMS/cse-platform/src/data/syllabus.ts'
    
    print("Reading file...")
    content = read_file(filepath)
    
    print("Removing master.txt references...")
    content = remove_master_references(content)
    
    print("Writing updated file...")
    write_file(filepath, content)
    
    print("Done! All master.txt references have been removed.")

if __name__ == '__main__':
    main()
