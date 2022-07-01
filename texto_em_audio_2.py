import pyttsx3

# - - Armazenando em uma variavel e Iniciando a library - -
robo = pyttsx3.init()
# - - Captando texto a ser convertido. - -
texto = input('Digite seu texto e aperte ENTER!: ')

robo.say(texto)

robo.runAndWait()