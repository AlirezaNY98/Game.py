# Never be a slave to the rules.
from sys import exit


# main function
def qa_game():
    # for more discipline in output
    print("\t\t==========QA==========")

    # language selection by client
    lang = input("Choose your language:\n1-EN\n2-PE\n>> ")

    print("\t\t==========QA==========")

    # language = english
    if "1" in lang or "o" in lang or "O" in lang:

        print("*** Welcome to the QA game ***")

        # take client name
        name = input("Enter your name:\n>> ")

        # take client gender
        player_gender = input("Select your gender:\n1-Female\t2-male\n>> ")

        print("\t\t==========QA==========")

        print("*** Main Menu ***")

        # menu selection by client(start game , about , exit)
        select_menu = input("1.Start the game\n2.About QA\n3.Exit\n>> ")

        print("\t\t==========QA==========")

        # menu : start game (female)
        if "1" in select_menu and "1" in player_gender:

            # take bot gender from client
            agent_gender = input(f"* tip: You can stop the game by writing \"exit\"\n"
                                 f"Hello \"Mrs.{name}\", we are happy to see you here.\nnow you can select your"
                                 f" opponent:\n1-Anahita\t2-Keykavos\n>> ")

            print("\t\t==========QA==========")

            # select female bot
            if agent_gender == "1":

                agent_gender = "Anahita"

            # select male bot
            elif agent_gender == "2":

                agent_gender = "Keykavos"

            # exit
            else:

                # function exit
                die_in("Wrong number ...")

        # menu : start game (male)
        elif "1" in select_menu and "2" in player_gender:

            # take bot gender from client
            agent_gender = input(f"* tip: You can stop the game by writing \"exit\"\n"
                                 f"Hello \"Mr.{name}\", now you are here. select your opponent\n"
                                 f"(we just have \"Keykavos\" for you, \"{name}\" if you want"
                                 f" Female\"anahita\" agent enter '1'):\n1-more\t2-Keykavos\n>> ")

            print("\t\t==========QA==========")

            # select female bot
            if agent_gender == "1":

                agent_gender = input(f"astaghferolahhhhh!!!\nthats haram brother!!"
                                     f"for customer oriented we put \"anahita\" option but we know you choose "
                                     f"\"keykavos\"\n* tip: Allah watching you."
                                     f"\n1-anahita\t2-keykavos\n>> ")

                # select female bot
                if agent_gender == "1":

                    agent_gender = "anahita"

                    print("OK. we select \"anahita\" for you but come down from devil`s donkey bro.")

                    print("\t\t==========QA==========")

                # select male bot
                elif agent_gender == "2":

                    agent_gender = "keykavos"

                    print("Finally. you came down from devil`s donkey brother.")

                    print("\t\t==========QA==========")

                # exit
                else:
                    die_in("Wrong number...")

                    print("\t\t==========QA==========")

            # select male bot
            elif agent_gender == "2":
                agent_gender = "keykavos"

                print(f"Nice. i like you, \"{name}\"")

                print("\t\t==========QA==========")

            # exit
            else:

                die_in("Wrong number...")

                print("\t\t==========QA==========")

        # menu: about QA (female)
        elif "2" in select_menu and "1" in player_gender:

            # introduce text
            print(f"*** Hey \"Mrs.{name}\",welcome to QA game ***\n"
                  f"this is a 2-players game. you and our agent. each correct answer has 1 '+' point.\n"
                  f"lets start the game,good luck and have fun.")

            # start game after about
            select = input("Are you ready?(Yes/No):>> ")

            print("\t\t==========QA==========")

            # start game (same body as line 39)
            if "Y" in select or "y" in select:

                agent_gender = input(f"* tip: You can stop the game by writing \"exit\"\n"
                                     f"\"Mrs.{name}\", now you can select your opponent:\n1-Anahita\t2-Keykavos\n>> ")

                print("\t\t==========QA==========")

                if agent_gender == "1":

                    agent_gender = "Anahita"

                elif agent_gender == "2":

                    agent_gender = "Keykavos"

                else:

                    die_in("Wrong number ...")
            else:

                die_in("Go and come whenever you are ready.")

        # menu: about QA (male)
        elif "2" in select_menu and "2" in player_gender:

            # introduce text
            print(f"*** Hey \"Mr.{name}\",welcome to QA game ***\n"
                  f"this is a 2-players game. you and our agent. each correct answer has 1 '+' point."
                  f"lets start the game,good luck and have fun.")

            # start game after about
            select = input("Are you ready?(Yes/No):>> ")

            print("\t\t==========QA==========")

            # start game (same body as line 65)
            if "Y" in select or "y" in select:

                agent_gender = input(f"*tip: You can stop the game by writing \"exit\" \n"
                                     f"\"Mr.{name}\", now you are here. select your opponent"
                                     f"(we just have \"Keykavos\" for you \"{name}\""
                                     f"if you want Female\"anahita\" agent enter '1'):\n1-more\t2-Keykavos\n>> ")

                print("\t\t==========QA==========")

                if agent_gender == "1":

                    agent_gender = input(f"astaghferolah!!!\nthats haram brother!!!"
                                         f"for customer oriented we put \"anahita\" option, "
                                         f"but we know you choose \"keykavos\""
                                         f"\n*tip: Allah watching you."
                                         f"\n1-anahita\t2-keykavos\n>> ")

                    if agent_gender == "1":

                        agent_gender = "anahita"

                        print("OK. we select \"anahita\" for you but come down from devil`s donkey bro.")

                        print("\t\t==========QA==========")

                    elif agent_gender == "2":

                        agent_gender = "keykavos"

                        print("Finally. you came down from devil`s donkey, brother.")

                        print("\t\t==========QA==========")

                    else:
                        die_in("Wrong number...")

                        print("\t\t==========QA==========")

                elif agent_gender == "2":
                    agent_gender = "keykavos"

                    print(f"Nice. you are a good man, {name}")

                    print("\t\t==========QA==========")

                else:

                    die_in("Wrong number...")

                    print("\t\t==========QA==========")

            # exit
            else:

                die_in("Go and come whenever you are ready.")

        # menu: exit
        elif "3" in select_menu:

            die_in(f":( Come back soon {name}")

            print("\t\t==========QA==========")
        # exit
        else:

            die_in("Wrong number!!! start again")

            print("\t\t==========QA==========")

        # call question function
        question(1, "What is the name of the python 2022 course teacher?", "Khaje nasir tosy", "Abbas bo azar",
                 "Prof. mehrdad naderi", "Ali was dead and I gave him a pair of pants", "3",
                 f"{agent_gender}: True, respect plus for \"Prof. naderi\"",
                 f"{agent_gender}: Realy!! i don`t talk to you anymore.")

        question(2, "Which football team logo is not shown on IR TV?", "AC roma", "Chelsea", "Manchester", "PSG", "1",
                 f"{agent_gender}: True, lets Censor some wolf bibi.", f"{agent_gender}: AC roma, you need check your"
                                                                       f" instagram !!!")

        question(3, "How call a function in python?", "Screaming", "Use function name+()", "Use video call",
                 "I need google", "2", f"{agent_gender}: Noice, after function call me, smart.", f"{agent_gender}: "
                                                                                                 f"2 Is correct, "
                                                                                                 f"yo looser. ")

        question(4, "He named the international day of quds:", "The United Nations (UN)", "Imam khomeini",
                 "Barack obama", "Ali dayi", "2", f"{agent_gender}: Damn {name}, you are intelligent",
                 f"{agent_gender}: Bruh, answer is imam khomeini, this is quds!!!")

        question(5, "How to find ASCII number of a character?", "ord('character')", "chr('character')", "Ask the ASCII",
                 "Who is ASCII?", "1", f"{agent_gender}: Clever, call me sometimes <3.", f"{agent_gender}: 1 Is "
                                                                                         f"correct option, so close!!")

        # middle game menu (continue , show score)
        select = int(input("Now we are at the middle of game,select one of this options:\n1.continue\n2.show score"
                           "\n>> "))

        # menu: show score
        if select == 2:

            # call score function
            show_score(name, agent_gender)

            # select for continue
            select = input("Do you want continue?(Yes/No):>> ")

            # continue game
            if "Y" in select or "y" in select:

                print("Let`s continue:")

            # exit
            else:
                die_in("Go and come whenever you are ready.")

        # menu: continue
        else:

            print("\t\t==========QA==========")

            print("Let`s continue:")

        question(6, "What is the apple company logo?", "Cherries", "Cucumber", "Apple", "Nectarine", "3",
                 f"{agent_gender}: Brilliant, now i need apple to eat.(0-0 i am a robot damn!!)",
                 f"{agent_gender}: Apple is the correct answer , i want to see you !!! not joking.")

        question(7, "How many inputs should there be in the function?", "1", "4", "1000", "5", "4",
                 f"{agent_gender}: wow, nice i like this one", f"{agent_gender}: 5 Is the answer , nice try")

        question(8, "What is it: that has only one 'r'?", "Abbas bo azar", "mohammad ali kley", "pelle", "CR7", "1",
                 f"{agent_gender}: great, do you know abbas is my favorite name ", f"{agent_gender}: abbas is the "
                                                                                   f"answer, don`t fuck with them.")

        question(9, "Which one is incorrect?", "print(f{\"text\"})", "print(\"text{}\".format())", "print(f\"{}text\")",
                 "print(value)", "1", f"{agent_gender}: Nice, you saw the tip", f"{agent_gender}: 1 Is correct answer"
                                                                                f",i win this game i think XD.")

        question(10, "Do you like this game?", "Yes", "ّNo", "Not bad", "IDK", "1",
                 f"{agent_gender}: We are not selfish ;). thank you for playing our game", f"{agent_gender}: ok.")

        # call write in text file function for write client score
        result_file(f"{name},This is your Score: ")

        # call write in text file function for write client score
        result_file(str(point_player))

        # call write in text file function for write client score < 5
        if point_player < 5:
            result_file("\nYou lose against a bot. you need this :")

            result_file("\nhttps://bmbgk.ir/?q=how+defeat+a+bot+in+a+simple+game")

        # call write in text file function for write client score >= 5
        else:
            result_file("\nYou win this battle, good job.\nthis is your gift:")

            result_file("\nhttps://bruno-simon.com")

        # last menu (score , end)
        select = int(input("End of questions:\n1- show score\n2- end\n>> "))

        # call score function
        if select == 1:

            # call show score function
            show_score(name, agent_gender)

            # last massage for client
            print("So we are here at the end...\nwe creat a text file for you and put a surprise on that."
                  "\ncheck it now .(in the same location where game is).\n\t\t=========AN===========")

            input("without saying goodbye?")

        # exit
        else:

            # last massage for client
            print("So we are here at the end...\nwe creat a text file for you and put a surprise on that."
                  "\ncheck it now .(in the same location where game is).\n\t\t=========AN===========")

            input("without saying goodbye?")

    # language = persian
    elif "2" in lang or "t" in lang or "T" in lang:

        print("*** به بازی پرسش و پاسخ خوش آمدید ***")

        # take client name
        name = input("نام خود را وارد کنید:\n>> ")

        # take client gender
        player_gender = input("جنسیت خود را انتخاب کنید:\n1-بانو\t2-آقا\n>> ")

        print("\t\t==========QA==========")

        print("*** منوی اصلی ***")

        # menu selection by client(start game , about , exit)
        select_menu = input("1.شروع بازی\n2.درباره ی بازی\n3.خروج\n>> ")

        print("\t\t==========QA==========")

        # menu : start game (female)
        if "1" in select_menu and "1" in player_gender:

            # take bot gender from client
            agent_gender = input(f"* نکته: با نوشتن کلمه ی خروج در هر مرحله از بازی ، به طور کامل بازی متوقف می شود.\n"
                                 f"سلام خانم {name} ، خوشحالیم که ما رو همراهی می فرمایید.\nحالا رقیب خودتون رو انتخاب"
                                 f" نمایید:\n1-آناهیتا\t2-کیکاوس\n>> ")

            print("\t\t==========QA==========")

            # select female bot
            if agent_gender == "1":

                agent_gender = "آناهیتا"

            # select male bot
            elif agent_gender == "2":

                agent_gender = "کیکاوس"

            # exit
            else:

                die_in("عدد اشتباه وارد شده است.")

        # menu : start game (male)
        elif "1" in select_menu and "2" in player_gender:

            # take bot gender from client
            agent_gender = input(f"* نکته: با نوشتن کلمه ی خروج در هر مرحله از بازی ، به طور کامل بازی متوقف می شود.\n"
                                 f"سلام \"آقا {name}\", رقیب خودتون رو انتخاب نمایید.\n"
                                 f"ما فقط برای شما \"کیکاوس\" را داریم, \"{name}\" اگر شما رقیب"
                                 f" خانم\"آناهیتا\" را میخواهید گزینه ی 1 را بزنید):\n1-گزینه ی بیشتر\t2-کیکاوس\n>> ")

            print("\t\t==========QA==========")

            # select female bot
            if agent_gender == "1":

                agent_gender = input(f"استغفرالله!!!\nزشته برادر من!!"
                                     f"ما برای مشتری مداری از شما پرسیدیم \"آناهیتا\" رو میخواهید یا نه، نه "
                                     f"اینکه شما انتخابش کنید. "
                                     f"\n* نکته: خدا ترسی کم شده."
                                     f"\n1-آناهیتا\t2-کیکاوس\n>> ")

                # select female bot
                if agent_gender == "1":

                    agent_gender = "آناهیتا"

                    print("خوب. ما برای شما \"آناهیتا\" رو انتخاب کردیم ولی شما دفعه بعد از خر شیطان به "
                          "پایین آمده و کیکاوس را انتخاب نمایید.")

                    print("\t\t==========QA==========")

                # select male bot
                elif agent_gender == "2":

                    agent_gender = "کیکاوس"

                    print("ایولا. بلاخره از خر شیطان پایین آمدید.")

                    print("\t\t==========QA==========")

                # exit
                else:
                    die_in("عدد اشتباه وارد شده است.")

                    print("\t\t==========QA==========")

            # select male bot
            elif agent_gender == "2":
                agent_gender = "کیکاوس"

                print(f"عالی. کیکاوس انتخاب اول و آخر همه, \"{name}\"")

                print("\t\t==========QA==========")

            # exit
            else:

                die_in("عدد اشتباه وارد شده است.")

                print("\t\t==========QA==========")

        # menu: about QA (female)
        elif "2" in select_menu and "1" in player_gender:

            # introduce text
            print(f"*** سلام \"خانوم {name}\",به بازی ما خوش آمدید ***\n"
                  f"این بک بازی دو نفره ی فان هست که شما با جواب صحبح دادن به سوالات یک امتیاز به"
                  f" امتیازات خودتون اضافه میکنید.\n"
                  f"بریم که شروع کنیم,خوش بگذره.")

            # start game after about
            select = input("آماده ای?(بله/خیر):>> ")

            print("\t\t==========QA==========")

            # start game (same body as line 343)
            if "ب" in select or "ا" in select:

                agent_gender = input(
                    f"* نکته: با نوشتن کلمه ی خروج در هر مرحله از بازی ، به طور کامل بازی متوقف می شود.\n"
                    f"سلام خانم  {name} ، خوشحالیم که ما رو همراهی می فرمایید.\nحالا رقیب خودتون رو انتخاب"
                    f" نمایید:\n1-آناهیتا\t2-کیکاوس\n>> ")

                print("\t\t==========QA==========")

                if agent_gender == "1":

                    agent_gender = "آناهیتا"

                elif agent_gender == "2":

                    agent_gender = "کیکاوس"

                else:

                    die_in("عدد اشتباه وارد شده است.")
            else:

                die_in("برو هر وقت آماده بودی بیا. برگردیا، ما منتظریم.")

        # menu: about QA (female)
        elif "2" in select_menu and "2" in player_gender:

            # introduce text
            print(f"*** سلام \"آقا {name}\",به بازی ما خوش آمدید ***\n"
                  f"این بک بازی دو نفره ی فان هست که شما با جواب صحبح دادن به سوالات یک امتیاز به"
                  f" امتیازات خودتون اضافه میکنید.\n"
                  f"بریم که شروع کنیم,خوش بگذره.")

            # start game after about
            select = input("آماده ای?(بله/خیر):>> ")

            print("\t\t==========QA==========")

            # start game (same body as line 368)
            if "ب" in select or "ا" in select:

                agent_gender = input(f"* نکته: با نوشتن کلمه ی خروج در هر مرحله از بازی ، به طور کامل بازی متوقف می "
                                     f"شود.\n "
                                     f"سلام \"آقا{name}\" ,رقیب خودتون رو انتخاب نمایید.\n"
                                     f"ما فقط برای شما \"کیکاوس\" را داریم, \"{name}\" اگر شما رقیب"
                                     f" خانم\"آناهیتا\" "
                                     f"را میخواهید گزینه ی 1 را بزنید:\n1-گزینه ی بیشتر\t2-کیکاوس\n>> ")

                print("\t\t==========QA==========")

                if agent_gender == "1":

                    agent_gender = input(f"استغفرالله!!!\nزشته برادر من!!"
                                         f"ما برای مشتری مداری از شما پرسیدیم \"آناهیتا\" رو میخواهید یا نه، نه"
                                         f"اینکه شما انتخابش کنید. "
                                         f"\n* نکته: خدا ترسی کم شده."
                                         f"\n1-آناهیتا\t2-کیکاوس\n>> ")

                    if agent_gender == "1":

                        agent_gender = "آناهیتا"

                        print("خوب. ما برای شما \"آناهیتا\" رو انتخاب کردیم ولی شما دفعه بعد از خر شیطان به "
                              "پایین آمده و کیکاوس را انتخاب نمایید.")

                        print("\t\t==========QA==========")

                    elif agent_gender == "2":

                        agent_gender = "کیکاوس"

                        print("ایولا. بلاخره از خر شیطان پایین آمدید.")

                        print("\t\t==========QA==========")

                    else:
                        die_in("عدد اشتباه وارد شده است.")

                        print("\t\t==========QA==========")

                elif agent_gender == "2":
                    agent_gender = "کیکاوس"

                    print(f"عالی. کیکاوس انتخاب اول و آخر همه, \"{name}\"")

                    print("\t\t==========QA==========")

                else:

                    die_in("عدد اشتباه وارد شده است.")

                    print("\t\t==========QA==========")

            else:

                die_in("برو هر وقت آماده بودی بیا. برگردیا، ما منتظریم.")

        # menu: exit
        elif "3" in select_menu:

            die_in(f":( زودی بیا پیشمون {name}")

            print("\t\t==========QA==========")

        # exit
        else:

            die_in("عدد اشتباه وارد شده است. دوباره تلاش کنید.")

            print("\t\t==========QA==========")

        # call question function
        question_pe(1, "نام استاد دوره ی پایتون 2022؟", "خواجه نصیر طوسی", "عباس بوعذار",
                    "استاد مهرداد نادری", "اون علی که مرده بود و من بهش شلوار دادم", "3",
                    f"{agent_gender}: درسته, احترام + برای استاد نادری :",
                    f"{agent_gender}: جدا!! دیگه باها تصحبت نمیکنم.")

        question_pe(2, "لوگو کدام تیم را تلوزیون ما سانسور کرد؟", "رم", "چلسی", "منچستر", "پی اس جی", "1",
                    f"{agent_gender}: دقیقا ، بریم بی ادبی گرگ سانسور کنیم :)", f"{agent_gender}: رم, "
                                                                                f"بیا برات اینستا نصب کنم !!!")

        question_pe(3, "چجوری در پایتون یک تابع رو صدا کنیم؟", "داد بزنیم", "Use function name+()", "تماس تصویری"
                                                                                                    " بگیریم",
                    "از محمد بخوایم صداش کنه", "2", f"{agent_gender}: عالی ، کاملا درست."
                    f"{agent_gender}: دیگه اینو باید میگفتی"
                    f" جدی!!! بزار یه زنگ به محمد بزنم بیاد پیشت !!! 2 درست بود. ","jui")

        question_pe(4, "چه کسی روز جهانی قدس را نام گذاری کرد؟", "سازمان ملل متحد", "امام خمینی (ره)",
                    "باراک حسین اوباما", "علی دایی(اوشاخلاری)", "2",
                    f"{agent_gender}: ماشالا {name}, دیگه داری میبری منو ",
                    f"{agent_gender}: جواب درست امام خمینی بود، داریم درباره قدس حرف میزنیما!!!")

        question_pe(5, "نحوه پیدا کردن عدد ASCII یک کاراکتر:", "ord('character')", "chr('character')", "از ASCII"
                                                                                                       " میپرسیم",
                    "ASCII کی هست؟", "1", f"{agent_gender}: باریکلا, دانلود گدرت برای تو. ", f"{agent_gender}"
                                                                                             f": "
                                                                                             f"جواب درست یک بود، "
                                                                                             f"خیلی نزدیک بودی!!")
        # middle game menu (continue , show score)
        select = int(input("خوب رسیدیم به میانه ی بازی"
                           "، یه اسراحت ریز کنیم یا ادامه بدیم؟:\n1.ادامه بازی\n2.نشان دادن امتیاز"
                           "\n>> "))

        # menu: show score
        if select == 2:

            # call score function
            show_score_pe(name, agent_gender)

            # select for continue
            select = input("ادامه بدیم؟(بله/خیر):>> ")

            # continue game
            if "ب" in select or "ا" in select:

                print("برو که بریم:")

            # exit
            else:
                die_in("برو هروقت اماده بودی بیا، یادت نره ها.")

        # menu: continue
        else:

            print("\t\t==========QA==========")

            print("برو که بریم:")

        question_pe(6, "لوگوی کمپانی اپل چیست؟", "شلیل", "خیار", "سیب", "آواکادو", "3",
                    f"{agent_gender}: دست خوش, اسم سیب اومد گشنم شد.(0-0 ای وای، من که یه رباتم!!)",
                    f"{agent_gender}: سیب گزینه ی درست بود , دوره ی زبان استاد رو سریع ثبت نام کن، سریع!!")

        question_pe(7, "چه تعداد ورودی مرسوم است برای هر تابع؟", "1", "4", "1000", "5", "4",
                    f"{agent_gender}: عالی، نکته بین کی بودی!",
                    f"{agent_gender}: جواب درست گزینه ی 4 بود , تلاش خوبی بود.")

        question_pe(8, "اون فقط یه دونه 'ر' داره:", "عباس بوعذار", "محمد علی کلی", "پله", "رونالدو", "1",
                    f"{agent_gender}: درسته، میدونستی عباس رفیق منه؟ ", f"{agent_gender}: عباس گزینه ی درست بود "
                                                                        f"هیچ وقت با عباس ها در نیوفت.")

        question_pe(9, "کدام نادرست است؟", "print(f{\"text\"})", "print(\"text{}\".format())", "print(f\"{}text\")",
                    "print(value)", "1", f"{agent_gender}: قوی، نکته رو فهمیدی .", f"{agent_gender}: جواب درست 1 بود"
                                                                                   f",من "
                                                                                   f"این بازی رو میبرم آخر سر:).")

        question_pe(10, "سرعت نور چگونه است?", "خوب است", "ّبد نیست", "سلام دارد", "به خانواده سلام برسونید", "1",
                    f"{agent_gender}: سرعت نور از شما تشکر میکنه", f"{agent_gender}: یادت باشه، سرعت نور"
                                                                   f" همیشه خوب است!!")

        # call write in text file function for write client score
        result_file(f"{name},امتیاز شما: ")

        # call write in text file function for write client score
        result_file(str(point_player))

        # call write in text file function for write client score < 5
        if point_player < 5:

            result_file("\nاز یه بات باختی، به این احتیاج داری:")

            result_file("\nhttps://bmbgk.ir/?q=%DA%86%DA%AF%D9%88%D9%86%D9%87+%DB%8C%DA%A9+%D8%A8%D8%A7%D8%AA+%D8%B"
                        "1%D8%A7+%D8%AF%D8%B1+%DB%8C%DA%A9+%D8%A8%D8%A7%D8%B2%DB%8C+%D8%B3%D8%A7%D8%AF%D9%87+%D8%B4%D"
                        "A%A9%D8%B3%D8%AA+%D8%AF%D9%87%DB%8C%D9%85%D8%9F")

        # call write in text file function for write client score >= 5
        else:
            result_file("\nبر طبل شادانه بکوب، پیروز این میدان تو بودی.\nاین هم هدیه شما:")

            result_file("\nhttps://bruno-simon.com")

        # last menu (score , end)
        select = int(input("پایان سوالات:\n1- نشان دادن امتیازات\n2- پایان\n>> "))

        # call score function
        if select == 1:

            # call show score function
            show_score_pe(name, agent_gender)

            # last massage for client
            print("خوب رسیدیم به آخرش...\nما یک تکست فایل برات ایجاد کردیم که شامل یه سورپرایز هست."
                  "\nهمین الان چک کنش (دقیقا در همین مسیری که بازی قرار داره ساخته شده.).")

            print("\t\t==========AN==========")

            input("بدون خداحافظی میخواستی بری؟")

        # exit
        else:

            # last massage for client
            print("خوب رسیدیم به آخرش...\nما یک تکست فایل برات ایجاد کردیم که شامل یه سورپرایز هست."
                  "\nهمین الان چک کنش (دقیقا در همین مسیری که بازی قرار داره ساخته شده.).")

            print("\t\t==========AN==========")

            input("بدون خداحافظی میخواستی بری؟")

    # language = wrong number or character (exit)
    else:

        die_in("Wrong number...")

        print("\t\t==========QA==========")


# exit function
def die_in(text):
    print(text)

    exit(0)


# function question: count = for number of question , ask = question text , op_1-4 = question options
# c_answer = correct answer , agent_l = text when client give a correct answer
# agent_w = text when client give a incorrect answer
def question(count, ask, op_1, op_2, op_3, op_4, c_answer, agent_l, agent_w):
    global point_player, point_agent

    print(f"question {count}:\n{ask}\n1.{op_1}\n2.{op_2}\n3.{op_3}\n4.{op_4}")

    answer = input(">> ")

    if c_answer in answer:

        print(agent_l)

        point_player += 1

    elif "e" in answer:

        die_in("Bye!!!")

    else:
        print(agent_w)

        point_agent += 1

    print("\t\t----------QA----------")


# function show score: name = line 21 , agent gender = select by client in body
def show_score(name, agent_gender):
    print(f"{name}`s score: {point_player} \n{agent_gender}`s score: {point_agent} ")

    print("\t\t==========QA==========")


# same question function just in persian
def question_pe(count, ask, op_1, op_2, op_3, op_4, c_answer, agent_l, agent_w):
    global point_player, point_agent

    print(f"سوال {count}:\n{ask}\n1.{op_1}\n2.{op_2}\n3.{op_3}\n4.{op_4}")

    answer = input(">> ")

    if c_answer in answer:

        print(agent_l)

        point_player += 1

    elif "خ" in answer:

        die_in("چرا رفتی، چرا من بی قرارم!!")
    else:
        print(agent_w)

        point_agent += 1

    print("\t\t----------QA----------")


# same score function just in persian
def show_score_pe(name, agent_gender):
    print(f"امتیاز {name}: {point_player} \nامتیاز {agent_gender}: {point_agent} ")

    print("\t\t==========QA==========")


# function write text file: text = text for writing in text file
def result_file(text):
    result_a = open("Result-QA-Game.txt", 'a+')

    result_a.write(text)


# start program
if __name__ == '__main__':
    # var for save player point
    point_player = 0
    # var for save bot point
    point_agent = 0
    # var for show points
    score = 0
    # create text file
    result_w = open("Result-QA-Game.txt", 'w+')
    # call main function
    qa_game()

# Never be a slave to the rules.
