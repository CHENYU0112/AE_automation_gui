@staticmethod
def validate_entry(P):
        return P == "" or P == "." or (P.count('.') <= 1 and P.replace('.', '').isdigit())

@staticmethod
def validate_vin_entry(P):
        if P == "":
            return True
        parts = P.split(',')
        return all(part.strip() == "" or part.strip() == "." or (part.strip().count('.') <= 1 and part.strip().replace('.', '').isdigit()) for part in parts)

@staticmethod
def validate_eload_entry(P):
        if P == "":
            return True
        parts = P.split(',')
        return all(part.strip() == "" or part.strip() == "." or (part.strip().count('.') <= 1 and part.strip().replace('.', '').isdigit()) for part in parts)
@staticmethod
def safe_float_list(value, field_name):
        try:
                return [float(v.strip()) for v in value.split(',') if v.strip()]
        except ValueError:
                raise ValueError(f"Invalid input for {field_name}")
@staticmethod
def safe_float(value, field_name):
        try:
                return float(value) if value else 0
        except ValueError:
                raise ValueError(f"Invalid input for {field_name}")
