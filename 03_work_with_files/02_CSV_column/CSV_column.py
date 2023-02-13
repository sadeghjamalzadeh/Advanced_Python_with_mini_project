def process(path):
    with open(path, 'r') as f:
        new_lines = ''
        lines = f.readlines()
        for line in lines:
            temp = sum(map(int, line.strip().split(',')))
            new_line = line.strip() + ',' + str(temp) + '\n'
            new_lines = new_lines + new_line
    with open('ans.csv', 'w') as nf:
        nf.write(new_lines)

