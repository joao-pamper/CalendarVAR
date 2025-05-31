import requests
from pymongo import MongoClient

def get_html():
    r = requests.get("https://www.raposaazul.com.br/proximos-jogos-cruzeiro")
    return r.text

def write_to_file(html : str):
    # write html to file to investigate
    with open("html_body.txt", "w") as f:
        f.write(html)
        # sample html of target lines
        # <li class="mb-2"><a href="/jogo/cruzeiro-x-palmeiras-29-05-2025" class="font-semibold hover:text-blue-900">Cruzeiro x Palmeiras</a> - 01/06/2025  às 19:30 - campeonato Brasileiro - Estádio Governador Magalhães Pinto</li>  <li class="mb-2"><a href="/jogo/cruzeiro-x-gremio-11-07-2025" class="font-semibold hover:text-blue-900">Cruzeiro x Gremio</a> - 11/07/2025  às 21:00 - campeonato Brasileiro - Estádio Governador Magalhães Pinto</li>  <li class="mb-2"><a href="/jogo/cruzeiro-x-juventude-18-07-2025" class="font-semibold hover:text-blue-900">Cruzeiro x Juventude</a> - 18/07/2025  às 21:00 - campeonato Brasileiro - Estádio Governador Magalhães Pinto</li>  <li class="mb-2"><a href="/jogo/cruzeiro-x-ceara-25-07-2025" class="font-semibold hover:text-blue-900">Cruzeiro x Ceara</a> - 25/07/2025  às 21:00 - campeonato Brasileiro - Estádio Governador Magalhães Pinto</li>  <li class="mb-2"><a href="/jogo/cruzeiro-x-santos-08-08-2025" class="font-semibold hover:text-blue-900">Cruzeiro x Santos</a> - 08/08/2025  às 21:00 - campeonato Brasileiro - Estádio Governador Magalhães Pinto</li> 
        # <li class="mb-2"><a href="/jogo/vitoria-x-cruzeiro-10-06-2025" class="font-semibold hover:text-blue-900">Vitoria x Cruzeiro</a> -  12/06/2025  às 19:00 - campeonato Brasileiro - Estádio Manoel Barradas</li>  <li class="mb-2"><a href="/jogo/fluminense-x-cruzeiro-15-07-2025" class="font-semibold hover:text-blue-900">Fluminense x Cruzeiro</a> -  15/07/2025  às 21:00 - campeonato Brasileiro - Estadio Jornalista Mário Filho</li>  <li class="mb-2"><a href="/jogo/corinthians-x-cruzeiro-22-07-2025" class="font-semibold hover:text-blue-900">Corinthians x Cruzeiro</a> -  22/07/2025  às 21:00 - campeonato Brasileiro - Neo Química Arena</li>  <li class="mb-2"><a href="/jogo/botafogo-x-cruzeiro-01-08-2025" class="font-semibold hover:text-blue-900">Botafogo x Cruzeiro</a> -  01/08/2025  às 21:00 - campeonato Brasileiro - Estádio Olímpico Nilton Santos</li>  <li class="mb-2"><a href="/jogo/mirassol-x-cruzeiro-15-08-2025" class="font-semibold hover:text-blue-900">Mirassol x Cruzeiro</a> -  15/08/2025  às 21:00 - campeonato Brasileiro - Estádio José Maria de Campos Maia</li>                </ol>


def parse_html(html: str):
    """
    Gets full html of website with domain https://www.raposaazul.com.br/proximos-jogos-cruzeiro and 
    returns a dictionary of the next 5 home and 5 away games. (Might not be the exact next 10 games)

    The script works as follows
    1. get the lengthy lines
    2. slect the ones that have <li tag
    3. get 5 away or home matches from that line
    """
    html_list = html.splitlines()

    content = []
    
    for html_line in html_list:
        # get lengthy lines
        if len(html_line) > 600:
            stripped_line = html_line.split(' ')

            # select lines with <li tag
            if '<li' in stripped_line:
                
                # get the 5 matches from that line
                for i, text in enumerate(stripped_line):
                    if text == 'class="font-semibold':
                        team1 = stripped_line[i + 1]
                        team2 = stripped_line[i + 3]

                        game_date1 = stripped_line[i + 5]
                        game_date2 = stripped_line[i + 6]
                        if '/' in game_date1:
                            game_date = game_date1
                        else:
                            game_date = game_date2

                        game_time1 = stripped_line[i + 8]
                        game_time2 = stripped_line[i + 9]
                        if ':' in game_time1:
                            game_time = game_time1
                        else:
                            game_time = game_time2

                        team1, team2 = normalize_teams(team1, team2)

                        game_content = {}

                        game_content["team1"] = team1
                        game_content["team2"] = team2
                        game_content["game_date"] = game_date
                        game_content["game_time"] = game_time

                        content.append(game_content)
    return content

def normalize_teams(team1 : str, team2 : str):
    """
    Will normalize the text in a rule based algorithm. 

    ie. from (hover:text-blue-900">Cruzeiro, Palmeiras</a>) to (Cruzeiro, Palmeiras)
    """
    i1 = len(team1) - 1
    while i1 >= 0:
        if team1[i1] == ">":
            team1_normalized = team1[i1 + 1:]
        i1 -= 1

    for i2, char2 in enumerate(team2):
        if char2 == "<":
            team2_normalized = team2[:i2]

    return team1_normalized, team2_normalized

def add_content_to_db(content: list):
    client = MongoClient("localhost", 27017)

    db = client.calendarVAR

    games = db.games

    for game in content:
        result = games.find_one({"game_date" : game["game_date"]})

        if result is None:
            games.insert_one(game)

    client.close()


if __name__ == "__main__":
    # request html body from url
    html = get_html()

    # investigate html
    # write_to_file(html)

    # get content from html
    content = parse_html(html)

    # add content to mongo
    add_content_to_db(content)

    # sample_content = [
    #     {
    #         "team1": "Cruzeiro",
    #         "team2": "Palmeiras",
    #         "game_date": "01/06/2025",
    #         "game_time": "19:30",
    #     },
    #     {
    #         "team1": "Cruzeiro",
    #         "team2": "Gremio",
    #         "game_date": "11/07/2025",
    #         "game_time": "21:00",
    #     },
    #     {
    #         "team1": "Cruzeiro",
    #         "team2": "Juventude",
    #         "game_date": "18/07/2025",
    #         "game_time": "21:00",
    #     },
    #     {
    #         "team1": "Cruzeiro",
    #         "team2": "Ceara",
    #         "game_date": "25/07/2025",
    #         "game_time": "21:00",
    #     },
    #     {
    #         "team1": "Cruzeiro",
    #         "team2": "Santos",
    #         "game_date": "08/08/2025",
    #         "game_time": "21:00",
    #     },
    #     {
    #         "team1": "Vitoria",
    #         "team2": "Cruzeiro",
    #         "game_date": "12/06/2025",
    #         "game_time": "19:00",
    #     },
    #     {
    #         "team1": "Fluminense",
    #         "team2": "Cruzeiro",
    #         "game_date": "15/07/2025",
    #         "game_time": "21:00",
    #     },
    #     {
    #         "team1": "Corinthians",
    #         "team2": "Cruzeiro",
    #         "game_date": "22/07/2025",
    #         "game_time": "21:00",
    #     },
    #     {
    #         "team1": "Botafogo",
    #         "team2": "Cruzeiro",
    #         "game_date": "01/08/2025",
    #         "game_time": "21:00",
    #     },
    #     {
    #         "team1": "Mirassol",
    #         "team2": "Cruzeiro",
    #         "game_date": "15/08/2025",
    #         "game_time": "21:00",
    #     },
    # ]