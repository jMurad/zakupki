import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from PySide2 import QtWidgets
from PySide2.QtCore import QThread, QObject, Signal, Slot
import gui
from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QRegExpValidator
from PySide2 import QtCore
import threading


class GuiClass(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    sig = Signal(object)
    sig2 = Signal(object)
    sig3 = Signal(object)
    params = Signal(int, int)

    def __init__(self):
        super().__init__()
        self.regions = [
            'Адыгея Респ',
            'Алтай Респ',
            'Алтайский край',
            'Амурская обл',
            'Архангельская обл',
            'Астраханская обл',
            'Байконур г',
            'Башкортостан Респ',
            'Белгородская обл',
            'Брянская обл',
            'Бурятия Респ',
            'Владимирская обл',
            'Волгоградская обл',
            'Вологодская обл',
            'Воронежская обл',
            'Дагестан Респ',
            'Еврейская Аобл',
            'Забайкальский край',
            'Ивановская обл',
            'Ингушетия Респ',
            'Иркутская обл',
            'Кабардино-Балкарская Респ',
            'Калининградская обл',
            'Калмыкия Респ',
            'Калужская обл',
            'Камчатский край',
            'Карачаево-Черкесская Респ',
            'Карелия Респ',
            'Кемеровская обл',
            'Кировская обл',
            'Коми Респ',
            'Костромская обл',
            'Краснодарский край',
            'Красноярский край',
            'Крым Респ',
            'Курганская обл',
            'Курская обл',
            'Ленинградская обл',
            'Липецкая обл',
            'Магаданская обл',
            'Марий Эл Респ',
            'Мордовия Респ',
            'Москва',
            'Московская обл',
            'Мурманская обл',
            'Ненецкий АО',
            'Нижегородская обл',
            'Новгородская обл',
            'Новосибирская обл',
            'Омская обл',
            'Оренбургская обл',
            'Орловская обл',
            'Пензенская обл',
            'Пермский край',
            'Приморский край',
            'Псковская обл',
            'Ростовская обл',
            'Рязанская обл',
            'Самарская обл',
            'Санкт-Петербург',
            'Саратовская обл',
            'Саха /Якутия/ Респ',
            'Сахалинская обл',
            'Свердловская обл',
            'Севастополь г',
            'Северная Осетия - Алания Респ',
            'Смоленская обл',
            'Ставропольский край',
            'Тамбовская обл',
            'Татарстан Респ',
            'Тверская обл',
            'Томская обл',
            'Тульская обл',
            'Тыва Респ',
            'Тюменская обл',
            'Удмуртская Респ',
            'Ульяновская обл',
            'Хабаровский край',
            'Хакасия Респ',
            'Ханты-Мансийский Автономный округ - Югра АО',
            'Челябинская обл',
            'Чеченская Респ',
            'Чувашская Республика - Чувашия',
            'Чукотский АО',
            'Ямало-Ненецкий АО',
            'Ярославская обл'
        ]
        self.pbValue = 0
        self.setupUi(self)
        self.listWidget.addItems(self.regions)

        validator = QRegExpValidator(QRegExp("[0-9]{0,25}"))
        self.lineEdit_2.setValidator(validator)
        self.lineEdit_3.setValidator(validator)
        self.lineEdit_4.setValidator(validator)
        validator = QRegExpValidator(QRegExp("[0-2]{0,1}[1-9]{1}\.[0-1]{0,1}[1-2]{1}\.[1-2]{1}[0-9]{3}"))
        self.lineEdit_5.setValidator(validator)
        self.lineEdit_6.setValidator(validator)
        self.lineEdit_7.setValidator(validator)
        self.lineEdit_8.setValidator(validator)
        validator = QRegExpValidator(QRegExp("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"))
        self.lineEdit_10.setValidator(validator)
        self.lineEdit_1.textChanged.connect(lambda: self.valid_form('lineEdit_9'))
        self.lineEdit_2.textChanged.connect(lambda: self.valid_form('lineEdit_2'))
        self.lineEdit_9.textChanged.connect(lambda: self.valid_form('lineEdit_9'))
        self.checkBox_1.stateChanged.connect(lambda: self.valid_form('checkBox_1'))
        self.checkBox_2.stateChanged.connect(lambda: self.valid_form('checkBox_2'))
        self.checkBox_3.stateChanged.connect(lambda: self.valid_form('fz1'))
        self.checkBox_4.stateChanged.connect(lambda: self.valid_form('fz2'))
        self.checkBox_5.stateChanged.connect(lambda: self.valid_form('fz2'))
        self.listWidget.itemSelectionChanged.connect(lambda: self.valid_form('listWidget'))

        self.pushButton_1.clicked.connect(self.find)
        self.pushButton_2.clicked.connect(self.start)
        self.pushButton_4.clicked.connect(self.stop)

        self.poisk = Poisk()

        self.poisk.callTotalResults.connect(self.set_total_results)
        self.poisk.callExFunction.connect(self.increment_progress)
        self.poisk.endPoisk.connect(self.end_poisk())
        self.evt1 = threading.Event()
        self.evt2 = threading.Event()
        self.evt3 = threading.Event()
        self.thread1 = threading.Thread(target=self.poisk.get_all_pages, args=(2, 500, self.evt1, self.evt2))
        self.thread2 = threading.Thread(target=self.poisk.get_total_results, args=(self.evt2, self.evt3,))
        self.thread3 = threading.Thread(target=self.poisk.find_protocols, args=(self.evt3,))

        # self.thread.started.connect(self.poisk.find_protocols)
        # self.thread.started.connect(lambda: self.poisk.get_all_pages(2, 500))
        # self.thread.started.connect(self.poisk.get_total_results)

    def closeEvent(self, e):
        self.stop()

    def valid_form(self, elem):
        if elem == 'checkBox_1':
            if self.checkBox_2.isChecked() & self.checkBox_1.isChecked():
                self.checkBox_2.setChecked(False)
        if elem == 'checkBox_2':
            if self.checkBox_2.isChecked() & self.checkBox_1.isChecked():
                self.checkBox_1.setChecked(False)
        if elem == 'fz1':
            if not (self.checkBox_3.checkState() | self.checkBox_4.checkState() | self.checkBox_5.checkState()):
                self.checkBox_4.setChecked(True)
        if elem == 'fz2':
            if not (self.checkBox_3.checkState() | self.checkBox_4.checkState() | self.checkBox_5.checkState()):
                self.checkBox_3.setChecked(True)
        if elem == 'lineEdit_9':
            text = self.lineEdit_1.text()
            if text == '':
                self.lineEdit_9.setText('')
        if elem == 'listWidget':
            cr = self.listWidget.currentRow()
            if len(self.listWidget.selectedItems()) >= 6:
                self.listWidget.setCurrentRow(self.listWidget.currentRow(), QtCore.QItemSelectionModel.Deselect)

    def validate_input(self):
        ss = self.lineEdit_1.text()
        cf = [int(bool(self.checkBox_1.checkState())),
              int(bool(self.checkBox_2.checkState()))
              ]
        fz = [int(bool(self.checkBox_3.checkState())),
              int(bool(self.checkBox_4.checkState())),
              int(bool(self.checkBox_5.checkState()))
              ]
        on = self.lineEdit_2.text()
        ph = [int(bool(self.checkBox_6.checkState())),
              int(bool(self.checkBox_7.checkState())),
              int(bool(self.checkBox_8.checkState())),
              int(bool(self.checkBox_9.checkState()))
              ]
        pf = self.lineEdit_3.text()
        pt = self.lineEdit_4.text()
        df = self.lineEdit_5.text()
        dt = self.lineEdit_6.text()
        uf = self.lineEdit_7.text()
        ut = self.lineEdit_8.text()
        rg = [x.data() for x in self.listWidget.selectedIndexes()]
        ex = self.lineEdit_9.text()
        return [ss, cf, fz, on, ph, pf, pt, df, dt, uf, ut, rg, ex]

    def find(self):
        self.evt1.set()
        inputdata = self.validate_input()
        self.poisk.set_params(inputdata)
        self.thread1.start()
        # self.poisk.get_all_pages(2, 500)
        print(self.thread2.isAlive())
        self.thread2.start()
        # self.poisk.get_total_results()

    def start(self):
        self.find()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(self.poisk.totalPages)
        self.thread3.start()
        self.pbValue = 0

    def stop(self):
        self.poisk.active = False
        # self.thread3.quit()
        # self.thread3.wait()
        self.progressBar.setValue(0)

    def end_poisk(self):
        # self.thread3.quit()
        pass

    def increment_progress(self):
        if self.poisk.active:
            self.pbValue += 1
            self.progressBar.setValue(self.pbValue)

    def set_total_results(self, text):
        self.label_20.setText(text)


class Poisk(QObject):
    callExFunction = Signal()
    callTotalResults = Signal(str)
    endPoisk = Signal(str)

    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()
        self.regions_dic = {
            'Адыгея Респ': ['region_regions_5277349', '5277349'],
            'Алтай Респ': ['region_regions_5277385', '5277385'],
            'Алтайский край': ['region_regions_5277388', '5277388'],
            'Амурская обл': ['region_regions_5277403', '5277403'],
            'Архангельская обл': ['region_regions_5277339', '5277339'],
            'Астраханская обл': ['region_regions_5277355', '5277355'],
            'Байконур г': ['region_regions_5277409', '5277409'],
            'Башкортостан Респ': ['region_regions_5277363', '5277363'],
            'Белгородская обл': ['region_regions_5277318', '5277318'],
            'Брянская обл': ['region_regions_5277319', '5277319'],
            'Бурятия Респ': ['region_regions_5277397', '5277397'],
            'Владимирская обл': ['region_regions_5277320', '5277320'],
            'Волгоградская обл': ['region_regions_5277356', '5277356'],
            'Вологодская обл': ['region_regions_5277340', '5277340'],
            'Воронежская обл': ['region_regions_5277321', '5277321'],
            'Дагестан Респ': ['region_regions_5277361', '5277361'],
            'Еврейская Аобл': ['region_regions_5277407', '5277407'],
            'Забайкальский край': ['region_regions_5277394', '5277394'],
            'Ивановская обл': ['region_regions_5277322', '5277322'],
            'Ингушетия Респ': ['region_regions_5277350', '5277350'],
            'Иркутская обл': ['region_regions_5277389', '5277389'],
            'Кабардино-Балкарская Респ': ['region_regions_5277351', '5277351'],
            'Калининградская обл': ['region_regions_5277341', '5277341'],
            'Калмыкия Респ': ['region_regions_5277360', '5277360'],
            'Калужская обл': ['region_regions_5277323', '5277323'],
            'Камчатский край': ['region_regions_5277404', '5277404'],
            'Карачаево-Черкесская Респ': ['region_regions_5277352', '5277352'],
            'Карелия Респ': ['region_regions_5277337', '5277337'],
            'Кемеровская обл': ['region_regions_5277390', '5277390'],
            'Кировская обл': ['region_regions_5277369', '5277369'],
            'Коми Респ': ['region_regions_5277338', '5277338'],
            'Костромская обл': ['region_regions_5277324', '5277324'],
            'Краснодарский край': ['region_regions_5277353', '5277353'],
            'Красноярский край': ['region_regions_5277398', '5277398'],
            'Крым Респ': ['region_regions_8408974', '8408974'],
            'Курганская обл': ['region_regions_5277378', '5277378'],
            'Курская обл': ['region_regions_5277325', '5277325'],
            'Ленинградская обл': ['region_regions_5277342', '5277342'],
            'Липецкая обл': ['region_regions_5277326', '5277326'],
            'Магаданская обл': ['region_regions_5277405', '5277405'],
            'Марий Эл Респ': ['region_regions_5277364', '5277364'],
            'Мордовия Респ': ['region_regions_5277365', '5277365'],
            'Москва': ['region_regions_5277335', '5277335'],
            'Московская обл': ['region_regions_5277327', '5277327'],
            'Мурманская обл': ['region_regions_5277343', '5277343'],
            'Ненецкий АО': ['region_regions_5277345', '5277345'],
            'Нижегородская обл': ['region_regions_5277370', '5277370'],
            'Новгородская обл': ['region_regions_5277346', '5277346'],
            'Новосибирская обл': ['region_regions_5277391', '5277391'],
            'Омская обл': ['region_regions_5277392', '5277392'],
            'Оренбургская обл': ['region_regions_5277371', '5277371'],
            'Орловская обл': ['region_regions_5277328', '5277328'],
            'Пензенская обл': ['region_regions_5277372', '5277372'],
            'Пермский край': ['region_regions_5277373', '5277373'],
            'Приморский край': ['region_regions_5277401', '5277401'],
            'Псковская обл': ['region_regions_5277344', '5277344'],
            'Ростовская обл': ['region_regions_5277357', '5277357'],
            'Рязанская обл': ['region_regions_5277329', '5277329'],
            'Самарская обл': ['region_regions_5277374', '5277374'],
            'Санкт-Петербург': ['region_regions_5277347', '5277347'],
            'Саратовская обл': ['region_regions_5277375', '5277375'],
            'Саха /Якутия/ Респ': ['region_regions_5277400', '5277400'],
            'Сахалинская обл': ['region_regions_5277406', '5277406'],
            'Свердловская обл': ['region_regions_5277383', '5277383'],
            'Севастополь г': ['region_regions_8408975', '8408975'],
            'Северная Осетия - Алания Респ': ['region_regions_5277359', '5277359'],
            'Смоленская обл': ['region_regions_5277330', '5277330'],
            'Ставропольский край': ['region_regions_5277354', '5277354'],
            'Тамбовская обл': ['region_regions_5277331', '5277331'],
            'Татарстан Респ': ['region_regions_5277366', '5277366'],
            'Тверская обл': ['region_regions_5277332', '5277332'],
            'Томская обл': ['region_regions_5277393', '5277393'],
            'Тульская обл': ['region_regions_5277333', '5277333'],
            'Тыва Респ': ['region_regions_5277386', '5277386'],
            'Тюменская обл': ['region_regions_5277379', '5277379'],
            'Удмуртская Респ': ['region_regions_5277367', '5277367'],
            'Ульяновская обл': ['region_regions_5277376', '5277376'],
            'Хабаровский край': ['region_regions_5277402', '5277402'],
            'Хакасия Респ': ['region_regions_5277387', '5277387'],
            'Ханты-Мансийский Автономный округ - Югра АО': ['region_regions_5277381', '5277381'],
            'Челябинская обл': ['region_regions_5277380', '5277380'],
            'Чеченская Респ': ['region_regions_5277358', '5277358'],
            'Чувашская Республика - Чувашия': ['region_regions_5277368', '5277368'],
            'Чукотский АО': ['region_regions_5277408', '5277408'],
            'Ямало-Ненецкий АО': ['region_regions_5277382', '5277382'],
            'Ярославская обл': ['region_regions_5277334', '5277334']
        }
        self.searchString = ''
        self.conformity = [0, 0]
        self.fz = [1, 1, 1]
        self.orderNumber = ''
        self.phase = [1, 1, 1, 1]
        self.pfFrom = ''
        self.pfTo = ''
        self.pdFrom = ''
        self.pdTo = ''
        self.udFrom = ''
        self.udTo = ''
        self.regions = []
        self.exclText = ''
        self.totalPages = 0
        self.trueResult = []
        self.allPages = []
        self.params = {
            'searchString': f'searchString={self.searchString}&',
            'conf': ['morphology=on&', 'strictEqual=on&'],
            'pageNumber': 'pageNumber=',
            'sortDirection': 'sortDirection=false&',
            'recordsPerPage': 'recordsPerPage=_',
            'showLotsInfoHidden': 'showLotsInfoHidden=false&',
            'fz': ['fz44=on&', 'fz223=on&', 'fz94=on&'],
            'orderNumber': f'orderNumber={self.orderNumber}&',
            'phase': ['af=on&', 'ca=on&', 'pc=on&', 'pa=on&'],
            'priceFromToGeneral': [f'priceFromGeneral={self.pfFrom}&', f'priceToGeneral={self.pfTo}&'],
            'currencyIdGeneral': 'currencyIdGeneral=-1&',
            'publishDateFromTo': [f'publishDateFrom={self.pdFrom}&', f'publishDateTo={self.pdTo}&'],
            'updateDateFromTo': [f'updateDateFrom={self.udFrom}&', f'updateDateTo={self.udTo}&'],
            'region_regions_': f'{self.regions}',
            'regions': f'regions={self.regions}',
            'regionDeleted': 'regionDeleted=false&',
            'sortBy': 'sortBy=UPDATE_DATE&',
            'exclText': f'exclText={self.exclText}'
        }
        self.sess = requests.Session()
        self.active = True

    def set_params(self, inputdata):
        self.searchString = inputdata[0]
        self.conformity = inputdata[1]
        self.fz = inputdata[2]
        self.orderNumber = inputdata[3]
        self.phase = inputdata[4]
        self.pfFrom = inputdata[5]
        self.pfTo = inputdata[6]
        self.pdFrom = inputdata[7]
        self.pdTo = inputdata[8]
        self.udFrom = inputdata[9]
        self.udTo = inputdata[10]
        self.regions = inputdata[11]
        self.exclText = inputdata[12]

    def generate_request(self, pgnum, rpp):
        url = f'http://zakupki.gov.ru/epz/order/quicksearch/search.html?'
        if self.searchString != '':
            url = url + self.params['searchString']

        url = url + \
            self.params['conf'][0] * self.conformity[0] + \
            self.params['conf'][1] * self.conformity[1]

        url = url + self.params['pageNumber'] + str(pgnum) + '&'
        url = url + self.params['sortDirection']
        url = url + self.params['recordsPerPage'] + str(rpp) + '&'
        url = url + self.params['showLotsInfoHidden']
        url = url + \
            self.params['fz'][0] * self.fz[0] + \
            self.params['fz'][1] * self.fz[1] + \
            self.params['fz'][2] * self.fz[2]

        if self.orderNumber != '':
            url = url + self.params['orderNumber']

        url = url + \
            self.params['phase'][0] * self.phase[0] + \
            self.params['phase'][1] * self.phase[1] + \
            self.params['phase'][2] * self.phase[2] + \
            self.params['phase'][3] * self.phase[3]

        if self.pfFrom != '':
            url = url + self.params['priceFromToGeneral'][0]

        if self.pfTo != '':
            url = url + self.params['priceFromToGeneral'][1]

        url = url + self.params['currencyIdGeneral']

        if self.pdFrom != '':
            url = url + self.params['publishDateFromTo'][0]

        if self.pdTo != '':
            url = url + self.params['publishDateFromTo'][1]

        if self.udFrom != '':
            url = url + self.params['updateDateFromTo'][0]

        if self.udTo != '':
            url = url + self.params['updateDateFromTo'][1]

        if self.regions:
            prm1 = prm2 = ''
            for rg in self.regions:
                reg = self.regions_dic[rg][0]
                prm1 = prm1 + reg + '=' + reg + '&'
                reg = self.regions_dic[rg][1]
                prm2 = prm2 + reg + '%2C'
            url = url + prm1 + 'regions=' + prm2[0:-3] + '&'

        if (self.searchString != '') & (self.exclText != ''):
            url = url + self.params['exclText']

        return url

    def get_html(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/73.0.3683.86 Safari/537.36',
            'referer': 'http://zakupki.gov.ru/epz/main/public/home.html',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1'
        }
        r = self.sess.get(url, headers=headers)
        return r.text

    @Slot()
    def find_protocols(self, evt3):
        evt3.wait()
        print('s3_start')
        k = 0
        self.active = True
        for page in self.allPages:
            htmlpage = self.get_html(page)
            bscontent = BeautifulSoup(htmlpage, 'lxml')
            content = bscontent.findAll('div', class_='registerBox')
            for cnt in content:
                if self.active:
                    urlprotocol = BeautifulSoup(str(cnt), 'lxml').select('div.reportBox li a')[1].attrs["href"]
                    if 'http://' not in urlprotocol:
                        urlprotocol = 'http://zakupki.gov.ru' + urlprotocol
                    idzakupki = urlprotocol.split('=')[1]
                    htmlprotocol = self.get_html(urlprotocol)
                    soup = BeautifulSoup(htmlprotocol, 'lxml')
                    resultsoup = soup.find(text=re.compile(r'Протокол признания участника уклонившимся'))
                    datetm = 'not found'
                    if resultsoup:
                        datetm = resultsoup.parent.parent.parent.select('td')[1].select('div span')[1].text.strip()
                        resultstr = {'datetime': datetm, 'id': idzakupki, 'url': urlprotocol}
                        self.trueResult.append(resultstr)
                        self.send_notification(datetm, str(resultstr))
                    k += 1
                    print({'datetime': datetm, 'id': idzakupki, 'url': urlprotocol}, k, '\n')
                    self.callExFunction.emit()
        self.endPoisk.emit('1')
        print('s3_end')

    @Slot()
    def get_all_pages(self, counts, rpp, evt1, evt2):
        evt1.wait()
        print('s1_start')
        self.totalPages = counts * rpp
        self.allPages.clear()
        self.trueResult.clear()
        for i in range(1, counts + 1):
            self.allPages.append(self.generate_request(i, rpp))
        self.endPoisk.emit('2')
        print('s1_end')
        evt2.set()

    @Slot()
    def get_total_results(self, evt2, evt3):
        print('s2_start')
        evt2.wait()
        # page = self.allPages[0]
        page = self.generate_request(1, 10)
        htmlpage = self.get_html(page)
        bscontent = BeautifulSoup(htmlpage, 'lxml')
        totalresults = bscontent.select('p.allRecords')[0].select('strong')[0].text
        self.callTotalResults.emit(totalresults)
        self.endPoisk.emit('3')
        print('s2_end')
        evt3.set()

    def get_protocol_found(self, stat):
        print('s3')
        itr = 0
        if stat:
            for tr in self.trueResult:
                itr += 1
                print(tr, itr)
        return self.trueResult

    def send_notification(self, datetm, message):
        pass
        minutes = self.time_condition(datetm)
        if minutes < 30:
            self.send_email(message)

    @staticmethod
    def send_email(message):
        fromaddr = "exsend@bk.ru"
        toaddr = "deit91@yandex.ru"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Уведомление"

        body = message
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()

        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        # server.starttls()
        server.login('exsend@bk.ru', 'Darum353694')
        server.auth_plain()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

    @staticmethod
    def time_condition(datetm):
        date = datetm.split(' (')[0]
        tz = datetm.split('(')[1][3:-1]
        if tz == '':
            tz = 0
        else:
            tz = int(tz)
        datetm = datetime.strptime(date, '%d.%m.%Y %H:%M')
        dt = datetime.now()
        timemsk = datetm - timedelta(hours=tz)
        razn = dt - timemsk
        minutes = round(divmod(razn.total_seconds(), 60)[0])
        return minutes


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = GuiClass()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
