import requests

def get_html():
    r = requests.get("https://www.raposaazul.com.br/proximos-jogos-cruzeiro")
    return r.text

def write_to_file(html):
    # write html to file to investigate
    with open("html_body.txt", "w") as f:
        f.write(html)
        # sample html of target line
        #                       <li class="mb-2"><a href="/jogo/cruzeiro-x-palmeiras-29-05-2025" class="font-semibold hover:text-blue-900">Cruzeiro x Palmeiras</a> - 01/06/2025  às 19:30 - campeonato Brasileiro - Estádio Governador Magalhães Pinto</li>  <li class="mb-2"><a href="/jogo/cruzeiro-x-gremio-11-07-2025" class="font-semibold hover:text-blue-900">Cruzeiro x Gremio</a> - 11/07/2025  às 21:00 - campeonato Brasileiro - Estádio Governador Magalhães Pinto</li>  <li class="mb-2"><a href="/jogo/cruzeiro-x-juventude-18-07-2025" class="font-semibold hover:text-blue-900">Cruzeiro x Juventude</a> - 18/07/2025  às 21:00 - campeonato Brasileiro - Estádio Governador Magalhães Pinto</li>  <li class="mb-2"><a href="/jogo/cruzeiro-x-ceara-25-07-2025" class="font-semibold hover:text-blue-900">Cruzeiro x Ceara</a> - 25/07/2025  às 21:00 - campeonato Brasileiro - Estádio Governador Magalhães Pinto</li>  <li class="mb-2"><a href="/jogo/cruzeiro-x-santos-08-08-2025" class="font-semibold hover:text-blue-900">Cruzeiro x Santos</a> - 08/08/2025  às 21:00 - campeonato Brasileiro - Estádio Governador Magalhães Pinto</li> 
        #                      <li class="mb-2"><a href="/jogo/vitoria-x-cruzeiro-10-06-2025" class="font-semibold hover:text-blue-900">Vitoria x Cruzeiro</a> -  12/06/2025  às 19:00 - campeonato Brasileiro - Estádio Manoel Barradas</li>  <li class="mb-2"><a href="/jogo/fluminense-x-cruzeiro-15-07-2025" class="font-semibold hover:text-blue-900">Fluminense x Cruzeiro</a> -  15/07/2025  às 21:00 - campeonato Brasileiro - Estadio Jornalista Mário Filho</li>  <li class="mb-2"><a href="/jogo/corinthians-x-cruzeiro-22-07-2025" class="font-semibold hover:text-blue-900">Corinthians x Cruzeiro</a> -  22/07/2025  às 21:00 - campeonato Brasileiro - Neo Química Arena</li>  <li class="mb-2"><a href="/jogo/botafogo-x-cruzeiro-01-08-2025" class="font-semibold hover:text-blue-900">Botafogo x Cruzeiro</a> -  01/08/2025  às 21:00 - campeonato Brasileiro - Estádio Olímpico Nilton Santos</li>  <li class="mb-2"><a href="/jogo/mirassol-x-cruzeiro-15-08-2025" class="font-semibold hover:text-blue-900">Mirassol x Cruzeiro</a> -  15/08/2025  às 21:00 - campeonato Brasileiro - Estádio José Maria de Campos Maia</li>                </ol>

        # they are both lists and len of > 700
        # first check len and then check if the first tag is <li> 

def parse_html(html):
    html_list = html.splitlines()
    
    for html_line in html_list:
        if len(html_line) > 600:
            # decide if line is one of the ones we want or not
            stripped_line = html_line.split(' ')
            # print(stripped_line)
            # print()
            # print()

            if '<li' in stripped_line:
                print(stripped_line)

    return "to be finished"

if __name__ == "__main__":
    # request html body from url
    html = get_html()

    #write_to_file(html)

    # get content from html
    content = parse_html(html)

    # add content to db
    #add_content_to_db(content)