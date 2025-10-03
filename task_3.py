import re

def normalize_phone(phone_number):
    clean_phone = re.sub(r"[^\d+]", "", phone_number.strip())
    if clean_phone.startswith("+"):
        if clean_phone.startswith("+38"):
            return clean_phone
        elif clean_phone.startswith("+380"):
            return clean_phone
        else:
            return clean_phone
    if clean_phone.startswith("380"):
        return "+" + clean_phone

    return "+38" + clean_phone