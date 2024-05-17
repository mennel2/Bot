from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('Привет! Я - бот, который расскажет тебе все про лицей 533. Что бы ты хотел(а) узнать?\n'
                              '/location - Как добраться до корпуса\n'
                              '/help - Просмотреть команды\n'
                              '/teachers - Посмотреть список учителей гуманитарных классов\n'
                              '/exam - Узнать примерное содержание экзамена\n'
                              )

def teachers_command(update, context):
    update.message.reply_text("Вот список преподавателей:\n"
                              "Андрианова Екатерина Николаевна - ОБЖ\n"
                              "Артамонова Анна Олеговна - физика\n"
                              "Битюкова Марина Николаевна - биология\n"
                              "Вдовиченко Даниил Андреевич - химия\n"
                              "Дивенков Владимир Андреевич - информатика\n"
                              "Иванова Татьяна Алексеевна - химия\n"
                              "Казакова Елена Олеговна - искусство\n"
                              "Кузнецова Ольга Геннадьевна - русский, риторика, литература\n"
                              "Нанобашвили Татьяна Вячеславовна - история, куратор всех гум. классов\n"
                              "Никифорова Светлана Олеговна - география\n"
                              "Облендер Анастасия Борисовна - история русского, древнерусская литература\n"
                              "Прадун Светлана Александровна - литература, русский\n"
                              "Ремнёв Денис Константинович - физкультура\n"
                              "Соколов Юрий Алексеевич - история древнего мира\n"
                              "Тарабукина Арина Валерьевна - литература, поэтика\n"
                              "Тишунин Алексей Викторович - обществознание\n"
                              "Травкин Сергей Николаевич - история\n"
                              "Туманова Ирина Михайловна - математика\n"
                              "Чайковская Арина Алексеевна - английский\n"
                              "Шайдуров Павел Александрович - английский\n")

def exam_com(update, context):
    update.message.reply_text("Вот что будет на вступительных:\n"
                              "Для начала надо добраться до корпуса на Таллинской 26к.2(если не очень понимаешь как - введи команду /location)\n"
                              "Дальше надо пройти через турникет и подняться на 4 этаж, повернуть направо в рекреацию и уточнить кабинеты, в которых будут проходить экзамены, которые ты сдаешь\n"
                              "Тест по общей эрудиции включает в себя вопросы по МХК(в пределах Санкт-Петербурга), проверку знаний пословиц и поговорок и известных фраз на подобие свобода, равенство и братство, в которых пропущено слово и его надо вставить, в то же время проводится тест по русскому, в котором проверяются базовые знания\n"
                              "На тесте по истории у тебя спросят, что вы проходили в этом году и будут задавать вопросы только по тем темам, которые были в году\n"
                              "На тесте по английскому языку письменные вопросы будут разбиты в несколько блоков по уровню сложности и включают в себя знания грамматики и лексики, на устной части проводится стандартный опрос - задаются вопросы про тебя, твою семью, хобби и так далее\n"
                              "На тесте по литературе тебя спросят, какие книги ты читал кроме программных, какие жанры тебе нравятся и что вы проходили в этом году, далее будут вопросы по пройденным в году произведениям\n"
                              "На этом вступительные закончены и остается только ждать результата, который придет по электронной почте, удачи!")

def loc_com(update, context):
    update.message.reply_text('Тебе нужна станция метро Новочеркасская, дальше найди 9 выход и поднимись. После этого иди вперед, пока слева не увидишь "Пятерочку", тогда поворачивай налево и увидишь здание')

def help_command(update, context):
    update.message.reply_text('Вот что я могу рассказать:\n'
                              '/location - Как добраться до корпуса\n'
                              '/help - Просмотреть команды\n'
                              '/teachers - Посмотреть список учителей\n'
                              '/exam - Узнать примерное содержание экзамена\n')

def unknown(update, context):
    update.message.reply_text("Извини, я не понимаю, что ты имеешь в виду")

def main():
    updater = Updater("7019507148:AAGedJXqCjL1ZYejw_I4tYn5VTtZ2Be9pCw")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("exam", exam_com))
    dispatcher.add_handler(CommandHandler("location", loc_com)),
    dispatcher.add_handler(CommandHandler("start", start)),
    dispatcher.add_handler(CommandHandler("teachers", teachers_command)),
    dispatcher.add_handler(CommandHandler("help", help_command)),
    dispatcher.add_handler(MessageHandler(Filters.command, unknown)),


    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()