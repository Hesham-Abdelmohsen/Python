# from abc import ABC




class User :

    __slots__ = ['search_user_name', 'search_password', 'first_name', 'last_name', 'user_name']

    def login_page(self):

        print('*******************************************************************')
        print('Welcome to the Quiz game program V2.0!')
        print('*******************************************************************')

        while True:

            search_user_name = input('Please enter your username: ')
            search_password = input('Please enter your password: ')

            for i in range(len(objects)):

                if objects[i].user_name == search_user_name :

                    if objects[i].password == search_password :
                        objects[i].main_menue()

                    else:
                        print('wrong user name or password')
                        break
                else :
                    print('wrong user name or password')
                    break

            continue

    def switch_account(self):

        print('**************')
        print('you logged out')
        print('**************')
        self.login_page()

    def update_your_name(self):

        self.first_name = input('enter your new first name: ')
        self.last_name = input('enter your new last name: ')
        self.main_menue()



    def set_information(self):

        while True:

            self.user_name = input('please enter your user name : ')

            for i in range(len(objects)):

                if self == objects[i]:
                    print('this user name already exist , please enter another one ')
                    break

                elif i == len(objects)-1 :
                    self.password = input('please enter your password : ')
                    self.first_name = input('please enter first name : ')
                    self.last_name = input('please enter last name : ')
                    objects.append(self)
                    return

            continue

    def __eq__(self, other):

        if self.user_name == other.user_name:
            return True

        else:
            return False



    def Exist_the_program(self):
        exit()

# //***************************************************************//
# //***************************************************************//

class Admin(User):

    __slots__ = ['first_name', 'last_name', 'user_name', 'password', 'role', 'choice', 'test_user_name', 'test_role']

    def __init__(self):

        self.first_name = 'user'
        self.last_name = 'user'
        self.user_name = 'admin'
        self.password = '123'
        self.role = 'admin'
        # self.choice = 0

    def main_menue(self):

        print('Welcome', self.first_name, self.last_name , '(ADMIN), please choose from the following options: ')
        print('[1] Switch accounts ')
        print('[2] Update your name ')
        print('[3] View all users ')
        print('[4] Add new user ')
        print('[5] View all questions ')
        print('[6] Add new question ')
        print('[7] Load questions from file ')
        print('[8] Exit the program ')

        while True:
            self.choice = int(input('My choice: '))

            if self.choice < 1 or self.choice > 8 :
                print('please enter valid choice number from 1 to 8 ')
                continue

            else:
                if self.choice == 1:
                    self.switch_account()

                elif self.choice == 2:
                    self.update_your_name()

                if self.choice == 3:
                    self.view_all_users()

                if self.choice == 4:
                    self.add_new_user()

                if self.choice == 5:
                    self.view_all_question()

                if self.choice == 6:
                    self.add_new_question()

                if self.choice == 7:
                    self.load_question_from_file()

                if self.choice == 8:
                    self.Exist_the_program()




    def view_all_users(self):

        print('Existing users in the system: ')
        print("{:15}{:15}{:15}{:15}".format('First name ', 'Last name ', 'Username ', 'Role '))
        for i in range(len(objects)):
            print("{:15}{:15}{:15}{:15}".format(objects[i].first_name, objects[i].last_name, objects[i].user_name, objects[i].role))

        print('Press [n] if you want to add a new user or [b] to go back to the main menu. ')

        while True:

            self.choice = input()

            if self.choice == 'n':
                self.add_new_user()


            elif self.choice == 'b':
                self.main_menue()

            else:
                print('invalid choice, please enter [n] or [b] only ')
                continue






    def add_new_user(self):

        while True:
            self.test_role = input('enter your role "admin" OR "player": ')

            if self.test_role == 'admin':
                obj_admin =  Admin()
                obj_admin.set_information()
                break

            elif self.test_role == 'player':
                obj_player = Player()
                obj_player.set_information()
                break

            else:
                print('**************')
                print('invalid choice')
                print('**************')
                continue

        self.choice =input('Press [n] if you want to switch account or [b] to go back to the main menu. ')

        while True :

            if self.choice == 'n':
                self.switch_account()
                break

            elif self.choice == 'b':
                self.main_menue()
                break

            else:
                print('invalid choice, please enter [n] or [b] only ')
                continue

    def add_new_question(self):

        all_question_object.add_new_question()
        self.view_all_question()


    def view_all_question(self):

        all_question_object.view_all_question()

    def load_question_from_file(self):

        all_question_object.load_question_from_file()









# //***************************************************************//
# //***************************************************************//

class Player(User):

    __slots__ = ['first_name', 'last_name', 'user_name', 'password', 'role', 'choice']

    def __init__(self):
        self.first_name = 'user'
        self.last_name = 'user'
        self.user_name = 'player'
        self.password = '123'
        self.role = 'player'

    def main_menue(self):


        print('Welcome', self.first_name, self.last_name , '(PLAYER), please choose from the following options: ')
        print('[1] Switch accounts ')
        print('[2] Update your name ')
        print('[3] Start a new quiz ')
        print('[4] Display your scores statistics ')
        print('[5] Display all your scores ')
        print('[6] Display details of your last 2 quizzes ')
        print('[7] Exit the program ')

        while True:

            self.choice = int(input('My choice: '))

            if self.choice < 1 or self.choice > 7:
                print('please enter valid choice number from 1 to 8 ')
                continue

            else:
                if self.choice == 1:
                    self.switch_account()

                elif self.choice == 2:
                    self.update_your_name()

                if self.choice == 3:
                    self.start_new_quiz()

                if self.choice == 4:
                    self.display_all_your_scores_statistics()

                if self.choice == 5:
                    self.display_all_your_scores()

                if self.choice == 6:
                    self.display_details_for_last_2_quizes()

                if self.choice == 7:
                    self.Exist_the_program()

# //***************************************************************//
# //***************************************************************//
class All_quesion:

    def load_question_from_file(self):

        try:
            text = input('please enter file name: ')
            text += '.txt'
            f = open(text, 'r')

            count = 0
            for line in f:
                count += 1

            f.seek(0)

            i = 0

            while i < count:

                x = f.readline()

                if x == 'MCQ\n':

                    m = MCQ()

                    m.question = f.readline()



                    m.choice1 = f.readline()
                    m.choice2 = f.readline()
                    m.choice3 = f.readline()
                    m.choice4 = f.readline()
                    m.right_answer = m.choice1
                    mcq_lst.append(m)

                    i += 5



                elif x == 'TF\n':
                    t = TF()
                    t.question = f.readline()
                    t.right_answer = f.readline()
                    i += 2

                    tf_lst.append(t)



                elif x == 'COMPLETE\n':
                    c = Complete()
                    c.question = f.readline()
                    c.right_answer = f.readline()
                    i += 2
                    complete_lst.append(c)

                i += 1

        except IOError as e:   # check if file exist or not
            print('Unable to open the file: ', e)




    def view_all_question(self):

        if len(mcq_lst) + len(tf_lst) +len(complete_lst) < 1 :
            print('you must add question first ')
            return

        print('Number of questions available:', len(mcq_lst) + len(tf_lst) + len(complete_lst))

        mcq_obj.view_all_question()
        tf_obj.view_all_question()
        complete_obj.view_all_question()

        while True:
            print('-------------------------------------------------------------------------------------')
            print('Press [d] and the question ID if you want to delete a question (Example: d 2)')
            print('Press [b] if you want to go back to the main menu')

            self.choice = input().split()

            if self.choice[0] == 'd':

                if int(self.choice[1]) < 3 or int(self.choice[1]) > ID:
                    print('invalid, please enter a valid ID')
                    continue

                else:
                    self.delete_question()
                    self.view_all_question()


            elif self.choice[0] == 'b':
                admin_object.main_menue()

            else:
                print('invalid')
                continue


    def delete_question(self):

        for i in range(len(mcq_lst)):
            if mcq_lst[i].id == int(self.choice[1]):
                del mcq_lst[i]
                return

        for i in range(len(tf_lst)):
            if tf_lst[i].id == int(self.choice[1]):
                del tf_lst[i]
                return

        for i in range(len(complete_lst)):
            if complete_lst[i].id == int(self.choice[1]):
                del complete_lst[i]
                return

    def add_new_question(self):

        while True:

            self.choice = input('mcq or tf or complete: ')

            if self.choice == 'mcq':
                object_mcq = MCQ()
                object_mcq.add_new_question()
                return

            elif self.choice == 'tf':
                object_tf = TF()
                object_tf.add_new_question()
                return

            elif self.choice == 'complete':
                object_complete = Complete()
                object_complete.add_new_question()
                return

            else:
                print('invalid choice')
                continue


    def __eq__(self, other):

        if self.question == other.question:
            return True
        else:
            return False


# //***************************************************************//
# //***************************************************************//
class MCQ(All_quesion):

    __slots__ = ['question', 'choice1', 'choice2', 'choice3', 'choice4', 'right_answer', 'id']

    def __init__(self):
        global ID
        self.id = ID
        ID += 1

    def view_all_question(self):

        print('---------------------------------------------------')
        print('MC Questions list (Total:', len(mcq_lst),'Questions)')
        print('---------------------------------------------------')

        for i in range(len(mcq_lst)):
            print( '[' + str(i+1) + ']' + '(ID:' + str(mcq_lst[i].id) + ')' , mcq_lst[i].question )
            print("{:20}{:15}{:15}{:15}".format("     *[a]" + mcq_lst[i].choice1  , "[b]"+  mcq_lst[i].choice2 , "[c]" + mcq_lst[i].choice3 , "[d]" +  mcq_lst[i].choice4 ))








    def add_new_question(self):
        while True:
            self.question = input('enter the question: ')

            for i in range(len(mcq_lst)):
                if self == mcq_lst[i]:
                    print('this question in already exist ')
                    continue

            self.choice1 = input('enter the first choice : ')
            self.choice2 = input('enter the second choice: ')
            self.choice3 = input('enter the third choice : ')
            self.choice4 = input('enter the fourth choice: ')
            self.right_answer = input('enter the right answer: ')
            mcq_lst.append(self)
            return

# //***************************************************************//
# //***************************************************************//
class TF(All_quesion):

    __slots__ = ['question', 'right_answer', 'id']

    def __init__(self):

        global ID
        self.id = ID
        ID += 1





    def view_all_question(self):

        print('---------------------------------------------------')
        print('TF Questions list (Total:', len(tf_lst), 'Questions)')
        print('---------------------------------------------------')

        for i in range(len(tf_lst)):
            print('[' + str(i + 1) + ']' + '(ID:' + str(tf_lst[i].id) + ')', tf_lst[i].question + '(Answer:' + tf_lst[i].right_answer + ')' )

    def add_new_question(self):
        while True:
            self.question = input('enter the question: ')

            for i in range(len(tf_lst)):
                if self == tf_lst[i]:
                    print('this question in already exist ')
                    continue

            self.right_answer = input('enter the right answer: ')
            tf_lst.append(self)
            return


# //***************************************************************//
# //***************************************************************//
class Complete(All_quesion):

    __slots__ = ['question', 'right_answer', 'id']


    def __init__(self):
        global ID
        self.id = ID
        ID += 1



    def view_all_question(self):

        print('---------------------------------------------------')
        print('Complete Questions list (Total:', len(complete_lst),'Questions)')
        print('---------------------------------------------------')

        for i in range(len(complete_lst)):
            print('[' + str(i + 1) + ']' + '(ID:' + str(complete_lst[i].id) + ')', complete_lst[i].question + '(Answer:' + complete_lst[i].right_answer + ')' )










    def add_new_question(self):
        while True:
            self.question = input('enter the question: ')

            for i in range(len(complete_lst)):
                if self == complete_lst[i]:
                    print('this question in already exist ')
                    continue

            self.right_answer = input('enter the right answer: ')
            complete_lst.append(self)
            return


# //***************************************************************//
# //***************************************************************//

ID = 0

mcq_lst = []
tf_lst = []
complete_lst = []
all_question_object = All_quesion()


mcq_obj =  MCQ()
tf_obj = TF()               # for accessing classes
complete_obj = Complete()



admin_object = Admin()
# admin_object.main_menue()

player_object = Player()

# admin_object.load_questionx_from_file()

objects = []  # for storing users
#
objects.append(admin_object)
objects.append(player_object)

admin_object.load_question_from_file()


