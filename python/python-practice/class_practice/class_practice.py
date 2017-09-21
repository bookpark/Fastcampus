class Employee:
    '''고용자 관련 정보를 가집니다.'''
    def __init__(self, name, department, job_title, year):
        self.name = name
        self.department = department
        self.job_title = job_title
        self.year = year

    def _get_show_info_text(self):
        return f'''이름: {self.name}
부서: {self.department}
직책: {self.job_title}
연차: {self.year}'''

    def show_info(self):
        print(self._get_show_info_text())

    '''@staticmethod
    def duty():
        import random
        employees = ('박부기', '김승준', '김재홍', '김기홍', '이한영')
        selected_employee = random.choice(employees)
        return Employee(selected_employee, '개발', '팀장', '5')'''
