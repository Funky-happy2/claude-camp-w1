import random
import os
from datetime import datetime

lang_choice = input("Select language / 选择语言:\n1. English\n2. 中文 (Chinese)\nChoose / 选择 (1 or 2): ").strip()
lang = "zh" if lang_choice == "2" else "en"

translations = {
    "en": {
        "welcome": "🎉 Welcome to the Greeting Generator! 🎉",
        "enter_name": "Enter your name: ",
        "enter_age": "Enter your age: ",
        "generating": "✨ Generating your greeting... ✨",
        "greeting_type": "Greeting style: {style}",
        "greetings": [
            {
                "style": "🎩 Formal",
                "text": "🎩 Good day, {name}. It is with the utmost respect and courtesy that I address you on this fine occasion. You are {age} years of age, which most elegantly places your year of birth in {birth_year}. The passage of time has clearly served you well. A sincere pleasure to make your acquaintance, and I do hope our paths cross again.",
                "save_prompt": "💾 Shall I have the honour of preserving this greeting for posterity? (yes/no): ",
                "save_yes": "✅ The greeting has been duly preserved in '{filename}' with the greatest of care.",
                "save_no": "Very well. The greeting shall not be archived.",
                "again": "Shall I have the honour of composing another greeting? (yes/no): ",
                "goodbye": "🎩 I bid you a most respectful farewell. Until we meet again, good day.",
                "ok_again": "🎩 Splendid. Allow me to compose another with the utmost care.",
                "invalid_again": "🎩 I beg your pardon — I shall take that as a request to continue.",
            },
            {
                "style": "👋 Casual",
                "text": "👋 Hey hey, {name}! So great to meet you! Can you believe you're already {age} years old?! Like, where does the time even go?! You've been on this planet since {birth_year} — that's honestly wild. Anyway, you seem super cool and I'm really glad we got to chat! 😄✌️",
                "save_prompt": "💾 Wanna save this one? (yes/no): ",
                "save_yes": "✅ Saved to '{filename}'! Nice one!",
                "save_no": "All good, no worries!",
                "again": "Hey, want me to whip up another one? (yes/no): ",
                "goodbye": "👋 Laters! Catch ya around! 😄✌️",
                "ok_again": "👋 Aight, cool! Let's do another one!",
                "invalid_again": "👋 Haha okay, I'll just make another one anyway!",
            },
            {
                "style": "🥳 Enthusiastic",
                "text": "🥳 OH MY GOODNESS, {name}!!! WELCOME WELCOME WELCOME!!! I AM SO INCREDIBLY EXCITED TO MEET YOU RIGHT NOW!!! YOU ARE {age} YEARS OLD AND THAT IS THE MOST AMAZING THING I HAVE EVER HEARD!!! BORN IN {birth_year}?! A LEGEND!!! AN ABSOLUTE LEGEND!!! THIS IS THE BEST DAY EVER!!! 🎊🎉🎈🎆🎇",
                "save_prompt": "💾 OH DO YOU WANNA SAVE THIS?! IT'S SO GOOD!!! (yes/no): ",
                "save_yes": "✅ SAVED TO '{filename}'!!! IT'S SAVED FOREVER!!! AMAZING!!! 🎊🎉",
                "save_no": "OK BUT IT WAS SO GOOD THOUGH!!!",
                "again": "OH WOW DO YOU WANT ANOTHER GREETING?! (yes/no): ",
                "goodbye": "🥳 BYEEEEE!!! THIS WAS THE BEST THING EVER!!! COME BACK SOON!!! 🎊🎉🎈",
                "ok_again": "🥳 YES YES YES!!! LET'S DO IT AGAIN!!! THIS IS SO EXCITING!!!",
                "invalid_again": "🥳 I'M JUST GONNA MAKE ANOTHER ONE BECAUSE WHY NOT!!!",
            },
            {
                "style": "🌟 Poetic",
                "text": "🌟 Ah, {name}! Like a star ignited in the heavens of {birth_year}, you have blazed a trail across {age} magnificent years. Each moment of your life a verse, each breath a stanza in the grand poem of existence. May the chapters yet unwritten be your finest, and may starlight forever guide your path. 🌸🌙✨",
                "save_prompt": "💾 Shall these words be pressed like flowers, kept for all time? (yes/no): ",
                "save_yes": "✅ These words now rest, immortalised within '{filename}'... 🌸",
                "save_no": "Then let it drift, like petals on the wind...",
                "again": "Shall the muse visit once more? (yes/no): ",
                "goodbye": "🌟 May your path be ever lit by stars, farewell dear soul. 🌸🌙✨",
                "ok_again": "🌟 The quill dips once more into the inkwell of inspiration...",
                "invalid_again": "🌟 In silence, the answer speaks — let the verses flow again...",
            },
            {
                "style": "🔮 Mysterious",
                "text": "🔮 The oracle stirs... the mists part... a name emerges from the void... {name}... yes... born beneath the skies of {birth_year}, you have journeyed {age} long years through realms seen and unseen. The stars have watched your every step. What secrets do you carry? The crystal ball does not say... not yet. 🌙🕯️🌫️",
                "save_prompt": "💾 Shall this message be sealed away... kept in the shadows... forever? (yes/no): ",
                "save_yes": "✅ The message is sealed... hidden away in '{filename}'... 🌙🕯️",
                "save_no": "So it shall fade... like all things fade... into nothing...",
                "again": "Does the oracle foresee another greeting? (yes/no): ",
                "goodbye": "🔮 The mists close... you fade into the beyond... until next time... 🌙🕯️🌫️",
                "ok_again": "🔮 The crystal ball swirls... another vision takes shape...",
                "invalid_again": "🔮 The oracle interprets your silence... another greeting shall be revealed...",
            },
            {
                "style": "☠️ Pirate",
                "text": "☠️ AHOY there, {name}! Blimey, what a fine specimen ye be! {age} years old, havin' sailed the seas since the grand year of {birth_year}! I've plundered treasure across seven seas but ne'er met a soul quite like yerself! Join me crew and together we'll find glory beyond imagination! The horizon awaits, ye scallywag! ⚓🦜💀🗺️",
                "save_prompt": "💾 Shall we lock this treasure in the chest, matey? (yes/no): ",
                "save_yes": "✅ Treasure locked away in '{filename}'! ⚓💀",
                "save_no": "Aye, some treasure's best left unguarded!",
                "again": "Shall we set sail for another greeting, ye scallywag? (yes/no): ",
                "goodbye": "☠️ Fair winds to ye, matey! May yer seas be calm! ⚓🦜💀",
                "ok_again": "☠️ Heave ho! Plottin' a course for another greeting!",
                "invalid_again": "☠️ Arrr, I'll take that as a yes, ye landlubber!",
            },
            {
                "style": "🤖 Robot",
                "text": "🤖 GREETINGS, HUMAN DESIGNATION: {name}. SCANNING... SCAN COMPLETE. AGE CONFIRMED: {age} YEARS. BIRTH YEAR LOGGED: {birth_year}. YOU HAVE SUCCESSFULLY EXISTED FOR {age} ROTATIONS AROUND THE SUN. PROBABILITY OF AWESOMENESS: 99.7%. INITIATING FRIENDSHIP PROTOCOL... FRIENDSHIP ESTABLISHED. BEEP BOOP. 💾🔩⚙️",
                "save_prompt": "💾 COMMAND: SAVE GREETING TO PERMANENT STORAGE? (yes/no): ",
                "save_yes": "✅ SAVE COMPLETE. FILE: '{filename}'. DATA SECURED. BEEP. 💾",
                "save_no": "ACKNOWLEDGED. SAVE COMMAND CANCELLED.",
                "again": "QUERY: GENERATE ANOTHER GREETING? (yes/no): ",
                "goodbye": "🤖 FAREWELL PROTOCOL INITIATED. GOODBYE, HUMAN. BEEP BOOP. 💾🔩⚙️",
                "ok_again": "🤖 AFFIRMATIVE. RESTARTING GREETING GENERATION SEQUENCE. BEEP.",
                "invalid_again": "🤖 INPUT UNRECOGNISED. DEFAULTING TO: GENERATE ANOTHER GREETING.",
            },
            {
                "style": "🧙 Wizard",
                "text": "🧙 By the ancient scrolls and the light of Arcanum, I bid thee welcome, dear {name}! The celestial records confirm thou wert brought into this world in the year {birth_year}, and hast now accumulated {age} years of wisdom and wonder. Thy aura shimmers with untold potential! May your magic never falter and your quest forever lead you toward glory! 🔮📜⭐",
                "save_prompt": "💾 Dost thou wish to inscribe these words upon the ancient scrolls? (yes/no): ",
                "save_yes": "✅ The words are inscribed upon the scrolls of '{filename}'! 📜⭐",
                "save_no": "Very well, the words shall dissolve into the aether.",
                "again": "Dost thou wish for another enchantment? (yes/no): ",
                "goodbye": "🧙 Fare thee well, brave soul! May your magic guide you home! 🔮📜⭐",
                "ok_again": "🧙 By the ancient scrolls, let us conjure another greeting!",
                "invalid_again": "🧙 The runes are unclear, but the spell shall be cast again!",
            },
            {
                "style": "🏆 Sports Coach",
                "text": "🏆 LISTEN UP, {name}! You've been in the game since {birth_year} and you've put in {age} years of hard work — and it SHOWS! You've got the hunger, you've got the drive, and today is YOUR day to shine! I don't care what anyone else says — you are a CHAMPION! Now get out there and give it everything you've got! LET'S GOOOO! 💪🔥🥇",
                "save_prompt": "💾 You want to KEEP this one?! SAVE IT! (yes/no): ",
                "save_yes": "✅ LOCKED IN! Saved to '{filename}'! CHAMPIONS KEEP RECORDS! 💪🔥",
                "save_no": "NO WORRIES! Keep moving! Eyes forward! 💪",
                "again": "You want ANOTHER one?! Are you ready?! (yes/no): ",
                "goodbye": "🏆 Go get 'em champ! You've got this! See ya out there! 💪🔥🥇",
                "ok_again": "🏆 THAT'S THE SPIRIT! Let's go again! Hustle hustle hustle!",
                "invalid_again": "🏆 I'm gonna take that as a YES! Let's GO!",
            },
            {
                "style": "🌴 Laid-back",
                "text": "🌴 Heyyy {name}, welcome, welcome... no rush, no stress, just good vibes only. So you've been chillin' on this Earth since {birth_year}, that's like... {age} whole years of just living your best life. That's beautiful, man. Really beautiful. Grab a coconut, feel the breeze, you're exactly where you're supposed to be. 🌊😎✌️",
                "save_prompt": "💾 Hey, wanna hold onto this one? No pressure... (yes/no): ",
                "save_yes": "✅ Saved to '{filename}'... nice... it's there whenever you need it... 🌊",
                "save_no": "No worries... it'll come back around... 🌊",
                "again": "Hey, you want another one? No pressure either way... (yes/no): ",
                "goodbye": "🌴 Take it easy, friend... stay cool... 🌊😎✌️",
                "ok_again": "🌴 Sure thing... no rush... let's see what comes up...",
                "invalid_again": "🌴 All good... I'll just roll with it...",
            },
        ],
    },
    "zh": {
        "welcome": "🎉 欢迎使用问候语生成器！🎉",
        "enter_name": "请输入您的姓名：",
        "enter_age": "请输入您的年龄：",
        "generating": "✨ 正在生成您的问候语... ✨",
        "greeting_type": "问候语风格：{style}",
        "greetings": [
            {
                "style": "🎩 正式",
                "text": "🎩 您好，{name} 先生/女士。在此庄重场合，谨向您致以最诚挚的问候。您今年贵庚 {age} 岁，想来您诞生于 {birth_year} 年。岁月如梭，而您风采依旧。能与您相识，实乃荣幸之至，期待日后有缘再会。",
                "save_prompt": "💾 荣幸为您将此问候语妥善存档，可否？(是/否)：",
                "save_yes": "✅ 问候语已依照最高礼仪妥善存档于 '{filename}'。",
                "save_no": "好的。此问候语将不予存档。",
                "again": "荣幸为您再赋一段问候，可否？(是/否)：",
                "goodbye": "🎩 在此向您致以最诚挚的告别，期待来日再会，保重。",
                "ok_again": "🎩 甚好。请容我再度精心为您呈上一段问候。",
                "invalid_again": "🎩 恕我未能领会，姑且将其视为继续之请。",
            },
            {
                "style": "👋 随意",
                "text": "👋 嗨嗨嗨，{name}！超开心认识你！你都已经 {age} 岁了？！时间过得也太快了吧！你从 {birth_year} 年就在这个星球上啦——说真的，好神奇哦！反正你看起来超级酷的，很高兴咱们能聊上！😄✌️",
                "save_prompt": "💾 要不要保存这个？(是/否)：",
                "save_yes": "✅ 保存到 '{filename}' 了！不错哦！",
                "save_no": "没事，随便的！",
                "again": "嘿，要我再整一个吗？(是/否)：",
                "goodbye": "👋 拜拜啦！有缘再见哦！😄✌️",
                "ok_again": "👋 哦吼，好嘞！咱再来一个！",
                "invalid_again": "👋 哈哈好吧，我就当你要了，再来一个！",
            },
            {
                "style": "🥳 热情",
                "text": "🥳 天哪天哪天哪，{name}！！！欢迎欢迎超级大欢迎！！！我现在激动得不行！！！你居然已经 {age} 岁了！！！这是我听过的最厉害的事情！！！{birth_year} 年出生的传奇！！！绝对的传奇！！！今天是最棒的一天！！！🎊🎉🎈🎆🎇",
                "save_prompt": "💾 你想保存这个吗！！！太好了！！！(是/否)：",
                "save_yes": "✅ 保存到 '{filename}' 了！！！永远保存了！！！太棒了！！！🎊🎉",
                "save_no": "好吧但是真的太好了啊！！！",
                "again": "天哪你还想要一个吗！！！(是/否)：",
                "goodbye": "🥳 拜拜啊啊啊！！！这是最最最棒的体验！！！快回来哦！！！🎊🎉🎈",
                "ok_again": "🥳 好好好！！！再来一个！！！太兴奋了！！！",
                "invalid_again": "🥳 管它呢反正再来一个就完了！！！",
            },
            {
                "style": "🌟 诗意",
                "text": "🌟 啊，{name}！如同 {birth_year} 年在苍穹中点燃的星辰，你已走过 {age} 载绚烂岁月。你生命里的每一刻，都是这壮阔诗篇中的一行，每一次呼吸，都是生命交响乐中的一个音符。愿未来的篇章，是你最华彩的乐章，愿星光永远为你引路。🌸🌙✨",
                "save_prompt": "💾 这些文字，可否如落花般珍藏，留存永久？(是/否)：",
                "save_yes": "✅ 这些文字已安然留存于 '{filename}'，化为永恒…… 🌸",
                "save_no": "那便随风而散，如落花飘零……",
                "again": "缪斯可否再度降临？(是/否)：",
                "goodbye": "🌟 愿星光照亮你前行的路，别了，亲爱的灵魂。🌸🌙✨",
                "ok_again": "🌟 羽笔再度蘸墨，灵感的长卷徐徐展开……",
                "invalid_again": "🌟 沉默中自有答案，让诗意再度流淌……",
            },
            {
                "style": "🔮 神秘",
                "text": "🔮 神谕涌动……迷雾散开……虚空中浮现一个名字……{name}……是的……你诞生于 {birth_year} 年的苍穹之下，已在这可见与不可见的世界间穿行了整整 {age} 个春秋。繁星目睹了你每一步的踪迹。你究竟携带着怎样的秘密？水晶球尚未言明……至少，现在还没有。🌙🕯️🌫️",
                "save_prompt": "💾 此讯息，是否应封存于黑暗之中……永远？(是/否)：",
                "save_yes": "✅ 讯息已封存……深藏于 '{filename}' 之中…… 🌙🕯️",
                "save_no": "于是它将消散……如一切终将消散……归于虚无……",
                "again": "神谕是否预见下一段问候？(是/否)：",
                "goodbye": "🔮 迷雾合拢……你消散于虚空之中……直到下次相遇……🌙🕯️🌫️",
                "ok_again": "🔮 水晶球旋转……另一个幻象正在成形……",
                "invalid_again": "🔮 神谕读解你的沉默……另一段问候即将揭晓……",
            },
            {
                "style": "☠️ 海盗",
                "text": "☠️ 哟吼，{name}！你可真是条好汉！{age} 岁了，自 {birth_year} 年就扬帆于江湖之上！我走遍七海，掠夺无数宝藏，却从未见过像你这般人物！快来加入我的船队，咱们一起闯荡，寻那传说中的荣耀与宝藏！海风呼啸，前路等着你呢，你这个家伙！⚓🦜💀🗺️",
                "save_prompt": "💾 要把这份宝藏锁进箱子里吗，老伙计？(是/否)：",
                "save_yes": "✅ 宝藏已锁进 '{filename}'！⚓💀",
                "save_no": "哈，有些宝藏就是要随风飘的！",
                "again": "咱们要再启航寻一段新问候吗，你这家伙？(是/否)：",
                "goodbye": "☠️ 顺风顺水啊，老伙计！愿你航途平稳！⚓🦜💀",
                "ok_again": "☠️ 起锚！驶向下一段问候的航程！",
                "invalid_again": "☠️ 哦吼，我就当你说行了，你这个陆地佬！",
            },
            {
                "style": "🤖 机器人",
                "text": "🤖 您好，人类代号：{name}。正在扫描……扫描完成。年龄已确认：{age} 岁。出生年份已记录：{birth_year} 年。您已成功绕太阳运行 {age} 圈。超酷概率：99.7%。正在启动友谊协议……友谊已建立。滴滴答答。💾🔩⚙️",
                "save_prompt": "💾 指令：将问候语保存至永久存储？(是/否)：",
                "save_yes": "✅ 保存完成。文件：'{filename}'。数据已入库。滴。💾",
                "save_no": "已确认。保存指令已取消。",
                "again": "查询：生成另一段问候语？(是/否)：",
                "goodbye": "🤖 正在执行告别协议。再见，人类。滴滴答答。💾🔩⚙️",
                "ok_again": "🤖 确认。重启问候生成序列。滴。",
                "invalid_again": "🤖 输入无法识别。默认操作：生成另一段问候。",
            },
            {
                "style": "🧙 巫师",
                "text": "🧙 以古老卷轴之名，以阿卡纳之光，吾向汝致意，亲爱的 {name}！天界记载确认，汝于 {birth_year} 年降临此世，如今已积累 {age} 载智慧与奇迹。汝之气息中涌动着无尽潜能！愿你的魔法生生不息，愿你的征途永远指向荣耀！🔮📜⭐",
                "save_prompt": "💾 汝是否希望将这些文字铭刻于古老卷轴之上？(是/否)：",
                "save_yes": "✅ 文字已铭刻于 '{filename}' 的古老卷轴上！📜⭐",
                "save_no": "好吧，这些文字将消散于以太之中。",
                "again": "汝是否希望再得一段咒语？(是/否)：",
                "goodbye": "🧙 保重，勇敢的灵魂！愿魔法引你归家！🔮📜⭐",
                "ok_again": "🧙 以古老卷轴之名，吾等再度召唤一段问候！",
                "invalid_again": "🧙 符文尚不明朗，但咒语仍将再度施展！",
            },
            {
                "style": "🏆 教练",
                "text": "🏆 听好了，{name}！你从 {birth_year} 年就入场了，已经打拼了整整 {age} 年——而且这一切都看得出来！你有冲劲，你有韧劲，今天就是属于你的日子！我不管别人怎么说——你就是冠军！现在出去，把你所有的一切都拼出来！冲啊！💪🔥🥇",
                "save_prompt": "💾 你想留住这个吗？！保存它！(是/否)：",
                "save_yes": "✅ 锁定！已保存至 '{filename}'！冠军都记录成绩！💪🔥",
                "save_no": "没问题！继续前进！眼睛向前看！💪",
                "again": "你还想再来一个？！准备好了吗！(是/否)：",
                "goodbye": "🏆 加油冠军！你可以的！赛场上见！💪🔥🥇",
                "ok_again": "🏆 就是这股劲！再来一次！冲冲冲！",
                "invalid_again": "🏆 我就当你说行了！冲啊！",
            },
            {
                "style": "🌴 佛系",
                "text": "🌴 嘿，{name}，来啦……不急不急，没有压力，只有好心情。你从 {birth_year} 年就在这地球上悠哉游哉，这都 {age} 年了，一直过着属于自己的生活。这很美好，真的很美好。拿杯椰子水，感受一下微风，你就在你该在的地方。🌊😎✌️",
                "save_prompt": "💾 嘿，想留着这个吗？没压力的……(是/否)：",
                "save_yes": "✅ 保存至 '{filename}'……不错……需要的时候随时可以看…… 🌊",
                "save_no": "没事……缘分到了自然会回来的……",
                "again": "嘿，想再来一个吗？没压力的……(是/否)：",
                "goodbye": "🌴 慢慢来，朋友……保持凉快……🌊😎✌️",
                "ok_again": "🌴 没问题……不急……看看这次出来啥……",
                "invalid_again": "🌴 都行……顺其自然吧……",
            },
        ],
    }
}

t = translations[lang]
save_dir = "Saved Greetings"
os.makedirs(save_dir, exist_ok=True)

print(t["welcome"])

name = input(t["enter_name"]).strip()
age_raw = input(t["enter_age"])
age_raw = "".join([char for char in age_raw if char.isdigit() or char == "."])
age = float(age_raw.strip())
birth_year = int(2026 - age)

while True:
    greeting = random.choice(t["greetings"])

    print(t["generating"])
    print(t["greeting_type"].format(style=greeting["style"]))
    greeting_text = greeting["text"].format(name=name, age=int(age), birth_year=birth_year)
    print(greeting_text)
    print()

    save = input(greeting["save_prompt"]).strip()
    if save.lower() in ("yes", "是"):
        filename = os.path.join(save_dir, f"{name}_greetings.txt")
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {greeting['style']}\n")
            f.write(f"Name: {name} | Age: {int(age)}\n")
            f.write(greeting_text + "\n\n")
        print(greeting["save_yes"].format(filename=filename))
    else:
        print(greeting["save_no"])

    again = input(greeting["again"]).strip()
    if again.lower() in ("no", "否"):
        print(greeting["goodbye"])
        break
    elif again.lower() in ("yes", "是"):
        print(greeting["ok_again"])
    else:
        print(greeting["invalid_again"])
