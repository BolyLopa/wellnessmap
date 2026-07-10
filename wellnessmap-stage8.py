# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: WellnessMap
def filter_entries(entries, filters=None):
    if filters is None:
        return entries[:]
    
    result = []
    for entry in entries:
        match = True
        
        if 'status' in filters and entry.get('status') != filters['status']:
            match = False
        elif 'category' in filters and entry.get('category') != filters['category']:
            match = False
        elif 'owner' in filters and entry.get('owner', '') != filters['owner']:
            match = False
        elif 'tag' in filters and filters['tag'] not in entry.get('tags', []):
            match = False
        
        if match:
            result.append(entry)
    
    return result
