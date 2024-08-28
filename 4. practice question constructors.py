# class has  constructor which takes name and marks of three subjects
# there is a method to find average of these marks
class Student:
    def __init__(self, name, m_eng, m_cs, m_mth):
        self.name = name
        self.m_eng = m_eng
        self.m_cs = m_cs
        self.m_mth = m_mth


    def average_fun(self,m_eng, m_cs, m_mth):
        average = (m_eng + m_cs + m_mth) // 3
        return average


student = Student("Abu bakr", 65, 65,56)
result = student.average_fun(student.m_eng, student.m_cs, student.m_mth)
print(f"average of marks is {result}")
