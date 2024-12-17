import re

class CustomerShortInfo:
    def __init__(self, first_name, last_name, phone_number, customer_id=None):
        if customer_id:
            self._set_id(customer_id)
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_phone_number(phone_number)

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
            phone_number = data[3].strip()

            return CustomerShortInfo(customer_id=customer_id, first_name=first_name,
                                     last_name=last_name, phone_number=phone_number)
        except Exception as e:
            raise ValueError(f"Error parsing CustomerShortInfo data: {e}")

    @staticmethod
    def __validate_id(customer_id):
        return isinstance(customer_id, int) and customer_id > 0


    @staticmethod
    def __validate_name(name):
        return isinstance(name, str) and name

    @staticmethod
    def __validate_phone_number(phone_number):
        phone_regex = r"^\+?[0-9]{10,15}$"
        return isinstance(phone_number, str) and re.match(phone_regex, phone_number)

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

    def get_phone_number(self):
        if hasattr(self, '_CustomerShortInfo__phone_number'):
            return self.__phone_number
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

    def set_phone_number(self, phone_number):
        if self.__validate_phone_number(phone_number):
            self.__phone_number = phone_number
        else:
            raise ValueError("Phone number must be a valid string with 10 to 15 digits, optionally starting with +.")

    def __eq__(self, other):
        if isinstance(other, CustomerShortInfo):
            return (self.get_first_name() == other.get_first_name() and
                    self.get_last_name() == other.get_last_name() and
                    self.get_phone_number() == other.get_phone_number())
        return False

    def __str__(self):
        return (f"Customer short info [ID: {self.get_customer_id()}, Name: {self.get_first_name()} {self.get_last_name()}, "
                f"Phone: {self.get_phone_number()}]")
