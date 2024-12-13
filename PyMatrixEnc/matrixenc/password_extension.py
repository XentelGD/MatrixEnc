def extend_password(password, length):

    final_pass = ""

    while len(final_pass) < length:
        final_pass += password

    final_pass = final_pass[0:length]
    return final_pass
