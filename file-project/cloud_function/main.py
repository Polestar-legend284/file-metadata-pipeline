def process_file(event, context):
    name = event['name']
    size = event['size']
    ftype = name.split('.')[-1]
    print(f"File uploaded: {name}, size: {size} bytes, type: {ftype}")
