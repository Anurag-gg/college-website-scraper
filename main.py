from selenium import webdriver
import time


driver = webdriver.Edge(executable_path= "enter the webdriver path" , log_path= 'NUL')
driver.get("http://exam.msrit.edu/index.php")

cap = input("enter the captcha \n")

with open('usn_is.txt' , 'w') as f:
    for i in range(1,170):
        element = driver.find_element_by_id("usn")
        element.send_keys(f"1MS20IS{i:03}-T")
        element2 = driver.find_element_by_id("osolCatchaTxt0")
        element2.send_keys(cap)



        driver.find_element_by_class_name("buttongo").click()

        
        try:
            name = driver.find_element_by_tag_name("h3")
            cgpa = driver.find_elements_by_tag_name("p")

            
            data = f'1MS20IS{i:03}-T {float(cgpa[4].text):.2f}   {name.text} \n'
            f.write(data)

            print(cgpa[4].text)
            print(name.text ) 
        except Exception as e:
            print(e)
        driver.back()
