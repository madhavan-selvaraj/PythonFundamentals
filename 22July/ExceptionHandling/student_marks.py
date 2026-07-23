class student:
    def __init__(self, mark):
        if mark < 0 or mark > 100:
            raise ValueError("Mark should be between 0 to 100")
        self.mark = mark


s1 = student(120)
print(s1.mark)
