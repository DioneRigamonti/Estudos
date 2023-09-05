from winotify import Notification, audio

notificacao = Notification(app_id="Código Python", title="Notificação da Automação", msg="Automação finalizada com sucesso!!!", duration="long")

# add um audio na notificação
notificacao.set_audio(audio.LoopingAlarm, loop=False) # false pra tocar 1x só , true para tocar durante todo o tempo da notificação.

# add um botão na notificação , pode colocar um caminho de arquivo ou site, até mesmo uma função.

notificacao.add_actions(label="Abrir arquivo", launch=r"C:\Users")

notificacao.show()