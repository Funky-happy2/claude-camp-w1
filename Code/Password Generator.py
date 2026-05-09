import random
import string

lang_choice = input("🌐 Select language / 选择语言:\n1. 🇺🇸 English\n2. 🇨🇳 中文 (Chinese)\nChoose / 选择 (1 or 2): ").strip()
lang = "zh" if lang_choice == "2" else "en"

T = {
    "en": {
        "welcome": "🔐 Password Generator 🛡️",
        "preset_prompt": (
            "\n🏛️  Select a password regulation preset:\n"
            " 1. 🇺🇸 NIST Modern (US Gov)        — 15+ chars, any printable, no forced complexity\n"
            " 2. 💳 PCI-DSS (Finance)           — 12+ chars, upper+lower+digit+symbol required\n"
            " 3. 🏥 HIPAA (Healthcare)          — 8+ chars, upper+lower+digit+symbol required\n"
            " 4. 🏦 Chase Bank                  — 8-32 chars, limited symbols (!#$%+/=@~), no consecutive repeats\n"
            " 5. 📦 Amazon                      — 6-16 chars, must meet 3 of 4 character types\n"
            " 6. 💸 PayPal                      — 7-32 chars, no quotes, ampersand, or spaces\n"
            " 7. 🇫🇷 Ameli.fr (French Health)    — digits only, no sequential runs (e.g. 123)\n"
            " 8. 🛒 Alibaba                     — exactly 2 upper + 2 lower + 2 digits + 2 symbols (8 chars)\n"
            " 9. 🇦🇺 Bendigo Bank (Australia)    — exactly 8 characters, any type\n"
            "10. 🏛️  BBVA / Legacy Banking       — 1-6 chars, letters and numbers only\n"
            "11. 🎮 Runescape / Gaming          — letters and numbers only, no special chars\n"
            "12. ⚙️  Custom                      — choose your own character set\n"
            "Choose (1-12): "
        ),
        "enter_length": "📏 Enter password length: ",
        "enter_length_range": "📏 Enter password length ({min}-{max}): ",
        "enter_length_min": "📏 Enter password length (min {min}): ",
        "length_fixed": "📌 This preset always generates exactly {length} characters.",
        "char_type_prompt": (
            "🔣 Character set:\n"
            "1. 🔢 Numbers only\n"
            "2. 🔤 Letters and numbers\n"
            "3. 🔡 Letters, numbers, and common symbols (!@#$%^&*)\n"
            "4. ⌨️  All keyboard characters\n"
            "Choose (1-4): "
        ),
        "generated": "\n🔑 Password: {password}",
        "again": "\n🔄 Generate another? (yes/no): ",
        "goodbye": "👋 Goodbye! Stay secure! 🔒",
        "ok_again": "✅ Generating another password...",
        "invalid_again": "❓ Invalid input. Generating another password...",
    },
    "zh": {
        "welcome": "🔐 密码生成器 🛡️",
        "preset_prompt": (
            "\n🏛️  选择密码规范预设：\n"
            " 1. 🇺🇸 NIST现代标准（美国政府）    — 15+字符，任意可打印字符，无强制复杂度\n"
            " 2. 💳 PCI-DSS（金融）             — 12+字符，需含大小写字母、数字和符号\n"
            " 3. 🏥 HIPAA（医疗）               — 8+字符，需含大小写字母、数字和符号\n"
            " 4. 🏦 大通银行                    — 8-32字符，有限符号，不允许连续重复字符\n"
            " 5. 📦 亚马逊                      — 6-16字符，需满足4类中的3类\n"
            " 6. 💸 PayPal                      — 7-32字符，不允许引号、&符或空格\n"
            " 7. 🇫🇷 Ameli.fr（法国医保）        — 仅数字，不允许连续序列（如123）\n"
            " 8. 🛒 阿里巴巴                    — 恰好2大写+2小写+2数字+2符号（共8字符）\n"
            " 9. 🇦🇺 本迪戈银行（澳大利亚）      — 恰好8个字符，任意类型\n"
            "10. 🏛️  BBVA/传统银行               — 1-6字符，仅字母和数字\n"
            "11. 🎮 Runescape/游戏平台          — 仅字母和数字，无特殊字符\n"
            "12. ⚙️  自定义                      — 选择自己的字符集\n"
            "请选择（1-12）："
        ),
        "enter_length": "📏 请输入密码长度：",
        "enter_length_range": "📏 请输入密码长度（{min}-{max}）：",
        "enter_length_min": "📏 请输入密码长度（最少{min}字符）：",
        "length_fixed": "📌 此预设生成固定{length}个字符。",
        "char_type_prompt": (
            "🔣 字符集：\n"
            "1. 🔢 仅数字\n"
            "2. 🔤 字母和数字\n"
            "3. 🔡 字母、数字和常见符号（!@#$%^&*）\n"
            "4. ⌨️  所有键盘字符\n"
            "请选择（1-4）："
        ),
        "generated": "\n🔑 密码：{password}",
        "again": "\n🔄 是否再生成一个？（是/否）：",
        "goodbye": "👋 再见！注意安全！🔒",
        "ok_again": "✅ 正在生成另一个密码...",
        "invalid_again": "❓ 无效输入，正在生成另一个密码...",
    }
}

t = T[lang]

UPPER          = string.ascii_uppercase
LOWER          = string.ascii_lowercase
DIGITS         = string.digits
CHASE_SYMBOLS  = "!#$%+/=@~"
COMMON_SYMBOLS = "!@#$%^&*()"
PAYPAL_SYMBOLS = "".join(c for c in string.punctuation if c not in "\"'&")
ALL_SYMBOLS    = string.punctuation
ALL_PRINTABLE  = string.printable.strip()

CUSTOM_CHAR_SETS = {
    "1": DIGITS,
    "2": string.ascii_letters + DIGITS,
    "3": string.ascii_letters + DIGITS + COMMON_SYMBOLS,
    "4": ALL_PRINTABLE,
}

PRESET_LIMITS = {
    "1":  (15, None),
    "2":  (12, None),
    "3":  (8,  None),
    "4":  (8,  32),
    "5":  (6,  16),
    "6":  (7,  32),
    "7":  (6,  None),
    "10": (1,  6),
    "11": (8,  None),
}


def get_length(prompt, min_len=None, max_len=None):
    raw = input(prompt)
    digits = "".join(c for c in raw if c.isdigit())
    length = int(digits) if digits else 0
    if min_len:
        length = max(min_len, length)
    if max_len:
        length = min(max_len, length)
    return length if length > 0 else (min_len or 8)


def with_required(required_pools, full_pool, length):
    result = [random.choice(pool) for pool in required_pools]
    result += random.choices(full_pool, k=length - len(result))
    random.shuffle(result)
    return result


def fix_consecutive(chars):
    result = list(chars)
    pool = list(set(result))
    for i in range(1, len(result)):
        if result[i] == result[i - 1]:
            alternatives = [c for c in pool if c != result[i - 1]]
            if alternatives:
                result[i] = random.choice(alternatives)
    return result


def fix_sequential_digits(chars):
    result = list(chars)
    for i in range(2, len(result)):
        if all(c.isdigit() for c in result[i - 2:i + 1]):
            d0, d1, d2 = int(result[i-2]), int(result[i-1]), int(result[i])
            if d2 - d1 == d1 - d0:
                safe = [str(d) for d in range(10) if abs(d - d1) > 1]
                if safe:
                    result[i] = random.choice(safe)
    return result


def generate(preset, length):
    if preset == "1":
        return "".join(random.choices(ALL_PRINTABLE, k=length))

    if preset == "2":
        full = UPPER + LOWER + DIGITS + ALL_SYMBOLS
        return "".join(with_required([UPPER, LOWER, DIGITS, ALL_SYMBOLS], full, length))

    if preset == "3":
        full = UPPER + LOWER + DIGITS + ALL_SYMBOLS
        return "".join(with_required([UPPER, LOWER, DIGITS, ALL_SYMBOLS], full, length))

    if preset == "4":
        full = UPPER + LOWER + DIGITS + CHASE_SYMBOLS
        return "".join(fix_consecutive(with_required([], full, length)))

    if preset == "5":
        all_pools = [UPPER, LOWER, DIGITS, COMMON_SYMBOLS]
        random.shuffle(all_pools)
        full = UPPER + LOWER + DIGITS + COMMON_SYMBOLS
        return "".join(with_required(all_pools[:3], full, length))

    if preset == "6":
        full = UPPER + LOWER + DIGITS + PAYPAL_SYMBOLS
        return "".join(random.choices(full, k=length))

    if preset == "7":
        return "".join(fix_sequential_digits(list(random.choices(DIGITS, k=length))))

    if preset == "8":
        result = (
            random.choices(UPPER, k=2) +
            random.choices(LOWER, k=2) +
            random.choices(DIGITS, k=2) +
            random.choices(ALL_SYMBOLS, k=2)
        )
        random.shuffle(result)
        return "".join(result)

    if preset == "9":
        return "".join(random.choices(ALL_PRINTABLE, k=8))

    if preset == "10":
        return "".join(random.choices(string.ascii_letters + DIGITS, k=length))

    if preset == "11":
        return "".join(random.choices(string.ascii_letters + DIGITS, k=length))

    return ""


while True:
    print(t["welcome"])
    preset = input(t["preset_prompt"]).strip()

    if preset in ("8", "9"):
        print(t["length_fixed"].format(length=8))
        password = generate(preset, 8)

    elif preset == "12":
        char_choice = input(t["char_type_prompt"]).strip()
        chars = CUSTOM_CHAR_SETS.get(char_choice, CUSTOM_CHAR_SETS["2"])
        length = get_length(t["enter_length"])
        password = "".join(random.choices(chars, k=length))

    else:
        min_len, max_len = PRESET_LIMITS.get(preset, (8, None))
        if max_len:
            prompt = t["enter_length_range"].format(min=min_len, max=max_len)
        else:
            prompt = t["enter_length_min"].format(min=min_len)
        length = get_length(prompt, min_len, max_len)
        password = generate(preset, length)

    print(t["generated"].format(password=password))

    again = input(t["again"])
    if again.lower() in ("no", "否"):
        print(t["goodbye"])
        break
    elif again.lower() in ("yes", "是"):
        print(t["ok_again"])
    else:
        print(t["invalid_again"])
