# Read the file
with open('syllabus.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace - add the image back
old_text = "- The primary key of the table will be the key attribute of the entity set\\n\\n**Example**:"

new_text = "- The primary key of the table will be the key attribute of the entity set\\n\\n![ER to Table Conversion Rule 1](/images/unit2/er_to_table%20Conversion_rule1.png)\\n\\n**Example**:"

if old_text in content:
    content = content.replace(old_text, new_text)
    with open('syllabus.ts', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Successfully restored the Student entity diagram image!")
else:
    print("❌ Could not find the exact text to replace")
