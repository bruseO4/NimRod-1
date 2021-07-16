def uns(id):
    with open("photos.txt", "r") as a_file:
        list_lines = []
        for line in a_file:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            list_lines.append(line_list)
        
        
    list_lines[id]
uns(0)

