class StudentNode:
    def __init__(self, student_id, student_name, gpa):
        self.student_id = student_id
        self.student_name = student_name
        self.gpa = gpa
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, student_name, gpa):
        new = StudentNode(student_id, student_name, gpa)
        if self.head is None:
            self.head = new
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new

    def delete_student(self, student_id):
        current = self.head
        prev = None
        while current and current.student_id != student_id:
            prev = current
            current = current.next
        if current is None:
            print("Tələbə tapılmadı.")
            return
        if prev:
            prev.next = current.next
        else:
            self.head = current.next
        print(current.student_name, "silindi.")

    def show_all(self):
        current = self.head
        while current:
            print(current.student_id, current.student_name, current.gpa)
            current = current.next

    def show_above_80(self):
        current = self.head
        while current:
            if current.gpa > 80:
                print(current.student_id, current.student_name, current.gpa)
            current = current.next

    def search_by_name(self, name):
        current = self.head
        while current:
            if current.student_name == name:
                print(current.student_id, current.student_name, current.gpa)
                return
            current = current.next
        print("Tələbə tapılmadı.")

    def count(self):
        n = 0
        current = self.head
        while current:
            n += 1
            current = current.next
        return n


if __name__ == "__main__":
    students = StudentList()
    while True:
        print("\n1. Tələbə əlavə et")
        print("2. Tələbə sil")
        print("3. Bütün tələbələri göstər")
        print("4. GPA > 80 olanları göstər")
        print("5. Ada görə axtarış et")
        print("6. Tələbələrin sayını göstər")
        print("0. Çıxış")
        choice = input("Seçim: ")

        if choice == "1":
            students.add_student(input("student_id: "),
                                 input("student_name: "),
                                 float(input("gpa: ")))
        elif choice == "2":
            students.delete_student(input("student_id: "))
        elif choice == "3":
            students.show_all()
        elif choice == "4":
            students.show_above_80()
        elif choice == "5":
            students.search_by_name(input("student_name: "))
        elif choice == "6":
            print("Tələbələrin sayı:", students.count())
        elif choice == "0":
            break
        else:
            print("Yanlış seçim.")
