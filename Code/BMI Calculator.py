lang_choice = input("Select language / 选择语言:\n1. English\n2. 中文 (Chinese)\nChoose / 选择 (1 or 2): ").strip()
lang = "zh" if lang_choice == "2" else "en"

T = {
    "en": {
        "welcome": "⚖️ Welcome to the BMI Calculator! 💪",
        "enter_age": "🎂 Enter your age: ",
        "enter_gender": "👤 Select your gender:\n1. ♂️  Male\n2. ♀️  Female\n3. 🔒 Prefer not to say\nChoose (1-3): ",
        "enter_height": "📏 Enter your height in cm: ",
        "enter_weight": "🏋️ Enter your weight in kg: ",
        "bmi_result": "📊 Your BMI is: {bmi:.2f}",
        "child_note": "📌 Note: Standard BMI ranges are designed for adults. For those under 18, consult a doctor for a proper assessment.",
        "again": "🔄 Do you want to calculate again? (yes/no): ",
        "goodbye": "👋 Goodbye! Stay healthy! 💚",
        "ok_again": "🔄 Ok, let's calculate again!",
        "invalid_again": "🤔 Invalid input. Let's calculate again!",
        "advice": {
            "underweight": {
                "child": {
                    "male":   "🥗 You are underweight. Growing boys need plenty of protein, healthy fats, and calories to support muscle and bone development. Talk to a doctor or nutritionist.",
                    "female": "🥗 You are underweight. Growing girls need adequate nutrition for bone density and hormonal development. Talk to a doctor or nutritionist.",
                    "other":  "🥗 You are underweight. Growing bodies need nutrient-dense foods to support healthy development. Talk to a doctor or nutritionist.",
                },
                "adult": {
                    "male":   "🥗 You are underweight. Consider increasing your intake of protein-rich foods to support muscle mass. If weight loss was unintentional, consult a doctor.",
                    "female": "🥗 You are underweight. This can affect hormonal health and bone density. Focus on nutrient-dense foods and consult a doctor if concerned.",
                    "other":  "🥗 You are underweight. Consider eating more nutrient-dense foods and consult a doctor if the weight loss was unintentional.",
                },
                "senior": {
                    "male":   "🥗 You are underweight, which is a significant concern at your age. Prioritise protein to preserve muscle mass and consult your doctor.",
                    "female": "🥗 You are underweight, which increases fracture and osteoporosis risk. Ensure adequate calcium and vitamin D, and consult your doctor.",
                    "other":  "🥗 You are underweight, which is a significant concern for older adults. Focus on nutrient-rich foods and consult your doctor.",
                },
            },
            "normal": {
                "child": {
                    "male":   "✅ You have a healthy weight for your age. Keep up the active lifestyle and balanced diet! 🌟",
                    "female": "✅ You have a healthy weight for your age. Keep up the active lifestyle and balanced diet! 🌟",
                    "other":  "✅ You have a healthy weight for your age. Keep up the active lifestyle and balanced diet! 🌟",
                },
                "adult": {
                    "male":   "✅ You have a healthy weight. Consider adding strength training to maintain muscle mass and keep up the balanced diet! 🌟",
                    "female": "✅ You have a healthy weight. Make sure you're getting enough iron and calcium in your diet. Keep it up! 🌟",
                    "other":  "✅ You have a healthy weight. Maintain your balanced diet and regular exercise to stay this way! 🌟",
                },
                "senior": {
                    "male":   "✅ You have a healthy weight. Focus on maintaining muscle strength through light resistance exercise and adequate protein intake. 🌟",
                    "female": "✅ You have a healthy weight. Prioritise calcium, vitamin D, and light exercise to protect bone and muscle health. 🌟",
                    "other":  "✅ You have a healthy weight. Stay active and eat a balanced diet to maintain it as you age. 🌟",
                },
            },
            "overweight": {
                "child": {
                    "male":   "⚠️ You are overweight. Focus on fun physical activities and balanced meals rather than strict dieting. Talk to a doctor for personalised advice.",
                    "female": "⚠️ You are overweight. Focus on fun physical activities and balanced meals rather than strict dieting. Talk to a doctor for personalised advice.",
                    "other":  "⚠️ You are overweight. Focus on healthy habits and talk to a doctor for personalised advice.",
                },
                "adult": {
                    "male":   "⚠️ You are overweight. This raises your risk of cardiovascular disease and high blood pressure. Consider cardio exercise and cutting back on processed foods.",
                    "female": "⚠️ You are overweight. This can affect hormonal balance and increase health risks. Consider a balanced diet and regular exercise.",
                    "other":  "⚠️ You are overweight. Consider increasing physical activity and improving your diet. Consult a doctor if needed.",
                },
                "senior": {
                    "male":   "⚠️ You are overweight. A slightly higher BMI can sometimes be protective at your age — consult your doctor before making major lifestyle changes.",
                    "female": "⚠️ You are overweight. A slightly higher BMI can sometimes be protective at your age — consult your doctor before making major lifestyle changes.",
                    "other":  "⚠️ You are overweight. Consult your doctor before making changes — a slightly higher BMI may be acceptable at your age.",
                },
            },
            "obese": {
                "child": {
                    "male":   "🚨 You are obese. Please consult a doctor or paediatrician. Focus on family-wide healthy eating habits and active play rather than dieting alone.",
                    "female": "🚨 You are obese. Please consult a doctor or paediatrician. Focus on family-wide healthy eating habits and active play rather than dieting alone.",
                    "other":  "🚨 You are obese. Please consult a doctor or paediatrician for a personalised and age-appropriate plan.",
                },
                "adult": {
                    "male":   "🚨 You are obese. This significantly raises your risk of heart disease, diabetes, and hypertension. Please speak with a doctor about a safe plan.",
                    "female": "🚨 You are obese. This increases risk of diabetes, joint problems, and hormonal imbalances. Please speak with a doctor about a personalised plan.",
                    "other":  "🚨 You are obese. This carries significant health risks. Please consult a doctor about a safe and sustainable weight management plan.",
                },
                "senior": {
                    "male":   "🚨 You are obese. Please consult your doctor for a safe plan that focuses on mobility, joint health, and muscle preservation.",
                    "female": "🚨 You are obese. Please consult your doctor for a safe plan that considers joint health, bone density, and sustainable changes.",
                    "other":  "🚨 You are obese. Please consult your doctor for a personalised plan that is safe for your age and health needs.",
                },
            },
        },
    },
    "zh": {
        "welcome": "⚖️ 欢迎使用 BMI 计算器！💪",
        "enter_age": "🎂 请输入您的年龄：",
        "enter_gender": "👤 请选择您的性别：\n1. ♂️  男性\n2. ♀️  女性\n3. 🔒 不愿透露\n请选择（1-3）：",
        "enter_height": "📏 请输入您的身高（厘米）：",
        "enter_weight": "🏋️ 请输入您的体重（千克）：",
        "bmi_result": "📊 您的 BMI 是：{bmi:.2f}",
        "child_note": "📌 注意：标准BMI范围适用于成年人。18岁以下人群请咨询医生进行专业评估。",
        "again": "🔄 您想再计算一次吗？(是/否)：",
        "goodbye": "👋 再见！保持健康！💚",
        "ok_again": "🔄 好的，让我们再计算一次！",
        "invalid_again": "🤔 无效输入，让我们再计算一次！",
        "advice": {
            "underweight": {
                "child": {
                    "male":   "🥗 您的体重偏低。男孩成长期需要充足的蛋白质、健康脂肪和热量以支持肌肉和骨骼发育。请咨询医生或营养师。",
                    "female": "🥗 您的体重偏低。女孩成长期需要充足营养以支持骨密度和激素发育。请咨询医生或营养师。",
                    "other":  "🥗 您的体重偏低。成长中的身体需要营养丰富的食物以支持健康发育。请咨询医生或营养师。",
                },
                "adult": {
                    "male":   "🥗 您的体重偏低。建议增加富含蛋白质的食物摄入以维持肌肉量。若体重非自愿下降，请咨询医生。",
                    "female": "🥗 您的体重偏低，可能影响激素健康和骨密度。请注重营养均衡，如有需要请咨询医生。",
                    "other":  "🥗 您的体重偏低。建议增加营养丰富食物的摄入，如体重非自愿下降请咨询医生。",
                },
                "senior": {
                    "male":   "🥗 您的体重偏低，这对您这个年龄段是重要问题。请优先摄入蛋白质以保持肌肉量，并咨询医生。",
                    "female": "🥗 您的体重偏低，增加了骨折和骨质疏松的风险。请确保摄入足够的钙和维生素D，并咨询医生。",
                    "other":  "🥗 您的体重偏低，这对老年人是重要问题。请注重营养饮食并咨询医生。",
                },
            },
            "normal": {
                "child": {
                    "male":   "✅ 您的体重在健康范围内。继续保持积极的生活方式和均衡饮食！🌟",
                    "female": "✅ 您的体重在健康范围内。继续保持积极的生活方式和均衡饮食！🌟",
                    "other":  "✅ 您的体重在健康范围内。继续保持积极的生活方式和均衡饮食！🌟",
                },
                "adult": {
                    "male":   "✅ 您的体重正常。建议进行力量训练以维持肌肉量，继续保持均衡饮食！🌟",
                    "female": "✅ 您的体重正常。请确保饮食中含有足够的铁和钙。继续保持！🌟",
                    "other":  "✅ 您的体重正常。坚持均衡饮食和规律运动！🌟",
                },
                "senior": {
                    "male":   "✅ 您的体重正常。建议通过轻度抗阻训练和充足蛋白质来维持肌肉力量。🌟",
                    "female": "✅ 您的体重正常。请注重补充钙质和维生素D，并坚持适度运动以保护骨骼和肌肉健康。🌟",
                    "other":  "✅ 您的体重正常。保持积极的生活方式和均衡饮食以维持健康！🌟",
                },
            },
            "overweight": {
                "child": {
                    "male":   "⚠️ 您的体重偏高。重点应放在有趣的体育活动和均衡饮食上，而非严格节食。请咨询医生获取个性化建议。",
                    "female": "⚠️ 您的体重偏高。重点应放在有趣的体育活动和均衡饮食上，而非严格节食。请咨询医生获取个性化建议。",
                    "other":  "⚠️ 您的体重偏高。请注重培养健康习惯，并咨询医生获取个性化建议。",
                },
                "adult": {
                    "male":   "⚠️ 您的体重偏高，增加了心血管疾病和高血压的风险。建议增加有氧运动并减少加工食品摄入。",
                    "female": "⚠️ 您的体重偏高，可能影响激素平衡并增加健康风险。建议均衡饮食和规律运动。",
                    "other":  "⚠️ 您的体重偏高。建议增加运动量并改善饮食结构，如有需要请咨询医生。",
                },
                "senior": {
                    "male":   "⚠️ 您的体重偏高。对于您这个年龄段，稍高的BMI有时具有保护作用，进行重大生活方式改变前请先咨询医生。",
                    "female": "⚠️ 您的体重偏高。对于您这个年龄段，稍高的BMI有时具有保护作用，进行重大生活方式改变前请先咨询医生。",
                    "other":  "⚠️ 您的体重偏高。进行改变前请先咨询医生，稍高的BMI在您这个年龄段可能是可以接受的。",
                },
            },
            "obese": {
                "child": {
                    "male":   "🚨 您的BMI显示肥胖。请咨询医生或儿科医生。应以全家共同建立健康饮食习惯和积极运动为主，而非单纯节食。",
                    "female": "🚨 您的BMI显示肥胖。请咨询医生或儿科医生。应以全家共同建立健康饮食习惯和积极运动为主，而非单纯节食。",
                    "other":  "🚨 您的BMI显示肥胖。请咨询医生或儿科医生制定个性化的适龄方案。",
                },
                "adult": {
                    "male":   "🚨 您属于肥胖，显著增加了心脏病、糖尿病和高血压的风险。请尽快咨询医生制定安全的减重方案。",
                    "female": "🚨 您属于肥胖，增加了糖尿病、关节问题和激素失调的风险。请咨询医生制定个性化方案。",
                    "other":  "🚨 您属于肥胖，存在重大健康风险。请咨询医生制定安全、可持续的体重管理方案。",
                },
                "senior": {
                    "male":   "🚨 您属于肥胖。请咨询医生制定安全方案，重点关注行动能力、关节健康和肌肉保持。",
                    "female": "🚨 您属于肥胖。请咨询医生制定安全方案，综合考虑关节健康、骨密度和可持续改变。",
                    "other":  "🚨 您属于肥胖。请咨询医生制定适合您年龄和健康需求的个性化方案。",
                },
            },
        },
    },
}

t = T[lang]


def parse_num(s, allow_decimal=False):
    return "".join(c for c in s if c.isdigit() or (allow_decimal and c == "."))


def get_age_group(age):
    if age < 18:
        return "child"
    elif age < 65:
        return "adult"
    return "senior"


def get_gender(choice):
    if choice == "1":
        return "male"
    elif choice == "2":
        return "female"
    return "other"


while True:
    print(t["welcome"])

    age = int(parse_num(input(t["enter_age"])) or "0")
    gender = get_gender(input(t["enter_gender"]).strip())
    age_group = get_age_group(age)

    height = float(parse_num(input(t["enter_height"]), allow_decimal=True) or "0")
    weight = float(parse_num(input(t["enter_weight"]), allow_decimal=True) or "0")

    bmi = weight / ((height / 100) ** 2)
    print(t["bmi_result"].format(bmi=bmi))

    if age_group == "child":
        print(t["child_note"])

    if bmi < 18.5:
        category = "underweight"
    elif bmi < 25:
        category = "normal"
    elif bmi < 30:
        category = "overweight"
    else:
        category = "obese"

    print(t["advice"][category][age_group][gender])

    again = input(t["again"])
    if again.lower() in ("no", "否"):
        print(t["goodbye"])
        break
    elif again.lower() in ("yes", "是"):
        print(t["ok_again"])
    else:
        print(t["invalid_again"])
