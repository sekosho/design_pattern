# open_closed
from abc import ABCMeta, abstractmethod


class UserInfo:
    def __init__(self, user_name, job_name, nationality) -> None:
        self.user_name = user_name
        self.job_name = job_name
        self.nationality = nationality

    def __str__(self) -> str:
        return f"{self.user_name}、{self.job_name}、{self.nationality}"


# class UserInfoFilter:
#     @staticmethod
#     def filter_users_job(users, job_name):
#         for user in users:
#             if user.job_name == job_name:
#                 yield user

#     @staticmethod
#     def filter_users_nationality(users, nationality):
#         for user in users:
#             if user.nationality == nationality:
#                 yield user


class Comparation(metaclass=ABCMeta):
    @abstractmethod
    def is_equal(self, other):
        pass

    def __and__(self, other):
        return AndComparation(self, other)

    def __or__(self, other):
        return OrComparation(self, other)


class AndComparation(Comparation):
    def __init__(self) -> None:
        super().__init__()


class Filter(metaclass=ABCMeta):
    @abstractmethod
    def filter(self, comparation, items):
        pass


class JobNameComparation(Comparation):
    def __init__(self, job_name) -> None:
        self.job_name = job_name

    def is_equal(self, other):
        return self.job_name == other.job_name


class NationalityComparation(Comparation):
    def __init__(self, nationality) -> None:
        self.nationality = nationality

    def is_equal(self, other):
        return self.nationality == other.nationality


class UserInfoFilter(Filter):
    def filter(self, comparation, users):
        for user in users:
            if comparation.is_equal(user):
                yield user


taro = UserInfo("taro", "salary man", "Japan")
jiro = UserInfo("jiro", "police man", "Japan")
john = UserInfo("john", "salary man", "USA")
user_list = [taro, jiro, john]
# for man in UserInfoFilter.filter_users_job(user_list, "police man"):
#     print(man)

# for man in UserInfoFilter.filter_users_nationality(user_list, "Japan"):
#     print(man)
job_comparation = JobNameComparation("salary man")
user_filter = UserInfoFilter()
filtered_users = user_filter.filter(job_comparation, user_list)
for user in filtered_users:
    print(user)
