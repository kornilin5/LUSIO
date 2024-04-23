import dataclasses
from faker import Faker


@dataclasses.dataclass
class Users:
    login: str
    password: str
    name: str
    last_name: str
    second_name: str
    email: str
    confirm_password: str

    def create_login(self, ):
        fake = Faker()
        login = self.login + fake.user_name()
        return login

    def create_password(self, ):
        fake = Faker()
        password = self.password + fake.password()
        self.confirm_password = password
        return password

    def create_name(self, ):
        fake = Faker()
        name = self.name + fake.name()
        return name

    def create_email(self, ):
        fake = Faker()
        email = self.email + fake.email()
        return email

    def create_last_name(self, ):
        fake = Faker()
        last_name = self.last_name + fake.last_name()
        return last_name

    def create_confirm_password(self, ):
        return self.confirm_password

    def create_second_name(self, ):
        fake = Faker()
        second_name = self.second_name + fake.last_name()
        return second_name


user = Users(login='test',
             password="password",
             name='name',
             email='email',
             last_name='Last',
             confirm_password='password',
             second_name='Second')
