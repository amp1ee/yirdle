#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import os
import re
import random
import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome

wordlist = """
Аахен абака Аббас Абвер Абель абзац аборт абрам абрек абрис абхаз аваль аванс авгіт авгур Авель авізо аврал Аврам авран автол автор агава агама Агата агент Аглая агнця аграф агрус аґрус Адама адепт Адлер адрес адрон аероб аерон Аецій Ажнюк Азаре азарт Азаря азіат аймак айова айран айсор акант Аккра акорд акрил аксон актив актин актор акула акута акциз акція алгол Алдан алель алеут Алжир алжір алібі Аліма Аліна Аліса алича алкаш алкіл аллах алмаз алонж алтай алтей алтея алтин Алфій альба Альма альфа алярм амбар амбра амвон амеба аміак Амман ампер ампір амфор Анань Анапа анарх анаша Анвар Анвер ангар ангел ангол Андон Анеля аніон анкер Аннам анона анонс антей антик Антип антон анчар аорта Аоста апекс апель апеля апорт Аракс аргон Аргус аргус ареал арена арешт Арика аркан Аркас аркоз аркуш армія арм'як Арпад Арсен арсин Артек Артем артоз артур Артюр Артюх арф'яр архар архей архів Архип Арциз аршин аскет Аснар аспид аспід Ассам астат астма Астор Асуан асцит атака аташе атлас атлет Атрек аттик аудит афект афера афікс афіна афіни афіша афоня ахілл Ахіло Ахмад Ахмед ацтек Ашока Ашшур Аюдаг бабай бабак Бабеф бабій Бабій бабіт Бабич бабич бабка бабко бабня бабця багаж Багам багач багер багет багно багор бадан баддя Бажан базар базис байда байка Бакай бакан бакен бакун балда балет балик балія балка балон Балта банан Банат Банах банда банит банко банку банта баняк бараж барак баран барва барда бареж бар'єр баржа барій барит бариш Барка барка барон басил басищ баска басма басон бастр басюр батак батан батат батіг Батий батир батон батут Бауер Бахно бахур бахус бачок башта Баяра Баяря бебех бевзь Бевін Безак безум бейка бекар бекас бекет бекон Беліз Белла Белло беміт Бенеш Бенін бердо берег берет берил берло берма Бернс Берта бесса бетон Бєлов Бєрут бібка бібос бівак бивні бігос біґос бігун бідак бідар бідка бидло бідон бізон бійка бійня бійця Білай білан білет білий білка білко білль билля білок білон біляк Бімон біном біонт біота біржа бирка Бірма Бірон бісер бісик бістр битва битка бітлз биток биття бітум битюг Біхар бичищ бичня бичок бишак благо бланк Блейк блінт блиск блоки блоха блуза блюдо бляха бобер бобик бобир бобок Богно Богун бодня бодян боєць божба божищ Божко божок бозон боїнг бойко Бойко Бойль бойня бойок бокал болід бомба бонза бонна бонус Бопал борей борид борис борня борть Боряк босяк ботик бочка бочок браво брага брама брами Брамс брань Браун Брест Брехт Бріан бридж брижа брижі брика брила бриль бриля брита бритт бриця брова брови бронх броня брухт брюки брязк бубен Бубка бубка бубна бубон бугай бугор будда будка будні будяк Бузек бузок Буйко буйок буква букер букет букле букля булат булка бурав Бурак буран бурда Бурдо бурка бурса бурта бурун буряк бур'ян бурят бусел бусла бусол Буськ бутан бутик бутил бутон бутси буття буфер буфет буфон бухан бухта буцик Бучач Бучма бучок бювар бювет бюрко вабик вавка вагар вагон вагот вадим Вадуц важко важок вазка вазон Вайда вайда вайла вайло вакса Вакул валах Валга валер валет валик валін Валка валка Валко валок валуй валун вальс валюш Ванда ванна ванта вапно варан Варва Варга Варна варта варяг васаг васал Васса ватаг ватер ватин ватка Ватто вафля вахня вахта Ващук вдача вдова вдово Вебер вебер Векла векша Велес велет велич Веллс велюр венед верба верб'я верес верея верло верхи весел весен весло весна веста вечер вечір взвод вибіг вибій вибір вибух вивал вивар вивід вивіз вивих вівса вівця вигад вигин вигін вигук вигул відео видик виділ видих видко видра видро відро відун вижим віжка віжки візир візит візок виїзд війка війна війни Війон війце війця виказ викид вікно викот викуп викус Вілен вилив віліс виліт вилка вілла вилов вилом Вілор вимах вимін вимір вимок винар Вінер віник вініл вінок винос винце вінце віола Віоло випав випад випал випар випас випік випин випис випіт віраж вираз вирва виріб виріз вирій вирло вирок вируб вірус вірші висів вісім висип висок вісон віспа вість вітер витік витин вітка виток витоп виття віття вітця витяг вихід вихор вихра віхтя вічка вічко вішка вишня вищип вищир віщун віяла віяло влада Власа внуко внуча вобла вовна вовча вогул водій вожак вождь Вожик возій возик возищ вокал волан волга волик волок волос волот Волох волох волхв вольт воляр ворог ворок ворон ворса вотум вохра вошва вошка вояка вплив впуск врода вступ втеча втома втора вуаль вугор вугра вудій вудка вужак вужик вузда вузол вуйко вуйна вулик вусач вусик Вусик вусищ вусок вуста вушко в'юнка в'юнок в'юнця в'юрок в'ючак в'юшка в'язка в'язок в'ятич в'ятка В'ятка Гаага Габен Габон Габор Гавел гавот Гавро гагат Гаген Гагра гаддя гадка Гадяч ґазда газик газир газон Гаїна Гайдн гайка гайно гайок Галан галас Галац гален Гален галій галіт галич Галич галка галон галоп галун галча Гальс гамак гаман гамір гамма ганаш ґандж Ганза Ганка ганна ґанок Ганул ганус Гапон гараж гарем гарус гарця Гасан Гасик гасла гасло гатка Гафіз Гафія гачок Гашек гашиш Гаяна ґвалт гвинт гевея ґедзь геєна Геєць Гейтс гейша Гекла гекон гелер гелій Гелія гемма геній геном генрі Генуя геоїд Георг Герат Гердт герма герой Герра Герца герць гетит гетра гібон гідра гієна гилка гілка гілля гіляк Гілян гінея гінка гінця гіпюр Гірин гирка гірка гирло гісоп гість гітів гичка гічка глава главк гладь Глеба глиба Гліба Глива Гливо Глієр глина гліпт глист глиця глоса глузд глянс глянц Гмире Гмиря Гната гнейс гнида гнізд гнила гниль гнома гнояк гнуся Гоббс гобой говір Гоген гогіт Годой Гожик Голда Голик Голік голиш голка Голль Голля голод голос голуб гольф голяк Гомер Гомес гомін гомоз гонка гонки гонор ґонта Ґонта гончі гопак горіх горла горло горно горня город горох горст горща гостя гоцак грака Гракх гранд грант Грант грань грати графа грежа Грень Гресь Греся грець греця грива гридь гриль Грімм Гринь Гриня Гриць грище Гроза гроза гроно ґроно груба груда грудь грузд грунт ґрунт ґрунь група груша грязь Губар губка Гувер гугіт ґудзь Ґудзь гудок Гужва Гужон гузир гузка Гулак гуляш гумай гуміт гумка гумоз гумор гумус Гупал гурба Гурій Гурик гурія Гурія Гурон гурон Гусак гусак гусар гусит гуска гусло густа гуцул гучок давид Давід давка давне давок Давос Дагер даймо дайна дакар дакка далеч далія дамар дамба дамка данай даний Данил данія данка дання Дарій дарія даток Дауес Дацюк дачка дашок дбаха двері Двіна дебет дебіл дебіт дебош дебют девіз девон деїзм деїст декан декор Демид демон демос Дем'ян Деник денис денце дерен дереш дерій дерик дерть дерун Десна десть дефіс дечия джбан джгут джига Джойс Джонс джура дзбан дзвін дзвяк дзета дзига дзиґа дзьоб Дзюба дзюдо дзявк діана Дибан дивак диван дівер дівич дівка дівча дигер дідич дідищ дідок Дідух дідух дієта діжка Діжон дійво дійка дикун дилер ділер ділок димар Димер димок динар динас динод Дірак дірка диска диски диско дичка дишло днина днище добір добре добро довід довіз догма дожин дозір дозор дойда Дойль дойна доказ докер докір Докія долар домен домна домра Донат доніс донка донор донос донья допис допит Дорій Дорія Дорош досів досіл дотеп дотик дофін дохла доход дочка дошка дощик драга драйв драма дрань древо Дрейк дрейф дрена дрізд дриле дриль дрова дрозд Дрозд друза друзе друзі друїд дуаєн Дуала дубищ дубль Дубна Дубно дубок дувал дуван дудар дудка Дудко дуель дужка дукар дукат дукач дуліб думка Дунай дунст дупло дурил дурка дурра дутар дутик Дутра дуття духан дучка душка душко Дьйор дюбек дюкер дюшес Дядюр дятел дячок Дячок Дячук Еберт Евбея евенк Евора егіда едикт Едіта Ейлер екзот еклер екран елада Еліза елінг Еліот еліпс еліта Еллан еллін Ельба Ельза Елюар емаль Еміль енант ендем енець ензим еозин еоліт Еолія еоцен епіка епонж епоха епюра Еразм Ераст ербій ерзац еркер Ерліх Ернст ескер ескіз Ессен естет етвеш етика етнос етрол ефект ефель ефіоп Ефрос Євбаз євген Євлах Євлаш Євмен євнух єврей Євсей Євтух єгеря єдваб Єжова єзуїт Єлець Ємець Єнсен єресь Єрмак Єрмил єссей єство Єфима єфрем єхида жабка Жадан жакан жакет Жалай Жанна жарко жатка Желев желяр жених женця жеода жердя жереб жереп жерех жерло жерун жетон живіт жидок Жижич Жижка жижки жилет жилка жінка жират жираф Жирко жирок жирун житіє житія житло життя житце жменя жмудь жмута жмуть жнець жнива жниво жниця жовна жовно жовта жокей жолоб жорен Жорес жорно жрець жриця жуйка Жулай жулан жупан жупел журба жучок забіг забій забор завал завіз завій завіт завія завод завуч загад загал загар загин загін загул Задар задир задок задум заєць зажин зазор заїзд заїка зайдо зайти зайча закид закис заков закон закот закуп залік заліт залка залом замах замет замір заміс замок замор замша заноз занос запал запас запах запій запіл запис запит запор зараз заріз зарин зарок заруб заряд засіб засів засік засіл заспа засув затір затон затор захар захід зачин зачіп зачіс заява збита збори зброй зброя Збруч збруя збуто звада звала звало звіра звір'я звіря звита зґаґа згір'я згода зграя здача Здвиж здоба зебра земля зеніт Зенон зерно зерня зефір зжата зівок Зідан зілля зилот Зінич Зінка зірка Злата злато злива злить злоба злото злука злюка Зміїв зміна зміст змита змова знада знати знать знось зоман зооїд Зосим Зотик зофор зошит зрада зраза зріст Зубар зубик зубищ зубок зубра зулус зумер зумпф зчепа зябра з'явищ Ібсен Івана іврит Ігнат Ігоря ігрек ігрищ ідеал ідіом ідіот ієрей іжиця ізвод ізгой Ізмір Ізота ізюбр ікона іксія ілеус Іліан ілліч Ілляш Ілона ілька Ілько ільма імбир імідж інвар Інгул інгуш індій Індій індик індія індол індус Інеса інжир інтим іоній іоніт Іонія іонол іосиф Іпата іприт ірбіс Ірена Іріан ірина іртиш Ірчан ісаак іскра іслам іспит істик Істра ітрій іудей Іцхак ішіас їдець їздка їство йодид йодль йодол Йолон йолоп йомен кабак кабан кабза Кабот кабул Кабул кавер кавун Кавур кав'яр кагал каган Каган кагат кагла кагор Кагул Кадар кадет кадіб кадик кадри кадуб кажан казан казах казка казна казус кайла кайло кайма кайра калан калач калій калим калин каліф каліч Каліш Калка калус Калуш калюс камея камза камін камка камор камса канал Канар канар канат канва канна каное канон канун канюк капер Капет капіж капіт капля капок капор капот карат карга Карел карел карет кар'єр кариб Карія Карла карма Карпа карпо карст карта карук Карюк карюк Касас касир касія каска касог каста Касян катар катер катет катод каток Катон Катря Кафка кахля кацап качан качка качок качур Кашен кашка кашне кашуб каюта квадр квант кварк кварц кваша кваше квота Кебич кегль кегля Кейнс келар келеп келех келих келія Кельн кельт кенаф кенія кепка кермо кесар кесон кетон кетяг кефір кіанг кібуц Ківва ківер кивок кігтя кидій кидок кизил Кизим кізка кізяк кійло кийок кілер килим Кілія кілля кілок кімвр кім'ях Кінах кінва кінза кінік кінін кіоск кіпер кіпка кират Кирей кирея кирза Кирик Кирил кирка кірка Киров кирпа кірха кірця кисет кіска кісся кіста кисть кість китай кітва кіфоз кичка кишка кішка кишло кияка кладь Клайд клайм клака Клара Кларк кларк Клаус клема клерк клест кліка клінч кліпа кліпс кліть клиця кліще кліщі Клова клопа клоун клуня кльош клюка кметь кнель кнехт книга княжа князь коала коата кобза кобиз кобол кобра ковер Ковно когут кодак кодло кодон кожан кожух козак козел козир козли козуб койка койот кокон кокос колаж Колас колба колеж колет колій колір коліт колія Колон колон колос колун кольт Коман комар комік комин комір комиш комод комос Конан конго коник конищ конка Конон конус конюх коняр копав копал Копач копач копер копил копія копця коп'як корал коран корда корея корма короб корок короп Корор корча коряк косар Косач косач Косів Кость косяк котел котик котищ коток кофта Коцур кочет кошик кошма кошти Кошут кощій краля краса крауч кредо Крезо Крейн креол крива крига криже крижі криза крики крило криль криля кріса криця кроль крона круїз крупа Крупа крупи Крупп круча кряча Ксюта кубик кубло кубок кудла Кудре Кудря кузен кузня кузов Кузьм кукан кулаж кулак кулан Кулик кулик куліш кулон культ кумач кумжа кумик кумир кумис кумць кумця кунак куншт купаж купер Купер купка купол купон кураж курай Курас кур'єр курій Курил курія курка курко курок курси курча кусок Кутас кутас кутик кутин куток кутум кухар кухва кухля кухня куцак куцан кучер кучка кучма Кучук кушир Кушка кушка кущик кхмер кювет кюрій кюшон кяриз Кяхта лабаз лаваш лавіс лавка лавра лавро Лавро Лагос лагун ладан ладка Лазар лазар лазер лазня лазур лайка лайно Лайош лакей лакон лампа ламут ланка ланок лапка лапки лаптя лапша ларга ласій ласка ласти ласун латач латин латиш латка латук лауда Лаура лафет лафіт Лахор Лацис Лашез левіт Левка Левко легат легіт ледар ледач ледащ лежак лежня лейка лекаж Лекок лелія Лелюк леміш Лемко лемко лемур Лемця ленін Леонт лепет Лепід лепра лепта лерка Лесик летка летяг ліана Лібіх лівак Ліван ливар лівер Лівія лівра лівша лігво лідар лідер Лідій лідит лідія лижва ліжко лижня лізат лізин лізис лізол лизун лійка лікар лікер Лікія ліктя лілея лілія Лілль лиман Лимар лимар ліміт Лімож лимон лімфа линва лінза лінія линок лінюх ліпід липка лірик лиска ліска лісок листа листя лисун Лисюк літак литва литво літер літій літію літія литка лиття літун лихач лихва лицар ліцей ліція личак лічба личко лишай лишко Лішко Ллойд лобас лобик лобищ лобок лобур Ловеч ловля логер логік логос ложка Локер локон локус локша ломик ломка лонжа лопар лопіт лопух Лорка Лорко лотік лоток лотос лоція лошак Луара лубок лугів лудан лужок лузга Луїза Лукаш Лукер Луків Лукій Лукія Лук'ян лунка Лупій лупка луска лусок Лусон лутка луфар Луцай Луцик Луцьк лучка Лучка лучок львів Льока льоля льоха льохо Любар любас Любек Любеч Любим любка любов любок люгер люмен Люм'єр люнет люпин люпус люстр Лютер лютий лютич лютня Люція люшня лямка ляпас ляпіс ляпка ляшка Ляшко лящик мавка мавпа Мавра Мавро магія магма магот мадер мадяр мажор мазар мазер мазій мазка мазне мазня мазок мазун мазур Мазур мазут Маїна майво майка Майкл майно Майнц майор макар макет Малан Малер Малик малка малюк маляр маляс Мамай мамій Мамін мамка мамця манат манго манеж манер манія манка манна манто манул марал Марат маржа марія марка Марко Маркс марля Марта Марфа марші мар'яж Мар'ян масаж масив маска масло масон масть Масюк матер матка матня матюк Матюш Матяш мафія Махно махра Мацко мачок меблі мебля мегер мегом медик медок мезга мезон мейоз Мекка мелан мелос Меней Менем мерин мерія месія метал метан метек метил метис метка метод метол метоп метро мечик Мещер мігма Мідій мідія мідяк мийка мікоз мікст Милан мілан милий Милій Милія мімос мимря мінер мінея міній мінор мінус міраж мірза мірка Мирко мирон мирра мирта мисик місія миска мисль мисок місто місце місць митар мітка мітла мітоз міток митра миття Михей Михея міхур міцні мичка мишва мишей мишій мишка мішка Мишко мішма мішок миш'як Міщук Млада мливо мнець могар могер Могил могол могти модем модус Мозир мозки мозок мойва Мокій Мокія Мокша мокша молот молох моляр монах моном мопед морда моріг Моріс мороз морок морфа моряк моста мосяж мотет мотив мотка моток мотор мотуз мохер Мохор моцак мочар мочка мошва мошка мрець Мруць мряка мугир Мудла Мудло мужва мужик музей мукор мулат муліт мулла муляж муляр Муляр мумія мурза мурла Муром Мусій мусон муфта мушва мушка мушля мюзет Мюрат мюрид м'якун м'якуш м'ялка М'янма м'ясце м'яття м'ячик набат набіг набій набіл набір набоб навал навар навій навик навис навіс нагад нагай наган нагар нагин нагін нагне Нагоя нагул надій наділ надир надія надра надув нажив нажин Назар назва Назим наїзд Наїна найда наказ накат накип налив наліт намаз намел намет намив намір намул нанка нанос напад напій напір напис нарив наріз Нарин нарис народ нарта наряд насад Насер насів насип насит насос натер натяг натяк наука нафта нахил нація наяда небіж невід Невіс Негев негус недуг нелад нелюб нелюд немає неміч Неміш ненка ненця непал Непер нерви нерет нерка нероб нерол Нерон нерпа несун нетеч нетля нетрі нетто нехар Нечай нивка Нігер нігті нігтя ніжка низка Никін никла Никон Нільс Німан німка німфа нирка нірка нирок нитик нитка нітон ниття Ніцца нічия нічка новак ножар ножик нойон номад номен номер нонет Нонна норія норка норма норов носак носар носач носій носик Носко носок нотар нотка Нубія нудяр нужда нукер Нукус нулик нумер нурка нурко нурок нурта нутро Ньєпс Ньяса нюанс нявка оазис обвал обвід обвіз обвіс обгін оберт об'єкт обжин обида об'їзд обкат обкіс обком облік обліт облов облог облом обман обмет обмін обмір обрад образ обрив обріз обрій обрин обрис оброк обруб обрус обруч обряд обсяг обуда обхід обшир обшук Овдій Овдія овеча овище овочі Оврам Овруч овруч Овсій огайо огида огляд огник огнищ огонь огоря огріх одбив одбій одбір одвал одвар одвід одвіз одгин одгін одгул оддих одежа одеон одеса одзол од'їзд одкол одлив одліт одрив одріг одріз одруб одрух одсів одсік одхід одчай одчал одщеп ожина озеро озима озноб ойрот окань оката океан окіст Оккам оклад оклик окови окрик окріл окріп округ оксид оксія октан октет окунь окута олеат олеїн Олекс олена олень оленя олеум олива олімп оліфа олово олтар ольга омана Омаха омега омела омита омлет Омськ омуль онагр Онега Оника онікс онука онуко онуча ооліт опало опара опера опіка опіум опліт оплот оповз опока опона опора оптик опука опуст опція орава орало Орбан орбіт орган оргія орден ордер орель Орель ореля ореол Орест Орина оріон Орися оркан орлан орлик Орлик Орлов орлон Орлюк орляк оруда орфей орчик оршад осада осака осеїн оселя Осієк осика осіла осінь Осипа Осипо оскал оскар Оскіл ослик ослон ослюк осман Осман осмій осмол осмос особа осоїд осока Остап Остер остит остов остюк остяк осуга отава отара отвір отець отоса отрок офеня офіра офорт офсет охват Охеда Охрім очиць очище очкур Очкур очник Павел павич Павія Павла павло павук павун пагін падло падуб пазур пайза пайка пайок пакет пакіл пакля палас палац палаш палій палія палка палюх Памва Памво Памір пампа панас панда панич Панич панія панна панок Панче Папен папір папка парад параф парез париж парик парія парка парко парод парох парта парус парча пасаж пасат пасив пасія паска пасмо пасок паста пасха патер патик Патон пауза пафос пахва Пахом пахощ пацан пацюк пачка пашня пегас Педан пекан пекар пекін пекло пелех Пелех пемза пенал пенат Пенза пеніс перга перед перла перли перло перон перст перун Перун песик петит петля петро печер печія Пещак п'єска піала піано пивце пів'ют пижик пижмо піжон піїта пійло пікап Пікар пікет пікша пилав Пілат пилип пилка пілка пилок пілон пілот пиляк пиляр Пимін пінія пінка пінта Піпін пипка пиптя пірат пиріг пирій пірит пірол піроп пірце писар піски пісня писок пісок питво Пітер пітон пиття питун піфія піфос піхва піхви піхта пичка пічка пішак пишка пищик пласт плата плато Платт плаун плаха плебс плем'я плеск плесо плече плінт плита пліть плиця площа площо плюск пляма пнище побій побіл побір побит побої побут поваб поваг повар повів повід повіз повіт повія повня поган погар погон погук подив подій поділ подих подія подув подум поема пожар позер позив позіх позов поїзд показ покер покій покіс покіт покуп покут полба полив полій полик полин поліп полір поліс політ полія полоз полом полон полюс поляк помах помел помиї помий помор помпа понос понюх попас попик Попик попіл попит порей порив поріг поріз Порик порок пором порох Порта порти порто поруб порух поруч порча посаг посад посів посол посох поста посуд посуш Потап поташ Потій потік потир потія потоп потяг похід почеп почет почин пошта пошук поява права право прага праля праця праща преса пріль прима примо принц пріор проба Прова проза Пронь Пропп проса просо проти Проць проща прояв Пруст пруть пряжа пряже пряма пряха псюга псюка псюра псяка псяра птаха птахо пташа птиця пуант пугач пудик пудра пужка пузан Пузій пузир пузце пульс пульт Пулюй пункт пупок пурин пурка Пусан пуття пуфик пухир пухла пучка пучок Пушик пушка пушок пушта пшоно п'явка п'ядак п'ядич п'ядун п'янка п'ясть п'ятак п'ятка рабат рабин радар раджа радій Радим радіо Радія радон радця разок разом Раїна раїна Раїса райок район райця раква ракла ракло ракша рамка рампа ранет ранка рання ранок ранчо растр ратай ратин Рауль раунд рафід рафія Рахів рахіт рація рачок ребро ребус ревун регбі регіт редан редис редут режим резол резон резус рейка Реймс рекет релей релін реліт ремез реміз Ренан Ренар ренет реній ренін рента репер репет реп'ях ретуш решка рибак рибка рівне рівня ривок рідне рідня рієль рижій рижик ріжки Рижко рижок ріжок Рижук різак ризик різка різна різне різня Різун різун рийка рійок рикша рілля Ріман римар римач Римма ринва рінго риніт ринка ріння ринок ріпак ріпка рипус рисак риска ріска ритон ритор риття рифма рихва рицар рицин Ричка річка Рішар робак Робер робер робіт робот ровик рогач рогіз родак Роден родій родич Родос рожен рожок роз'єм розор розум ройок рокер років рокіт Ролан ролер ролик роман ромей ромен ронжа Ронка Ронта ропак росія ростр Ротач ротик роток ротор рочок рояль ртуть Рубан рубач Рубен рубіж Рубік рубін рубка рубль Рудик рудка рудня рудої рудяк Ружин руїна рукав рулет рулон румак румба румун рупія рупор рурка русак русин русич русло рутил рутин ручай ручка рушій рюмса Рюрик ряден рядно рядок ряжка ряска сабан сабза сабур саван савар Савел Савка Савко Сагач сагиб сагіб Садат саджа садка садно садок саєта сажка сажок сазан сайга сайда сайка Сайкс сайра Сакій сакля сакос Сакун салат салеп Салій салол салон салоп салют саман самба самбо саміт самка Самко Самор Самос самум санки сапер сапет сапка сапун сап'ян сарай саржа сарна сарос Сартр сатин сатир сауна Сафат сачок свара сваха светр свинг свінг свиня свист свита світа світч Свіфт свище свояк свято сеанс Севан Сегед седан Седик сезам сезон секта селен селех селін селюк селюх Семен семіт Семко сенат Сеник Сепір сепія Серет Серик серія серна серум серце серця сесія сетер Сіань сибір Сивак сівач сиваш Сиваш сівба сивка сивко сивуч сівши сигма сідач сідло сидня сідок Сіетл сієна Сієна сікач сиква сикоз силаж силач Силич силон силос силур сильф сімка Симон сінаж синап синаш синдх синод синок синус сінце синяк сипай сирин Сирія сірія сірка сірко Сірко сирок сироп Сірош сирть Сирюк сіряк Сисой сисун ситал ситар сітка ситко ситро ситце сифон січка січна сішка сищик скала скань скарб скарн скаут сквер скеля скетч Скиба Скипа скіпа скирт склад склеп скляр скоба скопа скопи скопо скоро скорс Скотт скотч скрап скрес скрик скрип скрут скунс слава слайд слань сленг слива слизь слина слинь сліпо слище слово слоїк слони слоня слуга слюда смага Смага смерд смерк смерч Сметс Сміла смисл смола сморж смуга смута снага сніп'я сниця снище Собко собор Совга совка совко совок содом Созон сойка сойот сокіл сокір солея солід солод солон Солон соляр сомик сомищ Сомко сомок сомон сонет сонце сонць сонях сопка соплі сопло сопор сопун сорит сорок сором сорус соска сосна сосок сосун сотка сотня софіт софія софка Софон софор сохла сошка Спаак спазм спаса спека спіла спина спирт спиця сплав сплін Спліт спорт сприт спрут спурт спуск спуст стадо стаєр стаза сталь стана станс стара старт Стась стати стать ствол створ стела стеле стеля стенд степи степс стерв Стефа стиль стіна стиск стовп стоїк стокс Стокс стола стопа стояк Стоян стоян страж страз страм страх стрес стриж стрий стрій стрим стріп строк строп струг струм струп струс стума ступа стяга стята субір сувій сугак судак Судан суддя судій судія судно судок суєта сукно сукня сулія Сульт сумах суміш сумка суніт супін Сурат сурик сурма сусак сусід сусло сутаж суфій сухар сучка сучко сучок суччя сушка Сушко сушня Сущук сфера схема схлип сходи схрон сцена сюжет сюїта сяйво табес табір табун тавот тавро тагал таган Тагіл Тадей Тадея Тадій тазик тазок таїна Таїса тайга такир такса таксі талан Талас талер талес таліб талій талик талиш талія талон тальк таляр тамга таміл Танас танід танін танок Танюк тапер тапір таран тарас тариф тасун татка татко тафта тахта тацет Тацит тачка твань твіст театр тезис тезка тезко теїзм теїст Текля текст телур тембр темза темка темна тенге теніс тенор тепло Терез Терек терем терен тер'єр терка терла терло терми терне терня терор терта терть тертя тесак тесла тесло тесля тесть тестя Тетер теург техас течія течка тешка тіара тибар Тибет тибон тивун тигря тидол тижня тикер Тимко тимол Тимон Тимор Тимур тиння тинок тиньк типаж типик тіпун тираж тиран тирит тирло тирса тісна тісто титан титар тітка Титко титло титул Тихін Тихон тичба тичка тічка тічня тічок тишко ткаля тлінь Тобол товар товща Тодор Тодос тойон токай токар токіо толай толар Толок Томас томат томик томищ Тонга тонер тонік тонна тонус топаз топка торба торги Торез торій торит Торич торос тотем тохар точка точок трава трави тракт транс транш траса траст трата траур Траян треба трель тренд трест третє третя трефа тріан тріас триба трієр тризм тріод трипс тріск троль тромб тромп тропа трояк троян труба труда трупа трута трюмо туаль тубус Тувім тугай тузик тукан тулій Тулон тулуб тулуз тулук тулун тумак туман тумба Туніс тупак тупій тупик тупіт турач Турин Турін турищ Турка Туров турок турун турча тусан тусок тутор туфіт туфлі туфля туфта тухла тушка тьотя тюбан тюбик Тюдор тюнер Тюрен тюрма тютюн тючок тягар тягач тягло тягол тяжба тямок убоїщ убрус увага ув'язь угара Углич углич угода угрин удала удово Уельс Уерта Ужвій ужита узбек узвар узвіз узута уйгур уклад уклон укріп Уласа Улита Уліян Улька Уляна Уляно умбра уміла уміст умова ум'ята уніат уніон унтер унука унуко унуча унція упиря упряж ураза урарт урина уруно усміх Усова успіх устав усташ Устим уступ утвір утеча утече утиль утиск утіха утома утята Ухань учень учора Ушиця ушкал ушкуй ущерб фабра Фавій Фавія фавор Фавст фавус фагот Фадей Фадея фазан фазис Фаїна файка факел факір фалда фалес фалос фальц фальш фанат фанер фанза фанти фантя фарба фариз фасад фасет фаска фасон фатум фауна фацет фація фаянс Федак Федан Федів Федик Федір Федиш Федос федот Федул Федун Федус Федюк Фекла фелах фелон феній феніл фенол феном Феона ферзь ферит ферма феска фетиш фіакр фібра фивей фідер фіджі фізик фізія фікус філей філер Філик філіт філія фільм фільц фімоз фінал фінік фініш фінка фіноз фіорд фірма фітин фітол Фішер фишка фішка фланг фланк флейт флейц флінт флірт флокс флора флюат флюїд фляга фобія Фокич фокус фомка фонон форма Форос форте форум фоска Фотій фотон фофан фраза франк Франс франт Франц фрахт фреза Фрейд фрейм френч фреон фронт Фрост фрукт фрунт фугас фужер фузея фузія фукус фуляр фураж фурія фурма фурор футор футро Фучик Фущич Фюнес фюрер хабар хазар хакас хакер халат халва Халеб халіф Халов хаміт хамка хамло хамса ханжа ханой ханша хапун Харко харчі харчо хасид хатка хвала хваст хвиля хвіст Хебей хедер хедив хендс херем херес хіазм Хівря хідня хижак хижка хілус хімік хімія Химка хімус Хим'юк хінін хінон хиряк хисть хітин хитна хітон хлист хлоп'я хлюст хмара хміль хоана хобот ходак Ходак ходжа Ходжа ходик ходка ходок Ходос ходун хозар хокей холін холка холод холоп холуй Хомів хомут хом'як хопер хопта хорал хорда хорей хорея Хорив Хорог Хорол хором Хотів хрест Хриса хруск хруст хряск хтось Хубей Худаш хунта хурал хурма хутір хутра хутро цапик цапок цапфа царат царга царик Царик царка Царук Цвейг цвіль цебер цебро цегла цедра цезар цезій целіт целон Цельс Цемко ценоз центр церат церій церит цесар Цефей цехін цибок цибук Цибух цибух цівка циган цикля цілик цілко цинга цинік цинія Цинна ципка ціпко ціп'як цироз цісар циста цитра цифір цифра цокіт цукат цукор цундр цурка цуцик цятка чабак чабан чабер Чавес чавун чагар чадра Чадюк чаєня чайка Чайко чайок чакан чалий чалка чалма чапан Чапек чапля чарка Чарлз чауше чахла чашка чвань чекан ченця черва черга череп черес чернь честь чехів чехія Чехун Чечня чешка Чигир чигир чижик чилим чинок чіпка чіпко чіпок чирва чирка чирок чиряк число читач читка Читко чихир Чишко чміль чобіт човен чокер чопик чопок чортя Чосер чотар чохла чохол чтиво чубар Чубар Чубач чубик чубищ чубок чубук чуваш чув'як чудак чудар чудій чудищ чужак Чуйко чукча чумак Чурай чурек чутка чуття Чухно чушка шабаш шабер шабля шабот шавка шажок шайба шайка шакал шалик шалон шаман шамот шанин шанкр шапка шарик Шарль Шарон шар'яж шасла шатен шатер шатія шатро шатун шафар шафка шахта шашка шваля шванк шварт шверт Швець швора шевер Шевко шевця шелак шелех шелон шельф шелюг шеляг шемая шепіт шерех шериф шибер шибка шиїзм шийка Шимко шинка шинок шипик шіпка шипун Ширак ширма шість шитво шиття шифер шифон шихта шишак шишка шкала шкапа шквал шкерт шкіра Шкляр шкода школа шкура шланг шлейф шлемо шліпс шлюха шляпа шмідт Шмідт шнапс шнека шокер шолом Шопен шорка шорня шорти шофер шпага шпала шпана шпача шпень шпига шпиль шпиця Шпола шпона шпора шприц шпуля шпунт шримс шрифт штаба шталт штамб штамп штани штейн штемп Штепа штиль штифт штора шторм штраф штрек штрих штука штурм шубат шубка шугай шукач Шукер шулер шулик Шульц шуляк Шуман шумер Шумер шумка шумко шумок шурин шуруп шуряк шуфля шушон шушун шхери шхуна щабля щастя щебет щезла щепій щепка щерба Щерба Щербо щигля щілка щипка щіпка щипок щипці щитик щітка щиток щічка щогла щупак щупик Щурат щурик щурка щучка юглон югурт юдоль Юзефа Юзефо юзист юїтка Юліан Юлина Юліус юмізм юніор юнкер юнкор юннат юнона юрист юрода юрфак Юрчак Юрчук Юстим юферс ябеда явище ягель ягода ягуар ядуха яєчко яєчня яєшня Язова Якова якоря ялець ялина ялиця яльця ямище ямщик янгол Янгон Яніна Янсен Янсон янтар Ярема ярига ярина Ярина яриця ярлик яруга ярчук ясена ясень ясеня ястик ятвяг ятера ятіль яхонт Яцків ячник ящера
"""
words = []
picked = 'xxxxx'
d = datetime.datetime.now()
picked_file = '/tmp/.yirdle-picked-' + d.strftime('%d.%m.%Y')

def init():
	global words

	word_array = re.split('\s+', wordlist)
	list_len = len(word_array)
	print(f"We have {list_len} words")
	words = sort_words(word_array)

def start_server(word):
	app.run(debug=True)


def is_appropriate(word):
	if (len(word) < 5):
		return False
	if (word.istitle() or '\'' in word):
		return False
	return True

def sort_words(word_array):
	sorted_set = []

	for word in word_array:
		if (is_appropriate(word)):
			#print(word)
			sorted_set.append(word)

	return sorted_set

def pick_a_random_word_of_the_day():
	global picked

	if not os.path.exists(picked_file):
		picked = random.choice(words)
		with open(picked_file, 'w') as pf:
			pf.write(picked)
	else:
		with open(picked_file, 'r') as pf:
			picked = pf.readline().rstrip('\r\n')

init()
pick_a_random_word_of_the_day()
app = Flask(__name__)
bootstrap = Bootstrap(app)
fa = FontAwesome(app)

@app.route('/')
def mainpage():
	return render_template('index.html', picked=picked[::-1], wordlist=words)

if __name__ == '__main__':
	app.run()
