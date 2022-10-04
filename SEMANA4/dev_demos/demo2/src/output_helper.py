def write_txt_file(data, output_path):
    file = open(output_path, 'w+')
    for line in data:
            file.write(line+'\n')
    with open(output_path, 'w') as file:
        result = {
          'statusCode': 'ok',
          'body': None
        }
    return result