import requests
import pandas as pd

# Sua chave de API do TMDb
api_key = '004db58bcb892991550558b97a52bc5a'

# Função para buscar a avaliação do filme no TMDb
def get_movie_rating(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
    response = requests.get(url)
    data = response.json()
    
    if data['results']:
        # Pegando o primeiro resultado e a avaliação
        movie = data['results'][0]
        rating = movie['vote_average']
        return rating
    else:
        return "-"

# Caminho para o arquivo .xlsx, assumindo que o Python e o Excel estão na mesma pasta
file_path = 'C:\\Projects\\python_exercise_repo\\teste\\1001Filmes.xlsx'

# Carregar a planilha com os filmes
df = pd.read_excel(file_path)

# Adicionar uma nova coluna para a nota
df['Nota TMDb'] = df['Filmes'].apply(get_movie_rating)

# Salvar a planilha atualizada
df.to_excel('planilha_com_notas.xlsx', index=False)

print("Planilha atualizada com notas salva!")
