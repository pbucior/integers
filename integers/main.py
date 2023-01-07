import utils

input_file_name = '../input.txt'
output_file_name = '../output.txt'

input_file = utils.read_file(input_file_name)
input_values = utils.get_values(input_file)
pairs = utils.make_pairs(input_values)
utils.write_to_file(output_file_name, pairs)
