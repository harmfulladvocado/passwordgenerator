import secrets
import string
import math

AMBIGUOUS = {'I', 'l', '1', 'O', '0'}

def ask_yesno(prompt, default=True):
    d = "Y/n" if default else "y/N"
    ans = input(f"{prompt} ({d}): ").strip().lower()
    if ans == "":
        return default
    return ans[0] == "y"

def get_int(prompt, minv, maxv, default=None):
    while True:
        s = input(f"{prompt}" + (f" [{default}]" if default is not None else "") + ": ").strip()
        if s == "" and default is not None:
            return default
        try:
            v = int(s)
            if minv <= v <= maxv:
                return v
        except ValueError:
            pass
        print(f"Invalid input — enter an integer between {minv} and {maxv}.")

def build_charset(include_lower, include_upper, include_digits, include_punct, exclude_ambiguous):
    chosen = []
    if include_lower:
        chosen.append(string.ascii_lowercase)
    if include_upper:
        chosen.append(string.ascii_uppercase)
    if include_digits:
        chosen.append(string.digits)
    if include_punct:
        chosen.append(string.punctuation)
    if not chosen:
        chosen = [
            string.ascii_lowercase,
            string.ascii_uppercase,
            string.digits,
            string.punctuation,
        ]
    groups = []
    for grp in chosen:
        if exclude_ambiguous:
            grp = "".join(ch for ch in grp if ch not in AMBIGUOUS)
        if grp:
            groups.append(grp)
    charset = "".join(sorted({c for g in groups for c in g}))
    return charset, groups

def secure_shuffle(seq):
    for i in range(len(seq) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        seq[i], seq[j] = seq[j], seq[i]

def generate_password(length, charset, required_groups):
    if not charset:
        return ""
    charset_list = list(charset)
    charset_set = set(charset_list)
    pwd = []
    for grp in required_groups:
        candidates = [c for c in grp if c in charset_set]
        if candidates:
            pwd.append(secrets.choice(candidates))
    remaining = length - len(pwd)
    if remaining > 0:
        pwd.extend(secrets.choice(charset_list) for _ in range(remaining))
    secure_shuffle(pwd)
    return "".join(pwd)

def estimate_entropy(length, pool_size):
    if pool_size <= 1:
        return 0.0
    return length * math.log2(pool_size)

if __name__ == "__main__":
    print("Password generator")
    length = get_int("How many characters? (4-128)", 4, 128, default=16)
    count = get_int("Number of passwords to generate? (1-20)", 1, 20, default=1)

    lower = True
    upper = True
    digits = True
    punct = True
    exclude_amb = True

    charset, groups = build_charset(lower, upper, digits, punct, exclude_amb)
    pool_size = len(charset)
    if pool_size == 0:
        print("There are no characters to build a password. Adjust your choices.")
    else:
        nonempty_groups = [g for g in groups if any(c in charset for c in g)]
        needed = len(nonempty_groups)
        if needed > length:
            print(f"Length adjusted from {length} to {needed} so each selected type gets at least one character.")
            length = needed
        entropy = estimate_entropy(length, pool_size)
        print(f"\nPool size: {pool_size} characters — Estimated entropy per password: {entropy:.1f} bits\n")
        for i in range(count):
            print(f"{i+1}: {generate_password(length, charset, groups)}")
