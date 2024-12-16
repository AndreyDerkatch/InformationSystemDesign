import re
from datetime import datetime


class CustomerShortInfo:
    def __init__(self, customer_id, first_name, last_name, email):
        self.__customer_id = self.__validate_id(customer_id)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)

    @staticmethod
    def from_string(data_str):
        try:
            # Предполагаем, что строка имеет формат: "id,first_name,last_name,email"
            data = data_str.split(',')
            if len(data) != 4:
                raise ValueError("Incorrect number of fields in the string.")

            customer_id = int(data[0].strip())
            first_name = data[1].strip()
            last_name = data[2].strip()
            email = data[3].strip()

            return CustomerShortInfo(customer_id, first_name, last_name, email)
        except Exception as e:
            raise ValueError(f"Error parsing CustomerShortInfo data: {e}")

    @staticmethod
    def __validate_id(customer_id):
        if isinstance(customer_id, int) and customer_id > 0:
            return customer_id
        raise ValueError("CustomerShortInfo ID must be a positive integer.")

    @staticmethod
    def __validate_name(name):
        if isinstance(name, str) and name:
            return name
        raise ValueError("Name must be a non-empty string up to 255 characters.")

    @staticmethod
    def __validate_email(email):
        email_regex = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+"
        if isinstance(email, str) and re.match(email_regex, email):
            return email
        raise ValueError("Invalid email format.")

    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def set_first_name(self, first_name):
        self.__first_name = self.__validate_name(first_name)

    def set_last_name(self, last_name):
        self.__last_name = self.__validate_name(last_name)

    def set_email(self, email):
        self.__email = self.__validate_email(email)

    def __eq__(self, other):
        if isinstance(other, CustomerShortInfo):
            return (self.__customer_id == other.__customer_id and
                    self.__first_name == other.__first_name and
                    self.__last_name == other.__last_name and
                    self.__email == other.__email)
        return False

    def __str__(self):
        return f"Customer short info [ID: {self.__customer_id}, Name: {self.__first_name} {self.__last_name}, Email: {self.__email}]"

    def __hash__(self):
        return hash(self.get_first_name()) + hash(self.get_last_name()) + hash(self.get_customer_id()) + hash(self.get_email())

