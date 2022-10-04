import mariadb
import dbcreds
import dbhelper


# password_input = user_info()

def login_info():
    username_input = input('please enter your username:')
    password_input = input('please enter your password:')
    results = dbhelper.run_statment('CALL check_username_password()' [username_input], [password_input])
    return results
    # return None (need confitional return id if exist else return none)


def post_content():
    blog_title = input('please enter your blog title:')
    blog_content = input('please enter your blog content:')
    results = dbhelper.run_statment('CALL blog_post(?)' [blog_title], [blog_content])
    return results

# def get_posts():
    

# login_info()
post_content()