import logging
import os

# Obtém o nome de usuário do sistema
username = os.getenv('USERNAME')

# Configura o logging
logging.basicConfig(filename=r"C:\Users\app.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Exemplo de logging que inclui o nome de usuário
try:
    # Seu código aqui
    resultado = 10 / 0  # Isso causará uma exceção

except Exception as e:
    # Registrar um erro, incluindo o nome de usuário
    logging.error(f"Ocorreu um erro para o usuário {username}: {str(e)}", exc_info=True)

# Registrar uma mensagem informativa que inclui o nome de usuário
logging.info(f"O usuário {username} executou com sucesso o script.")

# Registrar um aviso que inclui o nome de usuário
logging.warning(f"O usuário {username} recebeu um aviso importante.")

# Fechar o arquivo de log
logging.shutdown()
