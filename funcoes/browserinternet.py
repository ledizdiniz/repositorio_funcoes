import sys
import time

from PyQt5 import uic
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings, QWebEngineProfile
# pip uninstall PyQt5-sip
# pip install PyQt5-sip
# pip install PyQtWebEngine  para installar o modulo


from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication

#diretorio do git
diretorio = 'telas/'

class Web(QWebEngineView):

    def load(self, url):
        self.setUrl(QUrl(url))

    def adjustTitle(self):
        self.setWindowTitle(self.title())

    def disableJS(self):
        settings = QWebEngineSettings.globalSettings()
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, False)

    def remove(self):
        QWebEngineProfile.cookieStore().deleteAllCookies()

    def profile(self, nome):  # aqui voce aponta a pasta onde esta o cookie com o perfil do usuario
        defaultProfile = QWebEngineProfile.defaultProfile()
        defaultProfile.setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        cookies_path = 'cookies/' + nome + '/'

        defaultProfile.setCachePath(cookies_path)
        defaultProfile.setPersistentStoragePath(cookies_path)
        pass

class browserinternet(QWidget):
    def inicio(self,id,senha,novasenha,parent=None):
        super().__init__(parent)
        self.initUI(id,senha,novasenha)
        self.ui = uic.loadUi(r""+diretorio+"broserint.ui", self)
        self.ui.show()

    def initUI(self,id,senha,novasenha):
        web = Web()
        web.profile(id)
        web.load(
            "https://accounts.nintendo.com/reauthenticate?cancel_uri=https%3A%2F%2Faccounts.nintendo.com%2Fsecurity&show_nav=1&post_reauthenticate_redirect_uri=https%3A%2F%2Faccounts.nintendo.com%2Fpassword%2Fedit%3Fshow_nav%3D1")
        lay = QVBoxLayout(self)
        lay.addWidget(web)
        web.loadFinished.connect(lambda: self.carregar(senha,novasenha))

    def carregar(self, senha,novasenha):
      import autopy
      print('teste')
      from pynput.keyboard import Key, Controller
      keyboard = Controller()
      autopy.key.type_string(senha, wpm=100) #digita a senha
      keyboard.press(Key.enter)
      autopy.key.tap(autopy.key.Code.TAB)
      autopy.key.tap(autopy.key.Code.TAB)
      autopy.key.tap(autopy.key.Code.TAB)
      autopy.key.tap(autopy.key.Code.TAB)
      autopy.key.type_string(novasenha, wpm=100)
      autopy.key.tap(autopy.key.Code.TAB)
      autopy.key.type_string(novasenha, wpm=100)
      autopy.key.tap(autopy.key.Code.TAB)
      autopy.key.tap(autopy.key.Code.TAB)
      keyboard.press(Key.enter)
      time.sleep(1)

    def atual(self,senha):
         try:
             print('atualizar')
             coluna = ['idsenha', 'idacesso']
             valor = [senha, id]
             print(valor, coluna)
         except:
             pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browserinternet().inicio("teste","teste","teste")
    sys.exit(app.exec_())

