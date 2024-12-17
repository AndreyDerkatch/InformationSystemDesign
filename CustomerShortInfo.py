import re

class CustomerShortInfo:
    def __init__(self, first_name, last_name, email, customer_id=None):
        if customer_id:
            self._set_id(customer_id)
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

            return CustomerShortInfo(customer_id=customer_id, first_name=first_name, last_name=last_name, email=email)
        except Exception as e:
            raise ValueError(f"Error parsing CustomerShortInfo data: {e}")

    @staticmethod
    def __validate_id(customer_id):
        return isinstance(customer_id, int) and customer_id > 0
        

    @staticmethod
    def __validate_name(name):
        return isinstance(name, str) and name

    @staticmethod
    def __validate_email(email):
        email_regex = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+"
        return isinstance(email, str) and re.match(email_regex, email)

    def get_customer_id(self):
        if hasattr(self, '_CustomerShortInfo__customer_id'):
            return self.__customer_id
        return None

    def get_first_name(self):
        if hasattr(self, '_CustomerShortInfo__first_name'):
            return self.__first_name
        return None

    def get_last_name(self):
        if hasattr(self, '_CustomerShortInfo__last_name'):
            return self.__last_name
        return None

    def get_email(self):
        if hasattr(self, '_CustomerShortInfo__email'):
            return self.__email
        return None

    def _set_id(self, customer_id):
        if self.__validate_id(customer_id):
            self.__customer_id = customer_id
        else:
            raise ValueError("CustomerShortInfo ID must be a positive integer.")

    def set_first_name(self, first_name):
        if self.__validate_name(first_name):
            self.__first_name = first_name
        else:
            raise ValueError("Name must be a non-empty string up to 255 characters.")

    def set_last_name(self, last_name):
        if self.__validate_name(last_name):
            self.__last_name = last_name
        else:
            raise ValueError("Name must be a non-empty string up to 255 characters.")

    def set_email(self, email):
        if self.__validate_email(email):
            self.__email = email
        else:
            raise ValueError("Invalid email format.")

    def __eq__(self, other):
        if isinstance(other, CustomerShortInfo):
            return (self.get_customer_id() == other.get_customer_id() and
                    self.get_first_name() == other.get_first_name() and
                    self.get_last_name() == other.get_last_name() and
                    self.get_email() == other.get_email())
        return False

    def __str__(self):
        return f"Customer short info [ID: {self.get_customer_id()}, Name: {self.get_first_name()} {self.get_last_name()}, Email: {self.get_email()}]"
