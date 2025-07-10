def emailValidation(validator, email):
    return "Email is not correct." if validator(email) else "Email is correct."

doesNotStartWithAt = lambda email: not email.startswith("@")
print(emailValidation(doesNotStartWithAt, "@gmail.com"))
print(emailValidation(doesNotStartWithAt, "kkk@gmail.com"))

doesNotHaveSpace = lambda email: " " in email
print(emailValidation(doesNotHaveSpace, "Hello world"))
print(emailValidation(doesNotHaveSpace, "Helloworld"))

hasUppercaseAndLowercase = lambda email: any(c.islower() for c in email) and any(c.isupper() for c in email)
print(emailValidation(hasUppercaseAndLowercase, "hello world"))
print(emailValidation(hasUppercaseAndLowercase, "HELLO WORLD"))
print(emailValidation(hasUppercaseAndLowercase, "Hello world"))