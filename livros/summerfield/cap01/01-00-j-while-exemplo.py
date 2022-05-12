#! usr/bin/env python3

while True:
    item = get_next_item()
    if not item:
        break
    process_item(item)
