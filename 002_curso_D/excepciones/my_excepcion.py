class MiExcepcion(Exception):
    def __init__(self,err):
        print(f'impresiomnante, cometiste el siguinete error: {err}')


#lanzando mi propia excepcion
#raise MiExcepcion('hahahaha, persona poco culta')


# manejandola la excepcion
try:
    raise MiExcepcion('hahahahah, persona poco culta')
except:
    print('como vas a cometer ese eroor')