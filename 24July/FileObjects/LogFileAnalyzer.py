info_count = 0
error_count = 0
warning_count = 0
error_line = []
with open("log_file.txt") as f:
    for line in f:
        if line.startswith("INFO"):
            info_count += 1
        elif line.startswith("ERROR"):
            error_count += 1
            error_line.append(line)
        elif line.startswith("WARNING"):
            warning_count += 1

print(f"Count INFO messages:{info_count}")
print(f"Count ERROR messages:{error_count}")
print(f"Count WARNING messages:{warning_count}")


for line in error_line:
    print(line)

with open("error_log.txt", "w") as f:
    for line in error_line:
        f.write(line)
