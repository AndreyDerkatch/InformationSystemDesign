import re
from datetime import datetime

from CustomerShortInfo import CustomerShortInfo

class Customer(CustomerShortInfo):
    def __init__(self, first_name, last_name, phone_number, customer_id=None, email=None,
                 address=None, city=None, postal_code=None, country=None, date_joined=None):
        super().__init__(customer_id=customer_id, first_name=first_name, last_name=last_name, phone_number=phone_number)
        if email:
            self.set_email(email)
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
    def validate_email(email):
        email_regex = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+"
        return isinstance(email, str) and re.match(email_regex, email)

    @staticmethod
    def validate_non_empty_string(value):
        return isinstance(value, str) and value.strip()

    @staticmethod
    def validate_postal_code(postal_code):
        return isinstance(postal_code, str) and len(postal_code) == 6

    @staticmethod
    def validate_date_joined(date_joined):
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

    @staticmethod
    def from_dict(data: dict):
        date_time = datetime.strptime(data['date_joined'], '%Y-%m-%d %H:%M:%S') if data.get('date_joined') else None
        return Customer(
            customer_id=data['customer_id'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            phone_number=data.get('phone_number'),
            address=data.get('address'),
            city=data.get('city'),
            postal_code=data.get('postal_code'),
            country=data.get('country'),
            date_joined=date_time
        )

    def to_dict(self):
        return {
            'customer_id': self.get_customer_id(),
            'first_name': self.get_first_name(),
            'last_name': self.get_last_name(),
            'email': self.get_email(),
            'phone_number': self.get_phone_number(),
            'address': self.get_address(),
            'city': self.get_city(),
            'postal_code': self.get_postal_code(),
            'country': self.get_country(),
            'date_joined': self.get_date_joined().strftime('%Y-%m-%d %H:%M:%S') if self.get_date_joined() else None
        }
    
    def get_email(self):
        if hasattr(self, '_Customer__email'):
            return self.__email
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

    def set_email(self, email):
        if self.validate_email(email):
            self.__email = email
        else:
            raise ValueError("Invalid email format.")

    def set_address(self, address):        #
        if self.validate_non_empty_string(address):
            self.__address= address
        else:
            raise ValueError("Address must be a non-empty string.")

    def set_city(self, city):
        if self.validate_non_empty_string(city):
            self.__city = city
        else:
            raise ValueError("City must be a non-empty string.")

    def set_postal_code(self, postal_code):
        if self.validate_postal_code(postal_code):
            self.__postal_code = postal_code
        else:
            raise ValueError("Postal Code must be an string with up to 6 digits.")

    def set_country(self, country):
        if self.validate_non_empty_string(country):
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

    def __hash__(self):
        return hash(self.get_first_name()) + hash(self.get_last_name()) + hash(self.get_customer_id()) + hash(
            self.get_phone_number())
