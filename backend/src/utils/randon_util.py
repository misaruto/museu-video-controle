import string
import random
import uuid


def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

def uuid_generator():
  return str(uuid.uuid4())

def generate_randon_nick_name():
  nick_names = [
  "Zé Mané da Silva",
  "Tonho Liro Pancada",
  "Belmiro Fandangos",
  "Jujuba Doceiro",
  "Tibúrcio Pé-de-Mesa",
  "Serafina Trovoada",
  "Alcebíades Pirulito",
  "Zuleica Patavina",
  "Severino Pinga-Fogo",
  "Anastácio Mequetrefe",
  "Genoveva Pimpão",
  "Raimunda Zé-Caixão",
  "Florisbela Ximbica",
  "Jeremias Pé-de-Moleque",
  "Quitéria Cambalhota",
  "Arlindo Fumaça",
  "Virgulina Pancadão",
  "Chicão Batucada",
  "Lurdinha Pipoca",
  "Onofre Treme-Terra",
  ]
  return nick_names[random.randint(0,19)]