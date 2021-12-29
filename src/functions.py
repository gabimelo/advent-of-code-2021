def read_input(day, sample=False):
    file_path = f'src/day{day}/day{day}{"sample" if sample else ""}.txt'
    with open(file_path, mode='r') as open_file:
        return list(map(lambda x: x.strip(), open_file.readlines()))
