from twitter import api
from random import choice, randint
from time import sleep

def create_text():
    names_genius = ['Stephen Hawking', 'Albert Einstein', 'Marie Curie', 'Isaac Newton', 'Charles Darwin', 'Niels Boht', 'Nikola Tesla', 'Aristóteles', 'Thomas Edison', 'Jesus', 'Buda', 'Arquimedes', 'Ada Lovelace', 'Nicolau Copénico', 'Carl Sagan', 'Gregory Smith', 'Nietzsche', 'Santo Agostinho', 'David Hume', 'Karl Marx', 'Platão', 'Steve Jobs']
    cursos_names = ['Anestesiologia', 'Cancerologia', 'Cirurgia geral', 'Clínica médica', 'Cirurgia plástica', 'Coloproctologia', 'Dermatologia', 'Endocrinologia', 'Gastroenterologia', 'Genética médica', 'Geriatria', 'Ginecologia e obstetrícia', 'Hematologia', 'Mastologia', 'Medicina de emergência', 'Neurologia', 'Oftalmologia', 'Ortopedia', 'Pediatria', 'Psiquiatria', 'Urologia', 'Genética', 'Imagenologia', 'Biologia Molecular', 'Bioquímica', 'Análises ambientais', 'Análises bromatológicas', 'Engenharia Mecânica', 'Engenharia Biomédica']
    emojis_list = ['😍','🤓','🔖','😍🤓', '😍🤓🔖', '😍🔖', '🎓🔖', '😍🎓', '😍🎓🔖', '♥️😍', '♥️', '🏥😷', '🙅‍♀️🎓']
    frase_1 = 'Sim, eu {} sou mais inteligente que {}'
    frase_2 = 'Hahaha, eu {}, tenho certificado em {} cursos!!'
    frase_3 = 'Claro que sou uma adolecente promissora! Estudo {}h de {}'
    arroba = '@wtf_anapaula'
    pais_names = ['Venezuelano', 'Argentino', 'Mexicano', 'Eslavo', 'Frances', 'Italiano', 'Grego', 'Iraniano', 'Russo', 'Brasileiro', 'Tcheco', 'Latino', 'Romeno', 'Espanhol', 'Celta', 'Irlandes']
    temas_names = ['Marxismo', 'Neoplatonismo', 'a Escola Pitagórica', 'Aristotelismo', 'Iluminismo', 'Niilismo', 'Romantismo', 'Transcendentalismo', 'Racionalismo', 'Pragmatismo', 'Neocriticismo', 'Pós-modernismo', 'Idealismo', 'Materialismo', 'Escolástica', 'Empirismo', 'Metafisica', 'Bolchevismo', 'Esquerdismo', 'Social-democracia', 'Paramore é perfeito.']
    animais = ['feneco', 'peixe-bolha', 'polvo-dumbo', 'veado-de-penacho', 'lagosta-boxeadora', 'lesma-do-mar-azul', 'Pangolim', 'Dragão-marinho-folhado', 'Anta', 'Ligre', 'Toupeira-nariz-de-estrela']
    
    animal = choice(animais)
    emoji = choice(emojis_list)
    names = choice(names_genius)
    number = randint(1, 99)
    curses = choice(cursos_names)
    pais = choice(pais_names)
    temas = choice(temas_names)
    def frase1():
        return f'Sim, eu {arroba}, sou obviamente mais inteligente que {names} rs...{emoji}'
        
    def frase2():
        return f'Hahaha, eu, {arroba}, tenho certificado em {number} cursos!!...{emoji}'

    def frase3():
        return f'Claro que eu, {arroba}, sou uma adolescente promissora! Estudo {number}h de {curses} POR DIA...{emoji}'

    def frase4():
        return f'Ai, eu, {arroba}, tive um dia esplêndido, discuti sobre {temas} por horas com um {pais}...{emoji}'

    def frase5():
        return f'''De: {arroba}
Para: {arroba}

Estude mais sobre {curses}...{emoji}
        '''
    
    def frase6():
        return f'Todos deveriam ser que nem eu, {arroba} aprender sobre {temas}, o minimo né gente?'

    def frase7():
        return f'''Tem depressão? Estude sobre {curses} {emoji}
Conselho: {arroba}
'''
    
    def frase8():
        ana = randint(5, 9)
        doido = randint(1, 4)
        return f'''{arroba} - {ana}  X {pais} - {doido} 

Debate mais facil impossivel {emoji}
        '''
    def frase9():
        porcent = randint(65, 80)
        return f'Honestamente, eu {arroba}, acredito que a USP deveria me convocar para estudar, tipo, caras, eu sei {porcent}% mais que todos de lá.'
    
    def frase10():
        porcentag = randint(400, 500)
        livro = randint(66, 99)
        return f'O peso que, eu {arroba}, carrego por ser {porcentag}% mais inteligente que meus amigos e todos do recanto não está descrito, só nesses meses já estou no meu {livro} lido, e com uma gama de matéria para estudar que nem se compara com o resto que fica 24/7 reclamando no twitter rs..{emoji}'
    
    def frase11():
        return f'''Quem sou eu({arroba})
Futura especialista em {curses} ✅
Apaixonada pelas leituras de {temas} ✅
Amo em {pais} ✅
Fã do animal {animal} ✅

E FUTURA MÉDICA ✅✅✅
'''
    def frase12():
        return f'Eu, {arroba}, estou vendo um documentario sobre o animal {animal}, e logo mais continuar minhas leituras sobre {temas}, agora me diz, tem dia melhor? {emoji}'
    
    def frase13():
        return f'Eu, {arroba}, estou a quase uma semana que nenhum amigo conversa comigo, enfim, vou voltar a estudar {curses}...{emoji}'
    
    def frase14():
        return f''
    frases = [frase1(), frase2(), frase3(), frase4(), frase5(), frase6(), frase7(), frase8(), frase9(), frase10(), frase11(), frase12()]
    frase = choice(frases)
    return frase

def posting(frase):
    api.update_status(status=frase)

if __name__ == "__main__":
    while True:
        try:
            text = create_text()
            posting(text)
            sleep(30)
        except Exception as e:
            print(e)
