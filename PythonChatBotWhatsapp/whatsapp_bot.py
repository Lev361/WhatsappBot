from selenium import webdriver
import time



class WhatsappBot:
	def __init__(self):
		#parte 1 - A mensagem que voce quer enviar
		self.mensagem = "Bom dia, seja bem vindo ao meu Whatsapp."

		#parte 2 - Nome dos grupos ou pessoas a quem voce deseja enviar a mensagem
		self.grupos_ou_pessoas = ["ANDROMEDA"]
		options = webdriver.ChromeOptions()
		options.add_argument('lang=pt-br')
		self.driver = webdriver.Chrome(
			executable_path=r'C:\Users\SAM\Desktop\PythonChat\chromedriver.exe', chrome_options=options)

	def EnviarMensagens(self):
		self.driver.get('https://web.whatsapp.com')
		time.sleep(30)
		for grupo in self.grupos:
			grupo = self.driver.find_element_by_xpath(f"//span[@title'{grupo}']")
			time.sleep(3)
			grupo.click()
			chat.box = self.driver.find_element_by_class_name('_1awRl')
			time.sleep(3)
			chat_box.click()
			chat.box.send_keys(self.mensagem)
			botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
			time.sleep(3)
			botao_enviar.click()
			time.sleep(3)


bot = WhatsappBot()
bot.EnviarMensagens()