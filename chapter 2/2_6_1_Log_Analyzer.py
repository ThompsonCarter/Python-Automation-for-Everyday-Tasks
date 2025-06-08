
def count_errors(path):
    count = 0
    with open(path) as f:
        for line in f:
            if "ERROR" in line:
                count += 1
    return count

if __name__ == "__main__":
    print("Errors:", count_errors("app.log"))
