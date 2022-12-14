from django.db import models
from django.contrib.auth.models import User

class UserRequest(models.Model):
    STATUS = [
        (1, 'НОВАЯ ЗАЯВКА'),
        (2, 'ЗАЯВКА ЗАКРЫТА'),
    ]
    DEPARTMENT = [
        (1, 'ДП КАРАГАНДИНСКОЙ ОБЛАСТИ'),
        (2, 'ОКТЯБРЬСКИЙ ОП'),
        (3, 'ЦЕНТРАЛЬНЫЙ ОП'),
        (4, 'МИХАЙЛОВСКИЙ ОП'),
        (5, 'КИРОВСКИЙ ОП'),
        (6, 'ЮГО-ВОСТОЧНЫЙ ОП'),
        (7, 'ЖЕЛЕЗНОДОРОЖНЫЙ ОП'),
        (8, 'НОВО-МАЙКУДУКСКИЙ ОП'),
        (9, 'УП Г.КАРАГАНДЫ'),
        (10, 'ВОСТОЧНЫЙ ОП'),
        (11, 'СТАРОГОРОДСКОЙ ОП'),
        (12, 'УП Г.ТЕМИРТАУ'),
        (13, 'ОП Г.ЖЕЗКАЗГАН'),
        (14, 'ОП Г.САРАНЬ'),
        (15, 'ОП Г.ШАХТИНСК'),
        (16, 'ОП Г.ПРИОЗЕРСК'),
        (17, 'ОП Г.КАРАЖАЛ'),
        (18, 'ОП Г.САТПАЕВ'),
        (19, 'ОП Г.БАЛХАШ'),
        (20, 'ОП АБАЙСКОГО РАЙОНА'),
        (21, 'ТОПАРСКИЙ ОП'),
        (22, 'ОП БУХАР-ЖЫРАУСКОГО РАЙОНА'),
        (23, 'ОП ИМ.МУСТАФИНА'),
        (24, 'ОП ОСАКАРОВСКОГО РАЙОНА'),
        (25, 'ОП НУРИНСКОГО РАЙОНА'),
        (26, 'ОП КАРКАРАЛИНСКОГО РАЙОНА'),
        (27, 'ОП АКТОГАЙСКОГО РАЙОНА'),
        (28, 'ОП ШЕТСКОГО РАЙОНА'),
        (29, 'ОП ЖАНААРКИНСКОГО РАЙОНА'),
        (30, 'ОП УЛЫТАУСКОГО РАЙОНА'),
    ]
    MANAGEMENT = [
        (1, '01 РУКОВОДСТВО'),
        (2, '02 СОВЕТНИК/ПОМОЩНИК'),
        (3, '03 КРИМИНАЛЬНАЯ ПОЛИЦИЯ'),
        (4, '04 ПО БОРЬБЕ С ОРГ.ПРЕСТУПНОСТЬЮ'),
        (5, '05 ПО ПРОТИВОДЕЙСТВИЮ ЭКСТРЕМИЗМУ'),
        (6, '06 ПО ПРОТИВОДЕЙСТВИЮ НАРКОПРЕСТУПНОСТИ'),
        (7, '07 СЛЕДСТВИЕ'),
        (8, '08 ДОЗНАНИЕ'),
        (9, '09 СЛЕДСТВИЕ ВОЕННО-СЛЕДСТВЕННОГО ПОДРАЗДЕЛЕНИЯ'),
        (10, '10 ОПЕРАТИВНЫЕ СЛУЖБЫ ВОЕННО-СЛЕДСТВЕННОГО ПОДРАЗДЕЛЕНИЯ'),
        (11, '11 АДМИНИСТРАТИВНАЯ ПОЛИЦИЯ'),
        (12, '12 АДМИНИСТРАТИВНАЯ ПОЛИЦИЯ'),
        (13, '13 МПС - УИП'),
        (14, '14 МПС - ЮВEНАЛЬНАЯ ПОЛИЦИЯ'),
        (15, '15 МПС - ПРИЕМНИК-РАСПРЕДЕЛИТЕЛЬ'),
        (16, '16 МПС - СПЕЦИАЛЬНЫЙ ПРИЕМНИК'),
        (17, '17 МПС - ВОДНАЯ ПОЛИЦИЯ'),
        (18, '18 МПС - ПРИРОДООХРАННАЯ ПОЛИЦИЯ'),
        (19, '19 АДМИНИСТРАТИВНАЯ ПОЛИЦИЯ - ИВС'),
        (20, '20 МПС-ДОРОЖНО-ПАТРУЛЬНАЯ СЛУЖБА'),
        (21, '21 АДМИНИСТРАТИВНАЯ ПОЛИЦИЯ - РЭО'),
        (22, '22 АДМИНИСТРАТИВНАЯ ПОЛИЦИЯ - АДМПРАКТИКА'),
        (23, '23 МЕСТНАЯ ПОЛИЦЕЙСКАЯ СЛУЖБА'),
        (25, '25 МИГРАЦИОННАЯ СЛУЖБА'),
        (26, '26 МИГРАЦИОННАЯ СЛУЖБА - ДОКУМЕНТИРОВАНИЕ И РЕГИСТРАЦИЯ ГРАЖДАН'),
        (27, '27 ЦОУ'),
        (28, '28 ДЕЖУРНАЯ ЧАСТЬ'),
        (29, '29 УГОЛОВНО-ИСПОЛНИТЕЛЬНАЯ СИСТЕМА'),
        (30, '30 ВОЕННАЯ ПОЛИЦИЯ НГ'),
        (31, '31 НАЦИОНАЛЬНАЯ ГВАРДИЯ'),
        (32, '32 СЛЕДСТВИЕ СОБСТВЕННОЙ БЕЗОПАСНОСТИ'),
        (33, '33 ОПЕРАТИВНЫЕ СЛУЖБЫ СОБСТВЕННОЙ БЕЗОПАСНОСТИ'),
        (34, '34 КАДРОВАЯ ПОЛИТИКА'),
        (35, '35 ОПЕРАТИВНО-КРИМИНАЛИСТИЧЕСКИЕ ПОДРАЗДЕЛЕНИЯ'),
        (36, '36 ШТАБ - УЧЕТНО-РЕГИСТРАЦИОННАЯ ДИСЦИПЛИНА'),
        (37, '37 ПОДРАЗДЕЛЕНИЯ ИНФОРМАЦИОННОГО ОБЕСПЕЧЕНИЯ'),
        (38, '38 ИНТЕРПОЛ'),
        (39, '39 СЕДЬМОЙ ДЕПАРТАМЕНТ'),
        (40, '40 ДЕПАРТАМЕНТ'),
        (41, '41 ОПЕРАТИВНОЕ ПЛАНИРОВАНИЕ'),
        (42, '42 ПОДРАЗДЕЛЕНИЯ СПЕЦИАЛИЗИРОВАННОЙ СЛУЖБЫ ОХРАНЫ'),
        (43, '43 ДРУГОЕ (НЕ ОВД)'),
        (44, '44 ОГСО'),
        (45, '45 ПОДРАЗДЕЛЕНИЯ РАДИОСВЯЗИ ДИС (ТОЛЬКО ДЛЯ ТЕТРЫ)'),
        (46, '46 ЛИНИЯ А КРИМИНАЛЬНОЙ ПОЛИЦИИ'),
        (47, '47 ИНЫЕ'),
        (48, '48 ПОДРАЗДЕЛЕНИЯ ФИНАНСОВОГО ОБЕСПЕЧЕНИЯ'),
        (49, '49 ПОДРАЗДЕЛЕНИЯ ДОКУМЕНТАЦИОННОГО ОБЕСПЕЧЕНИЯ'),
        (50, '50 АДМИНИСТРАТИВНАЯ ПОЛИЦИЯ – ОКОД')
    ]
    DB = [
        (1, 'ИБД МВД РК'),
        (2, 'ИБД ОБЛАСТНОЙ'),
        (3, 'ИНФОСЕРВИС'),
        (4, 'АБД СТАТИСТИКА'),
        (5, 'АБД УОН'),
        (6, 'БЕРКУТ ГО')
    ]
    status = models.BigIntegerField('Статус', choices=STATUS, default=1)
    iin = models.CharField('ИИН', max_length=12)
    first_name = models.CharField('Фамилия', max_length=50)
    middle_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Отчество', max_length=50, blank=True, null=True)
    department = models.BigIntegerField('Подразделение', choices=DEPARTMENT)
    management = models.BigIntegerField('Служба', choices=MANAGEMENT)
    job = models.CharField('Должность', max_length=200)
    phone = models.CharField('Сотовый телефон', max_length=12)
    db = models.BigIntegerField('База данных', choices=DB)
    login = models.CharField('Логин', max_length=30,  blank=True, null=True)
    password = models.CharField('Пароль', max_length=30, blank=True, null=True)
    request_date = models.DateField('Дата подачи заявки', blank=True, null=True)
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    create_author = models.CharField('Автор создания', max_length=50, blank=True, null=True)
    change_date = models.DateTimeField('Дата изменения', auto_now=True, blank=True, null=True)
    change_author = models.CharField('Автор изменения', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Заявка пользователя'
        verbose_name_plural = 'Заявки пользователей'

