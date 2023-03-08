import utils
import read_csv
import charts
  

def run():
  continente = input('Type continent ==>  ')
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda i: i['Continent'] == continente, data))
  titulo = 'Diagrama de Población de Paises'
  countries = list(map(lambda x : x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages, titulo)
  
  country = input('Type country ==> ')
  result = utils.population_by_country(data, country)

  if len(result)>0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
    


if __name__ == '__main__':
  run()