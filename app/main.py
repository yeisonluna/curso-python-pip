import utils
import read_csv
import charts
import pandas as pd
  

def run():
  '''
  continente = input('Type continent ==>  ')
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda i: i['Continent'] == continente, data))
  titulo = 'Diagrama de Población de Paises'
  countries = list(map(lambda x : x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages, titulo)
  '''
  titulo = 'Diagrama de Población de Paises'

  df = pd.read_csv('data.csv') #Leo el archivo con pandas
  df = df[df['Continent']=='Europe'] #Filtro la columna continet con South America
  

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages, titulo)

  data = read_csv.read_csv('data.csv')
  country = input('Type country ==> ')
  print(country)


  result = utils.population_by_country(data, country)

  if len(result)>0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
    


if __name__ == '__main__':
  run()