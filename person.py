import fileinput

class Persona:
    
    
    def __init__(self, dni, lastName, firstName):
        self.dni = dni
        self.lastName = lastName
        self.firstName = firstName

        self.persona = f'dni: {self.dni}, lastName: {self.lastName}, firstName: {self.firstName}'
       

    def store(self):
        if self.check_if_exist():
            return False
        with open('personas.txt','a') as data: 
            data.write(str(self.persona) + '\n')
        return True

    def check_if_exist(self):
        with open('personas.txt') as file:
            while (line := file.readline().rstrip()):
                check = f'dni: {self.dni}, lastName: {self.lastName}, firstName: {self.firstName}'
                if check == line:
                    return True

            return False

    def update(self, lastname, firstname):
        newline = f'dni: {self.dni}, lastName: {lastname}, firstName: {firstname}'
        for line in fileinput.input('personas.txt', inplace = 1): 
            print(line.replace(self.persona, newline))
        return True

        # for line in fileinput.FileInput('personas.txt',inplace=1):
        #     if line.rstrip():
        #         print(line)


    def delete(self, target):
        with open('personas.txt', 'r') as fr:
        # reading line by line
            lines = fr.readlines()
            ptr = 1
            with open('personas.txt', 'w') as fw:
                for line in lines:
                
                    # we want to remove 5th line
                    if ptr != target:
                        fw.write(line)
                    ptr += 1
        return True

def delete_blank():
    with open('personas.txt','r+') as file:
        for line in file:
            if not line.isspace():
                file.write(line)



if __name__ == '__main__':
    # p = Persona(1, "Trump", "Donald")
    # p.store()
    # p2 = Persona(4, "example3", "Four")
    # p2.update('juan', 'suarez')
    #p.delete()
    #print(p.check_if_exist())
    delete_blank()