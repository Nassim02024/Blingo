import re, os

def add_trans_tags(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r">(.*?)<", re.DOTALL)

    def replacer(m):
        text = m.group(1)
        stripped = text.strip()
        # تجاهل الفارغ/تاجات جينجا/دجانغو
        if not stripped or stripped.startswith("{%") or stripped.startswith("{{"):
            return f">{text}<"
        # اقتباس مفرد + تهريب
        safe = stripped.replace("'", "\\'")
        return f">{{% trans '{safe}' %}}<"

    new_content = pattern.sub(replacer, content)

    new_path = file_path.replace(".html", ".html")
    with open(new_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("تم إنشاء:", new_path)


# جرب على ملف معين
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "templates" , "users" , "register.html")

add_trans_tags(file_path)
