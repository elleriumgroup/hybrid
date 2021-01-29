use hybrid;
delete from statcards_spr_f10r1;
insert into statcards_spr_f10r1(code, name) values
    ('01','01 - ОВД'), ('02','02 - СК РФ'), ('04','04 - ТАМОЖ.'), ('05','05 - СУД'), ('06','06 - ФСИН'), ('7','07 - ФСБ'),
    ('8','08 - ФССП'), ('9','09 - ИНОЙ'), ('10','10 - ГПН ФПС'), ('11','11 - ПС ФСБ'), ('14','14 - ФСКН');

delete from statcards_spr_f10r1_organ;
insert into statcards_spr_f10r1_organ(code, name) values
    ('1','01 - УМВД РОССИИ ПО Г. АРХАНГЕЛЬСК ПО ОБС. ОКТЯБРЬСКОГО ОКРУГА'),
    ('2','02 - ЛОМОНОСОВСКИЙ (ОП №3)'), ('3','03 - СОЛОМБАЛЬСКИЙ (ОП №5)'),
    ('4','04 - ИСАКОГОРСКИЙ (ОП №2)'), ('6','06 - СЕВЕРОДВИНСК'), ('7','07 - ВАРАВИНО-ФАКТОРИЯ (ОП №1)'),
    ('8','08 - ВЕЛЬСКИЙ'), ('9','09 - ВИЛЕГОДСКИЙ'), ('10','10 - ВИНОГРАДОВСКИЙ'), ('11','11 - ВЕРХНЕТОЕМСКИЙ'),
    ('12','12 - КАРГОПОЛЬСКИЙ'), ('13','13 - КОНОШСКИЙ'), ('14','14 - КОРЯЖМА'), ('15','15 - КОТЛАС'),
    ('16','16 - КОТЛАССКИЙ'), ('17','17 - КРАСНОБОРСКИЙ'), ('18','18 - ЛЕНСКИЙ'), ('19','19 - ЛЕШУКОНСКИЙ'),
    ('20','20 - МЕЗЕНСКИЙ'), ('22','22 - НОВОДВИНСК'), ('23','23 - НЯНДОМСКИЙ'), ('24','24 - ОНЕЖСКИЙ'),
    ('25','25 - ПИНЕЖСКИЙ'), ('26','26 - ПЛЕСЕЦКИЙ'), ('27','27 - ПРИМОРСКИЙ'), ('28','28 - УСТЬЯНСКИЙ'),
    ('29','29 - ХОЛМОГОРСКИЙ'), ('30','30 - ШЕНКУРСКИЙ'), ('45','45 - УМВД РОССИИ ПО ГОРОДУ АРХАНГЕЛЬСКУ'),
    ('63','63 - УУР УМВД РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ'), ('64','64 - МИРНЫЙ'), ('65','65 - 4-Й ОТДЕЛ');

delete from statcards_spr_f10r3_gasorg;
insert into statcards_spr_f10r3_gasorg(code, name) values

('1009724;01009724 - СО МУРМАНСКОГО ЛО МВД РОССИИ НА ТРАНСПОРТЕ
('1110001;01110001 - УМВД РОССИИ ПО Г.АРХАНГЕЛЬСКУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110002;01110002 - ОМВД РФ ПО Г. СЕВЕРОДВИНСКУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110003;01110003 - МО МВД РФ КОТЛАССКИЙ АРХАНГЕЛЬСКОЙ ОБЛАСТИ (КОТЛАССКИЙ, КОТЛАС, КОРЯЖМА)
('1110004;01110004 - ОМВД РФ ПО ВЕЛЬСКОМУ РАЙОНУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110005;01110005 - МО МВД РФ КРАСНОБОРСКИЙ АРХАНГЕЛЬСКОЙ ОБЛАСТИ (КРАСНОБОРСКИЙ, ВЕРХНЕТОЕМСКИЙ)
('1110006;01110006 - ОМВД РФ ПО КОНОШСКОМУ РАЙОНУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110007;01110007 - МО МВД РФ МЕЗЕНСКИЙ АРХАНГЕЛЬСКОЙ ОБЛАСТИ (МЕЗЕНСКИЙ, ЛЕШУКОНСКИЙ)
('1110008;01110008 - МО МВД РФ НЯНДОМСКИЙ АРХАНГЕЛЬСКОЙ ОБЛАСТИ (НЯНДОМСКИЙ, КАРГОПОЛЬСКИЙ)
('1110009;01110009 - ОМВД РФ ПО ОНЕЖСКОМУ РАЙОНУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110010;01110010 - ОМВД РФ ПО ПИНЕЖСКОМУ РАЙОНУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110011;01110011 - ОМВД РФ ПО ПЛЕСЕЦКОМУ РАЙОНУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110012;01110012 - МО МВД РФ ПРИМОРСКИЙ АРХАНГЕЛЬСКОЙ ОБЛАСТИ (ПРИМОРСКИЙ, НОВОДВИНСК)
('1110013;01110013 - ОМВД РФ ПО УСТЬЯНСКОМУ РАЙОНУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110014;01110014 - ОМВД РФ ПО ХОЛМОГОРСКОМУ РАЙОНУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110015;01110015 - УМВД РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110016;01110016 - СУ УМВД РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110017;01110017 - ОП 1 УМВД РОССИИ ПО Г.АРХАНГЕЛЬСКУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ (ВАРАВИНО-ФАКТОРИЯ, МАЙСКАЯ ГОРКА)
('1110018;01110018 - ОП 2 УМВД РОССИИ ПО Г.АРХАНГЕЛЬСКУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ (ИСАКОГОРСКИЙ, ЦИГЛОМЕНСКИЙ)
('1110019;01110019 - ОП 3 УМВД РОССИИ ПО Г.АРХАНГЕЛЬСКУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ (ЛОМОНОСОВСКИЙ)
('1110021;01110021 - ОП 5 УМВД РОССИИ ПО Г.АРХАНГЕЛЬСКУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ (СОЛОМБАЛЬСКИЙ, СЕВЕРНЫЙ, МАЙМАКСАНСКИЙ)
('1110023;01110023 - ОП ПО Г.КОРЯЖМЕ МО МВД РОССИИ КОТЛАССКИЙ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110024;01110024 - ОМВД РФ ПО ВИЛЕГОДСКОМУ РАЙОНУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110025;01110025 - ОМВД РФ ПО ЛЕНСКОМУ РАЙОНУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110027;01110027 - ОП ПО ПРИМОРСКОМУ РАЙОНУ МО МВД РОССИИ ПРИМОРСКИЙ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110029;01110029 - ОМВД РФ ПО ШЕНКУРСКОМУ РАЙОНУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110031;01110031 - ОП ПО КАРГОПОЛЬСКОМУ РАЙОНУ МО МВД РОССИИ НЯНДОМСКИЙ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110033;01110033 - ОМВД РФ ПО ВИНОГРАДОВСКОМУ РАЙОНУ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110034;01110034 - МО МВД РФ ПО ЗАТО МИРНЫЙ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
('1110035;01110035 - ОП НА ОВИРО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
1110037;01110037 - ОП ПО ЛЕШУКОНСКОМУ РАЙОНУ МО МВД РОССИИ МЕЗЕНСКИЙ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
1110039;01110039 - ОП ПО ВЕРХНЕТОЕМСКОМУ РАЙОНУ МО МВД РОССИИ КРАСНОБОРСКИЙ АРХАНГЕЛЬСКОЙ ОБЛАСТИ
2007703;02007703 - ГУ СУ СК РФ
2007706;02007706 - ЗИЦ ГУ МВД РОССИИ ПО Г. МОСКВА
2007707;02007707 - ВТОРОЕ СУ ГСУ СК РФ
2110001;02110001 - СУ СК РФ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110002;02110002 - СО ПО ОКТЯБРЬСКОМУ ОКРУГУ Г. АРХАНГЕЛЬСК СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110003;02110003 - СО ПО ЛОМОНОСОВСКОМУ ОКРУГУ Г.АРХАНГЕЛЬСК СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110004;02110004 - СО ПО СОЛОМБАЛЬСКОМУ ОКРУГУ Г.АРХАНГЕЛЬСК СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110005;02110005 - СО ПО ИСАКОГОРСКОМУ ОКРУГУ Г.АРХАНГЕЛЬСК СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110006;02110006 - КОРЯЖЕМСКИЙ МЕЖРАЙОННЫЙ СО СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110007;02110007 - СО ПО Г.НОВОДВИНСК СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110008;02110008 - СО ПО Г.СЕВЕРОДВИНСК СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110009;02110009 - ВЕЛЬСКИЙ МЕЖРАЙОННЫЙ СО СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110010;02110010 - КОТЛАССКИЙ МЕЖРАЙОННЫЙ СО СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110011;02110011 - НЯНДОМСКИЙ МЕЖРАЙОННЫЙ СО СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110012;02110012 - СО ПО Г.ОНЕГА СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110013;02110013 - СО ПО ПИНЕЖСКОМУ РАЙОНУ СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110014;02110014 - СО ПО ЗАТО Г.МИРНЫЙ СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110015;02110015 - ПРИМОРСКИЙ МЕЖРАЙОННЫЙ СО СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110016;02110016 - ХОЛМОГОРСКИЙ МЕЖРАЙОННЫЙ СО СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110018;02110018 - СО ПО ОКРУГУ ВАРАВИНО-ФАКТОРИЯ Г.АРХАНГЕЛЬСК СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110019;02110019 - ПЕРВЫЙ ОТДЕЛ ПО РАССЛЕДОВАНИЮ ОСОБО ВАЖНЫХ ДЕЛ СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110020;02110020 - ВТОРОЙ ОТДЕЛ ПО РАССЛЕДОВАНИЮ ОСОБО ВАЖНЫХ ДЕЛ СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
2110021;02110021 - ОТДЕЛЕНИЕ ПО РАССЛЕДОВАНИЮ ОСОБО ВАЖНЫХ ДЕЛ (О ПРЕСТУПЛЕНИЯХ ПРОШЛЫХ ЛЕТ) СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
2110035;02110035 - ОТДЕЛ ПО РАССЛЕДОВАНИЮ ОСОБО ВАЖНЫХ ДЕЛ СУ СК РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
4007701;04007701 - ФЕДЕРАЛЬНАЯ ТАМОЖЕННАЯ СЛУЖБА (ФТС РОССИИ)
4007702;04007702 - УПРАВЛЕНИЕ ПО ПРОТИВОДЕЙСТВИЮ КОРРУПЦИИ ФТС РОССИИ
4009609;04009609 - ЦЕНТРАЛЬНАЯ ЭНЕРГИТИЧЕСКАЯ ТАМОЖНЯ
4009701;04009701 - СЕВЕРО-ЗАПАДНОЕ ТАМОЖЕННОЕ УПРАВЛЕНИЕ
4009702;04009702 - СЕВЕРО-ЗАПАДНАЯ ОПЕРАТИВНАЯ ТАМОЖНЯ
4009703;04009703 - АРХАНГЕЛЬСКАЯ ТАМОЖНЯ
4009708;04009708 - МУРМАНСКАЯ ТАМОЖНЯ
4009724;04009724 - ОТДЕЛЕНИЕ ПО ПРОТИВОДЕЙСТВИЮ КОРРУПЦИИ АРХАНГЕЛЬСКОЙ ТАМОЖНИ
4009725;04009725 - СЛУЖБА ПО ПРОТИВОДЕЙСТВИЮ КОРРУПЦИИ СЕВЕРО-ЗАПАДНОГО ТАМОЖЕННОГО УПРАВЛЕНИЯ
6110001;06110001 - УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110003;06110003 - ФКУ ОИУ ОУХД-2 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110004;06110004 - ФКУ ОИУ ОУХД-4 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110005;06110005 - ФКУ ИСПРАВИТЕЛЬНАЯ КОЛОНИЯ № 1 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110006;06110006 - ФКУ ИСПРАВИТЕЛЬНАЯ КОЛОНИЯ №4 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110007;06110007 - ФКУ ИСПРАВИТЕЛЬНАЯ КОЛОНИЯ № 5 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110008;06110008 - ФКУ ИСПРАВИТЕЛЬНАЯ КОЛОНИЯ № 7 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110009;06110009 - ФКУ ИСПРАВИТЕЛЬНАЯ КОЛОНИЯ № 12 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110010;06110010 - ФКУ ИСПРАВИТЕЛЬНАЯ КОЛОНИЯ №14 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110011;06110011 - ФКУ ИСПРАВИТЕЛЬНАЯ КОЛОНИЯ № 16 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110012;06110012 - ФКУ ИСПРАВИТЕЛЬНАЯ КОЛОНИЯ № 29 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110013;06110013 - ФКУ ЛЕЧЕБНОЕ ИСПРАВИТЕЛЬНОЕ УЧРЕЖДЕНИЕ № 8 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110015;06110015 - ФКУ АРХАНГЕЛЬСКАЯ ВОСПИТАТЕЛЬНАЯ КОЛОНИЯ УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110016;06110016 - ФКУ ОБЛАСТНАЯ БОЛЬНИЦА УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110017;06110017 - ФКУ СЛЕДСТВЕННЫЙ ИЗОЛЯТОР № 1 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110018;06110018 - ФКУ СЛЕДСТВЕННЫЙ ИЗОЛЯТОР №2 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110019;06110019 - ФКУ СЛЕДСТВЕННЫЙ ИЗОЛЯТОР №3 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110020;06110020 - ФКУ СЛЕДСТВЕННЫЙ ИЗОЛЯТОР №4 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110032;06110032 - ИСПРАВИТЕЛЬНАЯ КОЛОНИЯ №21 ФКУ ОИУ ОУХД-2 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110033;06110033 - КОЛОНИЯ-ПОСЕЛЕНИЕ № 27 ФКУ ОИУ ОУХД-2 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110035;06110035 - КОЛОНИЯ-ПОСЕЛЕНИЕ № 23 ФКУ ОИУ ОУХД-4 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110036;06110036 - ИСПРАВИТЕЛЬНАЯ КОЛОНИЯ № 28 ФКУ ОИУ ОУХД-4 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110044;06110044 - ФКУ КОЛОНИЯ-ПОСЕЛЕНИЕ № 3 УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
6110045;06110045 - ФКУ КОЛОНИЯ-ПОСЕЛЕНИЕ №19 С ОСОБЫМИ УСЛОВИЯМИ ХОЗ.ДЕЯТЕЛЬНОСТИ УФСИН РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
7007701;07007701 - ФЕДЕРАЛЬНАЯ СЛУЖБА БЕЗОПАСНОСТИ РОССИЙСКОЙ ФЕДЕРАЦИИ
7110001;07110001 - РУФСБ РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
8110001;08110001 - УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110002;08110002 - ОСП ПО ПРИМОРСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110003;08110003 - ОСП ПО СОЛОМБАЛЬСКОМУ ОКРУГУ Г.АРХАНГЕЛЬСКА УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110004;08110004 - ОСП ПО ОКТЯБРЬСКОМУ ОКРУГУ Г.АРХАНГЕЛЬСКА УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110005;08110005 - ОСП ПО ЛОМОНОСОВСКОМУ ОКРУГУ Г.АРХАНГЕЛЬСКА УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110006;08110006 - ОСП ПО ИСАКОГОРСКОМУ ОКРУГУ Г.АРХАНГЕЛЬСКА УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110007;08110007 - ОСП ПО Г.НОВОДВИНСКУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110008;08110008 - ОСП ПО Г.СЕВЕРОДВИНСКУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110009;08110009 - ОСП ПО ВЕЛЬСКОМУ И ШЕНКУРСКОМУ РАЙОНАМ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110010;08110010 - ОСП ПО ВЕРХНЕТОЕМСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110012;08110012 - ОСП ПО ВИНОГРАДОВСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110013;08110013 - ОСП ПО КАРГОПОЛЬСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110014;08110014 - ОСП ПО КОНОШСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110016;08110016 - ОСП ПО Г.КОТЛАСУ И КОТЛАССКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110017;08110017 - ОСП ПО КРАСНОБОРСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110018;08110018 - ОСП ПО ЛЕНСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110020;08110020 - ОСП ПО МЕЗЕНСКОМУ И ЛЕШУКОНСКОМУ РАЙОНАМ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110021;08110021 - ОСП ПО НЯНДОМСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110022;08110022 - ОСП ПО ОНЕЖСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110023;08110023 - ОСП ПО ПИНЕЖСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110024;08110024 - ОСП ПО ПЛЕСЕЦКОМУ РАЙОНУ И Г.МИРНЫЙ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110025;08110025 - ОСП ПО УСТЬЯНСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110026;08110026 - ОСП ПО ХОЛМОГОРСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110029;08110029 - МЕЖРАЙОННЫЙ ОСП ПО ОСОБО ВАЖНЫМ ИСПОЛНИТЕЛЬНЫМ ПРОИЗВОДСТВАМ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110031;08110031 - РУКОВОДСТВО УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110045;08110045 - ОСП ПО Г.КОРЯЖМЕ И ВИЛЕГОДСКОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110053;08110053 - ООД УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8110055;08110055 - СПЕЦИАЛИЗИРОВАННЫЙ ОТДЕЛ ОПЕРАТИВНОГО ДЕЖУРСТВА УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
8111058;08111058 - ОСП ПО Г.НАРЬЯН-МАРУ И ЗАПОЛЯРНОМУ РАЙОНУ УФССП РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НАО
10110001;10110001 - УНД И ПР ГУ МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110006;10110006 - ОНД ПРИМОРСКОГО И ХОЛМОГОРСКОГО РАЙОНОВ УНД И ПР МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110007;10110007 - ОНД Г.СЕВЕРОДВИНСКА И ОНЕЖСКОГО РАЙОНА УНД И ПР МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110008;10110008 - ОНД Г.НОВОДВИНСКА УНД И ПР МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110009;10110009 - ОНД КОРЯЖМА, ВИЛЕГОДСКОГО И ЛЕНСКОГО РАЙОНОВ УНД И ПР МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110010;10110010 - ОНД Г.КОТЛАСА И КОТЛАССКОГО РАЙОНА УНД И ПР МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110011;10110011 - ОНД ВЕЛЬСКОГО И УСТЬЯНСКОГО РАЙОНОВ УНД И ПР МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110013;10110013 - ОНД ВИНОГРАДОВСКОГО И ШЕНКУРСКОГО РАЙОНОВ УНД И ПР ГУ МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110016;10110016 - ОНД ПО НЯНДОМСКОМУ, КАРГОПОЛЬСКОМУ И КОНОШСКОМУ РАЙОНАМ УНД И ПР МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110023;10110023 - ОНД ПИНЕЖСКОГО РАЙОНА УНД И ПР МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110024;10110024 - ОНД ПЛЕСЕЦКОГО РАЙОНА УНД И ПР МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110030;10110030 - ФГКУ СПЕЦИАЛЬНОЕ УПРАВЛЕНИЕ ФПС № 18 МЧС РОССИИ (АРХАНГЕЛЬСКАЯ ОБЛАСТЬ)
10110031;10110031 - ОНД Г.АРХАНГЕЛЬСКА УНД И ПР МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110043;10110043 - ОНД ЛЕШУКОНСКОГО И МЕЗЕНСКОГО РАЙОНОВ УНД И ПР МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
10110051;10110051 - ОНД ВЕРХНЕТОЕМСКОГО И КРАСНОБОРСКАЯ РАЙОНОВ УНД И ПР МЧС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
11110001;11110001 - ПОГРАНИЧНОЕ УПРАВЛЕНИЕ ФСБ РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ
11470001;11470001 - ПОГРАНИЧНОЕ УПРАВЛЕНИЕ ФСБ РОССИИ ПО ЗАПАДНОМУ АРКТИЧЕСКОМУ РАЙОНУ