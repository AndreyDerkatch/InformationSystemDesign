import tkinter as tk
from tkinter import ttk, messagebox
from AddCustomerController import AddCustomerController


class CustomerTableView:
    def __init__(self, root, controller):
        self.controller = controller
        self.controller.add_observer(self)

        # Переменные для отслеживания текущей страницы
        self.current_page = 1
        self.page_size = 10

        # Интерфейс окна
        self.root = root
        self.root.title("Customer Management")
        self.root.geometry("900x500")  # Размер окна
        self.root.resizable(False, False)  # Запрещаем изменение размера окна

        # Минимальные настройки стиля для сдержанности
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), foreground="#2F4F4F", background="#D3D3D3")
        style.configure("Treeview", rowheight=30, font=("Arial", 10))
        style.map("Treeview", background=[("selected", "#D3D3D3")])

        # Фрейм для таблицы
        self.table_frame = tk.Frame(root, bg="#F0F0F0")
        self.table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Таблица для отображения клиентов
        self.table = ttk.Treeview(
            self.table_frame,
            columns=('ID', '№', 'First Name', 'Last Name', 'Phone number'),
            show='headings',
            selectmode="browse",  # Выбор строк через клики
        )
        self.table.heading('№', text='№', anchor=tk.CENTER)
        self.table.heading('First Name', text='First Name', anchor=tk.W)
        self.table.heading('Last Name', text='Last Name', anchor=tk.W)
        self.table.heading('Phone number', text='Phone number', anchor=tk.W)

        # Настройки колонок таблицы
        self.table.column('ID', width=0, stretch=tk.NO)  # Скрытая колонка для ID
        self.table.column('№', width=50, anchor=tk.CENTER)
        self.table.column('First Name', width=150, anchor=tk.W)
        self.table.column('Last Name', width=150, anchor=tk.W)
        self.table.column('Phone number', width=200, anchor=tk.W)
        self.table.pack(fill=tk.BOTH, expand=True)

        # Добавление вертикального скроллбара
        scrollbar = ttk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Фрейм для кнопок
        button_frame = tk.Frame(root, bg="#F0F0F0")
        button_frame.pack(fill=tk.X, padx=20, pady=10)

        # Стиль кнопок в серых оттенках
        button_style = {
            "bg": "#D3D3D3", "fg": "black", "font": ("Arial", 10, "bold"),
            "activebackground": "#D3D3D3", "activeforeground": "white",  # Активный цвет
            "bd": 1, "relief": tk.RAISED, "width": 20, "height": 1
        }

        # Кнопки управления
        self.prev_button = tk.Button(button_frame, text="Предыдущие 10", command=self.load_previous, **button_style)
        self.next_button = tk.Button(button_frame, text="Следующие 10", command=self.load_next, **button_style)
        self.add_button = tk.Button(button_frame, text="Добавить клиента", command=self.open_add_customer_window, **button_style)
        self.del_button = tk.Button(button_frame, text="Удалить клиента", command=self.remove_customer, **button_style)
        self.view_button = tk.Button(button_frame, text="Подробнее", command=self.view_customer_details, **button_style)

        # Размещение кнопок в строке
        self.prev_button.pack(side=tk.LEFT, padx=10)
        self.next_button.pack(side=tk.LEFT, padx=10)
        self.add_button.pack(side=tk.RIGHT, padx=10)
        self.del_button.pack(side=tk.RIGHT, padx=10)
        self.view_button.pack(side=tk.RIGHT, padx=10)

        # Загрузка данных при старте
        self.update_buttons()
        self.load_page(self.current_page)

    def update(self, customers):
        # Обновление таблицы с новыми данными
        for row in self.table.get_children():
            self.table.delete(row)
        for i, customer in enumerate(customers):
            self.table.insert(
                '', tk.END, values=(
                    customer.get_customer_id(),
                    (self.current_page - 1) * 10 + i + 1,
                    customer.get_first_name(),
                    customer.get_last_name(),
                    customer.get_phone_number()
                )
            )

    def load_page(self, page):
        # Загрузка данных для текущей страницы
        loaded_count = len(self.controller.load_customers(page, self.page_size))
        self.update_buttons(loaded_count)

    def load_previous(self):
        # Переход на предыдущую страницу
        if self.current_page > 1:
            self.current_page -= 1
            self.load_page(self.current_page)

    def load_next(self):
        # Переход на следующую страницу
        self.current_page += 1
        self.load_page(self.current_page)

    def remove_customer(self):
        # Удаление выбранного клиента
        selected_items = self.table.selection()
        if not selected_items:
            messagebox.showwarning("Внимание", "Пожалуйста, выберите клиента для удаления.")
            return

        for item in selected_items:
            customer_id = self.table.item(item, "values")[0]
            self.controller.remove_customer(int(customer_id))

        self.refresh_page()

    def update_buttons(self, loaded_count=None):
        # Обновление состояния кнопок
        self.prev_button.config(state=tk.DISABLED if self.current_page == 1 else tk.NORMAL)
        self.next_button.config(state=tk.DISABLED if loaded_count is not None and loaded_count < self.page_size else tk.NORMAL)

    def open_add_customer_window(self):
        # Открытие окна добавления нового клиента
        add_controller = AddCustomerController(self, self.controller.repository)
        add_controller.show_add_window()

    def handle_error(self, error_message):
        # Обработка ошибок при загрузке данных
        messagebox.showerror("Ошибка", f"Не удалось загрузить данные: {error_message}")

    def refresh_page(self):
        # Перезагрузка данных для текущей страницы
        self.load_page(self.current_page)

    def view_customer_details(self):
        # Просмотр подробной информации о клиенте
        selected_items = self.table.selection()
        if not selected_items:
            messagebox.showwarning("Внимание", "Пожалуйста, выберите клиента для просмотра.")
            return

        customer_id = self.table.item(selected_items[0], "values")[0]
        customer = self.controller.get_customer_by_id(int(customer_id))

        if customer:
            self.open_customer_details_window(customer)
        else:
            messagebox.showwarning("Ошибка", "Не удалось загрузить информацию о клиенте.")

    def open_customer_details_window(self, customer):
        # Окно с подробной информацией о клиенте
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Подробная информация о клиенте {customer.get_first_name()} {customer.get_last_name()}")
        details_window.geometry("400x400")

        labels = [
            f"ID: {customer.get_customer_id()}",
            f"Имя: {customer.get_first_name()}",
            f"Фамилия: {customer.get_last_name()}",
            f"Телефон: {customer.get_phone_number()}",
            f"Email: {customer.get_email()}",
            f"Адрес: {customer.get_address()}",
            f"Город: {customer.get_city()}",
            f"Почтовый код: {customer.get_postal_code()}",
            f"Страна: {customer.get_country()}",
            f"Дата добавления: {customer.get_date_joined()}"
        ]

        # Размещение информации в окне
        for label in labels:
            tk.Label(details_window, text=label, font=("Arial", 10), anchor="w").pack(padx=10, pady=5, fill='x')

        # Кнопка для закрытия окна
        close_button = tk.Button(details_window, text="Закрыть", command=details_window.destroy)
        close_button.pack(pady=10)
