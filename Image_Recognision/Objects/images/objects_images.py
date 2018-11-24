def get_variables():
    variables = {"INPUT_LOGIN": "id:login_login_username",
                 "INPUT_PASSWORD": "id:login_login_password",
                 "SUBMIT_BUTTON": "id:login_submit",
                 "ERROR_MSG": "You have not provided the correct credentials to log in. "
                              "Please check your username and password are correct.",
                 "ERROR_ELE": "//div[contains(@class, 'alert')]",                 
                 "SUCCESSFUL_LOGIN_ELE": "id:sb-profile"
                 }
    return variables
