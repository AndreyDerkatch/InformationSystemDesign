import re
from datetime import datetime

from CustomerShortInfo import CustomerShortInfo

class Customer(CustomerShortInfo):
    def __init__(self, first_name, last_name, email, customer_id=None, phone_number=None,
                 address=None, city=None, postal_code=None, country=None, date_joined=None):
        super().__init__(customer_id=customer_id, first_name=first_name, last_name=last_name, email=email)
        if phone_number:
            self.set_phone_number(phone_number)
        if address:
            self.set_address(address)
        if city:
            self.set_city(city)
        if postal_code:
            self.set_postal_code(postal_code)
        if country:
            self.set_country(country)
        if date_joined:
            self.set_date_joined(date_joined)

    @staticmethod
    def __validate_phone_number(phone_number):
        phone_regex = r"^\+?[0-9]{10,15}$"
        return isinstance(phone_number, str) and re.match(phone_regex, phone_number)

    @staticmethod
    def __validate_non_empty_string(value):
        return isinstance(value, str) and value.strip()

    @staticmethod
    def __validate_postal_code(postal_code):
        return isinstance(postal_code, str) and len(postal_code) == 6

    @staticmethod
    def __validate_date_joined(date_joined):
        try:
            if isinstance(date_joined, str):
                return datetime.strptime(date_joined, '%Y-%m-%d %H:%M:%S')
            elif isinstance(date_joined, datetime):
                return date_joined
        except ValueError:
            raise ValueError("Date Joined must be a valid datetime in the format YYYY-MM-DD HH:MM:SS.")

    @staticmethod
    def from_string(data_str):
        try:
            # Предполагаем, что строка имеет формат: "id,first_name,last_name,email,phone_number,address,city,postal_code,country,date_joined"
            data = data_str.split(',')
            if len(data) != 10:
                raise ValueError("Incorrect number of fields in the string.")

            customer_id = int(data[0].strip())
            first_name = data[1].strip()
            last_name = data[2].strip()
            email = data[3].strip()
            phone_number = data[4].strip()
            address = data[5].strip()
            city = data[6].strip()
            postal_code = data[7].strip()
            country = data[8].strip()
            date_joined = data[9].strip()

            return Customer(customer_id=customer_id, first_name=first_name, last_name=last_name, email=email,
                            phone_number=phone_number, address=address, city=city, postal_code=postal_code,
                            country=country, date_joined=date_joined)
        except Exception as e:
            raise ValueError(f"Error parsing customer data: {e}")

    def get_phone_number(self):
        if hasattr(self, '_Customer__phone_number'):
            return self.__phone_number
        return None

    def get_address(self):
        if hasattr(self, '_Customer__address'):
            return self.__address
        return None

    def get_city(self):
        if hasattr(self, '_Customer__city'):
            return self.__city
        return None

    def get_postal_code(self):
        if hasattr(self, '_Customer__postal_code'):
            return self.__postal_code
        return None

    def get_country(self):
        if hasattr(self, '_Customer__country'):
            return self.__country
        return None

    def get_date_joined(self):
        if hasattr(self, '_Customer__date_joined'):
            return self.__date_joined
        return None

    def set_phone_number(self, phone_number):
        if self.__validate_phone_number(phone_number):
            self.__phone_number = phone_number
        else:
            raise ValueError("Phone number must be a valid string with 10 to 15 digits, optionally starting with +.")

    def set_address(self, address):        #
        if self.__validate_non_empty_string(address):
            self.__address= address
        else:
            raise ValueError("Address must be a non-empty string.")

    def set_city(self, city):
        if self.__validate_non_empty_string(city):
            self.__city = city
        else:
            raise ValueError("City must be a non-empty string.")

    def set_postal_code(self, postal_code):
        if self.__validate_postal_code(postal_code):
            self.__postal_code = postal_code
        else:
            raise ValueError("Postal Code must be an string with up to 6 digits.")

    def set_country(self, country):
        if self.__validate_non_empty_string(country):
            self.__country = country
        else:
            raise ValueError("Country must be a non-empty string.")

    def set_date_joined(self, date_joined):
        try:
            if isinstance(date_joined, str):
                self.__date_joined = datetime.strptime(date_joined, '%Y-%m-%d %H:%M:%S')
            elif isinstance(date_joined, datetime):
                self.__date_joined = date_joined
        except ValueError:
            raise ValueError("Date Joined must be a valid datetime in the format YYYY-MM-DD HH:MM:SS.")


    def __str__(self):
        return (f"Customer [ID: {self.get_customer_id()}, "
                f"Name: {self.get_first_name()} {self.get_last_name()}, "
                f"Email: {self.get_email()}, "
                f"Phone: {self.get_phone_number()}, "
                f"Address: {self.get_address()}, "
                f"City: {self.get_city()}, "
                f"Postal Code: {self.get_postal_code()}, "
                f"Country: {self.get_country()}, "
                f"Date Joined: {self.get_date_joined()}]")

    def short_info(self):
        return super().__str__()

    def __eq__(self, other):
        if isinstance(other, Customer):
            return super().__eq__(other)
        return False
