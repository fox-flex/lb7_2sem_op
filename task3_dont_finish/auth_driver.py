from os import path
import auth
from document import GoOutOfDoc

# Set up a test user and permission
auth.authenticator.add_user('root', 'password')
auth.authorizor.add_permission('add permission')
auth.authorizor.add_permission('read document')
auth.authorizor.add_permission('create user')
auth.authorizor.permit_user('su', 'root')
permissions = ('su', 'add permission', 'read document', 'create user')


class Editor:
    def __init__(self):
        self.username = None
        self.notebook = None
        self.menu_map = {
            "login": self.login,
            "add permission": self.add_permission_so_sb,
            "add user": self.add_new_user,
            # "read doc": self.read_doc,
            "read notebook": self.read_notebook,
            # "change doc": self.change_doc,
            "change notebook": self.change_notebook,
            # "save doc": self.save_doc,
            "save notebook": self.save_notebook,
            "quit": self.quit,
        }
        self.permissions = {'0': 'su', '1': 'add permission',
                            '2': 'read document', '3': 'create user'}

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username
                self.notebook = auth.authenticator.users[
                                                        self.username].notebook
                print('You successfully log in!')

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print(f"{e.username} is not logged in")
            return False
        except auth.NotPermittedError as e:
            print(f"{e.username} cannot {permission}")
            return False
        else:
            return True

    def add_new_user(self):
        if self.is_permitted('add user'):
            while True:
                nickname = input('Print name of new user:\t')
                password1 = input('Print password of new user:\t')
                password2 = input('Repeat password of new user:\t')
                if password1 == password2:
                    try:
                        auth.authenticator.add_user(nickname, password1)
                        auth.authorizor.permit_user('read doc', nickname)
                        auth.authorizor.permit_user('change doc', nickname)
                        auth.authorizor.permit_user('save doc into file',
                                                    nickname)
                        break
                    except auth.UsernameAlreadyExists:
                        print(f"Username {nickname} already exists, "
                              f"try another one!")
                    except auth.PasswordTooShort:
                        print(f"Username {nickname} too short, "
                              f"take stronger one!")
            print(f'You successfully create user {nickname}!')

    def add_permission_so_sb(self):
        if self.is_permitted('add permission'):
            print('To who you wanna give some permission?')
            nicknames = {str(i): name for i, name in
                         enumerate(auth.authenticator.users.keys())}
            for i, nickname in nicknames.items():
                print(f'\t{i} - {nickname}')
            while True:
                num = input("enter a number: ")
                try:
                    nickname = nicknames[num]
                    break
                except KeyError:
                    print(f"'{num}' is not a valid number, try again!")

            print('Which permission you wanna give?')
            for i, permission in self.permissions.items():
                print(f'\t{i} - {permission}')
            while True:
                num = input("enter a number: ")
                try:
                    permission = self.permissions[num]
                    break
                except KeyError:
                    print(f"'{num}' is not a valid number, try again!")
            auth.authorizor.permit_user(permission, nickname)
            print(f'You successfully add permission of {permission} to '
                  f'user {nickname}!')

    def read_notebook(self):
        if self.is_permitted("read notebook"):
            print('Your doc:\n' + '_' * 60)
            print(auth.authenticator.users[self.username].document)
            if not self.notebook:
                print('your notebook is empty')
                # notes = self.notebook.notes
            else:
                for note in self.notebook:
                    print(f"ID: {note.id}; tags: {note.tags}\n{note.memo}")
            print('_' * 60)

    def change_doc(self):
        if self.is_permitted("change doc"):
            doc = auth.authenticator.users[self.username].document
            print('Your doc:\n' + '_' * 60)
            print(doc)
            print('_' * 60)
            print('what you wanna to do?')
            chooses = {'0': 'change some line', '1': 'add new line'}
            for i, choose in chooses.items():
                print(f'{i}\t- {choose}')
            while True:
                choose = input("enter a number of command: ")
                try:
                    choose = chooses[choose]
                    break
                except KeyError:
                    print(f"'{choose}' is not a valid number, try again!")
            num_lines = str(doc).count('\n') + 1
            if choose == 'change some line':
                print(f'there are {num_lines} lines')
                while True:
                    num_line_to_change = input("enter a number of line "
                                               "which you wanna change: ")
                    try:
                        num_line_to_change = int(num_line_to_change)
                        if not (0 <= num_line_to_change < num_lines):
                            raise ValueError
                        break
                    except (TypeError, ValueError):
                        print(f"'{choose}' is not a valid number, try again!\n")

                for _ in range(num_line_to_change):
                    doc.cursor.end()
                    doc.cursor.forward()
                print(doc.cursor.position)
                while len(doc.characters) > doc.cursor.position and\
                        doc.characters[doc.cursor.position] != '\n':
                    doc.delete()

                is_bold = input('type \'y\' if this line should be bold:\t')
                is_italic = input('type \'y\' if this line should be '
                                  'italic:\t')
                is_underline = input('type \'y\' if this line should be '
                                     'underline:\t')
                new_text = input('enter new text in this line:\n')
                for char in new_text:
                    doc.insert(auth.Character(char, bold=is_bold,
                                              italic=is_italic,
                                              underline=is_underline))
            elif choose == 'add new line':
                print(f'there are {num_lines} lines')
                while True:
                    line_before_which_add = input("enter a number of line, "
                                                  "after which you wanna add "
                                                  "one more line: ")
                    try:
                        line_before_which_add = int(line_before_which_add)
                        if not (0 <= line_before_which_add < num_lines):
                            raise ValueError
                        break
                    except (TypeError, ValueError):
                        print(f"'{line_before_which_add}' is not a valid "
                              f"number, try again!\n")
                if not line_before_which_add == 0:
                    after_line = input('if you want to insert line after '
                                       'taken line print \'y\': ') == 'y'
                    after_line = 1 if after_line else 0
                    try:
                        for _ in range(line_before_which_add + after_line):
                            doc.cursor.end()
                            doc.cursor.forward()
                    except GoOutOfDoc:
                        doc.insert(auth.Character('\n'))
                # while doc.characters[doc.cursor.position] != '\n':
                #     doc.delete()
                is_bold = input('type \'y\' if this line should be bold:\t')
                is_italic = input('type \'y\' if this line should be '
                                  'italic:\t')
                is_underline = input('type \'y\' if this line should be '
                                     'underline:\t')
                new_text = input('enter new text in this line:\n')
                for char in new_text:
                    doc.insert(auth.Character(char, bold=is_bold,
                                              italic=is_italic,
                                              underline=is_underline))
                doc.insert(auth.Character('\n', bold=is_bold,
                                          italic=is_italic,
                                          underline=is_underline))
            doc.cursor.position = 0

    def change_notebook(self):
        if self.is_permitted("change notebook"):
            # print('Your doc:\n' + '_' * 60)
            # print(doc)
            # print('_' * 60)
            print('what you wanna to do?')
            chooses = {'0': 'change some note', '1': 'add new note'}
            for i, choose in chooses.items():
                print(f'{i}\t- {choose}')
            while True:
                choose = input("enter a number of command: ")
                try:
                    choose = chooses[choose]
                    break
                except KeyError:
                    print(f"'{choose}' is not a valid number, try again!")
            num_lines = str(self.notebook).count('\n') + 1
            if choose == 'change some note':
                print(f'there are {len(self.notebook.notes)} notes')
                while True:
                    num_line_to_change = input("enter a ID of note "
                                               "which you wanna change: ")
                    try:
                        num_line_to_change = int(num_line_to_change)
                        if not (0 < num_line_to_change <
                                self.notebook.notes+1):
                            raise ValueError
                        break
                    except (TypeError, ValueError):
                        print(f"'{choose}' is not a valid number, try again!\n")

                for _ in range(num_line_to_change):
                    doc.cursor.end()
                    doc.cursor.forward()
                print(doc.cursor.position)
                while len(doc.characters) > doc.cursor.position and\
                        doc.characters[doc.cursor.position] != '\n':
                    doc.delete()

                is_bold = input('type \'y\' if this line should be bold:\t')
                is_italic = input('type \'y\' if this line should be '
                                  'italic:\t')
                is_underline = input('type \'y\' if this line should be '
                                     'underline:\t')
                new_text = input('enter new text in this line:\n')
                for char in new_text:
                    doc.insert(auth.Character(char, bold=is_bold,
                                              italic=is_italic,
                                              underline=is_underline))
            elif choose == 'add new line':
                print(f'there are {num_lines} lines')
                while True:
                    line_before_which_add = input("enter a number of line, "
                                                  "after which you wanna add "
                                                  "one more line: ")
                    try:
                        line_before_which_add = int(line_before_which_add)
                        if not (0 <= line_before_which_add < num_lines):
                            raise ValueError
                        break
                    except (TypeError, ValueError):
                        print(f"'{line_before_which_add}' is not a valid "
                              f"number, try again!\n")
                if not line_before_which_add == 0:
                    after_line = input('if you want to insert line after '
                                       'taken line print \'y\': ') == 'y'
                    after_line = 1 if after_line else 0
                    try:
                        for _ in range(line_before_which_add + after_line):
                            doc.cursor.end()
                            doc.cursor.forward()
                    except GoOutOfDoc:
                        doc.insert(auth.Character('\n'))
                # while doc.characters[doc.cursor.position] != '\n':
                #     doc.delete()
                is_bold = input('type \'y\' if this line should be bold:\t')
                is_italic = input('type \'y\' if this line should be '
                                  'italic:\t')
                is_underline = input('type \'y\' if this line should be '
                                     'underline:\t')
                new_text = input('enter new text in this line:\n')
                for char in new_text:
                    doc.insert(auth.Character(char, bold=is_bold,
                                              italic=is_italic,
                                              underline=is_underline))
                doc.insert(auth.Character('\n', bold=is_bold,
                                          italic=is_italic,
                                          underline=is_underline))
            doc.cursor.position = 0

    def save_doc(self):
        if self.is_permitted("change doc"):
            file_name0 = f'./docs/doc_{self.username}'
            file_name = file_name0
            num = 0
            while path.exists(file_name):
                file_name = file_name0 + f'_{num}'
                num += 1
            auth.authenticator.users[self.username].document.save(file_name)

    def save_notebook(self):
        if self.is_permitted("change doc"):
            file_name0 = f'./docs/doc_{self.username}'
            file_name = file_name0
            num = 0
            while path.exists(file_name):
                file_name = file_name0 + f'_{num}'
                num += 1
            auth.authenticator.users[self.username].document.save(file_name)

    def quit(self):
        raise SystemExit()

    def menu(self):
        commands = {'1': 'login', '2': 'add permission', '3': 'add user',
                    '4': 'read doc', '5': 'change doc', '6': 'save doc',
                    '7': 'quit'}
        try:
            while True:
                print(
                    """
Please enter a command:
\t1 - login\tLogin
\t2 - add permission\tAdd permission of something to somebody
\t3 - add user\tAdd new user
\t4 - read notebook\tReed doc of this user
\t5 - change notebook\tChange doc of this user
\t6 - save notebook\tSave doc into the file
\t7 - quit\tQuit
"""
                )

                # answer = input("enter a number of command: ").lower()
                answer = input("enter a number of command: ")
                try:
                    func = self.menu_map[commands[answer]]
                except KeyError:
                    print(f"'{answer}' is not a valid option")
                else:
                    func()
        finally:
            print("Thank you for using the auth module")


if __name__ == '__main__':
    Editor().menu()
