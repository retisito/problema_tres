import json, re

def get_list_of_infections(json_file, filter = []):
    pattern = 'infec+io[sas,on,ones]'
    filter = ('|').join(filter)
    output = []
    error = None
    
    try:
        with open(json_file) as json_data:
            data = json.load(json_data)
    except Exception as e:
        error = e
    else:
        for key in data: 
            if (not re.search(pattern, data[key], re.IGNORECASE) == None and
                not re.search(filter, data[key], re.IGNORECASE) == None):
                output.append({key: data[key]})

    return output, error