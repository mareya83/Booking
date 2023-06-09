from time import sleep

from selenium.webdriver.common.by import By


class Actions:

    def __init__(self, driver: dict):
        self.driver = driver

    def send_keys(self, element, test_data):
        pass

    def click(self):
        pass

    def take_screenshot(self):
        pass

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def type_date(self, date):
        return self.find_element(By.XPATH, f"//span[@data-date='{date}']").click()

    def type_date(self, date):
        return self.find_element(By.XPATH, f"//span[@data-date='{date}']").click()

    def test_form(self, data: list, test_elements: list):
        print(data)

        elements_to_test = []

        self.driver.get("http://booking.com")

        sleep(10)

        self.find_element(
            By.XPATH, "//button[@aria-label='Скрыть меню входа в аккаунт.']").click()

        sleep(1)

        for test_element in test_elements:

            found_element = self.find_element(
                By.XPATH, list(test_element.values())[0])

            key = list(test_element.keys())[0]

            elements_to_test.append(
                {key: found_element})

        for element in elements_to_test:
<<<<<<< HEAD

            key = list(element.keys())[0]
            found_element = list(element.values())[0]

            for data_obj in data:
                data_obj_key = list(data_obj.keys())[0]
                data_obj_values = list(data_obj.values())[0]


                if data_obj_key == key:
                    found_element.click()
                    sleep(2)

                    if data_obj_key == "Date":
                        self.type_date(data_obj_values)
                        

                    elif data_obj_key == "Person":


                        elements_persons = ["Adults","Chilren","Rooms"]
                        persons = data_obj_values.split(",")

                        for i in range(len(elements_persons)):

                            if elements_persons[i] == "Adults":
                                persons[i] = int(persons[i]) - 2

                            elif elements_persons[i] == "Rooms":
                                persons[i] = int(persons[i]) - 1
                            
                            else :
                                persons[i] = int(persons[i])


                        test_elements_persons = self.find_elements(By.XPATH, "//button[@class='fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 d64a4ea64d']")
                        
                        for i in range(len(test_elements_persons)):
                            if persons[i] < 2 and elements_persons[i] == "Adults":

                                self.find_element(By.XPATH, "//button[@class='fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 cd7aa7c891']").click()

                            else:
                                for klick in range(persons[i]):
                                    test_elements_persons[i].click()
                        

                        sleep(10)

                    else:
                        found_element.send_keys(data_obj_values)
=======
            key = list(element.keys())[0]
            print("[KEY]", key)

            found_element = list(element.values())[0]
            print("[FOUND_ELEMENT]", found_element)
>>>>>>> 1e80e61ee22fccc88cb090db9049961375b6595a

            for data_obj in data:
                data_obj_key = list(data_obj.keys())[0]
                data_obj_values = list(data_obj.values())[0]

<<<<<<< HEAD
=======
                if data_obj_key == key:
                    sleep(2)
                    # YYYY:MM:DD
                    found_element.click()

                    if data_obj_key == 'Date':
                        self.type_date(data_obj_values)
                    else:
                        found_element.send_keys(data_obj_values)

                    # HW : Find how many person will book hotel
                    # Clue : 1) find elements ( button + )
                    # 2) Think how do user might to type "How many person will book hotel"
                    # Variety of :through "-" first number is -> how many of adults there ,first number -> how many children , third number -> how many rooms
                    # example : 2-1-1

        sleep(1)

>>>>>>> 1e80e61ee22fccc88cb090db9049961375b6595a
        print(elements_to_test)
