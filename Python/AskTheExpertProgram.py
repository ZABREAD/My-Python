from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('country_capital_list.txt') as file:
       for line in file:
           line = line.rstrip('\n')
           country, capital_city = line.split('/')
           country_capital_list[country] = capital_city
        
def write_to_file(country, capital_city):
    with open('new_facts.txt', 'a') as file:
        file.write('\n' + country + '/' + capital_city)
    

           
print('Ask the Expert - Welcome to my expert country capital program')
print('Test your knowedge on worldly places.')

root = Tk()
root.withdraw()

country_capital_list = {}

read_from_file()

while True:
    query_country = simpledialog.askstring('Country', 'Type the name of a country: ')

    if query_country in country_capital_list:
        result = country_capital_list[query_country]
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result + '!')
    else:
        new_city = simpledialog.askstring('Teach Me', 'I don\'y know. Please enlighten me. give me the name of the capital city of ' + query_country + '?')
        print(new_city)
        write_to_file(query_country, new_city)

    

root.mainloop()


#print(country_capital_list)
