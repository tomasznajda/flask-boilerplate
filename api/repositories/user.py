from api.models.user import User


class UserRepository:

    @staticmethod
    def add(first_name, last_name, age):
        user = User(first_name = first_name, last_name = last_name, age = age)
        return user.save()

    @staticmethod
    def update(id, first_name, last_name, age):
        user = UserRepository.get(id)
        user.first_name = first_name
        user.last_name = last_name
        user.age = age
        return user.save()

    @staticmethod
    def delete(id):
        user = UserRepository.get(id)
        return user.delete()

    @staticmethod
    def get(id):
        return User.query.filter_by(id = id).one_or_none()
